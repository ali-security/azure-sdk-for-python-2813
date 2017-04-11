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


class Encryption(Model):
    """The encryption settings on the storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param services: List of services which support encryption.
    :type services: :class:`EncryptionServices
     <azure.mgmt.storage.v20161201.models.EncryptionServices>`
    :ivar key_source: The encryption keySource (provider). Possible values
     (case-insensitive):  Microsoft.Storage. Default value: "Microsoft.Storage"
     .
    :vartype key_source: str
    """

    _validation = {
        'key_source': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'services': {'key': 'services', 'type': 'EncryptionServices'},
        'key_source': {'key': 'keySource', 'type': 'str'},
    }

    key_source = "Microsoft.Storage"

    def __init__(self, services=None):
        self.services = services
