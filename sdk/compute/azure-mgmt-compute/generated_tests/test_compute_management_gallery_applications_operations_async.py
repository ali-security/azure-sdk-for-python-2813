# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.compute.aio import ComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestComputeManagementGalleryApplicationsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.gallery_applications.begin_create_or_update(
                resource_group_name=resource_group.name,
                gallery_name="str",
                gallery_application_name="str",
                gallery_application={
                    "location": "str",
                    "description": "str",
                    "endOfLifeDate": "2020-02-20 00:00:00",
                    "eula": "str",
                    "id": "str",
                    "name": "str",
                    "privacyStatementUri": "str",
                    "releaseNoteUri": "str",
                    "supportedOSType": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                },
                api_version="2019-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.gallery_applications.get(
            resource_group_name=resource_group.name,
            gallery_name="str",
            gallery_application_name="str",
            api_version="2019-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.gallery_applications.begin_delete(
                resource_group_name=resource_group.name,
                gallery_name="str",
                gallery_application_name="str",
                api_version="2019-03-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_gallery(self, resource_group):
        response = self.client.gallery_applications.list_by_gallery(
            resource_group_name=resource_group.name,
            gallery_name="str",
            api_version="2019-03-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
