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


class OperationImpact(Model):
    """Represents impact of an operation, both in absolute and relative terms.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the impact dimension.
    :vartype name: str
    :ivar unit: The unit in which estimated impact to dimension is measured.
    :vartype unit: str
    :ivar change_value_absolute: The absolute impact to dimension.
    :vartype change_value_absolute: float
    :ivar change_value_relative: The relative impact to dimension (null if
     not applicable)
    :vartype change_value_relative: float
    """ 

    _validation = {
        'name': {'readonly': True},
        'unit': {'readonly': True},
        'change_value_absolute': {'readonly': True},
        'change_value_relative': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'change_value_absolute': {'key': 'changeValueAbsolute', 'type': 'float'},
        'change_value_relative': {'key': 'changeValueRelative', 'type': 'float'},
    }

    def __init__(self):
        self.name = None
        self.unit = None
        self.change_value_absolute = None
        self.change_value_relative = None
