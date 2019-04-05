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


class ShareAccessRight(Model):
    """Specifies the mapping between this particular user and the type of access
    he has on shares on this device.

    All required parameters must be populated in order to send to Azure.

    :param share_id: Required. The share ID.
    :type share_id: str
    :param access_type: Required. Type of access to be allowed on the share
     for this user. Possible values include: 'Change', 'Read', 'Custom'
    :type access_type: str or ~azure.mgmt.edgegateway.models.ShareAccessType
    """

    _validation = {
        'share_id': {'required': True},
        'access_type': {'required': True},
    }

    _attribute_map = {
        'share_id': {'key': 'shareId', 'type': 'str'},
        'access_type': {'key': 'accessType', 'type': 'str'},
    }

    def __init__(self, *, share_id: str, access_type, **kwargs) -> None:
        super(ShareAccessRight, self).__init__(**kwargs)
        self.share_id = share_id
        self.access_type = access_type
