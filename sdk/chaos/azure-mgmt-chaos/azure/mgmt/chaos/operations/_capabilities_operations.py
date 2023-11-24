# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
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
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str,
    parent_provider_namespace: str,
    parent_resource_type: str,
    parent_resource_name: str,
    target_name: str,
    subscription_id: str,
    *,
    continuation_token_parameter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", pattern=r"^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$"
        ),
        "parentProviderNamespace": _SERIALIZER.url(
            "parent_provider_namespace", parent_provider_namespace, "str", pattern=r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
        ),
        "parentResourceType": _SERIALIZER.url(
            "parent_resource_type", parent_resource_type, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "parentResourceName": _SERIALIZER.url(
            "parent_resource_name", parent_resource_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "targetName": _SERIALIZER.url("target_name", target_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

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
    resource_group_name: str,
    parent_provider_namespace: str,
    parent_resource_type: str,
    parent_resource_name: str,
    target_name: str,
    capability_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", pattern=r"^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$"
        ),
        "parentProviderNamespace": _SERIALIZER.url(
            "parent_provider_namespace", parent_provider_namespace, "str", pattern=r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
        ),
        "parentResourceType": _SERIALIZER.url(
            "parent_resource_type", parent_resource_type, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "parentResourceName": _SERIALIZER.url(
            "parent_resource_name", parent_resource_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "targetName": _SERIALIZER.url("target_name", target_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
        "capabilityName": _SERIALIZER.url(
            "capability_name", capability_name, "str", pattern=r"^[a-zA-Z0-9\-\.]+-\d\.\d$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    parent_provider_namespace: str,
    parent_resource_type: str,
    parent_resource_name: str,
    target_name: str,
    capability_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", pattern=r"^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$"
        ),
        "parentProviderNamespace": _SERIALIZER.url(
            "parent_provider_namespace", parent_provider_namespace, "str", pattern=r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
        ),
        "parentResourceType": _SERIALIZER.url(
            "parent_resource_type", parent_resource_type, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "parentResourceName": _SERIALIZER.url(
            "parent_resource_name", parent_resource_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "targetName": _SERIALIZER.url("target_name", target_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
        "capabilityName": _SERIALIZER.url(
            "capability_name", capability_name, "str", pattern=r"^[a-zA-Z0-9\-\.]+-\d\.\d$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    parent_provider_namespace: str,
    parent_resource_type: str,
    parent_resource_name: str,
    target_name: str,
    capability_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", pattern=r"^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$"
        ),
        "parentProviderNamespace": _SERIALIZER.url(
            "parent_provider_namespace", parent_provider_namespace, "str", pattern=r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
        ),
        "parentResourceType": _SERIALIZER.url(
            "parent_resource_type", parent_resource_type, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "parentResourceName": _SERIALIZER.url(
            "parent_resource_name", parent_resource_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"
        ),
        "targetName": _SERIALIZER.url("target_name", target_name, "str", pattern=r"^[a-zA-Z0-9_\-\.]+$"),
        "capabilityName": _SERIALIZER.url(
            "capability_name", capability_name, "str", pattern=r"^[a-zA-Z0-9\-\.]+-\d\.\d$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class CapabilitiesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.chaos.ChaosManagementClient`'s
        :attr:`capabilities` attribute.
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
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        continuation_token_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.Capability"]:
        """Get a list of Capability resources that extend a Target resource..

        :param resource_group_name: String that represents an Azure resource group. Required.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
         Required.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type. Required.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name. Required.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name. Required.
        :type target_name: str
        :param continuation_token_parameter: String that sets the continuation token. Default value is
         None.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Capability or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.chaos.models.Capability]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.CapabilityListResult] = kwargs.pop("cls", None)

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
                    resource_group_name=resource_group_name,
                    parent_provider_namespace=parent_provider_namespace,
                    parent_resource_type=parent_resource_type,
                    parent_resource_name=parent_resource_name,
                    target_name=target_name,
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
            deserialized = self._deserialize("CapabilityListResult", pipeline_response)
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
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities"
    }

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        **kwargs: Any
    ) -> _models.Capability:
        """Get a Capability resource that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group. Required.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
         Required.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type. Required.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name. Required.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name. Required.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name. Required.
        :type capability_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability or the result of cls(response)
        :rtype: ~azure.mgmt.chaos.models.Capability
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
        cls: ClsType[_models.Capability] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            parent_provider_namespace=parent_provider_namespace,
            parent_resource_type=parent_resource_type,
            parent_resource_name=parent_resource_name,
            target_name=target_name,
            capability_name=capability_name,
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

        deserialized = self._deserialize("Capability", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        **kwargs: Any
    ) -> None:
        """Delete a Capability that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group. Required.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
         Required.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type. Required.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name. Required.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name. Required.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name. Required.
        :type capability_name: str
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            parent_provider_namespace=parent_provider_namespace,
            parent_resource_type=parent_resource_type,
            parent_resource_name=parent_resource_name,
            target_name=target_name,
            capability_name=capability_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}"
    }

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        capability: _models.Capability,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Capability:
        """Create or update a Capability resource that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group. Required.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
         Required.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type. Required.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name. Required.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name. Required.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name. Required.
        :type capability_name: str
        :param capability: Capability resource to be created or updated. Required.
        :type capability: ~azure.mgmt.chaos.models.Capability
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability or the result of cls(response)
        :rtype: ~azure.mgmt.chaos.models.Capability
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        capability: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Capability:
        """Create or update a Capability resource that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group. Required.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
         Required.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type. Required.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name. Required.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name. Required.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name. Required.
        :type capability_name: str
        :param capability: Capability resource to be created or updated. Required.
        :type capability: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability or the result of cls(response)
        :rtype: ~azure.mgmt.chaos.models.Capability
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        capability: Union[_models.Capability, IO],
        **kwargs: Any
    ) -> _models.Capability:
        """Create or update a Capability resource that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group. Required.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
         Required.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type. Required.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name. Required.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name. Required.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name. Required.
        :type capability_name: str
        :param capability: Capability resource to be created or updated. Is either a Capability type or
         a IO type. Required.
        :type capability: ~azure.mgmt.chaos.models.Capability or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability or the result of cls(response)
        :rtype: ~azure.mgmt.chaos.models.Capability
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Capability] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(capability, (IOBase, bytes)):
            _content = capability
        else:
            _json = self._serialize.body(capability, "Capability")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            parent_provider_namespace=parent_provider_namespace,
            parent_resource_type=parent_resource_type,
            parent_resource_name=parent_resource_name,
            target_name=target_name,
            capability_name=capability_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
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

        deserialized = self._deserialize("Capability", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}"
    }
