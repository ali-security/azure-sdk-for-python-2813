# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python virtual_machine_create_with_security_type_confidential_vm.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machines.begin_create_or_update(
        resource_group_name="myResourceGroup",
        vm_name="myVM",
        parameters={
            "location": "westus",
            "properties": {
                "hardwareProfile": {"vmSize": "Standard_DC2as_v5"},
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}",
                            "properties": {"primary": True},
                        }
                    ]
                },
                "osProfile": {
                    "adminPassword": "{your-password}",
                    "adminUsername": "{your-username}",
                    "computerName": "myVM",
                },
                "securityProfile": {
                    "securityType": "ConfidentialVM",
                    "uefiSettings": {"secureBootEnabled": True, "vTpmEnabled": True},
                },
                "storageProfile": {
                    "imageReference": {
                        "offer": "2019-datacenter-cvm",
                        "publisher": "MicrosoftWindowsServer",
                        "sku": "windows-cvm",
                        "version": "17763.2183.2109130127",
                    },
                    "osDisk": {
                        "caching": "ReadOnly",
                        "createOption": "FromImage",
                        "managedDisk": {
                            "securityProfile": {"securityEncryptionType": "DiskWithVMGuestState"},
                            "storageAccountType": "StandardSSD_LRS",
                        },
                        "name": "myVMosdisk",
                    },
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2024-03-01/examples/virtualMachineExamples/VirtualMachine_Create_WithSecurityTypeConfidentialVM.json
if __name__ == "__main__":
    main()
