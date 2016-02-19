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

from msrest.serialization import Model


class ApplicationGatewayBackendAddress(Model):
    """
    Backend Address of application gateway

    :param str fqdn: Gets or sets the dns name
    :param str ip_address: Gets or sets the ip address
    """

    _required = []

    _attribute_map = {
        'fqdn': {'key': 'fqdn', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
    }

    def __init__(self, fqdn=None, ip_address=None):
        self.fqdn = fqdn
        self.ip_address = ip_address
