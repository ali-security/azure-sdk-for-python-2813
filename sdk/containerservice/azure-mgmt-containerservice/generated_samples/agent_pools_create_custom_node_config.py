# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.containerservice import ContainerServiceClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerservice
# USAGE
    python agent_pools_create_custom_node_config.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerServiceClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.agent_pools.begin_create_or_update(
        resource_group_name="rg1",
        resource_name="clustername1",
        agent_pool_name="agentpool1",
        parameters={
            "properties": {
                "count": 3,
                "kubeletConfig": {
                    "allowedUnsafeSysctls": ["kernel.msg*", "net.core.somaxconn"],
                    "cpuCfsQuota": True,
                    "cpuCfsQuotaPeriod": "200ms",
                    "cpuManagerPolicy": "static",
                    "failSwapOn": False,
                    "imageGcHighThreshold": 90,
                    "imageGcLowThreshold": 70,
                    "topologyManagerPolicy": "best-effort",
                },
                "linuxOSConfig": {
                    "swapFileSizeMB": 1500,
                    "sysctls": {
                        "kernelThreadsMax": 99999,
                        "netCoreWmemDefault": 12345,
                        "netIpv4IpLocalPortRange": "20000 60000",
                        "netIpv4TcpTwReuse": True,
                    },
                    "transparentHugePageDefrag": "madvise",
                    "transparentHugePageEnabled": "always",
                },
                "orchestratorVersion": "",
                "osType": "Linux",
                "vmSize": "Standard_DS2_v2",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2024-05-01/examples/AgentPoolsCreate_CustomNodeConfig.json
if __name__ == "__main__":
    main()
