# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import NetworkManagementClientConfiguration
from .operations import (
    ApplicationGatewaysOperations,
    ApplicationSecurityGroupsOperations,
    AvailableDelegationsOperations,
    AvailableEndpointServicesOperations,
    AvailablePrivateEndpointTypesOperations,
    AvailableResourceGroupDelegationsOperations,
    AvailableServiceAliasesOperations,
    AzureFirewallFqdnTagsOperations,
    AzureFirewallsOperations,
    BastionHostsOperations,
    BgpServiceCommunitiesOperations,
    ConnectionMonitorsOperations,
    DdosCustomPoliciesOperations,
    DdosProtectionPlansOperations,
    DefaultSecurityRulesOperations,
    ExpressRouteCircuitAuthorizationsOperations,
    ExpressRouteCircuitConnectionsOperations,
    ExpressRouteCircuitPeeringsOperations,
    ExpressRouteCircuitsOperations,
    ExpressRouteConnectionsOperations,
    ExpressRouteCrossConnectionPeeringsOperations,
    ExpressRouteCrossConnectionsOperations,
    ExpressRouteGatewaysOperations,
    ExpressRouteLinksOperations,
    ExpressRoutePortsLocationsOperations,
    ExpressRoutePortsOperations,
    ExpressRouteServiceProvidersOperations,
    FirewallPoliciesOperations,
    FirewallPolicyRuleGroupsOperations,
    FlowLogsOperations,
    HubVirtualNetworkConnectionsOperations,
    InboundNatRulesOperations,
    IpGroupsOperations,
    LoadBalancerBackendAddressPoolsOperations,
    LoadBalancerFrontendIPConfigurationsOperations,
    LoadBalancerLoadBalancingRulesOperations,
    LoadBalancerNetworkInterfacesOperations,
    LoadBalancerOutboundRulesOperations,
    LoadBalancerProbesOperations,
    LoadBalancersOperations,
    LocalNetworkGatewaysOperations,
    NatGatewaysOperations,
    NetworkInterfaceIPConfigurationsOperations,
    NetworkInterfaceLoadBalancersOperations,
    NetworkInterfaceTapConfigurationsOperations,
    NetworkInterfacesOperations,
    NetworkManagementClientOperationsMixin,
    NetworkProfilesOperations,
    NetworkSecurityGroupsOperations,
    NetworkWatchersOperations,
    Operations,
    P2SVpnGatewaysOperations,
    PacketCapturesOperations,
    PeerExpressRouteCircuitConnectionsOperations,
    PrivateEndpointsOperations,
    PrivateLinkServicesOperations,
    PublicIPAddressesOperations,
    PublicIPPrefixesOperations,
    ResourceNavigationLinksOperations,
    RouteFilterRulesOperations,
    RouteFiltersOperations,
    RouteTablesOperations,
    RoutesOperations,
    SecurityRulesOperations,
    ServiceAssociationLinksOperations,
    ServiceEndpointPoliciesOperations,
    ServiceEndpointPolicyDefinitionsOperations,
    ServiceTagsOperations,
    SubnetsOperations,
    UsagesOperations,
    VirtualHubRouteTableV2SOperations,
    VirtualHubsOperations,
    VirtualNetworkGatewayConnectionsOperations,
    VirtualNetworkGatewaysOperations,
    VirtualNetworkPeeringsOperations,
    VirtualNetworkTapsOperations,
    VirtualNetworksOperations,
    VirtualRouterPeeringsOperations,
    VirtualRoutersOperations,
    VirtualWansOperations,
    VpnConnectionsOperations,
    VpnGatewaysOperations,
    VpnLinkConnectionsOperations,
    VpnServerConfigurationsAssociatedWithVirtualWanOperations,
    VpnServerConfigurationsOperations,
    VpnSiteLinkConnectionsOperations,
    VpnSiteLinksOperations,
    VpnSitesConfigurationOperations,
    VpnSitesOperations,
    WebApplicationFirewallPoliciesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class NetworkManagementClient(
    NetworkManagementClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Network Client.

    :ivar application_gateways: ApplicationGatewaysOperations operations
    :vartype application_gateways:
     azure.mgmt.network.v2019_11_01.operations.ApplicationGatewaysOperations
    :ivar application_security_groups: ApplicationSecurityGroupsOperations operations
    :vartype application_security_groups:
     azure.mgmt.network.v2019_11_01.operations.ApplicationSecurityGroupsOperations
    :ivar available_delegations: AvailableDelegationsOperations operations
    :vartype available_delegations:
     azure.mgmt.network.v2019_11_01.operations.AvailableDelegationsOperations
    :ivar available_resource_group_delegations: AvailableResourceGroupDelegationsOperations
     operations
    :vartype available_resource_group_delegations:
     azure.mgmt.network.v2019_11_01.operations.AvailableResourceGroupDelegationsOperations
    :ivar available_service_aliases: AvailableServiceAliasesOperations operations
    :vartype available_service_aliases:
     azure.mgmt.network.v2019_11_01.operations.AvailableServiceAliasesOperations
    :ivar azure_firewalls: AzureFirewallsOperations operations
    :vartype azure_firewalls: azure.mgmt.network.v2019_11_01.operations.AzureFirewallsOperations
    :ivar azure_firewall_fqdn_tags: AzureFirewallFqdnTagsOperations operations
    :vartype azure_firewall_fqdn_tags:
     azure.mgmt.network.v2019_11_01.operations.AzureFirewallFqdnTagsOperations
    :ivar bastion_hosts: BastionHostsOperations operations
    :vartype bastion_hosts: azure.mgmt.network.v2019_11_01.operations.BastionHostsOperations
    :ivar ddos_custom_policies: DdosCustomPoliciesOperations operations
    :vartype ddos_custom_policies:
     azure.mgmt.network.v2019_11_01.operations.DdosCustomPoliciesOperations
    :ivar ddos_protection_plans: DdosProtectionPlansOperations operations
    :vartype ddos_protection_plans:
     azure.mgmt.network.v2019_11_01.operations.DdosProtectionPlansOperations
    :ivar available_endpoint_services: AvailableEndpointServicesOperations operations
    :vartype available_endpoint_services:
     azure.mgmt.network.v2019_11_01.operations.AvailableEndpointServicesOperations
    :ivar express_route_circuit_authorizations: ExpressRouteCircuitAuthorizationsOperations
     operations
    :vartype express_route_circuit_authorizations:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteCircuitAuthorizationsOperations
    :ivar express_route_circuit_peerings: ExpressRouteCircuitPeeringsOperations operations
    :vartype express_route_circuit_peerings:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteCircuitPeeringsOperations
    :ivar express_route_circuit_connections: ExpressRouteCircuitConnectionsOperations operations
    :vartype express_route_circuit_connections:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteCircuitConnectionsOperations
    :ivar peer_express_route_circuit_connections: PeerExpressRouteCircuitConnectionsOperations
     operations
    :vartype peer_express_route_circuit_connections:
     azure.mgmt.network.v2019_11_01.operations.PeerExpressRouteCircuitConnectionsOperations
    :ivar express_route_circuits: ExpressRouteCircuitsOperations operations
    :vartype express_route_circuits:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteCircuitsOperations
    :ivar express_route_service_providers: ExpressRouteServiceProvidersOperations operations
    :vartype express_route_service_providers:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteServiceProvidersOperations
    :ivar express_route_cross_connections: ExpressRouteCrossConnectionsOperations operations
    :vartype express_route_cross_connections:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteCrossConnectionsOperations
    :ivar express_route_cross_connection_peerings: ExpressRouteCrossConnectionPeeringsOperations
     operations
    :vartype express_route_cross_connection_peerings:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteCrossConnectionPeeringsOperations
    :ivar express_route_gateways: ExpressRouteGatewaysOperations operations
    :vartype express_route_gateways:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteGatewaysOperations
    :ivar express_route_connections: ExpressRouteConnectionsOperations operations
    :vartype express_route_connections:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteConnectionsOperations
    :ivar express_route_ports_locations: ExpressRoutePortsLocationsOperations operations
    :vartype express_route_ports_locations:
     azure.mgmt.network.v2019_11_01.operations.ExpressRoutePortsLocationsOperations
    :ivar express_route_ports: ExpressRoutePortsOperations operations
    :vartype express_route_ports:
     azure.mgmt.network.v2019_11_01.operations.ExpressRoutePortsOperations
    :ivar express_route_links: ExpressRouteLinksOperations operations
    :vartype express_route_links:
     azure.mgmt.network.v2019_11_01.operations.ExpressRouteLinksOperations
    :ivar firewall_policies: FirewallPoliciesOperations operations
    :vartype firewall_policies:
     azure.mgmt.network.v2019_11_01.operations.FirewallPoliciesOperations
    :ivar firewall_policy_rule_groups: FirewallPolicyRuleGroupsOperations operations
    :vartype firewall_policy_rule_groups:
     azure.mgmt.network.v2019_11_01.operations.FirewallPolicyRuleGroupsOperations
    :ivar ip_groups: IpGroupsOperations operations
    :vartype ip_groups: azure.mgmt.network.v2019_11_01.operations.IpGroupsOperations
    :ivar load_balancers: LoadBalancersOperations operations
    :vartype load_balancers: azure.mgmt.network.v2019_11_01.operations.LoadBalancersOperations
    :ivar load_balancer_backend_address_pools: LoadBalancerBackendAddressPoolsOperations operations
    :vartype load_balancer_backend_address_pools:
     azure.mgmt.network.v2019_11_01.operations.LoadBalancerBackendAddressPoolsOperations
    :ivar load_balancer_frontend_ip_configurations: LoadBalancerFrontendIPConfigurationsOperations
     operations
    :vartype load_balancer_frontend_ip_configurations:
     azure.mgmt.network.v2019_11_01.operations.LoadBalancerFrontendIPConfigurationsOperations
    :ivar inbound_nat_rules: InboundNatRulesOperations operations
    :vartype inbound_nat_rules: azure.mgmt.network.v2019_11_01.operations.InboundNatRulesOperations
    :ivar load_balancer_load_balancing_rules: LoadBalancerLoadBalancingRulesOperations operations
    :vartype load_balancer_load_balancing_rules:
     azure.mgmt.network.v2019_11_01.operations.LoadBalancerLoadBalancingRulesOperations
    :ivar load_balancer_outbound_rules: LoadBalancerOutboundRulesOperations operations
    :vartype load_balancer_outbound_rules:
     azure.mgmt.network.v2019_11_01.operations.LoadBalancerOutboundRulesOperations
    :ivar load_balancer_network_interfaces: LoadBalancerNetworkInterfacesOperations operations
    :vartype load_balancer_network_interfaces:
     azure.mgmt.network.v2019_11_01.operations.LoadBalancerNetworkInterfacesOperations
    :ivar load_balancer_probes: LoadBalancerProbesOperations operations
    :vartype load_balancer_probes:
     azure.mgmt.network.v2019_11_01.operations.LoadBalancerProbesOperations
    :ivar nat_gateways: NatGatewaysOperations operations
    :vartype nat_gateways: azure.mgmt.network.v2019_11_01.operations.NatGatewaysOperations
    :ivar network_interfaces: NetworkInterfacesOperations operations
    :vartype network_interfaces:
     azure.mgmt.network.v2019_11_01.operations.NetworkInterfacesOperations
    :ivar network_interface_ip_configurations: NetworkInterfaceIPConfigurationsOperations
     operations
    :vartype network_interface_ip_configurations:
     azure.mgmt.network.v2019_11_01.operations.NetworkInterfaceIPConfigurationsOperations
    :ivar network_interface_load_balancers: NetworkInterfaceLoadBalancersOperations operations
    :vartype network_interface_load_balancers:
     azure.mgmt.network.v2019_11_01.operations.NetworkInterfaceLoadBalancersOperations
    :ivar network_interface_tap_configurations: NetworkInterfaceTapConfigurationsOperations
     operations
    :vartype network_interface_tap_configurations:
     azure.mgmt.network.v2019_11_01.operations.NetworkInterfaceTapConfigurationsOperations
    :ivar network_profiles: NetworkProfilesOperations operations
    :vartype network_profiles: azure.mgmt.network.v2019_11_01.operations.NetworkProfilesOperations
    :ivar network_security_groups: NetworkSecurityGroupsOperations operations
    :vartype network_security_groups:
     azure.mgmt.network.v2019_11_01.operations.NetworkSecurityGroupsOperations
    :ivar security_rules: SecurityRulesOperations operations
    :vartype security_rules: azure.mgmt.network.v2019_11_01.operations.SecurityRulesOperations
    :ivar default_security_rules: DefaultSecurityRulesOperations operations
    :vartype default_security_rules:
     azure.mgmt.network.v2019_11_01.operations.DefaultSecurityRulesOperations
    :ivar network_watchers: NetworkWatchersOperations operations
    :vartype network_watchers: azure.mgmt.network.v2019_11_01.operations.NetworkWatchersOperations
    :ivar packet_captures: PacketCapturesOperations operations
    :vartype packet_captures: azure.mgmt.network.v2019_11_01.operations.PacketCapturesOperations
    :ivar connection_monitors: ConnectionMonitorsOperations operations
    :vartype connection_monitors:
     azure.mgmt.network.v2019_11_01.operations.ConnectionMonitorsOperations
    :ivar flow_logs: FlowLogsOperations operations
    :vartype flow_logs: azure.mgmt.network.v2019_11_01.operations.FlowLogsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.network.v2019_11_01.operations.Operations
    :ivar private_endpoints: PrivateEndpointsOperations operations
    :vartype private_endpoints:
     azure.mgmt.network.v2019_11_01.operations.PrivateEndpointsOperations
    :ivar available_private_endpoint_types: AvailablePrivateEndpointTypesOperations operations
    :vartype available_private_endpoint_types:
     azure.mgmt.network.v2019_11_01.operations.AvailablePrivateEndpointTypesOperations
    :ivar private_link_services: PrivateLinkServicesOperations operations
    :vartype private_link_services:
     azure.mgmt.network.v2019_11_01.operations.PrivateLinkServicesOperations
    :ivar public_ip_addresses: PublicIPAddressesOperations operations
    :vartype public_ip_addresses:
     azure.mgmt.network.v2019_11_01.operations.PublicIPAddressesOperations
    :ivar public_ip_prefixes: PublicIPPrefixesOperations operations
    :vartype public_ip_prefixes:
     azure.mgmt.network.v2019_11_01.operations.PublicIPPrefixesOperations
    :ivar route_filters: RouteFiltersOperations operations
    :vartype route_filters: azure.mgmt.network.v2019_11_01.operations.RouteFiltersOperations
    :ivar route_filter_rules: RouteFilterRulesOperations operations
    :vartype route_filter_rules:
     azure.mgmt.network.v2019_11_01.operations.RouteFilterRulesOperations
    :ivar route_tables: RouteTablesOperations operations
    :vartype route_tables: azure.mgmt.network.v2019_11_01.operations.RouteTablesOperations
    :ivar routes: RoutesOperations operations
    :vartype routes: azure.mgmt.network.v2019_11_01.operations.RoutesOperations
    :ivar bgp_service_communities: BgpServiceCommunitiesOperations operations
    :vartype bgp_service_communities:
     azure.mgmt.network.v2019_11_01.operations.BgpServiceCommunitiesOperations
    :ivar service_endpoint_policies: ServiceEndpointPoliciesOperations operations
    :vartype service_endpoint_policies:
     azure.mgmt.network.v2019_11_01.operations.ServiceEndpointPoliciesOperations
    :ivar service_endpoint_policy_definitions: ServiceEndpointPolicyDefinitionsOperations
     operations
    :vartype service_endpoint_policy_definitions:
     azure.mgmt.network.v2019_11_01.operations.ServiceEndpointPolicyDefinitionsOperations
    :ivar service_tags: ServiceTagsOperations operations
    :vartype service_tags: azure.mgmt.network.v2019_11_01.operations.ServiceTagsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.network.v2019_11_01.operations.UsagesOperations
    :ivar virtual_networks: VirtualNetworksOperations operations
    :vartype virtual_networks: azure.mgmt.network.v2019_11_01.operations.VirtualNetworksOperations
    :ivar subnets: SubnetsOperations operations
    :vartype subnets: azure.mgmt.network.v2019_11_01.operations.SubnetsOperations
    :ivar resource_navigation_links: ResourceNavigationLinksOperations operations
    :vartype resource_navigation_links:
     azure.mgmt.network.v2019_11_01.operations.ResourceNavigationLinksOperations
    :ivar service_association_links: ServiceAssociationLinksOperations operations
    :vartype service_association_links:
     azure.mgmt.network.v2019_11_01.operations.ServiceAssociationLinksOperations
    :ivar virtual_network_peerings: VirtualNetworkPeeringsOperations operations
    :vartype virtual_network_peerings:
     azure.mgmt.network.v2019_11_01.operations.VirtualNetworkPeeringsOperations
    :ivar virtual_network_gateways: VirtualNetworkGatewaysOperations operations
    :vartype virtual_network_gateways:
     azure.mgmt.network.v2019_11_01.operations.VirtualNetworkGatewaysOperations
    :ivar virtual_network_gateway_connections: VirtualNetworkGatewayConnectionsOperations
     operations
    :vartype virtual_network_gateway_connections:
     azure.mgmt.network.v2019_11_01.operations.VirtualNetworkGatewayConnectionsOperations
    :ivar local_network_gateways: LocalNetworkGatewaysOperations operations
    :vartype local_network_gateways:
     azure.mgmt.network.v2019_11_01.operations.LocalNetworkGatewaysOperations
    :ivar virtual_network_taps: VirtualNetworkTapsOperations operations
    :vartype virtual_network_taps:
     azure.mgmt.network.v2019_11_01.operations.VirtualNetworkTapsOperations
    :ivar virtual_routers: VirtualRoutersOperations operations
    :vartype virtual_routers: azure.mgmt.network.v2019_11_01.operations.VirtualRoutersOperations
    :ivar virtual_router_peerings: VirtualRouterPeeringsOperations operations
    :vartype virtual_router_peerings:
     azure.mgmt.network.v2019_11_01.operations.VirtualRouterPeeringsOperations
    :ivar virtual_wans: VirtualWansOperations operations
    :vartype virtual_wans: azure.mgmt.network.v2019_11_01.operations.VirtualWansOperations
    :ivar vpn_sites: VpnSitesOperations operations
    :vartype vpn_sites: azure.mgmt.network.v2019_11_01.operations.VpnSitesOperations
    :ivar vpn_site_links: VpnSiteLinksOperations operations
    :vartype vpn_site_links: azure.mgmt.network.v2019_11_01.operations.VpnSiteLinksOperations
    :ivar vpn_sites_configuration: VpnSitesConfigurationOperations operations
    :vartype vpn_sites_configuration:
     azure.mgmt.network.v2019_11_01.operations.VpnSitesConfigurationOperations
    :ivar vpn_server_configurations: VpnServerConfigurationsOperations operations
    :vartype vpn_server_configurations:
     azure.mgmt.network.v2019_11_01.operations.VpnServerConfigurationsOperations
    :ivar virtual_hubs: VirtualHubsOperations operations
    :vartype virtual_hubs: azure.mgmt.network.v2019_11_01.operations.VirtualHubsOperations
    :ivar hub_virtual_network_connections: HubVirtualNetworkConnectionsOperations operations
    :vartype hub_virtual_network_connections:
     azure.mgmt.network.v2019_11_01.operations.HubVirtualNetworkConnectionsOperations
    :ivar vpn_gateways: VpnGatewaysOperations operations
    :vartype vpn_gateways: azure.mgmt.network.v2019_11_01.operations.VpnGatewaysOperations
    :ivar vpn_connections: VpnConnectionsOperations operations
    :vartype vpn_connections: azure.mgmt.network.v2019_11_01.operations.VpnConnectionsOperations
    :ivar vpn_site_link_connections: VpnSiteLinkConnectionsOperations operations
    :vartype vpn_site_link_connections:
     azure.mgmt.network.v2019_11_01.operations.VpnSiteLinkConnectionsOperations
    :ivar vpn_link_connections: VpnLinkConnectionsOperations operations
    :vartype vpn_link_connections:
     azure.mgmt.network.v2019_11_01.operations.VpnLinkConnectionsOperations
    :ivar p2_svpn_gateways: P2SVpnGatewaysOperations operations
    :vartype p2_svpn_gateways: azure.mgmt.network.v2019_11_01.operations.P2SVpnGatewaysOperations
    :ivar vpn_server_configurations_associated_with_virtual_wan:
     VpnServerConfigurationsAssociatedWithVirtualWanOperations operations
    :vartype vpn_server_configurations_associated_with_virtual_wan:
     azure.mgmt.network.v2019_11_01.operations.VpnServerConfigurationsAssociatedWithVirtualWanOperations
    :ivar virtual_hub_route_table_v2_s: VirtualHubRouteTableV2SOperations operations
    :vartype virtual_hub_route_table_v2_s:
     azure.mgmt.network.v2019_11_01.operations.VirtualHubRouteTableV2SOperations
    :ivar web_application_firewall_policies: WebApplicationFirewallPoliciesOperations operations
    :vartype web_application_firewall_policies:
     azure.mgmt.network.v2019_11_01.operations.WebApplicationFirewallPoliciesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft
     Azure subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = NetworkManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.application_gateways = ApplicationGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.application_security_groups = ApplicationSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.available_delegations = AvailableDelegationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.available_resource_group_delegations = AvailableResourceGroupDelegationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.available_service_aliases = AvailableServiceAliasesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.azure_firewalls = AzureFirewallsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.azure_firewall_fqdn_tags = AzureFirewallFqdnTagsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.bastion_hosts = BastionHostsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.ddos_custom_policies = DdosCustomPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.ddos_protection_plans = DdosProtectionPlansOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.available_endpoint_services = AvailableEndpointServicesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_circuit_authorizations = ExpressRouteCircuitAuthorizationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_circuit_peerings = ExpressRouteCircuitPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_circuit_connections = ExpressRouteCircuitConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.peer_express_route_circuit_connections = PeerExpressRouteCircuitConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_circuits = ExpressRouteCircuitsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_service_providers = ExpressRouteServiceProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_cross_connections = ExpressRouteCrossConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_cross_connection_peerings = ExpressRouteCrossConnectionPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_gateways = ExpressRouteGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_connections = ExpressRouteConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_ports_locations = ExpressRoutePortsLocationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_ports = ExpressRoutePortsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.express_route_links = ExpressRouteLinksOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.firewall_policies = FirewallPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.firewall_policy_rule_groups = FirewallPolicyRuleGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.ip_groups = IpGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancers = LoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancer_backend_address_pools = LoadBalancerBackendAddressPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancer_frontend_ip_configurations = LoadBalancerFrontendIPConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.inbound_nat_rules = InboundNatRulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancer_load_balancing_rules = LoadBalancerLoadBalancingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancer_outbound_rules = LoadBalancerOutboundRulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancer_network_interfaces = LoadBalancerNetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.load_balancer_probes = LoadBalancerProbesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.nat_gateways = NatGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_interface_ip_configurations = NetworkInterfaceIPConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_interface_load_balancers = NetworkInterfaceLoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_interface_tap_configurations = NetworkInterfaceTapConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_profiles = NetworkProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_security_groups = NetworkSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.security_rules = SecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.default_security_rules = DefaultSecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.network_watchers = NetworkWatchersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.packet_captures = PacketCapturesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.connection_monitors = ConnectionMonitorsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.flow_logs = FlowLogsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2019-11-01")
        self.private_endpoints = PrivateEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.available_private_endpoint_types = AvailablePrivateEndpointTypesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.private_link_services = PrivateLinkServicesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.public_ip_addresses = PublicIPAddressesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.public_ip_prefixes = PublicIPPrefixesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.route_filters = RouteFiltersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.route_filter_rules = RouteFilterRulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.route_tables = RouteTablesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.routes = RoutesOperations(self._client, self._config, self._serialize, self._deserialize, "2019-11-01")
        self.bgp_service_communities = BgpServiceCommunitiesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.service_endpoint_policies = ServiceEndpointPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.service_endpoint_policy_definitions = ServiceEndpointPolicyDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.service_tags = ServiceTagsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize, "2019-11-01")
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.subnets = SubnetsOperations(self._client, self._config, self._serialize, self._deserialize, "2019-11-01")
        self.resource_navigation_links = ResourceNavigationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.service_association_links = ServiceAssociationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_network_peerings = VirtualNetworkPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_network_gateways = VirtualNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_network_gateway_connections = VirtualNetworkGatewayConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.local_network_gateways = LocalNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_network_taps = VirtualNetworkTapsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_routers = VirtualRoutersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_router_peerings = VirtualRouterPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_wans = VirtualWansOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_sites = VpnSitesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_site_links = VpnSiteLinksOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_sites_configuration = VpnSitesConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_server_configurations = VpnServerConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.virtual_hubs = VirtualHubsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.hub_virtual_network_connections = HubVirtualNetworkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_gateways = VpnGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_connections = VpnConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_site_link_connections = VpnSiteLinkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_link_connections = VpnLinkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.p2_svpn_gateways = P2SVpnGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.vpn_server_configurations_associated_with_virtual_wan = (
            VpnServerConfigurationsAssociatedWithVirtualWanOperations(
                self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
            )
        )
        self.virtual_hub_route_table_v2_s = VirtualHubRouteTableV2SOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )
        self.web_application_firewall_policies = WebApplicationFirewallPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-11-01"
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "NetworkManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
