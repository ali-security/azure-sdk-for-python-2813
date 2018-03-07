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

from .resource import Resource


class ExpressRouteCircuit(Resource):
    """ExpressRouteCircuit resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: The SKU.
    :type sku: ~azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitSku
    :param allow_classic_operations: Allow classic operations
    :type allow_classic_operations: bool
    :param circuit_provisioning_state: The CircuitProvisioningState state of
     the resource.
    :type circuit_provisioning_state: str
    :param service_provider_provisioning_state: The
     ServiceProviderProvisioningState state of the resource. Possible values
     are 'NotProvisioned', 'Provisioning', 'Provisioned', and 'Deprovisioning'.
     Possible values include: 'NotProvisioned', 'Provisioning', 'Provisioned',
     'Deprovisioning'
    :type service_provider_provisioning_state: str or
     ~azure.mgmt.network.v2017_06_01.models.ServiceProviderProvisioningState
    :param authorizations: The list of authorizations.
    :type authorizations:
     list[~azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitAuthorization]
    :param peerings: The list of peerings.
    :type peerings:
     list[~azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitPeering]
    :param service_key: The ServiceKey.
    :type service_key: str
    :param service_provider_notes: The ServiceProviderNotes.
    :type service_provider_notes: str
    :param service_provider_properties: The ServiceProviderProperties.
    :type service_provider_properties:
     ~azure.mgmt.network.v2017_06_01.models.ExpressRouteCircuitServiceProviderProperties
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param gateway_manager_etag: The GatewayManager Etag.
    :type gateway_manager_etag: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ExpressRouteCircuitSku'},
        'allow_classic_operations': {'key': 'properties.allowClassicOperations', 'type': 'bool'},
        'circuit_provisioning_state': {'key': 'properties.circuitProvisioningState', 'type': 'str'},
        'service_provider_provisioning_state': {'key': 'properties.serviceProviderProvisioningState', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[ExpressRouteCircuitAuthorization]'},
        'peerings': {'key': 'properties.peerings', 'type': '[ExpressRouteCircuitPeering]'},
        'service_key': {'key': 'properties.serviceKey', 'type': 'str'},
        'service_provider_notes': {'key': 'properties.serviceProviderNotes', 'type': 'str'},
        'service_provider_properties': {'key': 'properties.serviceProviderProperties', 'type': 'ExpressRouteCircuitServiceProviderProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'gateway_manager_etag': {'key': 'properties.gatewayManagerEtag', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, sku=None, allow_classic_operations: bool=None, circuit_provisioning_state: str=None, service_provider_provisioning_state=None, authorizations=None, peerings=None, service_key: str=None, service_provider_notes: str=None, service_provider_properties=None, provisioning_state: str=None, gateway_manager_etag: str=None, **kwargs) -> None:
        super(ExpressRouteCircuit, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.sku = sku
        self.allow_classic_operations = allow_classic_operations
        self.circuit_provisioning_state = circuit_provisioning_state
        self.service_provider_provisioning_state = service_provider_provisioning_state
        self.authorizations = authorizations
        self.peerings = peerings
        self.service_key = service_key
        self.service_provider_notes = service_provider_notes
        self.service_provider_properties = service_provider_properties
        self.provisioning_state = provisioning_state
        self.gateway_manager_etag = gateway_manager_etag
        self.etag = None
