# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._data_flow_debug_session_operations import (
    build_add_data_flow_request,
    build_create_data_flow_debug_session_request,
    build_delete_data_flow_debug_session_request,
    build_execute_command_request,
    build_query_data_flow_debug_sessions_by_workspace_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DataFlowDebugSessionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.synapse.artifacts.aio.ArtifactsClient`'s
        :attr:`data_flow_debug_session` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_data_flow_debug_session_initial(
        self, request: Union[_models.CreateDataFlowDebugSessionRequest, IO], **kwargs: Any
    ) -> Optional[_models.CreateDataFlowDebugSessionResponse]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.CreateDataFlowDebugSessionResponse]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _json = self._serialize.body(request, "CreateDataFlowDebugSessionRequest")

        request = build_create_data_flow_debug_session_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_data_flow_debug_session_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("CreateDataFlowDebugSessionResponse", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _create_data_flow_debug_session_initial.metadata = {"url": "/createDataFlowDebugSession"}

    @overload
    async def begin_create_data_flow_debug_session(
        self,
        request: _models.CreateDataFlowDebugSessionRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CreateDataFlowDebugSessionResponse]:
        """Creates a data flow debug session.

        :param request: Data flow debug session definition. Required.
        :type request: ~azure.synapse.artifacts.models.CreateDataFlowDebugSessionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CreateDataFlowDebugSessionResponse
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.CreateDataFlowDebugSessionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_data_flow_debug_session(
        self, request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.CreateDataFlowDebugSessionResponse]:
        """Creates a data flow debug session.

        :param request: Data flow debug session definition. Required.
        :type request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CreateDataFlowDebugSessionResponse
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.CreateDataFlowDebugSessionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_data_flow_debug_session(
        self, request: Union[_models.CreateDataFlowDebugSessionRequest, IO], **kwargs: Any
    ) -> AsyncLROPoller[_models.CreateDataFlowDebugSessionResponse]:
        """Creates a data flow debug session.

        :param request: Data flow debug session definition. Is either a
         CreateDataFlowDebugSessionRequest type or a IO type. Required.
        :type request: ~azure.synapse.artifacts.models.CreateDataFlowDebugSessionRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CreateDataFlowDebugSessionResponse
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.CreateDataFlowDebugSessionResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CreateDataFlowDebugSessionResponse] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_data_flow_debug_session_initial(
                request=request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("CreateDataFlowDebugSessionResponse", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_create_data_flow_debug_session.metadata = {"url": "/createDataFlowDebugSession"}

    @distributed_trace
    def query_data_flow_debug_sessions_by_workspace(
        self, **kwargs: Any
    ) -> AsyncIterable["_models.DataFlowDebugSessionInfo"]:
        """Query all active data flow debug sessions.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DataFlowDebugSessionInfo or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.synapse.artifacts.models.DataFlowDebugSessionInfo]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[_models.QueryDataFlowDebugSessionsResponse] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_query_data_flow_debug_sessions_by_workspace_request(
                    api_version=api_version,
                    template_url=self.query_data_flow_debug_sessions_by_workspace.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("QueryDataFlowDebugSessionsResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    query_data_flow_debug_sessions_by_workspace.metadata = {"url": "/queryDataFlowDebugSessions"}

    @overload
    async def add_data_flow(
        self, request: _models.DataFlowDebugPackage, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AddDataFlowToDebugSessionResponse:
        """Add a data flow into debug session.

        :param request: Data flow debug session definition with debug content. Required.
        :type request: ~azure.synapse.artifacts.models.DataFlowDebugPackage
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddDataFlowToDebugSessionResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.AddDataFlowToDebugSessionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def add_data_flow(
        self, request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AddDataFlowToDebugSessionResponse:
        """Add a data flow into debug session.

        :param request: Data flow debug session definition with debug content. Required.
        :type request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddDataFlowToDebugSessionResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.AddDataFlowToDebugSessionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def add_data_flow(
        self, request: Union[_models.DataFlowDebugPackage, IO], **kwargs: Any
    ) -> _models.AddDataFlowToDebugSessionResponse:
        """Add a data flow into debug session.

        :param request: Data flow debug session definition with debug content. Is either a
         DataFlowDebugPackage type or a IO type. Required.
        :type request: ~azure.synapse.artifacts.models.DataFlowDebugPackage or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddDataFlowToDebugSessionResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.AddDataFlowToDebugSessionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AddDataFlowToDebugSessionResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _json = self._serialize.body(request, "DataFlowDebugPackage")

        request = build_add_data_flow_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.add_data_flow.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("AddDataFlowToDebugSessionResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add_data_flow.metadata = {"url": "/addDataFlowToDebugSession"}

    @overload
    async def delete_data_flow_debug_session(  # pylint: disable=inconsistent-return-statements
        self,
        request: _models.DeleteDataFlowDebugSessionRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Deletes a data flow debug session.

        :param request: Data flow debug session definition for deletion. Required.
        :type request: ~azure.synapse.artifacts.models.DeleteDataFlowDebugSessionRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def delete_data_flow_debug_session(  # pylint: disable=inconsistent-return-statements
        self, request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Deletes a data flow debug session.

        :param request: Data flow debug session definition for deletion. Required.
        :type request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def delete_data_flow_debug_session(  # pylint: disable=inconsistent-return-statements
        self, request: Union[_models.DeleteDataFlowDebugSessionRequest, IO], **kwargs: Any
    ) -> None:
        """Deletes a data flow debug session.

        :param request: Data flow debug session definition for deletion. Is either a
         DeleteDataFlowDebugSessionRequest type or a IO type. Required.
        :type request: ~azure.synapse.artifacts.models.DeleteDataFlowDebugSessionRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _json = self._serialize.body(request, "DeleteDataFlowDebugSessionRequest")

        request = build_delete_data_flow_debug_session_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.delete_data_flow_debug_session.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    delete_data_flow_debug_session.metadata = {"url": "/deleteDataFlowDebugSession"}

    async def _execute_command_initial(
        self, request: Union[_models.DataFlowDebugCommandRequest, IO], **kwargs: Any
    ) -> Optional[_models.DataFlowDebugCommandResponse]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.DataFlowDebugCommandResponse]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(request, (IOBase, bytes)):
            _content = request
        else:
            _json = self._serialize.body(request, "DataFlowDebugCommandRequest")

        request = build_execute_command_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._execute_command_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("DataFlowDebugCommandResponse", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _execute_command_initial.metadata = {"url": "/executeDataFlowDebugCommand"}

    @overload
    async def begin_execute_command(
        self, request: _models.DataFlowDebugCommandRequest, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.DataFlowDebugCommandResponse]:
        """Execute a data flow debug command.

        :param request: Data flow debug command definition. Required.
        :type request: ~azure.synapse.artifacts.models.DataFlowDebugCommandRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either DataFlowDebugCommandResponse or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.DataFlowDebugCommandResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_execute_command(
        self, request: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.DataFlowDebugCommandResponse]:
        """Execute a data flow debug command.

        :param request: Data flow debug command definition. Required.
        :type request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either DataFlowDebugCommandResponse or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.DataFlowDebugCommandResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_execute_command(
        self, request: Union[_models.DataFlowDebugCommandRequest, IO], **kwargs: Any
    ) -> AsyncLROPoller[_models.DataFlowDebugCommandResponse]:
        """Execute a data flow debug command.

        :param request: Data flow debug command definition. Is either a DataFlowDebugCommandRequest
         type or a IO type. Required.
        :type request: ~azure.synapse.artifacts.models.DataFlowDebugCommandRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either DataFlowDebugCommandResponse or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.DataFlowDebugCommandResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataFlowDebugCommandResponse] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._execute_command_initial(
                request=request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("DataFlowDebugCommandResponse", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_execute_command.metadata = {"url": "/executeDataFlowDebugCommand"}
