# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    location_name: str,
    target_type_name: str,
    subscription_id: str,
    *,
    continuation_token_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-04-15-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        ),
        "locationName": _SERIALIZER.url("location_name", location_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
        "targetTypeName": _SERIALIZER.url("target_type_name", target_type_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if continuation_token_parameter is not None:
        _params["continuationToken"] = _SERIALIZER.query(
            "continuation_token_parameter", continuation_token_parameter, "str"
        )

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    location_name: str, target_type_name: str, capability_type_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-04-15-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes/{capabilityTypeName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        ),
        "locationName": _SERIALIZER.url("location_name", location_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
        "targetTypeName": _SERIALIZER.url("target_type_name", target_type_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
        "capabilityTypeName": _SERIALIZER.url(
            "capability_type_name", capability_type_name, "str", pattern=r"^[a-zA-Z0-9\-\.]+-\d\.\d$"
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class CapabilityTypesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.chaos.ChaosManagementClient`'s
        :attr:`capability_types` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        location_name: str,
        target_type_name: str,
        continuation_token_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.CapabilityType"]:
        """Get a list of Capability Type resources for given Target Type and location.

        :param location_name: String that represents a Location resource name. Required.
        :type location_name: str
        :param target_type_name: String that represents a Target Type resource name. Required.
        :type target_type_name: str
        :param continuation_token_parameter: String that sets the continuation token. Default value is
         None.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CapabilityType or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.chaos.models.CapabilityType]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.CapabilityTypeListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    location_name=location_name,
                    target_type_name=target_type_name,
                    subscription_id=self._config.subscription_id,
                    continuation_token_parameter=continuation_token_parameter,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("CapabilityTypeListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes"
    }

    @distributed_trace
    def get(
        self, location_name: str, target_type_name: str, capability_type_name: str, **kwargs: Any
    ) -> _models.CapabilityType:
        """Get a Capability Type resource for given Target Type and location.

        :param location_name: String that represents a Location resource name. Required.
        :type location_name: str
        :param target_type_name: String that represents a Target Type resource name. Required.
        :type target_type_name: str
        :param capability_type_name: String that represents a Capability Type resource name. Required.
        :type capability_type_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CapabilityType or the result of cls(response)
        :rtype: ~azure.mgmt.chaos.models.CapabilityType
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.CapabilityType] = kwargs.pop("cls", None)

        request = build_get_request(
            location_name=location_name,
            target_type_name=target_type_name,
            capability_type_name=capability_type_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CapabilityType", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Chaos/locations/{locationName}/targetTypes/{targetTypeName}/capabilityTypes/{capabilityTypeName}"
    }
