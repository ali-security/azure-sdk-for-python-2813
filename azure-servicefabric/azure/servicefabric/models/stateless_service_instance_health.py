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

from .replica_health import ReplicaHealth


class StatelessServiceInstanceHealth(ReplicaHealth):
    """Represents the health of the statelss service instance.
    Contains the instance aggregated health state, the health events and the
    unhealthy evaluations.
    .

    :param aggregated_health_state: The HealthState representing the
     aggregated health state of the entity computed by Health Manager.
     The health evaluation of the entity reflects all events reported on the
     entity and its children (if any).
     The aggregation is done by applying the desired health policy.
     . Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str
    :param health_events: The list of health events reported on the entity.
    :type health_events: list of :class:`HealthEvent
     <azure.servicefabric.models.HealthEvent>`
    :param unhealthy_evaluations: The unhealthy evaluations that show why the
     current aggregated health state was returned by Health Manager.
    :type unhealthy_evaluations: list of :class:`HealthEvaluationWrapper
     <azure.servicefabric.models.HealthEvaluationWrapper>`
    :param partition_id: Id of the partition to which this replica belongs.
    :type partition_id: str
    :param ServiceKind: Polymorphic Discriminator
    :type ServiceKind: str
    :param instance_id: Id of the stateless service instance.
    :type instance_id: str
    """ 

    _validation = {
        'ServiceKind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'health_events': {'key': 'HealthEvents', 'type': '[HealthEvent]'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'ServiceKind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_id': {'key': 'InstanceId', 'type': 'str'},
    }

    def __init__(self, aggregated_health_state=None, health_events=None, unhealthy_evaluations=None, partition_id=None, instance_id=None):
        super(StatelessServiceInstanceHealth, self).__init__(aggregated_health_state=aggregated_health_state, health_events=health_events, unhealthy_evaluations=unhealthy_evaluations, partition_id=partition_id)
        self.instance_id = instance_id
        self.ServiceKind = 'Stateless'
