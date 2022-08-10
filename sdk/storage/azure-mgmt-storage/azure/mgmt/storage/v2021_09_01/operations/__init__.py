# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._skus_operations import SkusOperations
from ._storage_accounts_operations import StorageAccountsOperations
from ._deleted_accounts_operations import DeletedAccountsOperations
from ._usages_operations import UsagesOperations
from ._management_policies_operations import ManagementPoliciesOperations
from ._blob_inventory_policies_operations import BlobInventoryPoliciesOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._object_replication_policies_operations import ObjectReplicationPoliciesOperations
from ._local_users_operations import LocalUsersOperations
from ._encryption_scopes_operations import EncryptionScopesOperations
from ._blob_services_operations import BlobServicesOperations
from ._blob_containers_operations import BlobContainersOperations
from ._file_services_operations import FileServicesOperations
from ._file_shares_operations import FileSharesOperations
from ._queue_services_operations import QueueServicesOperations
from ._queue_operations import QueueOperations
from ._table_services_operations import TableServicesOperations
from ._table_operations import TableOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'Operations',
    'SkusOperations',
    'StorageAccountsOperations',
    'DeletedAccountsOperations',
    'UsagesOperations',
    'ManagementPoliciesOperations',
    'BlobInventoryPoliciesOperations',
    'PrivateEndpointConnectionsOperations',
    'PrivateLinkResourcesOperations',
    'ObjectReplicationPoliciesOperations',
    'LocalUsersOperations',
    'EncryptionScopesOperations',
    'BlobServicesOperations',
    'BlobContainersOperations',
    'FileServicesOperations',
    'FileSharesOperations',
    'QueueServicesOperations',
    'QueueOperations',
    'TableServicesOperations',
    'TableOperations',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()