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

from .linked_service import LinkedService


class SybaseLinkedService(LinkedService):
    """Linked service for Sybase data source.

    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param server: Server name for connection. Type: string (or Expression
     with resultType string).
    :type server: object
    :param database: Database name for connection. Type: string (or Expression
     with resultType string).
    :type database: object
    :param schema: Schema name for connection. Type: string (or Expression
     with resultType string).
    :type schema: object
    :param authentication_type: AuthenticationType to be used for connection.
     Possible values include: 'Basic', 'Windows'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.SybaseAuthenticationType
    :param username: Username for authentication. Type: string (or Expression
     with resultType string).
    :type username: object
    :param password: Password for authentication.
    :type password: ~azure.mgmt.datafactory.models.SecureString
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'server': {'required': True},
        'database': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server': {'key': 'typeProperties.server', 'type': 'object'},
        'database': {'key': 'typeProperties.database', 'type': 'object'},
        'schema': {'key': 'typeProperties.schema', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecureString'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, server, database, connect_via=None, description=None, schema=None, authentication_type=None, username=None, password=None, encrypted_credential=None):
        super(SybaseLinkedService, self).__init__(connect_via=connect_via, description=description)
        self.server = server
        self.database = database
        self.schema = schema
        self.authentication_type = authentication_type
        self.username = username
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'Sybase'
