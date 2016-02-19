# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class HostingEnvironment(Resource):
    """
    Description of an hostingEnvironment (App Service Environment)

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param str hosting_environment_name: Name of the hostingEnvironment (App
     Service Environment)
    :param str hosting_environment_location: Location of the
     hostingEnvironment (App Service Environment), e.g. "West US"
    :param str status: Current status of the hostingEnvironment (App Service
     Environment). Possible values include: 'Preparing', 'Ready', 'Scaling',
     'Deleting'
    :param str vnet_name: Name of the hostingEnvironment's (App Service
     Environment) virtual network
    :param str vnet_resource_group_name: Resource group of the
     hostingEnvironment's (App Service Environment) virtual network
    :param str vnet_subnet_name: Subnet of the hostingEnvironment's (App
     Service Environment) virtual network
    :param VirtualNetworkProfile virtual_network: Description of the
     hostingEnvironment's (App Service Environment) virtual network
    :param str internal_load_balancing_mode: Specifies which endpoints to
     serve internally in the hostingEnvironment's (App Service Environment)
     VNET. Possible values include: 'None', 'Web', 'Publishing'
    :param str multi_size: Front-end VM size, e.g. "Medium", "Large"
    :param int multi_role_count: Number of front-end instances
    :param list worker_pools: Description of worker pools with worker size
     ids, VM sizes, and number of workers in each pool
    :param int ipssl_address_count: Number of IP SSL addresses reserved for
     this hostingEnvironment (App Service Environment)
    :param str database_edition: Edition of the metadata database for the
     hostingEnvironment (App Service Environment) e.g. "Standard"
    :param str database_service_objective: Service objective of the metadata
     database for the hostingEnvironment (App Service Environment) e.g. "S0"
    :param int upgrade_domains: Number of upgrade domains of this
     hostingEnvironment (App Service Environment)
    :param str subscription_id: Subscription of the hostingEnvironment (App
     Service Environment)
    :param str dns_suffix: DNS suffix of the hostingEnvironment (App Service
     Environment)
    :param str last_action: Last deployment action on this hostingEnvironment
     (App Service Environment)
    :param str last_action_result: Result of the last deployment action on
     this hostingEnvironment (App Service Environment)
    :param str allowed_multi_sizes: List of comma separated strings
     describing which VM sizes are allowed for front-ends
    :param str allowed_worker_sizes: List of comma separated strings
     describing which VM sizes are allowed for workers
    :param int maximum_number_of_machines: Maximum number of VMs in this
     hostingEnvironment (App Service Environment)
    :param list vip_mappings: Description of IP SSL mapping for this
     hostingEnvironment (App Service Environment)
    :param list environment_capacities: Current total, used, and available
     worker capacities
    :param list network_access_control_list: Access control list for
     controlling traffic to the hostingEnvironment (App Service Environment)
    :param bool environment_is_healthy: True/false indicating whether the
     hostingEnvironment (App Service Environment) is healthy
    :param str environment_status: Detailed message about with results of the
     last check of the hostingEnvironment (App Service Environment)
    :param str resource_group: Resource group of the hostingEnvironment (App
     Service Environment)
    :param str api_management_account_id: Api Management Account associated
     with this Hosting Environment
    :param bool suspended: True/false indicating whether the
     hostingEnvironment is suspended. The environment can be suspended e.g.
     when the management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic)
    """

    _required = []

    _attribute_map = {
        'hosting_environment_name': {'key': 'properties.name', 'type': 'str', 'flatten': True},
        'hosting_environment_location': {'key': 'properties.location', 'type': 'str', 'flatten': True},
        'status': {'key': 'properties.status', 'type': 'HostingEnvironmentStatus', 'flatten': True},
        'vnet_name': {'key': 'properties.vnetName', 'type': 'str', 'flatten': True},
        'vnet_resource_group_name': {'key': 'properties.vnetResourceGroupName', 'type': 'str', 'flatten': True},
        'vnet_subnet_name': {'key': 'properties.vnetSubnetName', 'type': 'str', 'flatten': True},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'VirtualNetworkProfile', 'flatten': True},
        'internal_load_balancing_mode': {'key': 'properties.internalLoadBalancingMode', 'type': 'InternalLoadBalancingMode', 'flatten': True},
        'multi_size': {'key': 'properties.multiSize', 'type': 'str', 'flatten': True},
        'multi_role_count': {'key': 'properties.multiRoleCount', 'type': 'int', 'flatten': True},
        'worker_pools': {'key': 'properties.workerPools', 'type': '[WorkerPool]', 'flatten': True},
        'ipssl_address_count': {'key': 'properties.ipsslAddressCount', 'type': 'int', 'flatten': True},
        'database_edition': {'key': 'properties.databaseEdition', 'type': 'str', 'flatten': True},
        'database_service_objective': {'key': 'properties.databaseServiceObjective', 'type': 'str', 'flatten': True},
        'upgrade_domains': {'key': 'properties.upgradeDomains', 'type': 'int', 'flatten': True},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str', 'flatten': True},
        'dns_suffix': {'key': 'properties.dnsSuffix', 'type': 'str', 'flatten': True},
        'last_action': {'key': 'properties.lastAction', 'type': 'str', 'flatten': True},
        'last_action_result': {'key': 'properties.lastActionResult', 'type': 'str', 'flatten': True},
        'allowed_multi_sizes': {'key': 'properties.allowedMultiSizes', 'type': 'str', 'flatten': True},
        'allowed_worker_sizes': {'key': 'properties.allowedWorkerSizes', 'type': 'str', 'flatten': True},
        'maximum_number_of_machines': {'key': 'properties.maximumNumberOfMachines', 'type': 'int', 'flatten': True},
        'vip_mappings': {'key': 'properties.vipMappings', 'type': '[VirtualIPMapping]', 'flatten': True},
        'environment_capacities': {'key': 'properties.environmentCapacities', 'type': '[StampCapacity]', 'flatten': True},
        'network_access_control_list': {'key': 'properties.networkAccessControlList', 'type': '[NetworkAccessControlEntry]', 'flatten': True},
        'environment_is_healthy': {'key': 'properties.environmentIsHealthy', 'type': 'bool', 'flatten': True},
        'environment_status': {'key': 'properties.environmentStatus', 'type': 'str', 'flatten': True},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str', 'flatten': True},
        'api_management_account_id': {'key': 'properties.apiManagementAccountId', 'type': 'str', 'flatten': True},
        'suspended': {'key': 'properties.suspended', 'type': 'bool', 'flatten': True},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, hosting_environment_name=None, hosting_environment_location=None, status=None, vnet_name=None, vnet_resource_group_name=None, vnet_subnet_name=None, virtual_network=None, internal_load_balancing_mode=None, multi_size=None, multi_role_count=None, worker_pools=None, ipssl_address_count=None, database_edition=None, database_service_objective=None, upgrade_domains=None, subscription_id=None, dns_suffix=None, last_action=None, last_action_result=None, allowed_multi_sizes=None, allowed_worker_sizes=None, maximum_number_of_machines=None, vip_mappings=None, environment_capacities=None, network_access_control_list=None, environment_is_healthy=None, environment_status=None, resource_group=None, api_management_account_id=None, suspended=None):
        super(HostingEnvironment, self).__init__(id=id, name=name, location=location, type=type, tags=tags)
        self.hosting_environment_name = hosting_environment_name
        self.hosting_environment_location = hosting_environment_location
        self.status = status
        self.vnet_name = vnet_name
        self.vnet_resource_group_name = vnet_resource_group_name
        self.vnet_subnet_name = vnet_subnet_name
        self.virtual_network = virtual_network
        self.internal_load_balancing_mode = internal_load_balancing_mode
        self.multi_size = multi_size
        self.multi_role_count = multi_role_count
        self.worker_pools = worker_pools
        self.ipssl_address_count = ipssl_address_count
        self.database_edition = database_edition
        self.database_service_objective = database_service_objective
        self.upgrade_domains = upgrade_domains
        self.subscription_id = subscription_id
        self.dns_suffix = dns_suffix
        self.last_action = last_action
        self.last_action_result = last_action_result
        self.allowed_multi_sizes = allowed_multi_sizes
        self.allowed_worker_sizes = allowed_worker_sizes
        self.maximum_number_of_machines = maximum_number_of_machines
        self.vip_mappings = vip_mappings
        self.environment_capacities = environment_capacities
        self.network_access_control_list = network_access_control_list
        self.environment_is_healthy = environment_is_healthy
        self.environment_status = environment_status
        self.resource_group = resource_group
        self.api_management_account_id = api_management_account_id
        self.suspended = suspended
