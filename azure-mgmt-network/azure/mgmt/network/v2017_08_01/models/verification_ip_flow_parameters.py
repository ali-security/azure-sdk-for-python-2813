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


class VerificationIPFlowParameters(Model):
    """Parameters that define the IP flow to be verified.

    :param target_resource_id: The ID of the target resource to perform
     next-hop on.
    :type target_resource_id: str
    :param direction: The direction of the packet represented as a 5-tuple.
     Possible values include: 'Inbound', 'Outbound'
    :type direction: str or :class:`Direction
     <azure.mgmt.network.v2017_08_01.models.Direction>`
    :param protocol: Protocol to be verified on. Possible values include:
     'TCP', 'UDP'
    :type protocol: str or :class:`Protocol
     <azure.mgmt.network.v2017_08_01.models.Protocol>`
    :param local_port: The local port. Acceptable values are a single integer
     in the range (0-65535). Support for * for the source port, which depends
     on the direction.
    :type local_port: str
    :param remote_port: The remote port. Acceptable values are a single
     integer in the range (0-65535). Support for * for the source port, which
     depends on the direction.
    :type remote_port: str
    :param local_ip_address: The local IP address. Acceptable values are valid
     IPv4 addresses.
    :type local_ip_address: str
    :param remote_ip_address: The remote IP address. Acceptable values are
     valid IPv4 addresses.
    :type remote_ip_address: str
    :param target_nic_resource_id: The NIC ID. (If VM has multiple NICs and IP
     forwarding is enabled on any of them, then this parameter must be
     specified. Otherwise optional).
    :type target_nic_resource_id: str
    """

    _validation = {
        'target_resource_id': {'required': True},
        'direction': {'required': True},
        'protocol': {'required': True},
        'local_port': {'required': True},
        'remote_port': {'required': True},
        'local_ip_address': {'required': True},
        'remote_ip_address': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
        'local_port': {'key': 'localPort', 'type': 'str'},
        'remote_port': {'key': 'remotePort', 'type': 'str'},
        'local_ip_address': {'key': 'localIPAddress', 'type': 'str'},
        'remote_ip_address': {'key': 'remoteIPAddress', 'type': 'str'},
        'target_nic_resource_id': {'key': 'targetNicResourceId', 'type': 'str'},
    }

    def __init__(self, target_resource_id, direction, protocol, local_port, remote_port, local_ip_address, remote_ip_address, target_nic_resource_id=None):
        self.target_resource_id = target_resource_id
        self.direction = direction
        self.protocol = protocol
        self.local_port = local_port
        self.remote_port = remote_port
        self.local_ip_address = local_ip_address
        self.remote_ip_address = remote_ip_address
        self.target_nic_resource_id = target_nic_resource_id
