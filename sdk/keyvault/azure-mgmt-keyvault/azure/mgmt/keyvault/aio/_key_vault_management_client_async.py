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

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration_async import KeyVaultManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class KeyVaultManagementClient(MultiApiClientMixin, _SDKClient):
    """The Azure management API provides a RESTful set of web services that interact with Azure Key Vault.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2019-09-01'
    _PROFILE_TAG = "azure.mgmt.keyvault.KeyVaultManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = KeyVaultManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(KeyVaultManagementClient, self).__init__(
            credential,
            self._config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-10-01: :mod:`v2016_10_01.models<azure.mgmt.keyvault.v2016_10_01.models>`
           * 2018-02-14: :mod:`v2018_02_14.models<azure.mgmt.keyvault.v2018_02_14.models>`
           * 2019-09-01: :mod:`v2019_09_01.models<azure.mgmt.keyvault.v2019_09_01.models>`
        """
        if api_version == '2016-10-01':
            from ..v2016_10_01 import models
            return models
        elif api_version == '2018-02-14':
            from ..v2018_02_14 import models
            return models
        elif api_version == '2019-09-01':
            from ..v2019_09_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2016-10-01: :class:`Operations<azure.mgmt.keyvault.v2016_10_01.aio.operations_async.Operations>`
           * 2018-02-14: :class:`Operations<azure.mgmt.keyvault.v2018_02_14.aio.operations_async.Operations>`
           * 2019-09-01: :class:`Operations<azure.mgmt.keyvault.v2019_09_01.aio.operations_async.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2016-10-01':
            from ..v2016_10_01.aio.operations_async import Operations as OperationClass
        elif api_version == '2018-02-14':
            from ..v2018_02_14.aio.operations_async import Operations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations_async import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2018-02-14: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2018_02_14.aio.operations_async.PrivateEndpointConnectionsOperations>`
           * 2019-09-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2019_09_01.aio.operations_async.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2018-02-14':
            from ..v2018_02_14.aio.operations_async import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations_async import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2018-02-14: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2018_02_14.aio.operations_async.PrivateLinkResourcesOperations>`
           * 2019-09-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2019_09_01.aio.operations_async.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2018-02-14':
            from ..v2018_02_14.aio.operations_async import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations_async import PrivateLinkResourcesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def vaults(self):
        """Instance depends on the API version:

           * 2016-10-01: :class:`VaultsOperations<azure.mgmt.keyvault.v2016_10_01.aio.operations_async.VaultsOperations>`
           * 2018-02-14: :class:`VaultsOperations<azure.mgmt.keyvault.v2018_02_14.aio.operations_async.VaultsOperations>`
           * 2019-09-01: :class:`VaultsOperations<azure.mgmt.keyvault.v2019_09_01.aio.operations_async.VaultsOperations>`
        """
        api_version = self._get_api_version('vaults')
        if api_version == '2016-10-01':
            from ..v2016_10_01.aio.operations_async import VaultsOperations as OperationClass
        elif api_version == '2018-02-14':
            from ..v2018_02_14.aio.operations_async import VaultsOperations as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations_async import VaultsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
