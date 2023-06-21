# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.trafficmanager import TrafficManagerManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-trafficmanager
# USAGE
    python endpoint_put_external_with_custom_headers.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = TrafficManagerManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.endpoints.create_or_update(
        resource_group_name="azuresdkfornetautoresttrafficmanager1421",
        profile_name="azsmnet6386",
        endpoint_type="ExternalEndpoints",
        endpoint_name="azsmnet7187",
        parameters={
            "name": "azsmnet7187",
            "properties": {
                "customHeaders": [{"name": "header-1", "value": "value-1"}, {"name": "header-2", "value": "value-2"}],
                "endpointLocation": "North Europe",
                "endpointStatus": "Enabled",
                "target": "foobar.contoso.com",
            },
            "type": "Microsoft.network/TrafficManagerProfiles/ExternalEndpoints",
        },
    )
    print(response)


# x-ms-original-file: specification/trafficmanager/resource-manager/Microsoft.Network/stable/2022-04-01/examples/Endpoint-PUT-External-WithCustomHeaders.json
if __name__ == "__main__":
    main()
