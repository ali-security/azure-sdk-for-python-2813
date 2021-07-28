# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ArtifactsClientConfiguration
from .operations import LinkedServiceOperations
from .operations import DatasetOperations
from .operations import PipelineOperations
from .operations import PipelineRunOperations
from .operations import TriggerOperations
from .operations import TriggerRunOperations
from .operations import DataFlowOperations
from .operations import DataFlowDebugSessionOperations
from .operations import SqlScriptOperations
from .operations import SparkJobDefinitionOperations
from .operations import NotebookOperations
from .operations import NotebookOperationResultOperations
from .operations import BigDataPoolsOperations
from .operations import WorkspaceGitRepoManagementOperations
from .operations import IntegrationRuntimesOperations
from .operations import LibraryOperations
from .operations import OperationResultOperations
from .operations import OperationStatusOperations
from .operations import SqlPoolsOperations
from .operations import WorkspaceOperations
from .. import models


class ArtifactsClient(object):
    """ArtifactsClient.

    :ivar linked_service: LinkedServiceOperations operations
    :vartype linked_service: azure.synapse.artifacts.aio.operations.LinkedServiceOperations
    :ivar dataset: DatasetOperations operations
    :vartype dataset: azure.synapse.artifacts.aio.operations.DatasetOperations
    :ivar pipeline: PipelineOperations operations
    :vartype pipeline: azure.synapse.artifacts.aio.operations.PipelineOperations
    :ivar pipeline_run: PipelineRunOperations operations
    :vartype pipeline_run: azure.synapse.artifacts.aio.operations.PipelineRunOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: azure.synapse.artifacts.aio.operations.TriggerOperations
    :ivar trigger_run: TriggerRunOperations operations
    :vartype trigger_run: azure.synapse.artifacts.aio.operations.TriggerRunOperations
    :ivar data_flow: DataFlowOperations operations
    :vartype data_flow: azure.synapse.artifacts.aio.operations.DataFlowOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session: azure.synapse.artifacts.aio.operations.DataFlowDebugSessionOperations
    :ivar sql_script: SqlScriptOperations operations
    :vartype sql_script: azure.synapse.artifacts.aio.operations.SqlScriptOperations
    :ivar spark_job_definition: SparkJobDefinitionOperations operations
    :vartype spark_job_definition: azure.synapse.artifacts.aio.operations.SparkJobDefinitionOperations
    :ivar notebook: NotebookOperations operations
    :vartype notebook: azure.synapse.artifacts.aio.operations.NotebookOperations
    :ivar notebook_operation_result: NotebookOperationResultOperations operations
    :vartype notebook_operation_result: azure.synapse.artifacts.aio.operations.NotebookOperationResultOperations
    :ivar big_data_pools: BigDataPoolsOperations operations
    :vartype big_data_pools: azure.synapse.artifacts.aio.operations.BigDataPoolsOperations
    :ivar workspace_git_repo_management: WorkspaceGitRepoManagementOperations operations
    :vartype workspace_git_repo_management: azure.synapse.artifacts.aio.operations.WorkspaceGitRepoManagementOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.synapse.artifacts.aio.operations.IntegrationRuntimesOperations
    :ivar library: LibraryOperations operations
    :vartype library: azure.synapse.artifacts.aio.operations.LibraryOperations
    :ivar operation_result: OperationResultOperations operations
    :vartype operation_result: azure.synapse.artifacts.aio.operations.OperationResultOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: azure.synapse.artifacts.aio.operations.OperationStatusOperations
    :ivar sql_pools: SqlPoolsOperations operations
    :vartype sql_pools: azure.synapse.artifacts.aio.operations.SqlPoolsOperations
    :ivar workspace: WorkspaceOperations operations
    :vartype workspace: azure.synapse.artifacts.aio.operations.WorkspaceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: The workspace development endpoint, for example https://myworkspace.dev.azuresynapse.net.
    :type endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{endpoint}'
        self._config = ArtifactsClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.linked_service = LinkedServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dataset = DatasetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline = PipelineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_run = PipelineRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger_run = TriggerRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow = DataFlowOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_script = SqlScriptOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_job_definition = SparkJobDefinitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notebook = NotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notebook_operation_result = NotebookOperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.big_data_pools = BigDataPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_git_repo_management = WorkspaceGitRepoManagementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.library = LibraryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_result = OperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pools = SqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace = WorkspaceOperations(
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
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ArtifactsClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
