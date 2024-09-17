# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import build_project_list_secrets_request
from .._vendor import ProjectClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
_Unset: Any = object()
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ProjectClientOperationsMixin(ProjectClientMixinABC):

    @overload
    async def _list_secrets(  # pylint: disable=protected-access
        self, connection_name_in_url: str, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models._models.ListSecretsResponse: ...
    @overload
    async def _list_secrets(  # pylint: disable=protected-access
        self,
        connection_name_in_url: str,
        *,
        connection_name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version_in_body: str,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models._models.ListSecretsResponse: ...
    @overload
    async def _list_secrets(  # pylint: disable=protected-access
        self, connection_name_in_url: str, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models._models.ListSecretsResponse: ...

    @distributed_trace_async
    async def _list_secrets(  # pylint: disable=protected-access
        self,
        connection_name_in_url: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        connection_name: str = _Unset,
        subscription_id: str = _Unset,
        resource_group_name: str = _Unset,
        workspace_name: str = _Unset,
        api_version_in_body: str = _Unset,
        **kwargs: Any
    ) -> _models._models.ListSecretsResponse:
        """List secrets for a given connection.

        :param connection_name_in_url: Connection Name. Required.
        :type connection_name_in_url: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword connection_name: Connection Name. Required.
        :paramtype connection_name: str
        :keyword subscription_id: The ID of the target subscription. Required.
        :paramtype subscription_id: str
        :keyword resource_group_name: The name of the Resource Group. Required.
        :paramtype resource_group_name: str
        :keyword workspace_name: The name of the workspace (Azire AI Studio hub). Required.
        :paramtype workspace_name: str
        :keyword api_version_in_body: The api version. Required.
        :paramtype api_version_in_body: str
        :return: ListSecretsResponse. The ListSecretsResponse is compatible with MutableMapping
        :rtype: ~azure.ai.project.models._models.ListSecretsResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models._models.ListSecretsResponse] = kwargs.pop("cls", None)  # pylint: disable=protected-access

        if body is _Unset:
            if connection_name is _Unset:
                raise TypeError("missing required argument: connection_name")
            if subscription_id is _Unset:
                raise TypeError("missing required argument: subscription_id")
            if resource_group_name is _Unset:
                raise TypeError("missing required argument: resource_group_name")
            if workspace_name is _Unset:
                raise TypeError("missing required argument: workspace_name")
            if api_version_in_body is _Unset:
                raise TypeError("missing required argument: api_version_in_body")
            body = {
                "apiVersionInBody": api_version_in_body,
                "connectionName": connection_name,
                "resourceGroupName": resource_group_name,
                "subscriptionId": subscription_id,
                "workspaceName": workspace_name,
            }
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_project_list_secrets_request(
            connection_name_in_url=connection_name_in_url,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "subscriptionId": self._serialize.url("self._config.subscription_id", self._config.subscription_id, "str"),
            "resourceGroupName": self._serialize.url(
                "self._config.resource_group_name", self._config.resource_group_name, "str"
            ),
            "workspaceName": self._serialize.url("self._config.workspace_name", self._config.workspace_name, "str"),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(
                _models._models.ListSecretsResponse, response.json()  # pylint: disable=protected-access
            )

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
