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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.media_service_operations import MediaServiceOperations
from . import models


class MediaServicesManagementClientConfiguration(AzureConfiguration):
    """Configuration for MediaServicesManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription id.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client
     request. Current version is 2015-10-01
    :type api_version: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2015-10-01', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if api_version is not None and not isinstance(api_version, str):
            raise TypeError("Optional parameter 'api_version' must be str.")
        if accept_language is not None and not isinstance(accept_language, str):
            raise TypeError("Optional parameter 'accept_language' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(MediaServicesManagementClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('mediaservicesmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.api_version = api_version
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class MediaServicesManagementClient(object):
    """Media Services resource management APIs.

    :ivar config: Configuration for client.
    :vartype config: MediaServicesManagementClientConfiguration

    :ivar media_service: MediaService operations
    :vartype media_service: .operations.MediaServiceOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure subscription id.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client
     request. Current version is 2015-10-01
    :type api_version: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2015-10-01', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        self.config = MediaServicesManagementClientConfiguration(credentials, subscription_id, api_version, accept_language, long_running_operation_retry_timeout, generate_client_request_id, base_url, filepath)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.media_service = MediaServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
