# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ProvisioningState(Enum):

    invalid = "Invalid"
    creating = "Creating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"


class AccountKeyType(Enum):

    primary = "Primary"
    secondary = "Secondary"


class PackageState(Enum):

    pending = "pending"
    active = "active"
    unmapped = "unmapped"
