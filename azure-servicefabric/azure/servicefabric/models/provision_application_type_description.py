# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .provision_application_type_description_base import ProvisionApplicationTypeDescriptionBase


class ProvisionApplicationTypeDescription(ProvisionApplicationTypeDescriptionBase):
    """Describes the operation to register or provision an application type using
    an application package uploaded to the Service Fabric image store.

    :param async_property: Indicates whether or not provisioning should occur
     asynchronously. When set to true, the provision operation returns when the
     request is accepted by the system, and the provision operation continues
     without any timeout limit. The default value is false. For large
     application packages, we recommend setting the value to true.
    :type async_property: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param application_type_build_path: The relative path for the application
     package in the image store specified during the prior upload operation.
    :type application_type_build_path: str
    """

    _validation = {
        'async_property': {'required': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'async_property': {'key': 'Async', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'application_type_build_path': {'key': 'ApplicationTypeBuildPath', 'type': 'str'},
    }

    def __init__(self, async_property, application_type_build_path=None):
        super(ProvisionApplicationTypeDescription, self).__init__(async_property=async_property)
        self.application_type_build_path = application_type_build_path
        self.kind = 'ImageStorePath'
