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


class ExportRequest(Model):
    """Export database parameters.

    :param storage_key_type: The type of the storage key to use. Possible
     values include: 'StorageAccessKey', 'SharedAccessKey'
    :type storage_key_type: str or ~azure.mgmt.sql.models.StorageKeyType
    :param storage_key: The storage key to use.  If storage key type is
     SharedAccessKey, it must be preceded with a "?."
    :type storage_key: str
    :param storage_uri: The storage uri to use.
    :type storage_uri: str
    :param administrator_login: The name of the SQL administrator.
    :type administrator_login: str
    :param administrator_login_password: The password of the SQL
     administrator.
    :type administrator_login_password: str
    :param authentication_type: The authentication type. Possible values
     include: 'SQL', 'ADPassword'. Default value: "SQL" .
    :type authentication_type: str or
     ~azure.mgmt.sql.models.AuthenticationType
    """

    _validation = {
        'storage_key_type': {'required': True},
        'storage_key': {'required': True},
        'storage_uri': {'required': True},
        'administrator_login': {'required': True},
        'administrator_login_password': {'required': True},
    }

    _attribute_map = {
        'storage_key_type': {'key': 'storageKeyType', 'type': 'StorageKeyType'},
        'storage_key': {'key': 'storageKey', 'type': 'str'},
        'storage_uri': {'key': 'storageUri', 'type': 'str'},
        'administrator_login': {'key': 'administratorLogin', 'type': 'str'},
        'administrator_login_password': {'key': 'administratorLoginPassword', 'type': 'str'},
        'authentication_type': {'key': 'authenticationType', 'type': 'AuthenticationType'},
    }

    def __init__(self, storage_key_type, storage_key, storage_uri, administrator_login, administrator_login_password, authentication_type="SQL"):
        self.storage_key_type = storage_key_type
        self.storage_key = storage_key
        self.storage_uri = storage_uri
        self.administrator_login = administrator_login
        self.administrator_login_password = administrator_login_password
        self.authentication_type = authentication_type
