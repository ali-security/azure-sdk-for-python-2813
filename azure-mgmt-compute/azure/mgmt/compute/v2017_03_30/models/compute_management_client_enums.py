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


class StatusLevelTypes(Enum):

    info = "Info"
    warning = "Warning"
    error = "Error"


class OperatingSystemTypes(Enum):

    windows = "Windows"
    linux = "Linux"


class VirtualMachineSizeTypes(Enum):

    basic_a0 = "Basic_A0"
    basic_a1 = "Basic_A1"
    basic_a2 = "Basic_A2"
    basic_a3 = "Basic_A3"
    basic_a4 = "Basic_A4"
    standard_a0 = "Standard_A0"
    standard_a1 = "Standard_A1"
    standard_a2 = "Standard_A2"
    standard_a3 = "Standard_A3"
    standard_a4 = "Standard_A4"
    standard_a5 = "Standard_A5"
    standard_a6 = "Standard_A6"
    standard_a7 = "Standard_A7"
    standard_a8 = "Standard_A8"
    standard_a9 = "Standard_A9"
    standard_a10 = "Standard_A10"
    standard_a11 = "Standard_A11"
    standard_a1_v2 = "Standard_A1_v2"
    standard_a2_v2 = "Standard_A2_v2"
    standard_a4_v2 = "Standard_A4_v2"
    standard_a8_v2 = "Standard_A8_v2"
    standard_a2m_v2 = "Standard_A2m_v2"
    standard_a4m_v2 = "Standard_A4m_v2"
    standard_a8m_v2 = "Standard_A8m_v2"
    standard_d1 = "Standard_D1"
    standard_d2 = "Standard_D2"
    standard_d3 = "Standard_D3"
    standard_d4 = "Standard_D4"
    standard_d11 = "Standard_D11"
    standard_d12 = "Standard_D12"
    standard_d13 = "Standard_D13"
    standard_d14 = "Standard_D14"
    standard_d1_v2 = "Standard_D1_v2"
    standard_d2_v2 = "Standard_D2_v2"
    standard_d3_v2 = "Standard_D3_v2"
    standard_d4_v2 = "Standard_D4_v2"
    standard_d5_v2 = "Standard_D5_v2"
    standard_d11_v2 = "Standard_D11_v2"
    standard_d12_v2 = "Standard_D12_v2"
    standard_d13_v2 = "Standard_D13_v2"
    standard_d14_v2 = "Standard_D14_v2"
    standard_d15_v2 = "Standard_D15_v2"
    standard_ds1 = "Standard_DS1"
    standard_ds2 = "Standard_DS2"
    standard_ds3 = "Standard_DS3"
    standard_ds4 = "Standard_DS4"
    standard_ds11 = "Standard_DS11"
    standard_ds12 = "Standard_DS12"
    standard_ds13 = "Standard_DS13"
    standard_ds14 = "Standard_DS14"
    standard_ds1_v2 = "Standard_DS1_v2"
    standard_ds2_v2 = "Standard_DS2_v2"
    standard_ds3_v2 = "Standard_DS3_v2"
    standard_ds4_v2 = "Standard_DS4_v2"
    standard_ds5_v2 = "Standard_DS5_v2"
    standard_ds11_v2 = "Standard_DS11_v2"
    standard_ds12_v2 = "Standard_DS12_v2"
    standard_ds13_v2 = "Standard_DS13_v2"
    standard_ds14_v2 = "Standard_DS14_v2"
    standard_ds15_v2 = "Standard_DS15_v2"
    standard_f1 = "Standard_F1"
    standard_f2 = "Standard_F2"
    standard_f4 = "Standard_F4"
    standard_f8 = "Standard_F8"
    standard_f16 = "Standard_F16"
    standard_f1s = "Standard_F1s"
    standard_f2s = "Standard_F2s"
    standard_f4s = "Standard_F4s"
    standard_f8s = "Standard_F8s"
    standard_f16s = "Standard_F16s"
    standard_g1 = "Standard_G1"
    standard_g2 = "Standard_G2"
    standard_g3 = "Standard_G3"
    standard_g4 = "Standard_G4"
    standard_g5 = "Standard_G5"
    standard_gs1 = "Standard_GS1"
    standard_gs2 = "Standard_GS2"
    standard_gs3 = "Standard_GS3"
    standard_gs4 = "Standard_GS4"
    standard_gs5 = "Standard_GS5"
    standard_h8 = "Standard_H8"
    standard_h16 = "Standard_H16"
    standard_h8m = "Standard_H8m"
    standard_h16m = "Standard_H16m"
    standard_h16r = "Standard_H16r"
    standard_h16mr = "Standard_H16mr"
    standard_l4s = "Standard_L4s"
    standard_l8s = "Standard_L8s"
    standard_l16s = "Standard_L16s"
    standard_l32s = "Standard_L32s"
    standard_nc6 = "Standard_NC6"
    standard_nc12 = "Standard_NC12"
    standard_nc24 = "Standard_NC24"
    standard_nc24r = "Standard_NC24r"
    standard_nv6 = "Standard_NV6"
    standard_nv12 = "Standard_NV12"
    standard_nv24 = "Standard_NV24"


class CachingTypes(Enum):

    none = "None"
    read_only = "ReadOnly"
    read_write = "ReadWrite"


class DiskCreateOptionTypes(Enum):

    from_image = "FromImage"
    empty = "Empty"
    attach = "Attach"


class StorageAccountTypes(Enum):

    standard_lrs = "Standard_LRS"
    premium_lrs = "Premium_LRS"


class PassNames(Enum):

    oobe_system = "OobeSystem"


class ComponentNames(Enum):

    microsoft_windows_shell_setup = "Microsoft-Windows-Shell-Setup"


class SettingNames(Enum):

    auto_logon = "AutoLogon"
    first_logon_commands = "FirstLogonCommands"


class ProtocolTypes(Enum):

    http = "Http"
    https = "Https"


class ResourceIdentityType(Enum):

    system_assigned = "SystemAssigned"


class MaintenanceOperationResultCodeTypes(Enum):

    none = "None"
    retry_later = "RetryLater"
    maintenance_aborted = "MaintenanceAborted"
    maintenance_completed = "MaintenanceCompleted"


class UpgradeMode(Enum):

    automatic = "Automatic"
    manual = "Manual"
    rolling = "Rolling"


class OperatingSystemStateTypes(Enum):

    generalized = "Generalized"
    specialized = "Specialized"


class ResourceSkuCapacityScaleType(Enum):

    automatic = "Automatic"
    manual = "Manual"
    none = "None"


class ResourceSkuRestrictionsType(Enum):

    location = "Location"


class ResourceSkuRestrictionsReasonCode(Enum):

    quota_id = "QuotaId"
    not_available_for_subscription = "NotAvailableForSubscription"


class IPVersion(Enum):

    ipv4 = "IPv4"
    ipv6 = "IPv6"


class VirtualMachineScaleSetSkuScaleType(Enum):

    automatic = "Automatic"
    none = "None"


class RollingUpgradeStatusCode(Enum):

    rolling_forward = "RollingForward"
    cancelled = "Cancelled"
    completed = "Completed"
    faulted = "Faulted"


class RollingUpgradeActionType(Enum):

    start = "Start"
    cancel = "Cancel"


class DiskCreateOption(Enum):

    empty = "Empty"
    attach = "Attach"
    from_image = "FromImage"
    import_enum = "Import"
    copy = "Copy"


class AccessLevel(Enum):

    none = "None"
    read = "Read"


class InstanceViewTypes(Enum):

    instance_view = "instanceView"
