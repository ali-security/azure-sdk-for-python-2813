# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.maintenance import MaintenanceManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-maintenance
# USAGE
    python configuration_assignments_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MaintenanceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="5b4b650e-28b9-4790-b3ab-ddbd88d727c4",
    )

    response = client.configuration_assignments.create_or_update(
        resource_group_name="examplerg",
        provider_name="Microsoft.Compute",
        resource_type="virtualMachineScaleSets",
        resource_name="smdtest1",
        configuration_assignment_name="workervmConfiguration",
        configuration_assignment={
            "properties": {
                "maintenanceConfigurationId": "/subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourcegroups/examplerg/providers/Microsoft.Maintenance/maintenanceConfigurations/configuration1"
            }
        },
    )
    print(response)


# x-ms-original-file: specification/maintenance/resource-manager/Microsoft.Maintenance/stable/2023-04-01/examples/ConfigurationAssignments_CreateOrUpdate.json
if __name__ == "__main__":
    main()
