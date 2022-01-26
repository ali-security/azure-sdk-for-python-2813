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
from ...operations._policy_exemptions_operations import build_create_or_update_request, build_delete_request, build_get_request, build_list_for_management_group_request, build_list_for_resource_group_request, build_list_for_resource_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PolicyExemptionsOperations:
    """PolicyExemptionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2020_09_01.models
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
    async def delete(
        self,
        scope: str,
        policy_exemption_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a policy exemption.

        This operation deletes a policy exemption, given its name and the scope it was created in. The
        scope of a policy exemption is the part of its ID preceding
        '/providers/Microsoft.Authorization/policyExemptions/{policyExemptionName}'.

        :param scope: The scope of the policy exemption. Valid scopes are: management group (format:
         '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format:
         '/subscriptions/{subscriptionId}'), resource group (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'.
        :type scope: str
        :param policy_exemption_name: The name of the policy exemption to delete.
        :type policy_exemption_name: str
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
            scope=scope,
            policy_exemption_name=policy_exemption_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyExemptions/{policyExemptionName}'}  # type: ignore


    @distributed_trace_async
    async def create_or_update(
        self,
        scope: str,
        policy_exemption_name: str,
        parameters: "_models.PolicyExemption",
        **kwargs: Any
    ) -> "_models.PolicyExemption":
        """Creates or updates a policy exemption.

        This operation creates or updates a policy exemption with the given scope and name. Policy
        exemptions apply to all resources contained within their scope. For example, when you create a
        policy exemption at resource group scope for a policy assignment at the same or above level,
        the exemption exempts to all applicable resources in the resource group.

        :param scope: The scope of the policy exemption. Valid scopes are: management group (format:
         '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format:
         '/subscriptions/{subscriptionId}'), resource group (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'.
        :type scope: str
        :param policy_exemption_name: The name of the policy exemption to delete.
        :type policy_exemption_name: str
        :param parameters: Parameters for the policy exemption.
        :type parameters: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemption
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyExemption, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemption
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyExemption"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'PolicyExemption')

        request = build_create_or_update_request(
            scope=scope,
            policy_exemption_name=policy_exemption_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('PolicyExemption', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PolicyExemption', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyExemptions/{policyExemptionName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        scope: str,
        policy_exemption_name: str,
        **kwargs: Any
    ) -> "_models.PolicyExemption":
        """Retrieves a policy exemption.

        This operation retrieves a single policy exemption, given its name and the scope it was created
        at.

        :param scope: The scope of the policy exemption. Valid scopes are: management group (format:
         '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format:
         '/subscriptions/{subscriptionId}'), resource group (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'.
        :type scope: str
        :param policy_exemption_name: The name of the policy exemption to delete.
        :type policy_exemption_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyExemption, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemption
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyExemption"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            scope=scope,
            policy_exemption_name=policy_exemption_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyExemption', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyExemptions/{policyExemptionName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyExemptionListResult"]:
        """Retrieves all policy exemptions that apply to a subscription.

        This operation retrieves the list of all policy exemptions associated with the given
        subscription that match the optional given $filter. Valid values for $filter are: 'atScope()',
        'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '{value}''. If $filter is not
        provided, the unfiltered list includes all policy exemptions associated with the subscription,
        including those that apply directly or from management groups that contain the given
        subscription, as well as any applied to objects contained within the subscription.

        :param filter: The filter to apply on the operation. Valid values for $filter are: 'atScope()',
         'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter is not provided, the unfiltered list includes
         all policy exemptions associated with the scope, including those that apply directly or apply
         from containing scopes. If $filter=atScope() is provided, the returned list only includes all
         policy exemptions that apply to the scope, which is everything in the unfiltered list except
         those applied to sub scopes contained within the given scope. If $filter=atExactScope() is
         provided, the returned list only includes all policy exemptions that at the given scope. If
         $filter=excludeExpired() is provided, the returned list only includes all policy exemptions
         that either haven't expired or didn't set expiration date. If $filter=policyAssignmentId eq
         '{value}' is provided. the returned list only includes all policy exemptions that are
         associated with the give policyAssignmentId.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyExemptionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemptionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyExemptionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyExemptionListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyExemptions'}  # type: ignore

    @distributed_trace
    def list_for_resource_group(
        self,
        resource_group_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyExemptionListResult"]:
        """Retrieves all policy exemptions that apply to a resource group.

        This operation retrieves the list of all policy exemptions associated with the given resource
        group in the given subscription that match the optional given $filter. Valid values for $filter
        are: 'atScope()', 'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '{value}''. If
        $filter is not provided, the unfiltered list includes all policy exemptions associated with the
        resource group, including those that apply directly or apply from containing scopes, as well as
        any applied to resources contained within the resource group.

        :param resource_group_name: The name of the resource group containing the resource.
        :type resource_group_name: str
        :param filter: The filter to apply on the operation. Valid values for $filter are: 'atScope()',
         'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter is not provided, the unfiltered list includes
         all policy exemptions associated with the scope, including those that apply directly or apply
         from containing scopes. If $filter=atScope() is provided, the returned list only includes all
         policy exemptions that apply to the scope, which is everything in the unfiltered list except
         those applied to sub scopes contained within the given scope. If $filter=atExactScope() is
         provided, the returned list only includes all policy exemptions that at the given scope. If
         $filter=excludeExpired() is provided, the returned list only includes all policy exemptions
         that either haven't expired or didn't set expiration date. If $filter=policyAssignmentId eq
         '{value}' is provided. the returned list only includes all policy exemptions that are
         associated with the give policyAssignmentId.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyExemptionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemptionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyExemptionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_for_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    filter=filter,
                    template_url=self.list_for_resource_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_for_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyExemptionListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_for_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyExemptions'}  # type: ignore

    @distributed_trace
    def list_for_resource(
        self,
        resource_group_name: str,
        resource_provider_namespace: str,
        parent_resource_path: str,
        resource_type: str,
        resource_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyExemptionListResult"]:
        """Retrieves all policy exemptions that apply to a resource.

        This operation retrieves the list of all policy exemptions associated with the specified
        resource in the given resource group and subscription that match the optional given $filter.
        Valid values for $filter are: 'atScope()', 'atExactScope()', 'excludeExpired()' or
        'policyAssignmentId eq '{value}''. If $filter is not provided, the unfiltered list includes all
        policy exemptions associated with the resource, including those that apply directly or from all
        containing scopes, as well as any applied to resources contained within the resource. Three
        parameters plus the resource name are used to identify a specific resource. If the resource is
        not part of a parent resource (the more common case), the parent resource path should not be
        provided (or provided as ''). For example a web app could be specified as
        ({resourceProviderNamespace} == 'Microsoft.Web', {parentResourcePath} == '', {resourceType} ==
        'sites', {resourceName} == 'MyWebApp'). If the resource is part of a parent resource, then all
        parameters should be provided. For example a virtual machine DNS name could be specified as
        ({resourceProviderNamespace} == 'Microsoft.Compute', {parentResourcePath} ==
        'virtualMachines/MyVirtualMachine', {resourceType} == 'domainNames', {resourceName} ==
        'MyComputerName'). A convenient alternative to providing the namespace and type name separately
        is to provide both in the {resourceType} parameter, format: ({resourceProviderNamespace} == '',
        {parentResourcePath} == '', {resourceType} == 'Microsoft.Web/sites', {resourceName} ==
        'MyWebApp').

        :param resource_group_name: The name of the resource group containing the resource.
        :type resource_group_name: str
        :param resource_provider_namespace: The namespace of the resource provider. For example, the
         namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines).
        :type resource_provider_namespace: str
        :param parent_resource_path: The parent resource path. Use empty string if there is none.
        :type parent_resource_path: str
        :param resource_type: The resource type name. For example the type name of a web app is 'sites'
         (from Microsoft.Web/sites).
        :type resource_type: str
        :param resource_name: The name of the resource.
        :type resource_name: str
        :param filter: The filter to apply on the operation. Valid values for $filter are: 'atScope()',
         'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter is not provided, the unfiltered list includes
         all policy exemptions associated with the scope, including those that apply directly or apply
         from containing scopes. If $filter=atScope() is provided, the returned list only includes all
         policy exemptions that apply to the scope, which is everything in the unfiltered list except
         those applied to sub scopes contained within the given scope. If $filter=atExactScope() is
         provided, the returned list only includes all policy exemptions that at the given scope. If
         $filter=excludeExpired() is provided, the returned list only includes all policy exemptions
         that either haven't expired or didn't set expiration date. If $filter=policyAssignmentId eq
         '{value}' is provided. the returned list only includes all policy exemptions that are
         associated with the give policyAssignmentId.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyExemptionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemptionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyExemptionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_for_resource_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    parent_resource_path=parent_resource_path,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    filter=filter,
                    template_url=self.list_for_resource.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_for_resource_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    parent_resource_path=parent_resource_path,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyExemptionListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_for_resource.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyExemptions'}  # type: ignore

    @distributed_trace
    def list_for_management_group(
        self,
        management_group_id: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyExemptionListResult"]:
        """Retrieves all policy exemptions that apply to a management group.

        This operation retrieves the list of all policy exemptions applicable to the management group
        that match the given $filter. Valid values for $filter are: 'atScope()', 'atExactScope()',
        'excludeExpired()' or 'policyAssignmentId eq '{value}''. If $filter=atScope() is provided, the
        returned list includes all policy exemptions that are assigned to the management group or the
        management group's ancestors.

        :param management_group_id: The ID of the management group.
        :type management_group_id: str
        :param filter: The filter to apply on the operation. Valid values for $filter are: 'atScope()',
         'atExactScope()', 'excludeExpired()' or 'policyAssignmentId eq '{value}''. If $filter is not
         provided, no filtering is performed. If $filter is not provided, the unfiltered list includes
         all policy exemptions associated with the scope, including those that apply directly or apply
         from containing scopes. If $filter=atScope() is provided, the returned list only includes all
         policy exemptions that apply to the scope, which is everything in the unfiltered list except
         those applied to sub scopes contained within the given scope. If $filter=atExactScope() is
         provided, the returned list only includes all policy exemptions that at the given scope. If
         $filter=excludeExpired() is provided, the returned list only includes all policy exemptions
         that either haven't expired or didn't set expiration date. If $filter=policyAssignmentId eq
         '{value}' is provided. the returned list only includes all policy exemptions that are
         associated with the give policyAssignmentId.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyExemptionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyExemptionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyExemptionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_for_management_group_request(
                    management_group_id=management_group_id,
                    filter=filter,
                    template_url=self.list_for_management_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_for_management_group_request(
                    management_group_id=management_group_id,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyExemptionListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_for_management_group.metadata = {'url': '/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Authorization/policyExemptions'}  # type: ignore
