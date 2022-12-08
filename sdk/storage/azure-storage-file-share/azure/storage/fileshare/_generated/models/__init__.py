# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessPolicy
from ._models_py3 import ClearRange
from ._models_py3 import CopyFileSmbInfo
from ._models_py3 import CorsRule
from ._models_py3 import DestinationLeaseAccessConditions
from ._models_py3 import DirectoryItem
from ._models_py3 import FileHTTPHeaders
from ._models_py3 import FileItem
from ._models_py3 import FileProperty
from ._models_py3 import FileRange
from ._models_py3 import FilesAndDirectoriesListSegment
from ._models_py3 import HandleItem
from ._models_py3 import LeaseAccessConditions
from ._models_py3 import ListFilesAndDirectoriesSegmentResponse
from ._models_py3 import ListHandlesResponse
from ._models_py3 import ListSharesResponse
from ._models_py3 import Metrics
from ._models_py3 import RetentionPolicy
from ._models_py3 import ShareFileRangeList
from ._models_py3 import ShareItemInternal
from ._models_py3 import SharePermission
from ._models_py3 import SharePropertiesInternal
from ._models_py3 import ShareProtocolSettings
from ._models_py3 import ShareSmbSettings
from ._models_py3 import ShareStats
from ._models_py3 import SignedIdentifier
from ._models_py3 import SmbMultichannel
from ._models_py3 import SourceLeaseAccessConditions
from ._models_py3 import SourceModifiedAccessConditions
from ._models_py3 import StorageError
from ._models_py3 import StorageServiceProperties
from ._models_py3 import StringEncoded

from ._azure_file_storage_enums import CopyStatusType
from ._azure_file_storage_enums import DeleteSnapshotsOptionType
from ._azure_file_storage_enums import FileLastWrittenMode
from ._azure_file_storage_enums import FileRangeWriteType
from ._azure_file_storage_enums import LeaseDurationType
from ._azure_file_storage_enums import LeaseStateType
from ._azure_file_storage_enums import LeaseStatusType
from ._azure_file_storage_enums import ListFilesIncludeType
from ._azure_file_storage_enums import ListSharesIncludeType
from ._azure_file_storage_enums import PermissionCopyModeType
from ._azure_file_storage_enums import ShareAccessTier
from ._azure_file_storage_enums import ShareRootSquash
from ._azure_file_storage_enums import StorageErrorCode
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessPolicy",
    "ClearRange",
    "CopyFileSmbInfo",
    "CorsRule",
    "DestinationLeaseAccessConditions",
    "DirectoryItem",
    "FileHTTPHeaders",
    "FileItem",
    "FileProperty",
    "FileRange",
    "FilesAndDirectoriesListSegment",
    "HandleItem",
    "LeaseAccessConditions",
    "ListFilesAndDirectoriesSegmentResponse",
    "ListHandlesResponse",
    "ListSharesResponse",
    "Metrics",
    "RetentionPolicy",
    "ShareFileRangeList",
    "ShareItemInternal",
    "SharePermission",
    "SharePropertiesInternal",
    "ShareProtocolSettings",
    "ShareSmbSettings",
    "ShareStats",
    "SignedIdentifier",
    "SmbMultichannel",
    "SourceLeaseAccessConditions",
    "SourceModifiedAccessConditions",
    "StorageError",
    "StorageServiceProperties",
    "StringEncoded",
    "CopyStatusType",
    "DeleteSnapshotsOptionType",
    "FileLastWrittenMode",
    "FileRangeWriteType",
    "LeaseDurationType",
    "LeaseStateType",
    "LeaseStatusType",
    "ListFilesIncludeType",
    "ListSharesIncludeType",
    "PermissionCopyModeType",
    "ShareAccessTier",
    "ShareRootSquash",
    "StorageErrorCode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
