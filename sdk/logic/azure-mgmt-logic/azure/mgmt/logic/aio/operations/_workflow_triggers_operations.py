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
from ...operations._workflow_triggers_operations import build_get_request, build_get_schema_json_request, build_list_callback_url_request, build_list_request, build_reset_request, build_run_request, build_set_state_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class WorkflowTriggersOperations:
    """WorkflowTriggersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.logic.models
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

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        workflow_name: str,
        top: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.WorkflowTriggerListResult"]:
        """Gets a list of workflow triggers.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param top: The number of items to be included in the result. Default value is None.
        :type top: int
        :param filter: The filter to apply on the operation. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either WorkflowTriggerListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.logic.models.WorkflowTriggerListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.WorkflowTriggerListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workflow_name=workflow_name,
                    api_version=api_version,
                    top=top,
                    filter=filter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workflow_name=workflow_name,
                    api_version=api_version,
                    top=top,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("WorkflowTriggerListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        workflow_name: str,
        trigger_name: str,
        **kwargs: Any
    ) -> "_models.WorkflowTrigger":
        """Gets a workflow trigger.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTrigger, or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.WorkflowTrigger
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.WorkflowTrigger"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('WorkflowTrigger', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}"}  # type: ignore


    @distributed_trace_async
    async def reset(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        workflow_name: str,
        trigger_name: str,
        **kwargs: Any
    ) -> None:
        """Resets a workflow trigger.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
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

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str

        
        request = build_reset_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            api_version=api_version,
            template_url=self.reset.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    reset.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/reset"}  # type: ignore


    @distributed_trace_async
    async def run(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        workflow_name: str,
        trigger_name: str,
        **kwargs: Any
    ) -> None:
        """Runs a workflow trigger.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
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

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str

        
        request = build_run_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            api_version=api_version,
            template_url=self.run.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    run.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/run"}  # type: ignore


    @distributed_trace_async
    async def get_schema_json(
        self,
        resource_group_name: str,
        workflow_name: str,
        trigger_name: str,
        **kwargs: Any
    ) -> "_models.JsonSchema":
        """Get the trigger schema as JSON.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JsonSchema, or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.JsonSchema
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.JsonSchema"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str

        
        request = build_get_schema_json_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            api_version=api_version,
            template_url=self.get_schema_json.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JsonSchema', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_schema_json.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/schemas/json"}  # type: ignore


    @distributed_trace_async
    async def set_state(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        workflow_name: str,
        trigger_name: str,
        set_state: "_models.SetTriggerStateActionDefinition",
        **kwargs: Any
    ) -> None:
        """Sets the state of a workflow trigger.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
        :param set_state: The workflow trigger state.
        :type set_state: ~azure.mgmt.logic.models.SetTriggerStateActionDefinition
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

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(set_state, 'SetTriggerStateActionDefinition')

        request = build_set_state_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.set_state.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_state.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/setState"}  # type: ignore


    @distributed_trace_async
    async def list_callback_url(
        self,
        resource_group_name: str,
        workflow_name: str,
        trigger_name: str,
        **kwargs: Any
    ) -> "_models.WorkflowTriggerCallbackUrl":
        """Get the callback URL for a workflow trigger.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workflow_name: The workflow name.
        :type workflow_name: str
        :param trigger_name: The workflow trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl, or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.WorkflowTriggerCallbackUrl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.WorkflowTriggerCallbackUrl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2019-05-01")  # type: str

        
        request = build_list_callback_url_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workflow_name=workflow_name,
            trigger_name=trigger_name,
            api_version=api_version,
            template_url=self.list_callback_url.metadata['url'],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('WorkflowTriggerCallbackUrl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_callback_url.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/listCallbackUrl"}  # type: ignore

