# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class AttestationProvider(TrackedResource):
    """Attestation service response message.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param trust_model: Trust model for the attestation service instance.
    :type trust_model: str
    :param status: Required. Status of attestation service. Possible values
     include: 'Ready', 'NotReady', 'Error'
    :type status: str or
     ~azure.mgmt.attestation.models.AttestationServiceStatus
    :param attest_uri: Gets the uri of attestation service
    :type attest_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'trust_model': {'key': 'properties.trustModel', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'attest_uri': {'key': 'properties.attestUri', 'type': 'str'},
    }

    def __init__(self, *, location: str, status, tags=None, trust_model: str=None, attest_uri: str=None, **kwargs) -> None:
        super(AttestationProvider, self).__init__(tags=tags, location=location, **kwargs)
        self.trust_model = trust_model
        self.status = status
        self.attest_uri = attest_uri


class AttestationProviderListResult(Model):
    """Attestation Providers List.

    :param value: Attestation Provider array.
    :type value: list[~azure.mgmt.attestation.models.AttestationProvider]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[AttestationProvider]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(AttestationProviderListResult, self).__init__(**kwargs)
        self.value = value


class AttestationServiceCreationParams(Model):
    """Parameters for creating an attestation service instance.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The supported Azure location where the
     attestation service instance should be created.
    :type location: str
    :param tags: The tags that will be assigned to the attestation service
     instance.
    :type tags: dict[str, str]
    :param properties: Required. Properties of the attestation service
     instance
    :type properties:
     ~azure.mgmt.attestation.models.AttestationServiceCreationSpecificParams
    """

    _validation = {
        'location': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'AttestationServiceCreationSpecificParams'},
    }

    def __init__(self, *, location: str, properties, tags=None, **kwargs) -> None:
        super(AttestationServiceCreationParams, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.properties = properties


class AttestationServiceCreationSpecificParams(Model):
    """Client supplied parameters used to create a new attestation service
    instance.

    :param attestation_policy: Name of attestation policy.
    :type attestation_policy: str
    :param policy_signing_certificates: JSON Web Key Set defining a set of
     X.509 Certificates that will represent the parent certificate for the
     signing certificate used for policy operations
    :type policy_signing_certificates:
     ~azure.mgmt.attestation.models.JSONWebKeySet
    """

    _attribute_map = {
        'attestation_policy': {'key': 'attestationPolicy', 'type': 'str'},
        'policy_signing_certificates': {'key': 'policySigningCertificates', 'type': 'JSONWebKeySet'},
    }

    def __init__(self, *, attestation_policy: str=None, policy_signing_certificates=None, **kwargs) -> None:
        super(AttestationServiceCreationSpecificParams, self).__init__(**kwargs)
        self.attestation_policy = attestation_policy
        self.policy_signing_certificates = policy_signing_certificates


class AttestationServicePatchParams(Model):
    """Parameters for patching an attestation service instance.

    :param tags: The tags that will be assigned to the attestation service
     instance.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(AttestationServicePatchParams, self).__init__(**kwargs)
        self.tags = tags


class AzureEntityResource(Resource):
    """The resource model definition for a Azure Resource Manager resource with an
    etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CloudError(Model):
    """An error response from Attestation.

    :param error:
    :type error: ~azure.mgmt.attestation.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """An error response from Attestation.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for displaying in a user interface.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message


class JSONWebKey(Model):
    """JSONWebKey.

    All required parameters must be populated in order to send to Azure.

    :param alg: Required. The "alg" (algorithm) parameter identifies the
     algorithm intended for
     use with the key.  The values used should either be registered in the
     IANA "JSON Web Signature and Encryption Algorithms" registry
     established by [JWA] or be a value that contains a Collision-
     Resistant Name.
    :type alg: str
    :param crv: The "crv" (curve) parameter identifies the curve type
    :type crv: str
    :param d: RSA private exponent or ECC private key
    :type d: str
    :param dp: RSA Private Key Parameter
    :type dp: str
    :param dq: RSA Private Key Parameter
    :type dq: str
    :param e: RSA public exponent, in Base64
    :type e: str
    :param k: Symmetric key
    :type k: str
    :param kid: Required. The "kid" (key ID) parameter is used to match a
     specific key.  This
     is used, for instance, to choose among a set of keys within a JWK Set
     during key rollover.  The structure of the "kid" value is
     unspecified.  When "kid" values are used within a JWK Set, different
     keys within the JWK Set SHOULD use distinct "kid" values.  (One
     example in which different keys might use the same "kid" value is if
     they have different "kty" (key type) values but are considered to be
     equivalent alternatives by the application using them.)  The "kid"
     value is a case-sensitive string.
    :type kid: str
    :param kty: Required. The "kty" (key type) parameter identifies the
     cryptographic algorithm
     family used with the key, such as "RSA" or "EC". "kty" values should
     either be registered in the IANA "JSON Web Key Types" registry
     established by [JWA] or be a value that contains a Collision-
     Resistant Name.  The "kty" value is a case-sensitive string.
    :type kty: str
    :param n: RSA modulus, in Base64
    :type n: str
    :param p: RSA secret prime
    :type p: str
    :param q: RSA secret prime, with p < q
    :type q: str
    :param qi: RSA Private Key Parameter
    :type qi: str
    :param use: Required. Use ("public key use") identifies the intended use
     of
     the public key. The "use" parameter is employed to indicate whether
     a public key is used for encrypting data or verifying the signature
     on data. Values are commonly "sig" (signature) or "enc" (encryption).
    :type use: str
    :param x: X coordinate for the Elliptic Curve point
    :type x: str
    :param x5c: The "x5c" (X.509 certificate chain) parameter contains a chain
     of one
     or more PKIX certificates [RFC5280].  The certificate chain is
     represented as a JSON array of certificate value strings.  Each
     string in the array is a base64-encoded (Section 4 of [RFC4648] --
     not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value.
     The PKIX certificate containing the key value MUST be the first
     certificate.
    :type x5c: list[str]
    :param y: Y coordinate for the Elliptic Curve point
    :type y: str
    """

    _validation = {
        'alg': {'required': True},
        'kid': {'required': True},
        'kty': {'required': True},
        'use': {'required': True},
    }

    _attribute_map = {
        'alg': {'key': 'alg', 'type': 'str'},
        'crv': {'key': 'crv', 'type': 'str'},
        'd': {'key': 'd', 'type': 'str'},
        'dp': {'key': 'dp', 'type': 'str'},
        'dq': {'key': 'dq', 'type': 'str'},
        'e': {'key': 'e', 'type': 'str'},
        'k': {'key': 'k', 'type': 'str'},
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'n': {'key': 'n', 'type': 'str'},
        'p': {'key': 'p', 'type': 'str'},
        'q': {'key': 'q', 'type': 'str'},
        'qi': {'key': 'qi', 'type': 'str'},
        'use': {'key': 'use', 'type': 'str'},
        'x': {'key': 'x', 'type': 'str'},
        'x5c': {'key': 'x5c', 'type': '[str]'},
        'y': {'key': 'y', 'type': 'str'},
    }

    def __init__(self, *, alg: str, kid: str, kty: str, use: str, crv: str=None, d: str=None, dp: str=None, dq: str=None, e: str=None, k: str=None, n: str=None, p: str=None, q: str=None, qi: str=None, x: str=None, x5c=None, y: str=None, **kwargs) -> None:
        super(JSONWebKey, self).__init__(**kwargs)
        self.alg = alg
        self.crv = crv
        self.d = d
        self.dp = dp
        self.dq = dq
        self.e = e
        self.k = k
        self.kid = kid
        self.kty = kty
        self.n = n
        self.p = p
        self.q = q
        self.qi = qi
        self.use = use
        self.x = x
        self.x5c = x5c
        self.y = y


class JSONWebKeySet(Model):
    """JSONWebKeySet.

    :param keys: The value of the "keys" parameter is an array of JWK values.
     By
     default, the order of the JWK values within the array does not imply
     an order of preference among them, although applications of JWK Sets
     can choose to assign a meaning to the order for their purposes, if
     desired.
    :type keys: list[~azure.mgmt.attestation.models.JSONWebKey]
    """

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[JSONWebKey]'},
    }

    def __init__(self, *, keys=None, **kwargs) -> None:
        super(JSONWebKeySet, self).__init__(**kwargs)
        self.keys = keys


class OperationList(Model):
    """List of supported operations.

    :param value: List of supported operations.
    :type value: list[~azure.mgmt.attestation.models.OperationsDefinition]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationsDefinition]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(OperationList, self).__init__(**kwargs)
        self.value = value


class OperationsDefinition(Model):
    """Definition object with the name and properties of an operation.

    :param name: Name of the operation.
    :type name: str
    :param display: Display object with properties of the operation.
    :type display: ~azure.mgmt.attestation.models.OperationsDisplayDefinition
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationsDisplayDefinition'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(OperationsDefinition, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationsDisplayDefinition(Model):
    """Display object with properties of the operation.

    :param provider: Resource provider of the operation.
    :type provider: str
    :param resource: Resource for the operation.
    :type resource: str
    :param operation: Short description of the operation.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(OperationsDisplayDefinition, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ProxyResource(Resource):
    """The resource model definition for a ARM proxy resource. It will have
    everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)
