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


class ContainerRegistryCredentials(Model):
    """Information about the Azure Container Registry which contains the images
    deployed to the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar login_server: The ACR login server name. User name is the first part
     of the FQDN.
    :vartype login_server: str
    :ivar password: The ACR primary password.
    :vartype password: str
    :ivar password2: The ACR secondary password.
    :vartype password2: str
    :ivar username: The ACR login username.
    :vartype username: str
    """

    _validation = {
        'login_server': {'readonly': True},
        'password': {'readonly': True},
        'password2': {'readonly': True},
        'username': {'readonly': True},
    }

    _attribute_map = {
        'login_server': {'key': 'loginServer', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'password2': {'key': 'password2', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
    }

    def __init__(self):
        self.login_server = None
        self.password = None
        self.password2 = None
        self.username = None
