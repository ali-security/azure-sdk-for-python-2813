# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ApplicationGatewayBackendHttpSettings(SubResource):
    """
    Backend address pool settings of application gateway

    :param id: Resource Id
    :type id: str
    :param port: Gets or sets the port
    :type port: int
    :param protocol: Gets or sets the protocol. Possible values include:
     'Http', 'Https'
    :type protocol: str
    :param cookie_based_affinity: Gets or sets the cookie affinity. Possible
     values include: 'Enabled', 'Disabled'
    :type cookie_based_affinity: str
    :param request_timeout: Gets or sets request timeout
    :type request_timeout: int
    :param probe: Gets or sets probe resource of application gateway
    :type probe: :class:`SubResource
     <networkmanagementclient.models.SubResource>`
    :param provisioning_state: Gets or sets Provisioning state of the backend
     http settings resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'port': {'key': 'properties.port', 'type': 'int'},
        'protocol': {'key': 'properties.protocol', 'type': 'ApplicationGatewayProtocol'},
        'cookie_based_affinity': {'key': 'properties.cookieBasedAffinity', 'type': 'ApplicationGatewayCookieBasedAffinity'},
        'request_timeout': {'key': 'properties.requestTimeout', 'type': 'int'},
        'probe': {'key': 'properties.probe', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, port=None, protocol=None, cookie_based_affinity=None, request_timeout=None, probe=None, provisioning_state=None, name=None, etag=None):
        super(ApplicationGatewayBackendHttpSettings, self).__init__(id=id)
        self.port = port
        self.protocol = protocol
        self.cookie_based_affinity = cookie_based_affinity
        self.request_timeout = request_timeout
        self.probe = probe
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
