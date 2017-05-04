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


class NodeInfo(Model):
    """Information about a node in Service Fabric cluster.

    :param name: The name of the node.
    :type name: str
    :param ip_address_or_fqdn: The IP address or fully qualified domain name
     of the node.
    :type ip_address_or_fqdn: str
    :param type: The type of the node.
    :type type: str
    :param code_version: The version of Service Fabric binaries that the node
     is running.
    :type code_version: str
    :param config_version: The version of Service Fabric cluster manifest
     that the node is using.
    :type config_version: str
    :param node_status: Possible values include: 'Invalid', 'Up', 'Down',
     'Enabling', 'Disabling', 'Disabled', 'Unknown', 'Removed'
    :type node_status: str
    :param node_up_time_in_seconds: Time in seconds since the node has been
     in NodeStatus Up. Value ero indicates that the node is not Up.
    :type node_up_time_in_seconds: str
    :param health_state: Possible values include: 'Invalid', 'Ok', 'Warning',
     'Error', 'Unknown'
    :type health_state: str
    :param is_seed_node: Indicates if the node is a seed node or not. Returns
     true if the node is a seed node, otherwise false. A quorum of seed nodes
     are required for proper operation of Service Fabric cluster.
    :type is_seed_node: bool
    :param upgrade_domain: The upgrade domain of the node.
    :type upgrade_domain: str
    :param fault_domain: The fault domain of the node.
    :type fault_domain: str
    :param id:
    :type id: :class:`NodeId <azure.servicefabric.models.NodeId>`
    :param instance_id: The id representing the node instance. While the Id
     of the node is deterministically generated from the node name and
     remains same across restarts, the InstanceId changes every time node
     restarts.
    :type instance_id: str
    :param node_deactivation_info:
    :type node_deactivation_info: :class:`NodeDeactivationInfo
     <azure.servicefabric.models.NodeDeactivationInfo>`
    :param is_stopped: Indicates if the node is stopped by calling stop node
     API or not. Returns true if the node is stopped, otherwise false.
    :type is_stopped: bool
    :param node_down_time_in_seconds: Time in seconds since the node has been
     in NodeStatus Down. Value zero indicates node is not NodeStatus Down.
    :type node_down_time_in_seconds: str
    """ 

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'ip_address_or_fqdn': {'key': 'IpAddressOrFQDN', 'type': 'str'},
        'type': {'key': 'Type', 'type': 'str'},
        'code_version': {'key': 'CodeVersion', 'type': 'str'},
        'config_version': {'key': 'ConfigVersion', 'type': 'str'},
        'node_status': {'key': 'NodeStatus', 'type': 'str'},
        'node_up_time_in_seconds': {'key': 'NodeUpTimeInSeconds', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'is_seed_node': {'key': 'IsSeedNode', 'type': 'bool'},
        'upgrade_domain': {'key': 'UpgradeDomain', 'type': 'str'},
        'fault_domain': {'key': 'FaultDomain', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'NodeId'},
        'instance_id': {'key': 'InstanceId', 'type': 'str'},
        'node_deactivation_info': {'key': 'NodeDeactivationInfo', 'type': 'NodeDeactivationInfo'},
        'is_stopped': {'key': 'IsStopped', 'type': 'bool'},
        'node_down_time_in_seconds': {'key': 'NodeDownTimeInSeconds', 'type': 'str'},
    }

    def __init__(self, name=None, ip_address_or_fqdn=None, type=None, code_version=None, config_version=None, node_status=None, node_up_time_in_seconds=None, health_state=None, is_seed_node=None, upgrade_domain=None, fault_domain=None, id=None, instance_id=None, node_deactivation_info=None, is_stopped=None, node_down_time_in_seconds=None):
        self.name = name
        self.ip_address_or_fqdn = ip_address_or_fqdn
        self.type = type
        self.code_version = code_version
        self.config_version = config_version
        self.node_status = node_status
        self.node_up_time_in_seconds = node_up_time_in_seconds
        self.health_state = health_state
        self.is_seed_node = is_seed_node
        self.upgrade_domain = upgrade_domain
        self.fault_domain = fault_domain
        self.id = id
        self.instance_id = instance_id
        self.node_deactivation_info = node_deactivation_info
        self.is_stopped = is_stopped
        self.node_down_time_in_seconds = node_down_time_in_seconds
