# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_at_management_group_scope_request(
    group_id: str,
    deployment_name: str,
    operation_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-05-10"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId}')
    path_format_arguments = {
        "groupId": _SERIALIZER.url("group_id", group_id, 'str', max_length=90, min_length=1),
        "deploymentName": _SERIALIZER.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "operationId": _SERIALIZER.url("operation_id", operation_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_at_management_group_scope_request(
    group_id: str,
    deployment_name: str,
    *,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-05-10"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations')
    path_format_arguments = {
        "groupId": _SERIALIZER.url("group_id", group_id, 'str', max_length=90, min_length=1),
        "deploymentName": _SERIALIZER.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_at_subscription_scope_request(
    deployment_name: str,
    operation_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-05-10"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId}')
    path_format_arguments = {
        "deploymentName": _SERIALIZER.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "operationId": _SERIALIZER.url("operation_id", operation_id, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_at_subscription_scope_request(
    deployment_name: str,
    subscription_id: str,
    *,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-05-10"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations')
    path_format_arguments = {
        "deploymentName": _SERIALIZER.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    deployment_name: str,
    operation_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-05-10"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations/{operationId}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "deploymentName": _SERIALIZER.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "operationId": _SERIALIZER.url("operation_id", operation_id, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    resource_group_name: str,
    deployment_name: str,
    subscription_id: str,
    *,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-05-10"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "deploymentName": _SERIALIZER.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class DeploymentOperationsOperations(object):
    """DeploymentOperationsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.resources.v2019_05_10.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_at_management_group_scope(
        self,
        group_id: str,
        deployment_name: str,
        operation_id: str,
        **kwargs: Any
    ) -> "_models.DeploymentOperation":
        """Gets a deployments operation.

        :param group_id: The management group ID.
        :type group_id: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param operation_id: The ID of the operation to get.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeploymentOperation, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_05_10.models.DeploymentOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_at_management_group_scope_request(
            group_id=group_id,
            deployment_name=deployment_name,
            operation_id=operation_id,
            template_url=self.get_at_management_group_scope.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeploymentOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_at_management_group_scope.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId}'}  # type: ignore


    @distributed_trace
    def list_at_management_group_scope(
        self,
        group_id: str,
        deployment_name: str,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.DeploymentOperationsListResult"]:
        """Gets all deployments operations for a deployment.

        :param group_id: The management group ID.
        :type group_id: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param top: The number of results to return.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DeploymentOperationsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.resources.v2019_05_10.models.DeploymentOperationsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentOperationsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_at_management_group_scope_request(
                    group_id=group_id,
                    deployment_name=deployment_name,
                    top=top,
                    template_url=self.list_at_management_group_scope.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_at_management_group_scope_request(
                    group_id=group_id,
                    deployment_name=deployment_name,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DeploymentOperationsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_at_management_group_scope.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{groupId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations'}  # type: ignore

    @distributed_trace
    def get_at_subscription_scope(
        self,
        deployment_name: str,
        operation_id: str,
        **kwargs: Any
    ) -> "_models.DeploymentOperation":
        """Gets a deployments operation.

        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param operation_id: The ID of the operation to get.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeploymentOperation, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_05_10.models.DeploymentOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_at_subscription_scope_request(
            deployment_name=deployment_name,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            template_url=self.get_at_subscription_scope.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeploymentOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_at_subscription_scope.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations/{operationId}'}  # type: ignore


    @distributed_trace
    def list_at_subscription_scope(
        self,
        deployment_name: str,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.DeploymentOperationsListResult"]:
        """Gets all deployments operations for a deployment.

        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param top: The number of results to return.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DeploymentOperationsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.resources.v2019_05_10.models.DeploymentOperationsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentOperationsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_at_subscription_scope_request(
                    deployment_name=deployment_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    template_url=self.list_at_subscription_scope.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_at_subscription_scope_request(
                    deployment_name=deployment_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DeploymentOperationsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_at_subscription_scope.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deployments/{deploymentName}/operations'}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        deployment_name: str,
        operation_id: str,
        **kwargs: Any
    ) -> "_models.DeploymentOperation":
        """Gets a deployments operation.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param operation_id: The ID of the operation to get.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeploymentOperation, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_05_10.models.DeploymentOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            deployment_name=deployment_name,
            operation_id=operation_id,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeploymentOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations/{operationId}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        deployment_name: str,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.DeploymentOperationsListResult"]:
        """Gets all deployments operations for a deployment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param top: The number of results to return.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DeploymentOperationsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.resources.v2019_05_10.models.DeploymentOperationsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeploymentOperationsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    deployment_name=deployment_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    deployment_name=deployment_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DeploymentOperationsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/deployments/{deploymentName}/operations'}  # type: ignore
