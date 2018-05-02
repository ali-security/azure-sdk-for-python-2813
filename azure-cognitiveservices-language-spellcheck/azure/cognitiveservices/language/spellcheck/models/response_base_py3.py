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


class ResponseBase(Model):
    """ResponseBase.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Identifiable

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'Identifiable': 'Identifiable'}
    }

    def __init__(self, **kwargs) -> None:
        super(ResponseBase, self).__init__(**kwargs)
        self._type = None
