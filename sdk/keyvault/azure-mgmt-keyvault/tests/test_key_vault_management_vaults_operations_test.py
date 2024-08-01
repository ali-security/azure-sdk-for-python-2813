# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.keyvault import KeyVaultManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


class TestKeyVaultManagementVaultsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(KeyVaultManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_resource_group(self, resource_group):
        response = self.client.vaults.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2023-07-01",
        )
        result = [r for r in response]
        assert result == []

    @recorded_by_proxy
    def test_list(self):
        response = self.client.vaults.list(
            filter="resourceType eq 'Microsoft.KeyVault/vaults'",
            api_version="2015-11-01",
        )
        result = [r for r in response]
        assert result