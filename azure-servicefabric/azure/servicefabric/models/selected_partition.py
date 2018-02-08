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


class SelectedPartition(Model):
    """This class returns information about the partition that the user-induced
    operation acted upon.

    :param service_name: The name of the service the partition belongs to.
    :type service_name: str
    :param partition_id: An internal ID used by Service Fabric to uniquely
     identify a partition. This is a randomly generated GUID when the service
     was created. The partition id is unique and does not change for the
     lifetime of the service. If the same service was deleted and recreated the
     ids of its partitions would be different.
    :type partition_id: str
    """

    _attribute_map = {
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
    }

    def __init__(self, service_name=None, partition_id=None):
        super(SelectedPartition, self).__init__()
        self.service_name = service_name
        self.partition_id = partition_id
