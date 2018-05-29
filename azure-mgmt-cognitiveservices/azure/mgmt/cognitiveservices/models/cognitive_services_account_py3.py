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


class CognitiveServicesAccount(Model):
    """Cognitive Services Account is an Azure resource representing the
    provisioned account, its type, location and SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param etag: Entity Tag
    :type etag: str
    :ivar id: The id of the created account
    :vartype id: str
    :param kind: Type of cognitive service account.
    :type kind: str
    :param location: The location of the resource
    :type location: str
    :ivar name: The name of the created account
    :vartype name: str
    :ivar provisioning_state: Gets the status of the cognitive services
     account at the time the operation was called. Possible values include:
     'Creating', 'ResolvingDNS', 'Moving', 'Deleting', 'Succeeded', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.cognitiveservices.models.ProvisioningState
    :param endpoint: Endpoint of the created account.
    :type endpoint: str
    :param internal_id: The internal identifier.
    :type internal_id: str
    :param sku: The SKU of Cognitive Services account.
    :type sku: ~azure.mgmt.cognitiveservices.models.Sku
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater than 128 characters and
     value no greater than 256 characters.
    :type tags: dict[str, str]
    :ivar type: Resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'internal_id': {'key': 'properties.internalId', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, etag: str=None, kind: str=None, location: str=None, endpoint: str=None, internal_id: str=None, sku=None, tags=None, **kwargs) -> None:
        super(CognitiveServicesAccount, self).__init__(**kwargs)
        self.etag = etag
        self.id = None
        self.kind = kind
        self.location = location
        self.name = None
        self.provisioning_state = None
        self.endpoint = endpoint
        self.internal_id = internal_id
        self.sku = sku
        self.tags = tags
        self.type = None
