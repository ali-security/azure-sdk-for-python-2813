# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._secrets_operations import build_create_or_update_request, build_get_request, build_list_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SecretsOperations:
    """SecretsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.keyvault.v2021_06_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        vault_name: str,
        secret_name: str,
        parameters: "_models.SecretCreateOrUpdateParameters",
        **kwargs: Any
    ) -> "_models.Secret":
        """Create or update a secret in a key vault in the specified subscription.  NOTE: This API is
        intended for internal use in ARM deployments. Users should use the data-plane REST service for
        interaction with vault secrets.

        :param resource_group_name: The name of the Resource Group to which the vault belongs.
        :type resource_group_name: str
        :param vault_name: Name of the vault.
        :type vault_name: str
        :param secret_name: Name of the secret.
        :type secret_name: str
        :param parameters: Parameters to create or update the secret.
        :type parameters:
         ~azure.mgmt.keyvault.v2021_06_01_preview.models.SecretCreateOrUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Secret, or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_06_01_preview.models.Secret
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Secret"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'SecretCreateOrUpdateParameters')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            secret_name=secret_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('Secret', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Secret', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName}"}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        vault_name: str,
        secret_name: str,
        parameters: "_models.SecretPatchParameters",
        **kwargs: Any
    ) -> "_models.Secret":
        """Update a secret in the specified subscription.  NOTE: This API is intended for internal use in
        ARM deployments.  Users should use the data-plane REST service for interaction with vault
        secrets.

        :param resource_group_name: The name of the Resource Group to which the vault belongs.
        :type resource_group_name: str
        :param vault_name: Name of the vault.
        :type vault_name: str
        :param secret_name: Name of the secret.
        :type secret_name: str
        :param parameters: Parameters to patch the secret.
        :type parameters: ~azure.mgmt.keyvault.v2021_06_01_preview.models.SecretPatchParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Secret, or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_06_01_preview.models.Secret
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Secret"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'SecretPatchParameters')

        request = build_update_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            secret_name=secret_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('Secret', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Secret', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName}"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        vault_name: str,
        secret_name: str,
        **kwargs: Any
    ) -> "_models.Secret":
        """Gets the specified secret.  NOTE: This API is intended for internal use in ARM deployments.
        Users should use the data-plane REST service for interaction with vault secrets.

        :param resource_group_name: The name of the Resource Group to which the vault belongs.
        :type resource_group_name: str
        :param vault_name: The name of the vault.
        :type vault_name: str
        :param secret_name: The name of the secret.
        :type secret_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Secret, or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_06_01_preview.models.Secret
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Secret"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-01-preview")  # type: str

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            secret_name=secret_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Secret', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName}"}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        vault_name: str,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.SecretListResult"]:
        """The List operation gets information about the secrets in a vault.  NOTE: This API is intended
        for internal use in ARM deployments. Users should use the data-plane REST service for
        interaction with vault secrets.

        :param resource_group_name: The name of the Resource Group to which the vault belongs.
        :type resource_group_name: str
        :param vault_name: The name of the vault.
        :type vault_name: str
        :param top: Maximum number of results to return. Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecretListResult or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.keyvault.v2021_06_01_preview.models.SecretListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-06-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SecretListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    top=top,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecretListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets"}  # type: ignore
