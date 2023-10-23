# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class DebugInfoResponse(msrest.serialization.Model):
    """DebugInfoResponse.

    :ivar type:
    :vartype type: str
    :ivar message:
    :vartype message: str
    :ivar stack_trace:
    :vartype stack_trace: str
    :ivar inner_exception:
    :vartype inner_exception: ~azure.mgmt.machinelearningservices.models.DebugInfoResponse
    :ivar data: Dictionary of :code:`<any>`.
    :vartype data: dict[str, any]
    :ivar error_response:
    :vartype error_response: ~azure.mgmt.machinelearningservices.models.ErrorResponse
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'inner_exception': {'key': 'innerException', 'type': 'DebugInfoResponse'},
        'data': {'key': 'data', 'type': '{object}'},
        'error_response': {'key': 'errorResponse', 'type': 'ErrorResponse'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword type:
        :paramtype type: str
        :keyword message:
        :paramtype message: str
        :keyword stack_trace:
        :paramtype stack_trace: str
        :keyword inner_exception:
        :paramtype inner_exception: ~azure.mgmt.machinelearningservices.models.DebugInfoResponse
        :keyword data: Dictionary of :code:`<any>`.
        :paramtype data: dict[str, any]
        :keyword error_response:
        :paramtype error_response: ~azure.mgmt.machinelearningservices.models.ErrorResponse
        """
        super(DebugInfoResponse, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.message = kwargs.get('message', None)
        self.stack_trace = kwargs.get('stack_trace', None)
        self.inner_exception = kwargs.get('inner_exception', None)
        self.data = kwargs.get('data', None)
        self.error_response = kwargs.get('error_response', None)


class ErrorAdditionalInfo(msrest.serialization.Model):
    """ErrorAdditionalInfo.

    :ivar type:
    :vartype type: str
    :ivar info: Anything.
    :vartype info: any
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword type:
        :paramtype type: str
        :keyword info: Anything.
        :paramtype info: any
        """
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.info = kwargs.get('info', None)


class ErrorResponse(msrest.serialization.Model):
    """ErrorResponse.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar error:
    :vartype error: ~azure.mgmt.machinelearningservices.models.RootError
    :ivar correlation: Dictionary of :code:`<string>`.
    :vartype correlation: dict[str, str]
    :ivar environment:
    :vartype environment: str
    :ivar location:
    :vartype location: str
    :ivar time:
    :vartype time: ~datetime.datetime
    :ivar component_name:
    :vartype component_name: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'error': {'key': 'error', 'type': 'RootError'},
        'correlation': {'key': 'correlation', 'type': '{str}'},
        'environment': {'key': 'environment', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
        'component_name': {'key': 'componentName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword error:
        :paramtype error: ~azure.mgmt.machinelearningservices.models.RootError
        :keyword correlation: Dictionary of :code:`<string>`.
        :paramtype correlation: dict[str, str]
        :keyword environment:
        :paramtype environment: str
        :keyword location:
        :paramtype location: str
        :keyword time:
        :paramtype time: ~datetime.datetime
        :keyword component_name:
        :paramtype component_name: str
        """
        super(ErrorResponse, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.error = kwargs.get('error', None)
        self.correlation = kwargs.get('correlation', None)
        self.environment = kwargs.get('environment', None)
        self.location = kwargs.get('location', None)
        self.time = kwargs.get('time', None)
        self.component_name = kwargs.get('component_name', None)


class InnerErrorResponse(msrest.serialization.Model):
    """InnerErrorResponse.

    :ivar code:
    :vartype code: str
    :ivar inner_error:
    :vartype inner_error: ~azure.mgmt.machinelearningservices.models.InnerErrorResponse
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorResponse'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword code:
        :paramtype code: str
        :keyword inner_error:
        :paramtype inner_error: ~azure.mgmt.machinelearningservices.models.InnerErrorResponse
        """
        super(InnerErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.inner_error = kwargs.get('inner_error', None)


class RegistryDiscoveryDto(msrest.serialization.Model):
    """RegistryDiscoveryDto.

    :ivar registry_name:
    :vartype registry_name: str
    :ivar tenant_id:
    :vartype tenant_id: str
    :ivar primary_region:
    :vartype primary_region: str
    :ivar regions:
    :vartype regions: list[str]
    :ivar subscription_id:
    :vartype subscription_id: str
    :ivar resource_group:
    :vartype resource_group: str
    :ivar workspace_name:
    :vartype workspace_name: str
    :ivar primary_region_resource_provider_uri:
    :vartype primary_region_resource_provider_uri: str
    """

    _attribute_map = {
        'registry_name': {'key': 'registryName', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'primary_region': {'key': 'primaryRegion', 'type': 'str'},
        'regions': {'key': 'regions', 'type': '[str]'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'workspace_name': {'key': 'workspaceName', 'type': 'str'},
        'primary_region_resource_provider_uri': {'key': 'primaryRegionResourceProviderUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword registry_name:
        :paramtype registry_name: str
        :keyword tenant_id:
        :paramtype tenant_id: str
        :keyword primary_region:
        :paramtype primary_region: str
        :keyword regions:
        :paramtype regions: list[str]
        :keyword subscription_id:
        :paramtype subscription_id: str
        :keyword resource_group:
        :paramtype resource_group: str
        :keyword workspace_name:
        :paramtype workspace_name: str
        :keyword primary_region_resource_provider_uri:
        :paramtype primary_region_resource_provider_uri: str
        """
        super(RegistryDiscoveryDto, self).__init__(**kwargs)
        self.registry_name = kwargs.get('registry_name', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.primary_region = kwargs.get('primary_region', None)
        self.regions = kwargs.get('regions', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.resource_group = kwargs.get('resource_group', None)
        self.workspace_name = kwargs.get('workspace_name', None)
        self.primary_region_resource_provider_uri = kwargs.get('primary_region_resource_provider_uri', None)


class RootError(msrest.serialization.Model):
    """RootError.

    :ivar code:
    :vartype code: str
    :ivar severity:
    :vartype severity: int
    :ivar message:
    :vartype message: str
    :ivar message_format:
    :vartype message_format: str
    :ivar message_parameters: Dictionary of :code:`<string>`.
    :vartype message_parameters: dict[str, str]
    :ivar reference_code:
    :vartype reference_code: str
    :ivar details_uri:
    :vartype details_uri: str
    :ivar target:
    :vartype target: str
    :ivar details:
    :vartype details: list[~azure.mgmt.machinelearningservices.models.RootError]
    :ivar inner_error:
    :vartype inner_error: ~azure.mgmt.machinelearningservices.models.InnerErrorResponse
    :ivar debug_info:
    :vartype debug_info: ~azure.mgmt.machinelearningservices.models.DebugInfoResponse
    :ivar additional_info:
    :vartype additional_info: list[~azure.mgmt.machinelearningservices.models.ErrorAdditionalInfo]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'message_format': {'key': 'messageFormat', 'type': 'str'},
        'message_parameters': {'key': 'messageParameters', 'type': '{str}'},
        'reference_code': {'key': 'referenceCode', 'type': 'str'},
        'details_uri': {'key': 'detailsUri', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[RootError]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorResponse'},
        'debug_info': {'key': 'debugInfo', 'type': 'DebugInfoResponse'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword code:
        :paramtype code: str
        :keyword severity:
        :paramtype severity: int
        :keyword message:
        :paramtype message: str
        :keyword message_format:
        :paramtype message_format: str
        :keyword message_parameters: Dictionary of :code:`<string>`.
        :paramtype message_parameters: dict[str, str]
        :keyword reference_code:
        :paramtype reference_code: str
        :keyword details_uri:
        :paramtype details_uri: str
        :keyword target:
        :paramtype target: str
        :keyword details:
        :paramtype details: list[~azure.mgmt.machinelearningservices.models.RootError]
        :keyword inner_error:
        :paramtype inner_error: ~azure.mgmt.machinelearningservices.models.InnerErrorResponse
        :keyword debug_info:
        :paramtype debug_info: ~azure.mgmt.machinelearningservices.models.DebugInfoResponse
        :keyword additional_info:
        :paramtype additional_info:
         list[~azure.mgmt.machinelearningservices.models.ErrorAdditionalInfo]
        """
        super(RootError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.severity = kwargs.get('severity', None)
        self.message = kwargs.get('message', None)
        self.message_format = kwargs.get('message_format', None)
        self.message_parameters = kwargs.get('message_parameters', None)
        self.reference_code = kwargs.get('reference_code', None)
        self.details_uri = kwargs.get('details_uri', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.inner_error = kwargs.get('inner_error', None)
        self.debug_info = kwargs.get('debug_info', None)
        self.additional_info = kwargs.get('additional_info', None)
