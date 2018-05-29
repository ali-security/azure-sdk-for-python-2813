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


class CheckNameAvailabilityInput(Model):
    """Input of check name availability API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The Search service name to validate. Search service
     names must only contain lowercase letters, digits or dashes, cannot use
     dash as the first two or last one characters, cannot contain consecutive
     dashes, and must be between 2 and 60 characters in length.
    :type name: str
    :ivar type: Required. The type of the resource whose name is to be
     validated. This value must always be 'searchServices'. Default value:
     "searchServices" .
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "searchServices"

    def __init__(self, *, name: str, **kwargs) -> None:
        super(CheckNameAvailabilityInput, self).__init__(**kwargs)
        self.name = name
