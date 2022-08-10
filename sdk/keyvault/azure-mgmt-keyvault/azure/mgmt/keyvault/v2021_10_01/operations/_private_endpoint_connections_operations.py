# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union, cast

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    vault_name: str,
    private_endpoint_connection_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str', pattern=r'^[a-zA-Z0-9-]{3,24}$'),
        "privateEndpointConnectionName": _SERIALIZER.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_put_request(
    subscription_id: str,
    resource_group_name: str,
    vault_name: str,
    private_endpoint_connection_name: str,
    *,
    json: Optional[_models.PrivateEndpointConnection] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str', pattern=r'^[a-zA-Z0-9-]{3,24}$'),
        "privateEndpointConnectionName": _SERIALIZER.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request_initial(
    subscription_id: str,
    resource_group_name: str,
    vault_name: str,
    private_endpoint_connection_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str', pattern=r'^[a-zA-Z0-9-]{3,24}$'),
        "privateEndpointConnectionName": _SERIALIZER.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_list_by_resource_request(
    subscription_id: str,
    resource_group_name: str,
    vault_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "vaultName": _SERIALIZER.url("vault_name", vault_name, 'str', pattern=r'^[a-zA-Z0-9-]{3,24}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class PrivateEndpointConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.keyvault.v2021_10_01.KeyVaultManagementClient`'s
        :attr:`private_endpoint_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        **kwargs: Any
    ) -> Optional[_models.PrivateEndpointConnection]:
        """Gets the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault.
        :type resource_group_name: str
        :param vault_name: The name of the key vault.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection, or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.PrivateEndpointConnection or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.PrivateEndpointConnection]]

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore


    @distributed_trace
    def put(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        properties: _models.PrivateEndpointConnection,
        **kwargs: Any
    ) -> _models.PrivateEndpointConnection:
        """Updates the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault.
        :type resource_group_name: str
        :param vault_name: The name of the key vault.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault.
        :type private_endpoint_connection_name: str
        :param properties: The intended state of private endpoint connection.
        :type properties: ~azure.mgmt.keyvault.v2021_10_01.models.PrivateEndpointConnection
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PrivateEndpointConnection, or the result of cls(response)
        :rtype: ~azure.mgmt.keyvault.v2021_10_01.models.PrivateEndpointConnection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PrivateEndpointConnection]

        _json = self._serialize.body(properties, 'PrivateEndpointConnection')

        request = build_put_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.put.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))

        deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    put.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore


    def _delete_initial(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        **kwargs: Any
    ) -> Optional[_models.PrivateEndpointConnection]:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.PrivateEndpointConnection]]

        
        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)

        if response.status_code == 202:
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _delete_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore


    @distributed_trace
    def begin_delete(
        self,
        resource_group_name: str,
        vault_name: str,
        private_endpoint_connection_name: str,
        **kwargs: Any
    ) -> LROPoller[_models.PrivateEndpointConnection]:
        """Deletes the specified private endpoint connection associated with the key vault.

        :param resource_group_name: Name of the resource group that contains the key vault.
        :type resource_group_name: str
        :param vault_name: The name of the key vault.
        :type vault_name: str
        :param private_endpoint_connection_name: Name of the private endpoint connection associated
         with the key vault.
        :type private_endpoint_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either PrivateEndpointConnection or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.keyvault.v2021_10_01.models.PrivateEndpointConnection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PrivateEndpointConnection]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vault_name=vault_name,
                private_endpoint_connection_name=private_endpoint_connection_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('PrivateEndpointConnection', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True:
            polling_method = cast(PollingMethod, ARMPolling(
                lro_delay,
                
                
                **kwargs
        ))  # type: PollingMethod
        elif polling is False: polling_method = cast(PollingMethod, NoPolling())
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName}"}  # type: ignore

    @distributed_trace
    def list_by_resource(
        self,
        resource_group_name: str,
        vault_name: str,
        **kwargs: Any
    ) -> Iterable[_models.PrivateEndpointConnectionListResult]:
        """The List operation gets information about the private endpoint connections associated with the
        vault.

        :param resource_group_name: Name of the resource group that contains the key vault.
        :type resource_group_name: str
        :param vault_name: The name of the key vault.
        :type vault_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PrivateEndpointConnectionListResult or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.keyvault.v2021_10_01.models.PrivateEndpointConnectionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.PrivateEndpointConnectionListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    api_version=api_version,
                    template_url=self.list_by_resource.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_resource_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    vault_name=vault_name,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PrivateEndpointConnectionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections"}  # type: ignore
