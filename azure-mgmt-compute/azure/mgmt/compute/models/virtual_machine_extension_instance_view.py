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


class VirtualMachineExtensionInstanceView(Model):
    """
    The instance view of a virtual machine extension.

    :param name: Gets or sets the virtual machine extension name.
    :type name: str
    :param type: Gets or sets the full type of the extension handler which
     includes both publisher and type.
    :type type: str
    :param type_handler_version: Gets or sets the type version of the
     extension handler.
    :type type_handler_version: str
    :param substatuses: Gets or sets the resource status information.
    :type substatuses: list of :class:`InstanceViewStatus
     <computemanagementclient.models.InstanceViewStatus>`
    :param statuses: Gets or sets the resource status information.
    :type statuses: list of :class:`InstanceViewStatus
     <computemanagementclient.models.InstanceViewStatus>`
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'type_handler_version': {'key': 'typeHandlerVersion', 'type': 'str'},
        'substatuses': {'key': 'substatuses', 'type': '[InstanceViewStatus]'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, name=None, type=None, type_handler_version=None, substatuses=None, statuses=None):
        self.name = name
        self.type = type
        self.type_handler_version = type_handler_version
        self.substatuses = substatuses
        self.statuses = statuses
