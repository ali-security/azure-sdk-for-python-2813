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


class ListContentKeysResponse(Model):
    """Class of response for listContentKeys action.

    :param content_keys: ContentKeys used by current Streaming Locator
    :type content_keys:
     list[~azure.mgmt.media.models.StreamingLocatorContentKey]
    """

    _attribute_map = {
        'content_keys': {'key': 'contentKeys', 'type': '[StreamingLocatorContentKey]'},
    }

    def __init__(self, **kwargs):
        super(ListContentKeysResponse, self).__init__(**kwargs)
        self.content_keys = kwargs.get('content_keys', None)
