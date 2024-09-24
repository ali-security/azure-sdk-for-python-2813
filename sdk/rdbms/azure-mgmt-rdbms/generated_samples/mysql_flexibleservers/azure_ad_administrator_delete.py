# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-rdbms
# USAGE
    python azure_ad_administrator_delete.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MySQLManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="ffffffff-ffff-ffff-ffff-ffffffffffff",
    )

    client.azure_ad_administrators.begin_delete(
        resource_group_name="testrg",
        server_name="mysqltestsvc4",
        administrator_name="ActiveDirectory",
    ).result()


# x-ms-original-file: specification/mysql/resource-manager/Microsoft.DBforMySQL/AAD/stable/2023-12-30/examples/AzureADAdministratorDelete.json
if __name__ == "__main__":
    main()
