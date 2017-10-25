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


class CheckNameAvailabilityOutput(Model):
    """Output of check name availability API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_available: Indicates whether the name is available.
    :vartype name_available: bool
    :ivar reason: The reason why the name is not available.
    :vartype reason: str
    :ivar message: The detailed error message describing why the name is not
     available.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self):
        self.name_available = None
        self.reason = None
        self.message = None
