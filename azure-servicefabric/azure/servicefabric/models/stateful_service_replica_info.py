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

from .replica_info import ReplicaInfo


class StatefulServiceReplicaInfo(ReplicaInfo):
    """Represents a stateful service replica. This includes information about the
    identity, role, status, health, node name, uptime, and other details about
    the replica.

    :param replica_status: Possible values include: 'Invalid', 'InBuild',
     'Standby', 'Ready', 'Down', 'Dropped'
    :type replica_status: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param health_state: Possible values include: 'Invalid', 'Ok', 'Warning',
     'Error', 'Unknown'
    :type health_state: str or :class:`enum <azure.servicefabric.models.enum>`
    :param node_name:
    :type node_name: str
    :param address: The address the replica is listening on.
    :type address: str
    :param last_in_build_duration_in_seconds: The last in build duration of
     the replica in seconds.
    :type last_in_build_duration_in_seconds: str
    :param service_kind: Polymorphic Discriminator
    :type service_kind: str
    :param replica_role: Possible values include: 'Unknown', 'None',
     'Primary', 'IdleSecondary', 'ActiveSecondary'
    :type replica_role: str or :class:`enum <azure.servicefabric.models.enum>`
    :param replica_id:
    :type replica_id: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'replica_status': {'key': 'ReplicaStatus', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'address': {'key': 'Address', 'type': 'str'},
        'last_in_build_duration_in_seconds': {'key': 'LastInBuildDurationInSeconds', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'replica_role': {'key': 'ReplicaRole', 'type': 'str'},
        'replica_id': {'key': 'ReplicaId', 'type': 'str'},
    }

    def __init__(self, replica_status=None, health_state=None, node_name=None, address=None, last_in_build_duration_in_seconds=None, replica_role=None, replica_id=None):
        super(StatefulServiceReplicaInfo, self).__init__(replica_status=replica_status, health_state=health_state, node_name=node_name, address=address, last_in_build_duration_in_seconds=last_in_build_duration_in_seconds)
        self.replica_role = replica_role
        self.replica_id = replica_id
        self.service_kind = 'Stateful'
