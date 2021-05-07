# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------

from typing import List, Any, Optional, TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer
from six import python_2_unicode_compatible

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._generated import AzureAttestationRestClient
from ._generated.models import AttestationType, PolicyResult, PolicyCertificatesResult, JSONWebKey, AttestationCertificateManagementBody, PolicyCertificatesModificationResult as GeneratedPolicyCertificatesModificationResult
from ._configuration import AttestationClientConfiguration
from ._models import AttestationSigner, AttestationToken, AttestationResponse, StoredAttestationPolicy, AttestationSigningKey, PolicyCertificatesModificationResult
from ._common import Base64Url
import cryptography
import cryptography.x509
import base64
from azure.core.tracing.decorator import distributed_trace
from threading import Lock, Thread


class AttestationAdministrationClient(object):
    """Provides administrative APIs for managing an instance of the Attestation Service.

    :param str instance_url: base url of the service
    :param credential: Credentials for the caller used to interact with the service.
    :type credential: azure.core.credentials.TokenCredential
    :keyword Pipeline pipeline: If omitted, the standard pipeline is used.
    :keyword HttpTransport transport: If omitted, the standard pipeline is used.
    :keyword list[HTTPPolicy] policies: If omitted, the standard pipeline is used.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        instance_url,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not credential:
            raise ValueError("Missing credential.")
        self._config = AttestationClientConfiguration(credential, instance_url, **kwargs)
        self._client = AzureAttestationRestClient(credential, instance_url, **kwargs)
        self._statelock = Lock()
        self._signing_certificates = None

    @distributed_trace
    def get_policy(self, attestation_type, **kwargs): 
        #type(AttestationType, **Any) -> AttestationResult[str]:
        """ Retrieves the attestation policy for a specified attestation type.

        :param azure.security.attestation.AttestationType attestation_type: :class:`azure.security.attestation.AttestationType` for 
            which to retrieve the policy.
        :return AttestationResponse[str]: Attestation service response encapsulating a string attestation policy.

        """
        
        policyResult = self._client.policy.get(attestation_type, **kwargs)
        token = AttestationToken[PolicyResult](token=policyResult.token, body_type=PolicyResult)
        token_body = token.get_body()
        stored_policy = AttestationToken[StoredAttestationPolicy](token=token_body.policy, body_type=StoredAttestationPolicy)

        actual_policy = stored_policy.get_body().attestation_policy #type: bytes

        if self._config.token_validation_options.validate_token:
            token.validate_token(self._config.token_validation_options, self._get_signers(**kwargs))

        return AttestationResponse[str](token, actual_policy.decode('utf-8'))

    @distributed_trace
    def set_policy(self, attestation_type, attestation_policy, signing_key=None, **kwargs): 
        #type:(AttestationType, str, Optional[AttestationSigningKey], **Any) -> AttestationResponse[PolicyResult]
        """ Sets the attestation policy for the specified attestation type.

        :param azure.security.attestation.AttestationType attestation_type: :class:`azure.security.attestation.AttestationType` for 
            which to set the policy.
        :param str attestation_policy: Attestation policy to be set.
        :param Optional[AttestationSigningKey] signing_key: Optional signing key to be
            used to sign the policy before sending it to the service.
        :return AttestationResponse[PolicyResult]: Attestation service response encapsulating a :class:`PolicyResult`.

        .. note::
            If the attestation instance is in *Isolated* mode, then the 
            `signing_key` parameter MUST be a signing key containing one of the
            certificates returned by :meth:`get_policy_management_certificates`.

            If the attestation instance is in *AAD* mode, then the `signing_key` 
            parameter does not need to be provided.
        """
        policy_token = AttestationToken[StoredAttestationPolicy](
            body=StoredAttestationPolicy(attestation_policy = attestation_policy.encode('ascii')),
            signer=signing_key,
            body_type=StoredAttestationPolicy)
        policyResult = self._client.policy.set(attestation_type=attestation_type, new_attestation_policy=policy_token.serialize(), **kwargs)
        token = AttestationToken[PolicyResult](token=policyResult.token,
            body_type=PolicyResult)
        if self._config.token_validation_options.validate_token:
            if not token.validate_token(self._config.token_validation_options, self._get_signers(**kwargs)):
                raise Exception("Token Validation of PolicySet API failed.")


        return AttestationResponse[PolicyResult](token, token.get_body())

    @distributed_trace
    def get_policy_management_certificates(self, **kwargs):
        #type:(**Any) -> AttestationResponse[list[list[bytes]]]
        """ Retrieves the set of policy management certificates for the instance.

        The list of policy management certificates will only be non-empty if the
        attestation service instance is in Isolated mode.

        :return AttestationResponse[list[list[bytes]]: Attestation service response 
            encapsulating a list of DER encoded X.509 certificate chains.
        """

        cert_response = self._client.policy_certificates.get(**kwargs)
        token = AttestationToken[PolicyCertificatesResult](
            token=cert_response.token,
            body_type=PolicyCertificatesResult)
        if self._config.token_validation_options.validate_token:
            if not token.validate_token(self._config.token_validation_options, self._get_signers(**kwargs)):
                raise Exception("Token Validation of PolicyCertificates API failed.")
        certificates = []

        cert_list = token.get_body()

        for key in cert_list.policy_certificates.keys:
            key_certs = [base64.b64decode(cert) for cert in key.x5_c]
            certificates.append(key_certs)
        return AttestationResponse(token, certificates)

    @distributed_trace
    def add_policy_management_certificate(self, certificate_to_add, signing_key, **kwargs):
        #type:(bytes, AttestationSigningKey, **Any)-> AttestationResponse[PolicyCertificatesModificationResult]
        """ Adds a new policy management certificate to the set of policy management certificates for the instance.

        :param bytes certificate_to_add: DER encoded X.509 certificate to add to 
            the list of attestation policy management certificates.
        :param AttestationSigningKey signing_key: Signing Key representing one of 
            the *existing* attestation signing certificates.
        :return AttestationResponse[PolicyCertificatesModificationResult]: Attestation service response 
            encapsulating the status of the add request.

        The :class:`PolicyCertificatesModificationResult` response to the 
        :meth:`add_policy_management_certificate` API contains two attributes
        of interest. 
        
        The first is `certificate_resolution`, which indicates 
        whether the certificate in question is present in the set of policy 
        management certificates after the operation has completed, or if it is 
        absent.

        The second is the `thumbprint` of the certificate added. The `thumbprint`
        for the certificate is the SHA1 hash of the DER encoding of the
        certificate.

        """
        key=JSONWebKey(kty='RSA', x5_c = [ base64.b64encode(certificate_to_add).decode('ascii')])
        add_body = AttestationCertificateManagementBody(policy_certificate=key)
        cert_add_token = AttestationToken[AttestationCertificateManagementBody](
            body=add_body,
            signer=signing_key,
            body_type=AttestationCertificateManagementBody)

        cert_response = self._client.policy_certificates.add(cert_add_token.serialize(), **kwargs)
        token = AttestationToken[GeneratedPolicyCertificatesModificationResult](token=cert_response.token,
            body_type=GeneratedPolicyCertificatesModificationResult)
        if self._config.token_validation_options.validate_token:
            if not token.validate_token(self._config.token_validation_options, self._get_signers(**kwargs)):
                raise Exception("Token Validation of PolicyCertificate Add API failed.")
        return AttestationResponse[PolicyCertificatesModificationResult](token, PolicyCertificatesModificationResult._from_generated(token.get_body()))

    @distributed_trace
    def remove_policy_management_certificate(self, certificate_to_add, signing_key, **kwargs):
        #type:(bytes, AttestationSigningKey, **Any)-> AttestationResponse[PolicyCertificatesModificationResult]
        """ Removes a new policy management certificate to the set of policy management certificates for the instance.

        :param bytes certificate_to_add: DER encoded X.509 certificate to add to 
            the list of attestation policy management certificates.
        :param AttestationSigningKey signing_key: Signing Key representing one of 
            the *existing* attestation signing certificates.
        :return AttestationResponse[PolicyCertificatesModificationResult]: Attestation service response 
            encapsulating a list of DER encoded X.509 certificate chains.

        The :class:`PolicyCertificatesModificationResult` response to the 
        :meth:`remove_policy_management_certificate` API contains two attributes
        of interest. 
        
        The first is `certificate_resolution`, which indicates 
        whether the certificate in question is present in the set of policy 
        management certificates after the operation has completed, or if it is 
        absent.

        The second is the `thumbprint` of the certificate added. The `thumbprint`
        for the certificate is the SHA1 hash of the DER encoding of the
        certificate.
        
        """
        key=JSONWebKey(kty='RSA', x5_c = [ base64.b64encode(certificate_to_add).decode('ascii')])
        add_body = AttestationCertificateManagementBody(policy_certificate=key)
        cert_add_token = AttestationToken[AttestationCertificateManagementBody](
            body=add_body,
            signer=signing_key,
            body_type=AttestationCertificateManagementBody)

        cert_response = self._client.policy_certificates.remove(cert_add_token.serialize(), **kwargs)
        token = AttestationToken[GeneratedPolicyCertificatesModificationResult](token=cert_response.token,
            body_type=GeneratedPolicyCertificatesModificationResult)
        if self._config.token_validation_options.validate_token:
            if not token.validate_token(self._config.token_validation_options, self._get_signers(**kwargs)):
                raise Exception("Token Validation of PolicyCertificate Remove API failed.")
        return AttestationResponse[PolicyCertificatesModificationResult](token, PolicyCertificatesModificationResult._from_generated(token.get_body()))

    def _get_signers(self, **kwargs):
        #type(**Any) -> List[AttestationSigner]
        """ Returns the set of signing certificates used to sign attestation tokens.
        """

        with self._statelock:
            if (self._signing_certificates == None):
                signing_certificates = self._client.signing_certificates.get(**kwargs)
                self._signing_certificates = []
                for key in signing_certificates.keys:
                    # Convert the returned certificate chain into an array of X.509 Certificates.
                    certificates = []
                    for x5c in key.x5_c:
                        der_cert = base64.b64decode(x5c)
                        certificates.append(der_cert)
                    self._signing_certificates.append(AttestationSigner(certificates, key.kid))
            signers = self._signing_certificates
        return signers

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AttestationAdministrationClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
