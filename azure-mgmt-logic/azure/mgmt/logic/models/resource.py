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


class Resource(Model):
    """Resource.

    :param id: The resource id.
    :type id: str
    :param name: Gets the resource name.
    :type name: str
    :param type: Gets the resource type.
    :type type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None):
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags
