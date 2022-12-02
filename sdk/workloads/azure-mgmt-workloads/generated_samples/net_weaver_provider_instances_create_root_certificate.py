# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.workloads import WorkloadsClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-workloads
# USAGE
    python net_weaver_provider_instances_create_root_certificate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WorkloadsClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.provider_instances.begin_create(
        resource_group_name="myResourceGroup",
        monitor_name="mySapMonitor",
        provider_instance_name="myProviderInstance",
        provider_instance_parameter={
            "properties": {
                "providerSettings": {
                    "providerType": "SapNetWeaver",
                    "sapClientId": "111",
                    "sapHostFileEntries": ["127.0.0.1 name fqdn"],
                    "sapHostname": "name",
                    "sapInstanceNr": "00",
                    "sapPassword": "****",
                    "sapPasswordUri": "",
                    "sapPortNumber": "1234",
                    "sapSid": "SID",
                    "sapUsername": "username",
                    "sslPreference": "RootCertificate",
                }
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/workloads/resource-manager/Microsoft.Workloads/preview/2021-12-01-preview/examples/workloadmonitor/NetWeaverProviderInstances_Create_Root_Certificate.json
if __name__ == "__main__":
    main()
