# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

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
from ...operations._policy_set_definitions_operations import build_create_or_update_at_management_group_request, build_create_or_update_request, build_delete_at_management_group_request, build_delete_request, build_get_at_management_group_request, build_get_built_in_request, build_get_request, build_list_built_in_request, build_list_by_management_group_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PolicySetDefinitionsOperations:
    """PolicySetDefinitionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2018_05_01.models
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
        policy_set_definition_name: str,
        parameters: "_models.PolicySetDefinition",
        **kwargs: Any
    ) -> "_models.PolicySetDefinition":
        """Creates or updates a policy set definition.

        This operation creates or updates a policy set definition in the given subscription with the
        given name.

        :param policy_set_definition_name: The name of the policy set definition to create.
        :type policy_set_definition_name: str
        :param parameters: The policy set definition properties.
        :type parameters: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicySetDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'PolicySetDefinition')

        request = build_create_or_update_request(
            policy_set_definition_name=policy_set_definition_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        policy_set_definition_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a policy set definition.

        This operation deletes the policy set definition in the given subscription with the given name.

        :param policy_set_definition_name: The name of the policy set definition to delete.
        :type policy_set_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            policy_set_definition_name=policy_set_definition_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        policy_set_definition_name: str,
        **kwargs: Any
    ) -> "_models.PolicySetDefinition":
        """Retrieves a policy set definition.

        This operation retrieves the policy set definition in the given subscription with the given
        name.

        :param policy_set_definition_name: The name of the policy set definition to get.
        :type policy_set_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicySetDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            policy_set_definition_name=policy_set_definition_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace_async
    async def get_built_in(
        self,
        policy_set_definition_name: str,
        **kwargs: Any
    ) -> "_models.PolicySetDefinition":
        """Retrieves a built in policy set definition.

        This operation retrieves the built-in policy set definition with the given name.

        :param policy_set_definition_name: The name of the policy set definition to get.
        :type policy_set_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicySetDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_built_in_request(
            policy_set_definition_name=policy_set_definition_name,
            template_url=self.get_built_in.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_built_in.metadata = {'url': '/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicySetDefinitionListResult"]:
        """Retrieves the policy set definitions for a subscription.

        This operation retrieves a list of all the policy set definitions in the given subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicySetDefinitionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicySetDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions'}  # type: ignore

    @distributed_trace
    def list_built_in(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicySetDefinitionListResult"]:
        """Retrieves built-in policy set definitions.

        This operation retrieves a list of all the built-in policy set definitions.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicySetDefinitionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_built_in_request(
                    template_url=self.list_built_in.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_built_in_request(
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicySetDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_built_in.metadata = {'url': '/providers/Microsoft.Authorization/policySetDefinitions'}  # type: ignore

    @distributed_trace_async
    async def create_or_update_at_management_group(
        self,
        policy_set_definition_name: str,
        management_group_id: str,
        parameters: "_models.PolicySetDefinition",
        **kwargs: Any
    ) -> "_models.PolicySetDefinition":
        """Creates or updates a policy set definition.

        This operation creates or updates a policy set definition in the given management group with
        the given name.

        :param policy_set_definition_name: The name of the policy set definition to create.
        :type policy_set_definition_name: str
        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :param parameters: The policy set definition properties.
        :type parameters: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicySetDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'PolicySetDefinition')

        request = build_create_or_update_at_management_group_request(
            policy_set_definition_name=policy_set_definition_name,
            management_group_id=management_group_id,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update_at_management_group.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update_at_management_group.metadata = {'url': '/providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace_async
    async def delete_at_management_group(
        self,
        policy_set_definition_name: str,
        management_group_id: str,
        **kwargs: Any
    ) -> None:
        """Deletes a policy set definition.

        This operation deletes the policy set definition in the given management group with the given
        name.

        :param policy_set_definition_name: The name of the policy set definition to delete.
        :type policy_set_definition_name: str
        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_at_management_group_request(
            policy_set_definition_name=policy_set_definition_name,
            management_group_id=management_group_id,
            template_url=self.delete_at_management_group.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_at_management_group.metadata = {'url': '/providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace_async
    async def get_at_management_group(
        self,
        policy_set_definition_name: str,
        management_group_id: str,
        **kwargs: Any
    ) -> "_models.PolicySetDefinition":
        """Retrieves a policy set definition.

        This operation retrieves the policy set definition in the given management group with the given
        name.

        :param policy_set_definition_name: The name of the policy set definition to get.
        :type policy_set_definition_name: str
        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicySetDefinition, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_at_management_group_request(
            policy_set_definition_name=policy_set_definition_name,
            management_group_id=management_group_id,
            template_url=self.get_at_management_group.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicySetDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_at_management_group.metadata = {'url': '/providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName}'}  # type: ignore


    @distributed_trace
    def list_by_management_group(
        self,
        management_group_id: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicySetDefinitionListResult"]:
        """Retrieves all policy set definitions in management group.

        This operation retrieves a list of all the a policy set definition in the given management
        group.

        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicySetDefinitionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2018_05_01.models.PolicySetDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicySetDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_management_group_request(
                    management_group_id=management_group_id,
                    template_url=self.list_by_management_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_management_group_request(
                    management_group_id=management_group_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicySetDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_management_group.metadata = {'url': '/providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions'}  # type: ignore
