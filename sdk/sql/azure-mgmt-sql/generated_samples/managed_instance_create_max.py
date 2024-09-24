# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.sql import SqlManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-sql
# USAGE
    python managed_instance_create_max.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="20D7082A-0FC7-4468-82BD-542694D5042B",
    )

    response = client.managed_instances.begin_create_or_update(
        resource_group_name="testrg",
        managed_instance_name="testinstance",
        parameters={
            "location": "Japan East",
            "properties": {
                "administratorLogin": "dummylogin",
                "administratorLoginPassword": "PLACEHOLDER",
                "administrators": {
                    "azureADOnlyAuthentication": True,
                    "login": "bob@contoso.com",
                    "principalType": "User",
                    "sid": "00000011-1111-2222-2222-123456789111",
                    "tenantId": "00000011-1111-2222-2222-123456789111",
                },
                "collation": "SQL_Latin1_General_CP1_CI_AS",
                "databaseFormat": "AlwaysUpToDate",
                "dnsZonePartner": "/subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Sql/managedInstances/testinstance",
                "hybridSecondaryUsage": "Passive",
                "instancePoolId": "/subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Sql/instancePools/pool1",
                "licenseType": "LicenseIncluded",
                "maintenanceConfigurationId": "/subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/providers/Microsoft.Maintenance/publicMaintenanceConfigurations/SQL_JapanEast_MI_1",
                "minimalTlsVersion": "1.2",
                "proxyOverride": "Redirect",
                "publicDataEndpointEnabled": False,
                "requestedBackupStorageRedundancy": "Geo",
                "servicePrincipal": {"type": "SystemAssigned"},
                "storageSizeInGB": 1024,
                "subnetId": "/subscriptions/20D7082A-0FC7-4468-82BD-542694D5042B/resourceGroups/testrg/providers/Microsoft.Network/virtualNetworks/vnet1/subnets/subnet1",
                "timezoneId": "UTC",
                "vCores": 8,
            },
            "sku": {"name": "GP_Gen5", "tier": "GeneralPurpose"},
            "tags": {"tagKey1": "TagValue1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2023-05-01-preview/examples/ManagedInstanceCreateMax.json
if __name__ == "__main__":
    main()
