# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class OSUpdatesOperations:
    """OSUpdatesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~test_base.models
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

    def list(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        package_name: str,
        os_update_type: Union[str, "_models.OsUpdateType"],
        **kwargs: Any
    ) -> AsyncIterable["_models.OSUpdateListResult"]:
        """Lists the OS Updates in which the package were tested before.

        :param resource_group_name: The name of the resource group that contains the resource.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account.
        :type test_base_account_name: str
        :param package_name: The resource name of the Test Base Package.
        :type package_name: str
        :param os_update_type: The type of the OS Update.
        :type os_update_type: str or ~test_base.models.OsUpdateType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OSUpdateListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~test_base.models.OSUpdateListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OSUpdateListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-16-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'testBaseAccountName': self._serialize.url("test_base_account_name", test_base_account_name, 'str'),
                    'packageName': self._serialize.url("package_name", package_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['osUpdateType'] = self._serialize.query("os_update_type", os_update_type, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('OSUpdateListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/packages/{packageName}/osUpdates'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        package_name: str,
        os_update_resource_name: str,
        **kwargs: Any
    ) -> "_models.OSUpdateResource":
        """Gets an OS Update by name in which the package was tested before.

        :param resource_group_name: The name of the resource group that contains the resource.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account.
        :type test_base_account_name: str
        :param package_name: The resource name of the Test Base Package.
        :type package_name: str
        :param os_update_resource_name: The resource name of an OS Update.
        :type os_update_resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OSUpdateResource, or the result of cls(response)
        :rtype: ~test_base.models.OSUpdateResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OSUpdateResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-16-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'testBaseAccountName': self._serialize.url("test_base_account_name", test_base_account_name, 'str'),
            'packageName': self._serialize.url("package_name", package_name, 'str'),
            'osUpdateResourceName': self._serialize.url("os_update_resource_name", os_update_resource_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('OSUpdateResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/packages/{packageName}/osUpdates/{osUpdateResourceName}'}  # type: ignore
