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


class Volume(Model):
    """The properties of the volume.

    :param name: The name of the volume.
    :type name: str
    :param azure_file: The name of the Azure File volume.
    :type azure_file: :class:`AzureFileVolume
     <azure.mgmt.containerinstance.models.AzureFileVolume>`
    :param empty_dir: The empty directory volume.
    :type empty_dir: object
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'azure_file': {'key': 'azureFile', 'type': 'AzureFileVolume'},
        'empty_dir': {'key': 'emptyDir', 'type': 'object'},
    }

    def __init__(self, name, azure_file=None, empty_dir=None):
        self.name = name
        self.azure_file = azure_file
        self.empty_dir = empty_dir
