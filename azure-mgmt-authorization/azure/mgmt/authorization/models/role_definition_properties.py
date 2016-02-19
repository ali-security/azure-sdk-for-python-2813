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


class RoleDefinitionProperties(Model):
    """
    Role definition properties.

    :param str role_name: Gets or sets role name.
    :param str description: Gets or sets role definition description.
    :param str type: Gets or sets role type.
    :param list permissions: Gets or sets role definition permissions.
    :param list assignable_scopes: Gets or sets role definition assignable
     scopes.
    """

    _required = []

    _attribute_map = {
        'role_name': {'key': 'roleName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': '[Permission]'},
        'assignable_scopes': {'key': 'assignableScopes', 'type': '[str]'},
    }

    def __init__(self, role_name=None, description=None, type=None, permissions=None, assignable_scopes=None):
        self.role_name = role_name
        self.description = description
        self.type = type
        self.permissions = permissions
        self.assignable_scopes = assignable_scopes
