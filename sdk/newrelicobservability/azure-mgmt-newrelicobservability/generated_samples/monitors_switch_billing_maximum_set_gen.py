# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.newrelicobservability import NewRelicObservabilityMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-newrelicobservability
# USAGE
    python monitors_switch_billing_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NewRelicObservabilityMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="nqmcgifgaqlf",
    )

    response = client.monitors.switch_billing(
        resource_group_name="rgNewRelic",
        monitor_name="fhcjxnxumkdlgpwanewtkdnyuz",
        request={
            "azureResourceId": "enfghpfw",
            "organizationId": "k",
            "planData": {
                "billingCycle": "YEARLY",
                "effectiveDate": "2022-12-05T14:11:37.786Z",
                "planDetails": "tbbiaga",
                "usageType": "PAYG",
            },
            "userEmail": "ruxvg@xqkmdhrnoo.hlmbpm",
        },
    )
    print(response)


# x-ms-original-file: specification/newrelic/resource-manager/NewRelic.Observability/stable/2022-07-01/examples/Monitors_SwitchBilling_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
