# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.mongocluster import MongoClusterMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-mongocluster
# USAGE
    python mongo_clusters_create_pitr.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MongoClusterMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.mongo_clusters.begin_create_or_update(
        resource_group_name="TestResourceGroup",
        mongo_cluster_name="myMongoCluster",
        resource={
            "location": "westus2",
            "properties": {
                "createMode": "PointInTimeRestore",
                "restoreParameters": {
                    "pointInTimeUTC": "2023-01-13T20:07:35Z",
                    "sourceResourceId": "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/TestResourceGroup/providers/Microsoft.DocumentDB/mongoClusters/myOtherMongoCluster",
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-06-01-preview/MongoClusters_CreatePITR.json
if __name__ == "__main__":
    main()
