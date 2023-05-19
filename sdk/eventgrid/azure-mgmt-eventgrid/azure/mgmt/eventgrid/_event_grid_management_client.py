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
from ._configuration import EventGridManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    CaCertificatesOperations,
    ChannelsOperations,
    ClientGroupsOperations,
    ClientsOperations,
    DomainEventSubscriptionsOperations,
    DomainTopicEventSubscriptionsOperations,
    DomainTopicsOperations,
    DomainsOperations,
    EventSubscriptionsOperations,
    ExtensionTopicsOperations,
    NamespaceTopicEventSubscriptionsOperations,
    NamespaceTopicsOperations,
    NamespacesOperations,
    Operations,
    PartnerConfigurationsOperations,
    PartnerDestinationsOperations,
    PartnerNamespacesOperations,
    PartnerRegistrationsOperations,
    PartnerTopicEventSubscriptionsOperations,
    PartnerTopicsOperations,
    PermissionBindingsOperations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    SystemTopicEventSubscriptionsOperations,
    SystemTopicsOperations,
    TopicEventSubscriptionsOperations,
    TopicSpacesOperations,
    TopicTypesOperations,
    TopicsOperations,
    VerifiedPartnersOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class EventGridManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Azure EventGrid Management Client.

    :ivar ca_certificates: CaCertificatesOperations operations
    :vartype ca_certificates: azure.mgmt.eventgrid.operations.CaCertificatesOperations
    :ivar channels: ChannelsOperations operations
    :vartype channels: azure.mgmt.eventgrid.operations.ChannelsOperations
    :ivar client_groups: ClientGroupsOperations operations
    :vartype client_groups: azure.mgmt.eventgrid.operations.ClientGroupsOperations
    :ivar clients: ClientsOperations operations
    :vartype clients: azure.mgmt.eventgrid.operations.ClientsOperations
    :ivar domains: DomainsOperations operations
    :vartype domains: azure.mgmt.eventgrid.operations.DomainsOperations
    :ivar domain_topics: DomainTopicsOperations operations
    :vartype domain_topics: azure.mgmt.eventgrid.operations.DomainTopicsOperations
    :ivar domain_topic_event_subscriptions: DomainTopicEventSubscriptionsOperations operations
    :vartype domain_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.DomainTopicEventSubscriptionsOperations
    :ivar topic_event_subscriptions: TopicEventSubscriptionsOperations operations
    :vartype topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.TopicEventSubscriptionsOperations
    :ivar domain_event_subscriptions: DomainEventSubscriptionsOperations operations
    :vartype domain_event_subscriptions:
     azure.mgmt.eventgrid.operations.DomainEventSubscriptionsOperations
    :ivar event_subscriptions: EventSubscriptionsOperations operations
    :vartype event_subscriptions: azure.mgmt.eventgrid.operations.EventSubscriptionsOperations
    :ivar system_topic_event_subscriptions: SystemTopicEventSubscriptionsOperations operations
    :vartype system_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.SystemTopicEventSubscriptionsOperations
    :ivar namespace_topic_event_subscriptions: NamespaceTopicEventSubscriptionsOperations
     operations
    :vartype namespace_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.NamespaceTopicEventSubscriptionsOperations
    :ivar partner_topic_event_subscriptions: PartnerTopicEventSubscriptionsOperations operations
    :vartype partner_topic_event_subscriptions:
     azure.mgmt.eventgrid.operations.PartnerTopicEventSubscriptionsOperations
    :ivar namespaces: NamespacesOperations operations
    :vartype namespaces: azure.mgmt.eventgrid.operations.NamespacesOperations
    :ivar namespace_topics: NamespaceTopicsOperations operations
    :vartype namespace_topics: azure.mgmt.eventgrid.operations.NamespaceTopicsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.eventgrid.operations.Operations
    :ivar partner_configurations: PartnerConfigurationsOperations operations
    :vartype partner_configurations:
     azure.mgmt.eventgrid.operations.PartnerConfigurationsOperations
    :ivar partner_destinations: PartnerDestinationsOperations operations
    :vartype partner_destinations: azure.mgmt.eventgrid.operations.PartnerDestinationsOperations
    :ivar partner_namespaces: PartnerNamespacesOperations operations
    :vartype partner_namespaces: azure.mgmt.eventgrid.operations.PartnerNamespacesOperations
    :ivar partner_registrations: PartnerRegistrationsOperations operations
    :vartype partner_registrations: azure.mgmt.eventgrid.operations.PartnerRegistrationsOperations
    :ivar partner_topics: PartnerTopicsOperations operations
    :vartype partner_topics: azure.mgmt.eventgrid.operations.PartnerTopicsOperations
    :ivar permission_bindings: PermissionBindingsOperations operations
    :vartype permission_bindings: azure.mgmt.eventgrid.operations.PermissionBindingsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.eventgrid.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.eventgrid.operations.PrivateLinkResourcesOperations
    :ivar system_topics: SystemTopicsOperations operations
    :vartype system_topics: azure.mgmt.eventgrid.operations.SystemTopicsOperations
    :ivar topics: TopicsOperations operations
    :vartype topics: azure.mgmt.eventgrid.operations.TopicsOperations
    :ivar extension_topics: ExtensionTopicsOperations operations
    :vartype extension_topics: azure.mgmt.eventgrid.operations.ExtensionTopicsOperations
    :ivar topic_spaces: TopicSpacesOperations operations
    :vartype topic_spaces: azure.mgmt.eventgrid.operations.TopicSpacesOperations
    :ivar topic_types: TopicTypesOperations operations
    :vartype topic_types: azure.mgmt.eventgrid.operations.TopicTypesOperations
    :ivar verified_partners: VerifiedPartnersOperations operations
    :vartype verified_partners: azure.mgmt.eventgrid.operations.VerifiedPartnersOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-06-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
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
        self._config = EventGridManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.ca_certificates = CaCertificatesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.channels = ChannelsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.client_groups = ClientGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.clients = ClientsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domain_topics = DomainTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domain_topic_event_subscriptions = DomainTopicEventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.topic_event_subscriptions = TopicEventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.domain_event_subscriptions = DomainEventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.event_subscriptions = EventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.system_topic_event_subscriptions = SystemTopicEventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.namespace_topic_event_subscriptions = NamespaceTopicEventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partner_topic_event_subscriptions = PartnerTopicEventSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.namespaces = NamespacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.namespace_topics = NamespaceTopicsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.partner_configurations = PartnerConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partner_destinations = PartnerDestinationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partner_namespaces = PartnerNamespacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partner_registrations = PartnerRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.partner_topics = PartnerTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.permission_bindings = PermissionBindingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.system_topics = SystemTopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.topics = TopicsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.extension_topics = ExtensionTopicsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.topic_spaces = TopicSpacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.topic_types = TopicTypesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.verified_partners = VerifiedPartnersOperations(
            self._client, self._config, self._serialize, self._deserialize
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

    def __enter__(self) -> "EventGridManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
