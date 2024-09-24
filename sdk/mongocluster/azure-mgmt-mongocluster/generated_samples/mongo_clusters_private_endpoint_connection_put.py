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
    python mongo_clusters_private_endpoint_connection_put.py

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

    response = client.private_endpoint_connections.begin_create(
        resource_group_name="TestGroup",
        mongo_cluster_name="myMongoCluster",
        private_endpoint_connection_name="pecTest",
        resource={
            "properties": {"privateLinkServiceConnectionState": {"description": "Auto-Approved", "status": "Approved"}}
        },
    ).result()
    print(response)


# x-ms-original-file: 2024-06-01-preview/MongoClusters_PrivateEndpointConnectionPut.json
if __name__ == "__main__":
    main()
