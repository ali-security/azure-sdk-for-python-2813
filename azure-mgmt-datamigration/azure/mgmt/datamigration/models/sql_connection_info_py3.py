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

from .connection_info_py3 import ConnectionInfo


class SqlConnectionInfo(ConnectionInfo):
    """Information for connecting to SQL database server.

    All required parameters must be populated in order to send to Azure.

    :param user_name: User name
    :type user_name: str
    :param password: Password credential.
    :type password: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param data_source: Required. Data source in the format
     Protocol:MachineName\\SQLServerInstanceName,PortNumber
    :type data_source: str
    :param authentication: Authentication type to use for connection. Possible
     values include: 'None', 'WindowsAuthentication', 'SqlAuthentication',
     'ActiveDirectoryIntegrated', 'ActiveDirectoryPassword'
    :type authentication: str or
     ~azure.mgmt.datamigration.models.AuthenticationType
    :param encrypt_connection: Whether to encrypt the connection. Default
     value: True .
    :type encrypt_connection: bool
    :param additional_settings: Additional connection settings
    :type additional_settings: str
    :param trust_server_certificate: Whether to trust the server certificate.
     Default value: False .
    :type trust_server_certificate: bool
    """

    _validation = {
        'type': {'required': True},
        'data_source': {'required': True},
    }

    _attribute_map = {
        'user_name': {'key': 'userName', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'data_source': {'key': 'dataSource', 'type': 'str'},
        'authentication': {'key': 'authentication', 'type': 'str'},
        'encrypt_connection': {'key': 'encryptConnection', 'type': 'bool'},
        'additional_settings': {'key': 'additionalSettings', 'type': 'str'},
        'trust_server_certificate': {'key': 'trustServerCertificate', 'type': 'bool'},
    }

    def __init__(self, *, data_source: str, user_name: str=None, password: str=None, authentication=None, encrypt_connection: bool=True, additional_settings: str=None, trust_server_certificate: bool=False, **kwargs) -> None:
        super(SqlConnectionInfo, self).__init__(user_name=user_name, password=password, **kwargs)
        self.data_source = data_source
        self.authentication = authentication
        self.encrypt_connection = encrypt_connection
        self.additional_settings = additional_settings
        self.trust_server_certificate = trust_server_certificate
        self.type = 'SqlConnectionInfo'
