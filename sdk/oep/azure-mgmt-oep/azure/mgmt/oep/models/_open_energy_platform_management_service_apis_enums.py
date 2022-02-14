# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class CheckNameAvailabilityReason(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The reason why the given name is not available.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class Origin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"
