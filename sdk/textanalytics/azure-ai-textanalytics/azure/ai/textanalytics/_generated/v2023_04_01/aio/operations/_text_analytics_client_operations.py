# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from .....aio._lro_async import AsyncAnalyzeActionsLROPoller, AsyncAnalyzeActionsLROPollingMethod
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._text_analytics_client_operations import build_analyze_text_cancel_job_request, build_analyze_text_job_status_request, build_analyze_text_request, build_analyze_text_submit_job_request
from .._vendor import MixinABC
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TextAnalyticsClientOperationsMixin(MixinABC):

    @overload
    async def analyze_text(
        self,
        body: _models.AnalyzeTextTask,
        show_stats: Optional[bool] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AnalyzeTextTaskResult:
        """Request text analysis over a collection of documents.

        Submit a collection of text documents for analysis.  Specify a single unique task to be
        executed immediately.

        :param body: Collection of documents to analyze and a single task to execute. Required.
        :type body: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextTask
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics. Default value is None.
        :type show_stats: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeTextTaskResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextTaskResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def analyze_text(
        self,
        body: IO,
        show_stats: Optional[bool] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AnalyzeTextTaskResult:
        """Request text analysis over a collection of documents.

        Submit a collection of text documents for analysis.  Specify a single unique task to be
        executed immediately.

        :param body: Collection of documents to analyze and a single task to execute. Required.
        :type body: IO
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics. Default value is None.
        :type show_stats: bool
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeTextTaskResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextTaskResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace_async
    async def analyze_text(
        self,
        body: Union[_models.AnalyzeTextTask, IO],
        show_stats: Optional[bool] = None,
        **kwargs: Any
    ) -> _models.AnalyzeTextTaskResult:
        """Request text analysis over a collection of documents.

        Submit a collection of text documents for analysis.  Specify a single unique task to be
        executed immediately.

        :param body: Collection of documents to analyze and a single task to execute. Is either a model
         type or a IO type. Required.
        :type body: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextTask or IO
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics. Default value is None.
        :type show_stats: bool
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeTextTaskResult or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextTaskResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-04-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.AnalyzeTextTaskResult]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, 'AnalyzeTextTask')

        request = build_analyze_text_request(
            show_stats=show_stats,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.analyze_text.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AnalyzeTextTaskResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    analyze_text.metadata = {'url': "/:analyze-text"}  # type: ignore


    async def _analyze_text_submit_job_initial(
        self,
        body: Union[_models.AnalyzeTextJobsInput, IO],
        **kwargs: Any
    ) -> Optional[_models.AnalyzeTextJobState]:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-04-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.AnalyzeTextJobState]]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _json = self._serialize.body(body, 'AnalyzeTextJobsInput')

        request = build_analyze_text_submit_job_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._analyze_text_submit_job_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize('AnalyzeTextJobState', pipeline_response)

        if response.status_code == 202:
            response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))
            

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _analyze_text_submit_job_initial.metadata = {'url': "/analyze-text/jobs"}  # type: ignore


    @overload
    async def begin_analyze_text_submit_job(
        self,
        body: _models.AnalyzeTextJobsInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncAnalyzeActionsLROPoller[_models.AnalyzeTextJobState]:
        """Submit text analysis job.

        Submit a collection of text documents for analysis. Specify one or more unique tasks to be
        executed as a long-running operation.

        :param body: Collection of documents to analyze and one or more tasks to execute. Required.
        :type body: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextJobsInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncAnalyzeActionsLROPollingMethod.
         Pass in False for this operation to not poll, or pass in your own initialized polling object
         for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncAnalyzeActionsLROPoller that returns either AnalyzeTextJobState or
         the result of cls(response)
        :rtype:
         ~.....aio._lro_async.AsyncAnalyzeActionsLROPoller[~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextJobState]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_analyze_text_submit_job(
        self,
        body: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncAnalyzeActionsLROPoller[_models.AnalyzeTextJobState]:
        """Submit text analysis job.

        Submit a collection of text documents for analysis. Specify one or more unique tasks to be
        executed as a long-running operation.

        :param body: Collection of documents to analyze and one or more tasks to execute. Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncAnalyzeActionsLROPollingMethod.
         Pass in False for this operation to not poll, or pass in your own initialized polling object
         for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncAnalyzeActionsLROPoller that returns either AnalyzeTextJobState or
         the result of cls(response)
        :rtype:
         ~.....aio._lro_async.AsyncAnalyzeActionsLROPoller[~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextJobState]
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace_async
    async def begin_analyze_text_submit_job(
        self,
        body: Union[_models.AnalyzeTextJobsInput, IO],
        **kwargs: Any
    ) -> AsyncAnalyzeActionsLROPoller[_models.AnalyzeTextJobState]:
        """Submit text analysis job.

        Submit a collection of text documents for analysis. Specify one or more unique tasks to be
        executed as a long-running operation.

        :param body: Collection of documents to analyze and one or more tasks to execute. Is either a
         model type or a IO type. Required.
        :type body: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextJobsInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncAnalyzeActionsLROPollingMethod.
         Pass in False for this operation to not poll, or pass in your own initialized polling object
         for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncAnalyzeActionsLROPoller that returns either AnalyzeTextJobState or
         the result of cls(response)
        :rtype:
         ~.....aio._lro_async.AsyncAnalyzeActionsLROPoller[~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextJobState]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-04-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.AnalyzeTextJobState]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._analyze_text_submit_job_initial(  # type: ignore
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('AnalyzeTextJobState', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncAnalyzeActionsLROPollingMethod(
                lro_delay,
                
                path_format_arguments=path_format_arguments,
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncAnalyzeActionsLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncAnalyzeActionsLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_analyze_text_submit_job.metadata = {'url': "/analyze-text/jobs"}  # type: ignore

    @distributed_trace_async
    async def analyze_text_job_status(
        self,
        job_id: str,
        show_stats: Optional[bool] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        **kwargs: Any
    ) -> _models.AnalyzeTextJobState:
        """Get analysis status and results.

        Get the status of an analysis job.  A job may consist of one or more tasks.  Once all tasks are
        succeeded, the job will transition to the succeeded state and results will be available for
        each task.

        :param job_id: Job ID. Required.
        :type job_id: str
        :param show_stats: (Optional) if set to true, response will contain request and document level
         statistics. Default value is None.
        :type show_stats: bool
        :param top: The maximum number of resources to return from the collection. Default value is
         None.
        :type top: int
        :param skip: An offset into the collection of the first resource to be returned. Default value
         is None.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeTextJobState or the result of cls(response)
        :rtype: ~azure.ai.textanalytics.v2023_04_01.models.AnalyzeTextJobState
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.AnalyzeTextJobState]

        
        request = build_analyze_text_job_status_request(
            job_id=job_id,
            show_stats=show_stats,
            top=top,
            skip=skip,
            api_version=api_version,
            template_url=self.analyze_text_job_status.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AnalyzeTextJobState', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    analyze_text_job_status.metadata = {'url': "/analyze-text/jobs/{jobId}"}  # type: ignore


    async def _analyze_text_cancel_job_initial(  # pylint: disable=inconsistent-return-statements
        self,
        job_id: str,
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_analyze_text_cancel_job_request(
            job_id=job_id,
            api_version=api_version,
            template_url=self._analyze_text_cancel_job_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))


        if cls:
            return cls(pipeline_response, None, response_headers)

    _analyze_text_cancel_job_initial.metadata = {'url': "/analyze-text/jobs/{jobId}:cancel"}  # type: ignore


    @distributed_trace_async
    async def begin_analyze_text_cancel_job(
        self,
        job_id: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Cancel a long-running Text Analysis job.

        Cancel a long-running Text Analysis job.

        :param job_id: Job ID. Required.
        :type job_id: str
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

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._analyze_text_cancel_job_initial(  # type: ignore
                job_id=job_id,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})


        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncLROBasePolling(
                lro_delay,
                
                path_format_arguments=path_format_arguments,
                **kwargs
        ))  # type: AsyncPollingMethod
        elif polling is False: polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_analyze_text_cancel_job.metadata = {'url': "/analyze-text/jobs/{jobId}:cancel"}  # type: ignore
