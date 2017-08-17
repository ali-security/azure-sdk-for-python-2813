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


class EventSubscriptionUpdateParameters(Model):
    """Properties of the Event Subscription update.

    :param destination: Information about the destination where events have to
     be delivered for the event subscription.
    :type destination: :class:`EventSubscriptionDestination
     <azure.mgmt.eventgrid.models.EventSubscriptionDestination>`
    :param filter: Information about the filter for the event subscription.
    :type filter: :class:`EventSubscriptionFilter
     <azure.mgmt.eventgrid.models.EventSubscriptionFilter>`
    :param labels: List of user defined labels.
    :type labels: list of str
    """

    _attribute_map = {
        'destination': {'key': 'destination', 'type': 'EventSubscriptionDestination'},
        'filter': {'key': 'filter', 'type': 'EventSubscriptionFilter'},
        'labels': {'key': 'labels', 'type': '[str]'},
    }

    def __init__(self, destination=None, filter=None, labels=None):
        self.destination = destination
        self.filter = filter
        self.labels = labels
