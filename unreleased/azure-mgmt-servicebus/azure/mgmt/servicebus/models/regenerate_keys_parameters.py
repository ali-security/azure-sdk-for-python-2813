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


class RegenerateKeysParameters(Model):
    """Parameters supplied to the Regenerate Auth Rule.

    :param policykey: Key that needs to be regenerated . Possible values
     include: 'PrimaryKey', 'SecondaryKey'
    :type policykey: str or :class:`Policykey
     <azure.mgmt.servicebus.models.Policykey>`
    """ 

    _attribute_map = {
        'policykey': {'key': 'Policykey', 'type': 'Policykey'},
    }

    def __init__(self, policykey=None):
        self.policykey = policykey
