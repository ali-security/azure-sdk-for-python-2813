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


class VirtualNetworkGateway(Resource):
    """
    A common class for general resource information

    :param id: Resource Id
    :type id: str
    :param name: Resource name
    :type name: str
    :param type: Resource type
    :type type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param ip_configurations: IpConfigurations for Virtual network gateway.
    :type ip_configurations: list of
     :class:`VirtualNetworkGatewayIPConfiguration
     <networkmanagementclient.models.VirtualNetworkGatewayIPConfiguration>`
    :param gateway_type: The type of this virtual network gateway. Possible
     values include: 'Vpn', 'ExpressRoute'
    :type gateway_type: str
    :param vpn_type: The type of this virtual network gateway. Possible
     values include: 'PolicyBased', 'RouteBased'
    :type vpn_type: str
    :param enable_bgp: EnableBgp Flag
    :type enable_bgp: bool
    :param gateway_default_site: Gets or sets the reference of the
     LocalNetworkGateway resource which represents Local network site having
     default routes. Assign Null value in case of removing existing default
     site setting.
    :type gateway_default_site: :class:`SubResource
     <networkmanagementclient.models.SubResource>`
    :param sku: Gets or sets the reference of the VirtualNetworkGatewaySku
     resource which represents the sku selected for Virtual network gateway.
    :type sku: :class:`VirtualNetworkGatewaySku
     <networkmanagementclient.models.VirtualNetworkGatewaySku>`
    :param vpn_client_configuration: Gets or sets the reference of the
     VpnClientConfiguration resource which represents the P2S VpnClient
     configurations.
    :type vpn_client_configuration: :class:`VpnClientConfiguration
     <networkmanagementclient.models.VpnClientConfiguration>`
    :param bgp_settings: Virtual network gateway's BGP speaker settings
    :type bgp_settings: :class:`BgpSettings
     <networkmanagementclient.models.BgpSettings>`
    :param resource_guid: Gets or sets resource guid property of the
     VirtualNetworkGateway resource
    :type resource_guid: str
    :param provisioning_state: Gets or sets Provisioning state of the
     VirtualNetworkGateway resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'ip_configurations': {'key': 'properties.ipConfigurations', 'type': '[VirtualNetworkGatewayIPConfiguration]'},
        'gateway_type': {'key': 'properties.gatewayType', 'type': 'VirtualNetworkGatewayType'},
        'vpn_type': {'key': 'properties.vpnType', 'type': 'VpnType'},
        'enable_bgp': {'key': 'properties.enableBgp', 'type': 'bool'},
        'gateway_default_site': {'key': 'properties.gatewayDefaultSite', 'type': 'SubResource'},
        'sku': {'key': 'properties.sku', 'type': 'VirtualNetworkGatewaySku'},
        'vpn_client_configuration': {'key': 'properties.vpnClientConfiguration', 'type': 'VpnClientConfiguration'},
        'bgp_settings': {'key': 'properties.bgpSettings', 'type': 'BgpSettings'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None, ip_configurations=None, gateway_type=None, vpn_type=None, enable_bgp=None, gateway_default_site=None, sku=None, vpn_client_configuration=None, bgp_settings=None, resource_guid=None, provisioning_state=None, etag=None):
        super(VirtualNetworkGateway, self).__init__(id=id, name=name, type=type, location=location, tags=tags)
        self.ip_configurations = ip_configurations
        self.gateway_type = gateway_type
        self.vpn_type = vpn_type
        self.enable_bgp = enable_bgp
        self.gateway_default_site = gateway_default_site
        self.sku = sku
        self.vpn_client_configuration = vpn_client_configuration
        self.bgp_settings = bgp_settings
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
