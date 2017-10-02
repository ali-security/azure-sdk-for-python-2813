# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RemoteLoginInformation(Model):
    """Contains remote login details to SSH/RDP to a compute node in cluster.

    :param node_id: Id of the compute node
    :type node_id: str
    :param ip_address: ip address
    :type ip_address: str
    :param port: port number.
    :type port: float
    """

    _validation = {
        'node_id': {'required': True},
        'ip_address': {'required': True},
        'port': {'required': True},
    }

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'port': {'key': 'port', 'type': 'float'},
    }

    def __init__(self, node_id, ip_address, port):
        self.node_id = node_id
        self.ip_address = ip_address
        self.port = port
