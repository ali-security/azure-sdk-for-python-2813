# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AnalyticalStorageSchemaType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the types of schema for analytical storage."""

    WELL_DEFINED = "WellDefined"
    FULL_FIDELITY = "FullFidelity"


class ApiType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate the API type of the restorable database account."""

    MONGO_DB = "MongoDB"
    GREMLIN = "Gremlin"
    CASSANDRA = "Cassandra"
    TABLE = "Table"
    SQL = "Sql"
    GREMLIN_V2 = "GremlinV2"


class AuthenticationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Which authentication method Cassandra should use to authenticate clients. 'None' turns off
    authentication, so should not be used except in emergencies. 'Cassandra' is the default
    password based authentication. The default is 'Cassandra'.
    """

    NONE = "None"
    CASSANDRA = "Cassandra"
    LDAP = "Ldap"


class AzureConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """How to connect to the azure services needed for running the cluster."""

    NONE = "None"
    VPN = "VPN"


class BackupPolicyMigrationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the status of migration between backup policy types."""

    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class BackupPolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the mode of backups."""

    PERIODIC = "Periodic"
    CONTINUOUS = "Continuous"


class BackupStorageRedundancy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate type of backup storage redundancy."""

    GEO = "Geo"
    LOCAL = "Local"
    ZONE = "Zone"


class CompositePathSortOrder(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sort order for composite paths."""

    ASCENDING = "ascending"
    DESCENDING = "descending"


class ConflictResolutionMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the conflict resolution mode."""

    LAST_WRITER_WINS = "LastWriterWins"
    CUSTOM = "Custom"


class ConnectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of connection error that occurred."""

    UNKNOWN = "Unknown"
    OK = "OK"
    OPERATOR_TO_DATA_CENTER_NETWORK_ERROR = "OperatorToDataCenterNetworkError"
    DATACENTER_TO_DATACENTER_NETWORK_ERROR = "DatacenterToDatacenterNetworkError"
    INTERNAL_OPERATOR_TO_DATA_CENTER_CERTIFICATE_ERROR = "InternalOperatorToDataCenterCertificateError"
    INTERNAL_ERROR = "InternalError"


class ConnectorOffer(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The cassandra connector offer type for the Cosmos DB C* database account."""

    SMALL = "Small"


class ContinuousTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate type of Continuous backup tier."""

    CONTINUOUS7_DAYS = "Continuous7Days"
    CONTINUOUS30_DAYS = "Continuous30Days"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate the mode of account creation."""

    DEFAULT = "Default"
    RESTORE = "Restore"


class DatabaseAccountKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of database account. This can only be set at database account creation."""

    GLOBAL_DOCUMENT_DB = "GlobalDocumentDB"
    MONGO_DB = "MongoDB"
    PARSE = "Parse"


class DataType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The datatype for which the indexing behavior is applied to."""

    STRING = "String"
    NUMBER = "Number"
    POINT = "Point"
    POLYGON = "Polygon"
    LINE_STRING = "LineString"
    MULTI_POLYGON = "MultiPolygon"


class DedicatedGatewayType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DedicatedGatewayType for the service."""

    INTEGRATED_CACHE = "IntegratedCache"
    DISTRIBUTED_QUERY = "DistributedQuery"


class DefaultConsistencyLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The default consistency level and configuration settings of the Cosmos DB account."""

    EVENTUAL = "Eventual"
    SESSION = "Session"
    BOUNDED_STALENESS = "BoundedStaleness"
    STRONG = "Strong"
    CONSISTENT_PREFIX = "ConsistentPrefix"


class IndexingMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the indexing mode."""

    CONSISTENT = "consistent"
    LAZY = "lazy"
    NONE = "none"


class IndexKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of index."""

    HASH = "Hash"
    RANGE = "Range"
    SPATIAL = "Spatial"


class KeyKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The access key to regenerate."""

    PRIMARY = "primary"
    SECONDARY = "secondary"
    PRIMARY_READONLY = "primaryReadonly"
    SECONDARY_READONLY = "secondaryReadonly"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Kind of the connection string key."""

    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    PRIMARY_READONLY = "PrimaryReadonly"
    SECONDARY_READONLY = "SecondaryReadonly"


class ManagedCassandraProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the resource at the time the operation was called."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class ManagedCassandraResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the resource."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class MinimalTlsVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the minimum allowed Tls version. The default value is Tls 1.2. Cassandra and Mongo
    APIs only work with Tls 1.2.
    """

    TLS = "Tls"
    TLS11 = "Tls11"
    TLS12 = "Tls12"


class MongoRoleDefinitionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the Role Definition was built-in or user created."""

    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"


class NetworkAclBypass(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates what services are allowed to bypass firewall checks."""

    NONE = "None"
    AZURE_SERVICES = "AzureServices"


class NodeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the node in Cassandra ring."""

    NORMAL = "Normal"
    LEAVING = "Leaving"
    JOINING = "Joining"
    MOVING = "Moving"
    STOPPED = "Stopped"


class NodeStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the node is functioning or not."""

    UP = "Up"
    DOWN = "Down"


class NotebookWorkspaceName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """NotebookWorkspaceName."""

    DEFAULT = "default"


class OperationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate the operation type of the event."""

    CREATE = "Create"
    REPLACE = "Replace"
    DELETE = "Delete"
    RECREATE = "Recreate"
    SYSTEM_OPERATION = "SystemOperation"


class PartitionKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the kind of algorithm used for partitioning. For MultiHash, multiple partition keys
    (upto three maximum) are supported for container create.
    """

    HASH = "Hash"
    RANGE = "Range"
    MULTI_HASH = "MultiHash"


class PrimaryAggregationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The primary aggregation type of the metric."""

    NONE = "None"
    AVERAGE = "Average"
    TOTAL = "Total"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    LAST = "Last"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether requests from Public Network are allowed."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    SECURED_BY_PERIMETER = "SecuredByPerimeter"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes
    both an implicitly created identity and a set of user assigned identities. The type 'None' will
    remove any identities from the service.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    NONE = "None"


class RestoreMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the mode of the restore."""

    POINT_IN_TIME = "PointInTime"


class RoleDefinitionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the Role Definition was built-in or user created."""

    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"


class ServerVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the version of the MongoDB account."""

    THREE2 = "3.2"
    THREE6 = "3.6"
    FOUR0 = "4.0"
    FOUR2 = "4.2"
    FIVE0 = "5.0"
    SIX0 = "6.0"
    SEVEN0 = "7.0"


class ServiceSize(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Instance type for the service."""

    COSMOS_D4_S = "Cosmos.D4s"
    COSMOS_D8_S = "Cosmos.D8s"
    COSMOS_D16_S = "Cosmos.D16s"


class ServiceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the status of a service."""

    CREATING = "Creating"
    RUNNING = "Running"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ERROR = "Error"
    STOPPED = "Stopped"


class ServiceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ServiceType for the service."""

    SQL_DEDICATED_GATEWAY = "SqlDedicatedGateway"
    DATA_TRANSFER = "DataTransfer"
    GRAPH_API_COMPUTE = "GraphAPICompute"
    MATERIALIZED_VIEWS_BUILDER = "MaterializedViewsBuilder"


class SpatialType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the spatial type of index."""

    POINT = "Point"
    LINE_STRING = "LineString"
    POLYGON = "Polygon"
    MULTI_POLYGON = "MultiPolygon"


class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate current buildout status of the region."""

    UNINITIALIZED = "Uninitialized"
    INITIALIZING = "Initializing"
    INTERNALLY_READY = "InternallyReady"
    ONLINE = "Online"
    DELETING = "Deleting"


class TriggerOperation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation the trigger is associated with."""

    ALL = "All"
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    REPLACE = "Replace"


class TriggerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the Trigger."""

    PRE = "Pre"
    POST = "Post"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the connection string."""

    SQL = "Sql"
    TABLE = "Table"
    MONGO_DB = "MongoDB"
    CASSANDRA = "Cassandra"
    CASSANDRA_CONNECTOR_METADATA = "CassandraConnectorMetadata"
    GREMLIN = "Gremlin"
    SQL_DEDICATED_GATEWAY = "SqlDedicatedGateway"
    GREMLIN_V2 = "GremlinV2"
    UNDEFINED = "Undefined"


class UnitType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit of the metric."""

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    MILLISECONDS = "Milliseconds"
