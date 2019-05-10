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


class FormOperationError(Model):
    """Error reported during an operation.

    :param error_message: Message reported during the train operation.
    :type error_message: str
    """

    _attribute_map = {
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(self, *, error_message: str=None, **kwargs) -> None:
        super(FormOperationError, self).__init__(**kwargs)
        self.error_message = error_message
