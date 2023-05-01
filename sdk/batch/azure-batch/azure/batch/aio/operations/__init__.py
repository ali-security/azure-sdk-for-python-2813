# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import ApplicationsOperations
from ._operations import PoolOperations
from ._operations import AccountOperations
from ._operations import JobOperations
from ._operations import CertificatesOperations
from ._operations import FileOperations
from ._operations import JobScheduleOperations
from ._operations import TaskOperations
from ._operations import ComputeNodesOperations
from ._operations import ComputeNodeExtensionsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApplicationsOperations",
    "PoolOperations",
    "AccountOperations",
    "JobOperations",
    "CertificatesOperations",
    "FileOperations",
    "JobScheduleOperations",
    "TaskOperations",
    "ComputeNodesOperations",
    "ComputeNodeExtensionsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
