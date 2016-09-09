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

from .resource import Resource


class NodeResource(Resource):
    """A Node Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: ARM Resource ID
    :vartype id: str
    :ivar type: ARM Resource Type
    :vartype type: str
    :ivar name: ARM Resource Name
    :vartype name: str
    :ivar location: ARM Resource Location
    :vartype location: str
    :param tags: ARM Resource Tags
    :type tags: dict
    :param etag:
    :type etag: str
    :param gateway_id: Id of the gateway
    :type gateway_id: str
    :param connection_name: myhost.domain.com
    :type connection_name: str
    :param created: UTC date and time when node was first added to management
     service
    :type created: datetime
    :param updated: UTC date and time when node was last updated.
    :type updated: datetime
    """ 

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'gateway_id': {'key': 'properties.gatewayId', 'type': 'str'},
        'connection_name': {'key': 'properties.connectionName', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'updated': {'key': 'properties.updated', 'type': 'iso-8601'},
    }

    def __init__(self, tags=None, etag=None, gateway_id=None, connection_name=None, created=None, updated=None):
        super(NodeResource, self).__init__(tags=tags, etag=etag)
        self.gateway_id = gateway_id
        self.connection_name = connection_name
        self.created = created
        self.updated = updated
