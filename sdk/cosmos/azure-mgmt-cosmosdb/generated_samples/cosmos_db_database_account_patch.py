# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cosmosdb
# USAGE
    python cosmos_db_database_account_patch.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CosmosDBManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.database_accounts.begin_update(
        resource_group_name="rg1",
        account_name="ddb1",
        update_parameters={
            "identity": {
                "type": "SystemAssigned,UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/eu2cgroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/id1": {}
                },
            },
            "location": "westus",
            "properties": {
                "analyticalStorageConfiguration": {"schemaType": "WellDefined"},
                "backupPolicy": {
                    "periodicModeProperties": {
                        "backupIntervalInMinutes": 240,
                        "backupRetentionIntervalInHours": 720,
                        "backupStorageRedundancy": "Local",
                    },
                    "type": "Periodic",
                },
                "capacity": {"totalThroughputLimit": 2000},
                "consistencyPolicy": {
                    "defaultConsistencyLevel": "BoundedStaleness",
                    "maxIntervalInSeconds": 10,
                    "maxStalenessPrefix": 200,
                },
                "defaultIdentity": "FirstPartyIdentity",
                "enableAnalyticalStorage": True,
                "enableBurstCapacity": True,
                "enableFreeTier": False,
                "enablePartitionMerge": True,
                "ipRules": [{"ipAddressOrRange": "23.43.230.120"}, {"ipAddressOrRange": "110.12.240.0/12"}],
                "isVirtualNetworkFilterEnabled": True,
                "minimalTlsVersion": "Tls",
                "networkAclBypass": "AzureServices",
                "networkAclBypassResourceIds": [
                    "/subscriptions/subId/resourcegroups/rgName/providers/Microsoft.Synapse/workspaces/workspaceName"
                ],
                "virtualNetworkRules": [
                    {
                        "id": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnet1/subnets/subnet1",
                        "ignoreMissingVNetServiceEndpoint": False,
                    }
                ],
            },
            "tags": {"dept": "finance"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cosmos-db/resource-manager/Microsoft.DocumentDB/stable/2023-09-15/examples/CosmosDBDatabaseAccountPatch.json
if __name__ == "__main__":
    main()
