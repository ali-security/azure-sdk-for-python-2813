# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.2.4, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import ContainerRegistryConfiguration
from .operations import ContainerRegistryOperations
from .operations import ContainerRegistryRepositoryOperations
from .operations import ContainerRegistryBlobOperations
from .operations import AuthenticationOperations
from .. import models


class ContainerRegistry(object):
    """Metadata API definition for the Azure Container Registry runtime.

    :ivar container_registry: ContainerRegistryOperations operations
    :vartype container_registry: container_registry.aio.operations.ContainerRegistryOperations
    :ivar container_registry_repository: ContainerRegistryRepositoryOperations operations
    :vartype container_registry_repository: container_registry.aio.operations.ContainerRegistryRepositoryOperations
    :ivar container_registry_blob: ContainerRegistryBlobOperations operations
    :vartype container_registry_blob: container_registry.aio.operations.ContainerRegistryBlobOperations
    :ivar authentication: AuthenticationOperations operations
    :vartype authentication: container_registry.aio.operations.AuthenticationOperations
    :param url: Registry login URL.
    :type url: str
    """

    def __init__(
        self,
        url: str,
        **kwargs: Any
    ) -> None:
        base_url = '{url}'
        self._config = ContainerRegistryConfiguration(url, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.container_registry = ContainerRegistryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.container_registry_repository = ContainerRegistryRepositoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.container_registry_blob = ContainerRegistryBlobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.authentication = AuthenticationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ContainerRegistry":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
