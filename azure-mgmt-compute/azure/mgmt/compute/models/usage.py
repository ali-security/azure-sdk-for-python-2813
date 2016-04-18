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


class Usage(Model):
    """
    Describes Compute Resource Usage.

    :param unit: Gets or sets an enum describing the unit of measurement.
     Default value: "Count" .
    :type unit: str
    :param current_value: Gets or sets the current value of the usage.
    :type current_value: int
    :param limit: Gets or sets the limit of usage.
    :type limit: long
    :param name: Gets or sets the name of the type of usage.
    :type name: :class:`UsageName <computemanagementclient.models.UsageName>`
    """ 

    _validation = {
        'unit': {'required': True, 'constant': True},
        'current_value': {'required': True},
        'limit': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'long'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(self, current_value, limit, name):
        self.unit = "Count"
        self.current_value = current_value
        self.limit = limit
        self.name = name
