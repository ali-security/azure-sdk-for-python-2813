# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python security_partner_provider_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.security_partner_providers.begin_create_or_update(
        resource_group_name="rg1",
        security_partner_provider_name="securityPartnerProvider",
        parameters={
            "location": "West US",
            "properties": {
                "securityProviderName": "ZScaler",
                "virtualHub": {
                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualHubs/hub1"
                },
            },
            "tags": {"key1": "value1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-02-01/examples/SecurityPartnerProviderPut.json
if __name__ == "__main__":
    main()
