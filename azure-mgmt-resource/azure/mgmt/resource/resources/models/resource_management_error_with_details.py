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

from .resource_management_error import ResourceManagementError


class ResourceManagementErrorWithDetails(ResourceManagementError):
    """ResourceManagementErrorWithDetails

    :param code: Gets or sets the error code returned from the server.
    :type code: str
    :param message: Gets or sets the error message returned from the server.
    :type message: str
    :param target: Gets or sets the target of the error.
    :type target: str
    :param details: Gets or sets validation error.
    :type details: list of :class:`ResourceManagementError
     <resourcemanagementclient.models.ResourceManagementError>`
    """ 

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ResourceManagementError]'},
    }

    def __init__(self, code, message, target=None, details=None):
        super(ResourceManagementErrorWithDetails, self).__init__(code=code, message=message, target=target)
        self.details = details
