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


class StorageProfile(Model):
    """Specifies the storage settings for the virtual machine disks.

    :param image_reference: Specifies information about the image to use. You
     can specify information about platform images, marketplace images, or
     virtual machine images. This element is required when you want to use a
     platform image, marketplace image, or virtual machine image, but is not
     used in other creation operations.
    :type image_reference:
     ~azure.mgmt.compute.v2017_03_30.models.ImageReference
    :param os_disk: Specifies information about the operating system disk used
     by the virtual machine. <br><br> For more information about disks, see
     [About disks and VHDs for Azure virtual
     machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
    :type os_disk: ~azure.mgmt.compute.v2017_03_30.models.OSDisk
    :param data_disks: Specifies the parameters that are used to add a data
     disk to a virtual machine. <br><br> For more information about disks, see
     [About disks and VHDs for Azure virtual
     machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
    :type data_disks: list[~azure.mgmt.compute.v2017_03_30.models.DataDisk]
    """

    _attribute_map = {
        'image_reference': {'key': 'imageReference', 'type': 'ImageReference'},
        'os_disk': {'key': 'osDisk', 'type': 'OSDisk'},
        'data_disks': {'key': 'dataDisks', 'type': '[DataDisk]'},
    }

    def __init__(self, image_reference=None, os_disk=None, data_disks=None):
        self.image_reference = image_reference
        self.os_disk = os_disk
        self.data_disks = data_disks
