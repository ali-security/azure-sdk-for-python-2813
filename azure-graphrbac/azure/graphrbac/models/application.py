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


class Application(Model):
    """Active Directory application information.

    :param object_id: The object ID.
    :type object_id: str
    :param object_type: The object type.
    :type object_type: str
    :param app_id: The application ID.
    :type app_id: str
    :param app_permissions: The application permissions.
    :type app_permissions: list[str]
    :param available_to_other_tenants: Whether the application is be available
     to other tenants.
    :type available_to_other_tenants: bool
    :param display_name: The display name of the application.
    :type display_name: str
    :param identifier_uris: A collection of URIs for the application.
    :type identifier_uris: list[str]
    :param reply_urls: A collection of reply URLs for the application.
    :type reply_urls: list[str]
    :param homepage: The home page of the application.
    :type homepage: str
    :param oauth2_allow_implicit_flow: Whether to allow implicit grant flow
     for OAuth2
    :type oauth2_allow_implicit_flow: bool
    """

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'app_id': {'key': 'appId', 'type': 'str'},
        'app_permissions': {'key': 'appPermissions', 'type': '[str]'},
        'available_to_other_tenants': {'key': 'availableToOtherTenants', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'identifier_uris': {'key': 'identifierUris', 'type': '[str]'},
        'reply_urls': {'key': 'replyUrls', 'type': '[str]'},
        'homepage': {'key': 'homepage', 'type': 'str'},
        'oauth2_allow_implicit_flow': {'key': 'oauth2AllowImplicitFlow', 'type': 'bool'},
    }

    def __init__(self, object_id=None, object_type=None, app_id=None, app_permissions=None, available_to_other_tenants=None, display_name=None, identifier_uris=None, reply_urls=None, homepage=None, oauth2_allow_implicit_flow=None):
        self.object_id = object_id
        self.object_type = object_type
        self.app_id = app_id
        self.app_permissions = app_permissions
        self.available_to_other_tenants = available_to_other_tenants
        self.display_name = display_name
        self.identifier_uris = identifier_uris
        self.reply_urls = reply_urls
        self.homepage = homepage
        self.oauth2_allow_implicit_flow = oauth2_allow_implicit_flow
