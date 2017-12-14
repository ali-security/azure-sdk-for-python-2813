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

from msrest.serialization import Model


class VirtualMachineScaleSetVMInstanceView(Model):
    """The instance view of a virtual machine scale set VM.

    :param platform_update_domain: The Update Domain count.
    :type platform_update_domain: int
    :param platform_fault_domain: The Fault Domain count.
    :type platform_fault_domain: int
    :param rdp_thumb_print: The Remote desktop certificate thumbprint.
    :type rdp_thumb_print: str
    :param vm_agent: The VM Agent running on the virtual machine.
    :type vm_agent:
     ~azure.mgmt.compute.v2015_06_15.models.VirtualMachineAgentInstanceView
    :param disks: The disks information.
    :type disks: list[~azure.mgmt.compute.v2015_06_15.models.DiskInstanceView]
    :param extensions: The extensions information.
    :type extensions:
     list[~azure.mgmt.compute.v2015_06_15.models.VirtualMachineExtensionInstanceView]
    :param boot_diagnostics: Boot Diagnostics is a debugging feature which
     allows you to view Console Output and Screenshot to diagnose VM status.
     <br><br> For Linux Virtual Machines, you can easily view the output of
     your console log. <br><br> For both Windows and Linux virtual machines,
     Azure also enables you to see a screenshot of the VM from the hypervisor.
    :type boot_diagnostics:
     ~azure.mgmt.compute.v2015_06_15.models.BootDiagnosticsInstanceView
    :param statuses: The resource status information.
    :type statuses:
     list[~azure.mgmt.compute.v2015_06_15.models.InstanceViewStatus]
    """

    _attribute_map = {
        'platform_update_domain': {'key': 'platformUpdateDomain', 'type': 'int'},
        'platform_fault_domain': {'key': 'platformFaultDomain', 'type': 'int'},
        'rdp_thumb_print': {'key': 'rdpThumbPrint', 'type': 'str'},
        'vm_agent': {'key': 'vmAgent', 'type': 'VirtualMachineAgentInstanceView'},
        'disks': {'key': 'disks', 'type': '[DiskInstanceView]'},
        'extensions': {'key': 'extensions', 'type': '[VirtualMachineExtensionInstanceView]'},
        'boot_diagnostics': {'key': 'bootDiagnostics', 'type': 'BootDiagnosticsInstanceView'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, platform_update_domain=None, platform_fault_domain=None, rdp_thumb_print=None, vm_agent=None, disks=None, extensions=None, boot_diagnostics=None, statuses=None):
        super(VirtualMachineScaleSetVMInstanceView, self).__init__()
        self.platform_update_domain = platform_update_domain
        self.platform_fault_domain = platform_fault_domain
        self.rdp_thumb_print = rdp_thumb_print
        self.vm_agent = vm_agent
        self.disks = disks
        self.extensions = extensions
        self.boot_diagnostics = boot_diagnostics
        self.statuses = statuses
