# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._troubleshooters_operations import (
    build_continue_method_request,
    build_create_request,
    build_end_request,
    build_get_request,
    build_restart_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TroubleshootersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.selfhelp.aio.SelfHelpMgmtClient`'s
        :attr:`troubleshooters` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create(
        self,
        scope: str,
        troubleshooter_name: str,
        create_troubleshooter_request_body: Optional[_models.TroubleshooterResource] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TroubleshooterResource:
        """Creates the specific troubleshooter action under a resource or subscription using the
        ‘solutionId’ and  ‘properties.parameters’ as the trigger. :code:`<br/>` Azure Troubleshooters
        help with hard to classify issues, reducing the gap between customer observed problems and
        solutions by guiding the user effortlessly through the troubleshooting process. Each
        Troubleshooter flow represents a problem area within Azure and has a complex tree-like
        structure that addresses many root causes. These flows are prepared with the help of Subject
        Matter experts and customer support engineers by carefully considering previous support
        requests raised by customers. Troubleshooters terminate at a well curated solution based off of
        resource backend signals and customer manual selections.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :param create_troubleshooter_request_body: The required request body for this Troubleshooter
         resource creation. Default value is None.
        :type create_troubleshooter_request_body: ~azure.mgmt.selfhelp.models.TroubleshooterResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TroubleshooterResource or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.TroubleshooterResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        scope: str,
        troubleshooter_name: str,
        create_troubleshooter_request_body: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TroubleshooterResource:
        """Creates the specific troubleshooter action under a resource or subscription using the
        ‘solutionId’ and  ‘properties.parameters’ as the trigger. :code:`<br/>` Azure Troubleshooters
        help with hard to classify issues, reducing the gap between customer observed problems and
        solutions by guiding the user effortlessly through the troubleshooting process. Each
        Troubleshooter flow represents a problem area within Azure and has a complex tree-like
        structure that addresses many root causes. These flows are prepared with the help of Subject
        Matter experts and customer support engineers by carefully considering previous support
        requests raised by customers. Troubleshooters terminate at a well curated solution based off of
        resource backend signals and customer manual selections.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :param create_troubleshooter_request_body: The required request body for this Troubleshooter
         resource creation. Default value is None.
        :type create_troubleshooter_request_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TroubleshooterResource or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.TroubleshooterResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        scope: str,
        troubleshooter_name: str,
        create_troubleshooter_request_body: Optional[Union[_models.TroubleshooterResource, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.TroubleshooterResource:
        """Creates the specific troubleshooter action under a resource or subscription using the
        ‘solutionId’ and  ‘properties.parameters’ as the trigger. :code:`<br/>` Azure Troubleshooters
        help with hard to classify issues, reducing the gap between customer observed problems and
        solutions by guiding the user effortlessly through the troubleshooting process. Each
        Troubleshooter flow represents a problem area within Azure and has a complex tree-like
        structure that addresses many root causes. These flows are prepared with the help of Subject
        Matter experts and customer support engineers by carefully considering previous support
        requests raised by customers. Troubleshooters terminate at a well curated solution based off of
        resource backend signals and customer manual selections.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :param create_troubleshooter_request_body: The required request body for this Troubleshooter
         resource creation. Is either a TroubleshooterResource type or a IO[bytes] type. Default value
         is None.
        :type create_troubleshooter_request_body: ~azure.mgmt.selfhelp.models.TroubleshooterResource or
         IO[bytes]
        :return: TroubleshooterResource or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.TroubleshooterResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TroubleshooterResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_troubleshooter_request_body, (IOBase, bytes)):
            _content = create_troubleshooter_request_body
        else:
            if create_troubleshooter_request_body is not None:
                _json = self._serialize.body(create_troubleshooter_request_body, "TroubleshooterResource")
            else:
                _json = None

        _request = build_create_request(
            scope=scope,
            troubleshooter_name=troubleshooter_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("TroubleshooterResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("TroubleshooterResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get(self, scope: str, troubleshooter_name: str, **kwargs: Any) -> _models.TroubleshooterResource:
        """Gets troubleshooter instance result which includes the step status/result of the troubleshooter
        resource name that is being executed.:code:`<br/>` Get API is used to retrieve the result of a
        Troubleshooter instance, which includes the status and result of each step in the
        Troubleshooter workflow. This API requires the Troubleshooter resource name that was created
        using the Create API.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :return: TroubleshooterResource or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.TroubleshooterResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.TroubleshooterResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            scope=scope,
            troubleshooter_name=troubleshooter_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TroubleshooterResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def continue_method(  # pylint: disable=inconsistent-return-statements
        self,
        scope: str,
        troubleshooter_name: str,
        continue_request_body: Optional[_models.ContinueRequestBody] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the
        respective troubleshooter resource name. :code:`<br/>`Continue API is used to provide inputs
        that are required for the specific troubleshooter to progress into the next step in the
        process. This API is used after the Troubleshooter has been created using the Create API.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :param continue_request_body: The required request body for going to next step in
         Troubleshooter resource. Default value is None.
        :type continue_request_body: ~azure.mgmt.selfhelp.models.ContinueRequestBody
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def continue_method(  # pylint: disable=inconsistent-return-statements
        self,
        scope: str,
        troubleshooter_name: str,
        continue_request_body: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the
        respective troubleshooter resource name. :code:`<br/>`Continue API is used to provide inputs
        that are required for the specific troubleshooter to progress into the next step in the
        process. This API is used after the Troubleshooter has been created using the Create API.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :param continue_request_body: The required request body for going to next step in
         Troubleshooter resource. Default value is None.
        :type continue_request_body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def continue_method(  # pylint: disable=inconsistent-return-statements
        self,
        scope: str,
        troubleshooter_name: str,
        continue_request_body: Optional[Union[_models.ContinueRequestBody, IO[bytes]]] = None,
        **kwargs: Any
    ) -> None:
        """Uses ‘stepId’ and ‘responses’ as the trigger to continue the troubleshooting steps for the
        respective troubleshooter resource name. :code:`<br/>`Continue API is used to provide inputs
        that are required for the specific troubleshooter to progress into the next step in the
        process. This API is used after the Troubleshooter has been created using the Create API.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :param continue_request_body: The required request body for going to next step in
         Troubleshooter resource. Is either a ContinueRequestBody type or a IO[bytes] type. Default
         value is None.
        :type continue_request_body: ~azure.mgmt.selfhelp.models.ContinueRequestBody or IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(continue_request_body, (IOBase, bytes)):
            _content = continue_request_body
        else:
            if continue_request_body is not None:
                _json = self._serialize.body(continue_request_body, "ContinueRequestBody")
            else:
                _json = None

        _request = build_continue_method_request(
            scope=scope,
            troubleshooter_name=troubleshooter_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def end(  # pylint: disable=inconsistent-return-statements
        self, scope: str, troubleshooter_name: str, **kwargs: Any
    ) -> None:
        """Ends the troubleshooter action.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_end_request(
            scope=scope,
            troubleshooter_name=troubleshooter_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def restart(
        self, scope: str, troubleshooter_name: str, **kwargs: Any
    ) -> _models.RestartTroubleshooterResponse:
        """Restarts the troubleshooter API using applicable troubleshooter resource name as the
        input.:code:`<br/>` It returns new resource name which should be used in subsequent request.
        The old resource name is obsolete after this API is invoked.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param troubleshooter_name: Troubleshooter resource Name. Required.
        :type troubleshooter_name: str
        :return: RestartTroubleshooterResponse or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.RestartTroubleshooterResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.RestartTroubleshooterResponse] = kwargs.pop("cls", None)

        _request = build_restart_request(
            scope=scope,
            troubleshooter_name=troubleshooter_name,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        deserialized = self._deserialize("RestartTroubleshooterResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore
