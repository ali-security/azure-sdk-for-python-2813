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

from .sub_resource import SubResource


class BackendAddressPool(SubResource):
    """Pool of backend IP addresses.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar backend_ip_configurations: Gets collection of references to IP
     addresses defined in network interfaces.
    :vartype backend_ip_configurations:
     list[~azure.mgmt.network.v2017_09_01.models.NetworkInterfaceIPConfiguration]
    :ivar load_balancing_rules: Gets load balancing rules that use this
     backend address pool.
    :vartype load_balancing_rules:
     list[~azure.mgmt.network.v2017_09_01.models.SubResource]
    :ivar outbound_nat_rule: Gets outbound rules that use this backend address
     pool.
    :vartype outbound_nat_rule:
     ~azure.mgmt.network.v2017_09_01.models.SubResource
    :param provisioning_state: Get provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'backend_ip_configurations': {'readonly': True},
        'load_balancing_rules': {'readonly': True},
        'outbound_nat_rule': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'backend_ip_configurations': {'key': 'properties.backendIPConfigurations', 'type': '[NetworkInterfaceIPConfiguration]'},
        'load_balancing_rules': {'key': 'properties.loadBalancingRules', 'type': '[SubResource]'},
        'outbound_nat_rule': {'key': 'properties.outboundNatRule', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, provisioning_state: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(BackendAddressPool, self).__init__(id=id, **kwargs)
        self.backend_ip_configurations = None
        self.load_balancing_rules = None
        self.outbound_nat_rule = None
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
