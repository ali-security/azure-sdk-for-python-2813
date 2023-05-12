# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
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
from ...operations._pipeline_operations import (
    build_create_or_update_pipeline_request,
    build_create_pipeline_run_request,
    build_delete_pipeline_request,
    build_get_pipeline_request,
    build_get_pipelines_by_workspace_request,
    build_rename_pipeline_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PipelineOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.synapse.artifacts.aio.ArtifactsClient`'s
        :attr:`pipeline` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_pipelines_by_workspace(self, **kwargs: Any) -> AsyncIterable["_models.PipelineResource"]:
        """Lists pipelines.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PipelineResource or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.synapse.artifacts.models.PipelineResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[_models.PipelineListResponse] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_get_pipelines_by_workspace_request(
                    api_version=api_version,
                    template_url=self.get_pipelines_by_workspace.metadata["url"],
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
            deserialized = self._deserialize("PipelineListResponse", pipeline_response)
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

    get_pipelines_by_workspace.metadata = {"url": "/pipelines"}

    async def _create_or_update_pipeline_initial(
        self,
        pipeline_name: str,
        pipeline: Union[_models.PipelineResource, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> Optional[_models.PipelineResource]:
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
        cls: ClsType[Optional[_models.PipelineResource]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(pipeline, (IOBase, bytes)):
            _content = pipeline
        else:
            _json = self._serialize.body(pipeline, "PipelineResource")

        request = build_create_or_update_pipeline_request(
            pipeline_name=pipeline_name,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_or_update_pipeline_initial.metadata["url"],
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
        if response.status_code == 200:
            deserialized = self._deserialize("PipelineResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_pipeline_initial.metadata = {"url": "/pipelines/{pipelineName}"}

    @overload
    async def begin_create_or_update_pipeline(
        self,
        pipeline_name: str,
        pipeline: _models.PipelineResource,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.PipelineResource]:
        """Creates or updates a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param pipeline: Pipeline resource definition. Required.
        :type pipeline: ~azure.synapse.artifacts.models.PipelineResource
        :param if_match: ETag of the pipeline entity.  Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update. Default value is None.
        :type if_match: str
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
        :return: An instance of AsyncLROPoller that returns either PipelineResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.PipelineResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update_pipeline(
        self,
        pipeline_name: str,
        pipeline: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.PipelineResource]:
        """Creates or updates a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param pipeline: Pipeline resource definition. Required.
        :type pipeline: IO
        :param if_match: ETag of the pipeline entity.  Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update. Default value is None.
        :type if_match: str
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
        :return: An instance of AsyncLROPoller that returns either PipelineResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.PipelineResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update_pipeline(
        self,
        pipeline_name: str,
        pipeline: Union[_models.PipelineResource, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.PipelineResource]:
        """Creates or updates a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param pipeline: Pipeline resource definition. Is either a PipelineResource type or a IO type.
         Required.
        :type pipeline: ~azure.synapse.artifacts.models.PipelineResource or IO
        :param if_match: ETag of the pipeline entity.  Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update. Default value is None.
        :type if_match: str
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
        :return: An instance of AsyncLROPoller that returns either PipelineResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.synapse.artifacts.models.PipelineResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PipelineResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_pipeline_initial(
                pipeline_name=pipeline_name,
                pipeline=pipeline,
                if_match=if_match,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("PipelineResource", pipeline_response)
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

    begin_create_or_update_pipeline.metadata = {"url": "/pipelines/{pipelineName}"}

    @distributed_trace_async
    async def get_pipeline(
        self, pipeline_name: str, if_none_match: Optional[str] = None, **kwargs: Any
    ) -> Optional[_models.PipelineResource]:
        """Gets a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param if_none_match: ETag of the pipeline entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
         Default value is None.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineResource or None or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.PipelineResource or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[Optional[_models.PipelineResource]] = kwargs.pop("cls", None)

        request = build_get_pipeline_request(
            pipeline_name=pipeline_name,
            if_none_match=if_none_match,
            api_version=api_version,
            template_url=self.get_pipeline.metadata["url"],
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

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("PipelineResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_pipeline.metadata = {"url": "/pipelines/{pipelineName}"}

    async def _delete_pipeline_initial(  # pylint: disable=inconsistent-return-statements
        self, pipeline_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_pipeline_request(
            pipeline_name=pipeline_name,
            api_version=api_version,
            template_url=self._delete_pipeline_initial.metadata["url"],
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

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_pipeline_initial.metadata = {"url": "/pipelines/{pipelineName}"}

    @distributed_trace_async
    async def begin_delete_pipeline(self, pipeline_name: str, **kwargs: Any) -> AsyncLROPoller[None]:
        """Deletes a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_pipeline_initial(  # type: ignore
                pipeline_name=pipeline_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

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

    begin_delete_pipeline.metadata = {"url": "/pipelines/{pipelineName}"}

    async def _rename_pipeline_initial(  # pylint: disable=inconsistent-return-statements
        self, pipeline_name: str, new_name: Optional[str] = None, **kwargs: Any
    ) -> None:
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
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = _models.ArtifactRenameRequest(new_name=new_name)
        _json = self._serialize.body(_request, "ArtifactRenameRequest")

        request = build_rename_pipeline_request(
            pipeline_name=pipeline_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._rename_pipeline_initial.metadata["url"],
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

        if cls:
            return cls(pipeline_response, None, {})

    _rename_pipeline_initial.metadata = {"url": "/pipelines/{pipelineName}/rename"}

    @distributed_trace_async
    async def begin_rename_pipeline(
        self, pipeline_name: str, new_name: Optional[str] = None, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Renames a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param new_name: New name of the artifact. Default value is None.
        :type new_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._rename_pipeline_initial(  # type: ignore
                pipeline_name=pipeline_name,
                new_name=new_name,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

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

    begin_rename_pipeline.metadata = {"url": "/pipelines/{pipelineName}/rename"}

    @overload
    async def create_pipeline_run(
        self,
        pipeline_name: str,
        reference_pipeline_run_id: Optional[str] = None,
        is_recovery: Optional[bool] = None,
        start_activity_name: Optional[str] = None,
        parameters: Optional[Dict[str, JSON]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CreateRunResponse:
        """Creates a run of a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param reference_pipeline_run_id: The pipeline run identifier. If run ID is specified the
         parameters of the specified run will be used to create a new run. Default value is None.
        :type reference_pipeline_run_id: str
        :param is_recovery: Recovery mode flag. If recovery mode is set to true, the specified
         referenced pipeline run and the new run will be grouped under the same groupId. Default value
         is None.
        :type is_recovery: bool
        :param start_activity_name: In recovery mode, the rerun will start from this activity. If not
         specified, all activities will run. Default value is None.
        :type start_activity_name: str
        :param parameters: Parameters of the pipeline run. These parameters will be used only if the
         runId is not specified. Default value is None.
        :type parameters: dict[str, JSON]
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CreateRunResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.CreateRunResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_pipeline_run(
        self,
        pipeline_name: str,
        reference_pipeline_run_id: Optional[str] = None,
        is_recovery: Optional[bool] = None,
        start_activity_name: Optional[str] = None,
        parameters: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CreateRunResponse:
        """Creates a run of a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param reference_pipeline_run_id: The pipeline run identifier. If run ID is specified the
         parameters of the specified run will be used to create a new run. Default value is None.
        :type reference_pipeline_run_id: str
        :param is_recovery: Recovery mode flag. If recovery mode is set to true, the specified
         referenced pipeline run and the new run will be grouped under the same groupId. Default value
         is None.
        :type is_recovery: bool
        :param start_activity_name: In recovery mode, the rerun will start from this activity. If not
         specified, all activities will run. Default value is None.
        :type start_activity_name: str
        :param parameters: Parameters of the pipeline run. These parameters will be used only if the
         runId is not specified. Default value is None.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CreateRunResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.CreateRunResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_pipeline_run(
        self,
        pipeline_name: str,
        reference_pipeline_run_id: Optional[str] = None,
        is_recovery: Optional[bool] = None,
        start_activity_name: Optional[str] = None,
        parameters: Optional[Union[Dict[str, JSON], IO]] = None,
        **kwargs: Any
    ) -> _models.CreateRunResponse:
        """Creates a run of a pipeline.

        :param pipeline_name: The pipeline name. Required.
        :type pipeline_name: str
        :param reference_pipeline_run_id: The pipeline run identifier. If run ID is specified the
         parameters of the specified run will be used to create a new run. Default value is None.
        :type reference_pipeline_run_id: str
        :param is_recovery: Recovery mode flag. If recovery mode is set to true, the specified
         referenced pipeline run and the new run will be grouped under the same groupId. Default value
         is None.
        :type is_recovery: bool
        :param start_activity_name: In recovery mode, the rerun will start from this activity. If not
         specified, all activities will run. Default value is None.
        :type start_activity_name: str
        :param parameters: Parameters of the pipeline run. These parameters will be used only if the
         runId is not specified. Is either a {str: JSON} type or a IO type. Default value is None.
        :type parameters: dict[str, JSON] or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CreateRunResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.CreateRunResponse
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
        cls: ClsType[_models.CreateRunResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            if parameters is not None:
                _json = self._serialize.body(parameters, "{object}")
            else:
                _json = None

        request = build_create_pipeline_run_request(
            pipeline_name=pipeline_name,
            reference_pipeline_run_id=reference_pipeline_run_id,
            is_recovery=is_recovery,
            start_activity_name=start_activity_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_pipeline_run.metadata["url"],
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

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("CreateRunResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_pipeline_run.metadata = {"url": "/pipelines/{pipelineName}/createRun"}
