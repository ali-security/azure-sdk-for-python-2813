# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.desktopvirtualization import DesktopVirtualizationMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-desktopvirtualization
# USAGE
    python scaling_plan_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DesktopVirtualizationMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="daefabc0-95b4-48b3-b645-8a753a63c4fa",
    )

    response = client.scaling_plans.create(
        resource_group_name="resourceGroup1",
        scaling_plan_name="scalingPlan1",
        scaling_plan={
            "location": "centralus",
            "properties": {
                "description": "Description of Scaling Plan",
                "exclusionTag": "value",
                "friendlyName": "Scaling Plan 1",
                "hostPoolReferences": [
                    {
                        "hostPoolArmPath": "/subscriptions/daefabc0-95b4-48b3-b645-8a753a63c4fa/resourceGroups/resourceGroup1/providers/Microsoft.DesktopVirtualization/hostPools/hostPool1",
                        "scalingPlanEnabled": True,
                    }
                ],
                "hostPoolType": "Pooled",
                "schedules": [
                    {
                        "daysOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                        "name": "schedule1",
                        "offPeakLoadBalancingAlgorithm": "DepthFirst",
                        "offPeakStartTime": {"hour": 20, "minute": 0},
                        "peakLoadBalancingAlgorithm": "BreadthFirst",
                        "peakStartTime": {"hour": 8, "minute": 0},
                        "rampDownCapacityThresholdPct": 50,
                        "rampDownForceLogoffUsers": True,
                        "rampDownLoadBalancingAlgorithm": "DepthFirst",
                        "rampDownMinimumHostsPct": 20,
                        "rampDownNotificationMessage": "message",
                        "rampDownStartTime": {"hour": 18, "minute": 0},
                        "rampDownWaitTimeMinutes": 30,
                        "rampUpCapacityThresholdPct": 80,
                        "rampUpLoadBalancingAlgorithm": "DepthFirst",
                        "rampUpMinimumHostsPct": 20,
                        "rampUpStartTime": {"hour": 6, "minute": 0},
                    }
                ],
                "timeZone": "Central Standard Time",
            },
            "tags": {"tag1": "value1", "tag2": "value2"},
        },
    )
    print(response)


# x-ms-original-file: specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/stable/2024-04-03/examples/ScalingPlan_Create.json
if __name__ == "__main__":
    main()
