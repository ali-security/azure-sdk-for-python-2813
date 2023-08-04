# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AcceptedAudiences
from ._models_py3 import AttachedDatabaseConfiguration
from ._models_py3 import AttachedDatabaseConfigurationListResult
from ._models_py3 import AttachedDatabaseConfigurationsCheckNameRequest
from ._models_py3 import AzureCapacity
from ._models_py3 import AzureResourceSku
from ._models_py3 import AzureSku
from ._models_py3 import CheckNameRequest
from ._models_py3 import CheckNameResult
from ._models_py3 import Cluster
from ._models_py3 import ClusterCheckNameRequest
from ._models_py3 import ClusterListResult
from ._models_py3 import ClusterMigrateRequest
from ._models_py3 import ClusterPrincipalAssignment
from ._models_py3 import ClusterPrincipalAssignmentCheckNameRequest
from ._models_py3 import ClusterPrincipalAssignmentListResult
from ._models_py3 import ClusterUpdate
from ._models_py3 import ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties
from ._models_py3 import CosmosDbDataConnection
from ._models_py3 import DataConnection
from ._models_py3 import DataConnectionCheckNameRequest
from ._models_py3 import DataConnectionListResult
from ._models_py3 import DataConnectionValidation
from ._models_py3 import DataConnectionValidationListResult
from ._models_py3 import DataConnectionValidationResult
from ._models_py3 import Database
from ._models_py3 import DatabaseInviteFollowerRequest
from ._models_py3 import DatabaseInviteFollowerResult
from ._models_py3 import DatabaseListResult
from ._models_py3 import DatabasePrincipal
from ._models_py3 import DatabasePrincipalAssignment
from ._models_py3 import DatabasePrincipalAssignmentCheckNameRequest
from ._models_py3 import DatabasePrincipalAssignmentListResult
from ._models_py3 import DatabasePrincipalListRequest
from ._models_py3 import DatabasePrincipalListResult
from ._models_py3 import DatabaseStatistics
from ._models_py3 import DiagnoseVirtualNetworkResult
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import EventGridDataConnection
from ._models_py3 import EventHubDataConnection
from ._models_py3 import FollowerDatabaseDefinition
from ._models_py3 import FollowerDatabaseListResult
from ._models_py3 import Identity
from ._models_py3 import IotHubDataConnection
from ._models_py3 import KeyVaultProperties
from ._models_py3 import LanguageExtension
from ._models_py3 import LanguageExtensionsList
from ._models_py3 import ListResourceSkusResult
from ._models_py3 import ManagedPrivateEndpoint
from ._models_py3 import ManagedPrivateEndpointListResult
from ._models_py3 import ManagedPrivateEndpointsCheckNameRequest
from ._models_py3 import MigrationClusterProperties
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationResult
from ._models_py3 import OptimizedAutoscale
from ._models_py3 import OutboundNetworkDependenciesEndpoint
from ._models_py3 import OutboundNetworkDependenciesEndpointListResult
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointProperty
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionStateProperty
from ._models_py3 import ProxyResource
from ._models_py3 import ReadOnlyFollowingDatabase
from ._models_py3 import ReadWriteDatabase
from ._models_py3 import Resource
from ._models_py3 import ResourceSkuCapabilities
from ._models_py3 import ResourceSkuZoneDetails
from ._models_py3 import Script
from ._models_py3 import ScriptCheckNameRequest
from ._models_py3 import ScriptListResult
from ._models_py3 import SkuDescription
from ._models_py3 import SkuDescriptionList
from ._models_py3 import SkuLocationInfoItem
from ._models_py3 import SuspensionDetails
from ._models_py3 import SystemData
from ._models_py3 import TableLevelSharingProperties
from ._models_py3 import TrackedResource
from ._models_py3 import TrustedExternalTenant
from ._models_py3 import VirtualNetworkConfiguration

from ._kusto_management_client_enums import AzureScaleType
from ._kusto_management_client_enums import AzureSkuName
from ._kusto_management_client_enums import AzureSkuTier
from ._kusto_management_client_enums import BlobStorageEventType
from ._kusto_management_client_enums import CallerRole
from ._kusto_management_client_enums import ClusterNetworkAccessFlag
from ._kusto_management_client_enums import ClusterPrincipalRole
from ._kusto_management_client_enums import Compression
from ._kusto_management_client_enums import CreatedByType
from ._kusto_management_client_enums import DataConnectionKind
from ._kusto_management_client_enums import DatabasePrincipalRole
from ._kusto_management_client_enums import DatabasePrincipalType
from ._kusto_management_client_enums import DatabaseRouting
from ._kusto_management_client_enums import DatabaseShareOrigin
from ._kusto_management_client_enums import DefaultPrincipalsModificationKind
from ._kusto_management_client_enums import EngineType
from ._kusto_management_client_enums import EventGridDataFormat
from ._kusto_management_client_enums import EventHubDataFormat
from ._kusto_management_client_enums import IdentityType
from ._kusto_management_client_enums import IotHubDataFormat
from ._kusto_management_client_enums import Kind
from ._kusto_management_client_enums import LanguageExtensionImageName
from ._kusto_management_client_enums import LanguageExtensionName
from ._kusto_management_client_enums import MigrationClusterRole
from ._kusto_management_client_enums import PrincipalType
from ._kusto_management_client_enums import PrincipalsModificationKind
from ._kusto_management_client_enums import ProvisioningState
from ._kusto_management_client_enums import PublicIPType
from ._kusto_management_client_enums import PublicNetworkAccess
from ._kusto_management_client_enums import Reason
from ._kusto_management_client_enums import State
from ._kusto_management_client_enums import Status
from ._kusto_management_client_enums import Type
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AcceptedAudiences",
    "AttachedDatabaseConfiguration",
    "AttachedDatabaseConfigurationListResult",
    "AttachedDatabaseConfigurationsCheckNameRequest",
    "AzureCapacity",
    "AzureResourceSku",
    "AzureSku",
    "CheckNameRequest",
    "CheckNameResult",
    "Cluster",
    "ClusterCheckNameRequest",
    "ClusterListResult",
    "ClusterMigrateRequest",
    "ClusterPrincipalAssignment",
    "ClusterPrincipalAssignmentCheckNameRequest",
    "ClusterPrincipalAssignmentListResult",
    "ClusterUpdate",
    "ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties",
    "CosmosDbDataConnection",
    "DataConnection",
    "DataConnectionCheckNameRequest",
    "DataConnectionListResult",
    "DataConnectionValidation",
    "DataConnectionValidationListResult",
    "DataConnectionValidationResult",
    "Database",
    "DatabaseInviteFollowerRequest",
    "DatabaseInviteFollowerResult",
    "DatabaseListResult",
    "DatabasePrincipal",
    "DatabasePrincipalAssignment",
    "DatabasePrincipalAssignmentCheckNameRequest",
    "DatabasePrincipalAssignmentListResult",
    "DatabasePrincipalListRequest",
    "DatabasePrincipalListResult",
    "DatabaseStatistics",
    "DiagnoseVirtualNetworkResult",
    "EndpointDependency",
    "EndpointDetail",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "EventGridDataConnection",
    "EventHubDataConnection",
    "FollowerDatabaseDefinition",
    "FollowerDatabaseListResult",
    "Identity",
    "IotHubDataConnection",
    "KeyVaultProperties",
    "LanguageExtension",
    "LanguageExtensionsList",
    "ListResourceSkusResult",
    "ManagedPrivateEndpoint",
    "ManagedPrivateEndpointListResult",
    "ManagedPrivateEndpointsCheckNameRequest",
    "MigrationClusterProperties",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationResult",
    "OptimizedAutoscale",
    "OutboundNetworkDependenciesEndpoint",
    "OutboundNetworkDependenciesEndpointListResult",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointProperty",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionStateProperty",
    "ProxyResource",
    "ReadOnlyFollowingDatabase",
    "ReadWriteDatabase",
    "Resource",
    "ResourceSkuCapabilities",
    "ResourceSkuZoneDetails",
    "Script",
    "ScriptCheckNameRequest",
    "ScriptListResult",
    "SkuDescription",
    "SkuDescriptionList",
    "SkuLocationInfoItem",
    "SuspensionDetails",
    "SystemData",
    "TableLevelSharingProperties",
    "TrackedResource",
    "TrustedExternalTenant",
    "VirtualNetworkConfiguration",
    "AzureScaleType",
    "AzureSkuName",
    "AzureSkuTier",
    "BlobStorageEventType",
    "CallerRole",
    "ClusterNetworkAccessFlag",
    "ClusterPrincipalRole",
    "Compression",
    "CreatedByType",
    "DataConnectionKind",
    "DatabasePrincipalRole",
    "DatabasePrincipalType",
    "DatabaseRouting",
    "DatabaseShareOrigin",
    "DefaultPrincipalsModificationKind",
    "EngineType",
    "EventGridDataFormat",
    "EventHubDataFormat",
    "IdentityType",
    "IotHubDataFormat",
    "Kind",
    "LanguageExtensionImageName",
    "LanguageExtensionName",
    "MigrationClusterRole",
    "PrincipalType",
    "PrincipalsModificationKind",
    "ProvisioningState",
    "PublicIPType",
    "PublicNetworkAccess",
    "Reason",
    "State",
    "Status",
    "Type",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
