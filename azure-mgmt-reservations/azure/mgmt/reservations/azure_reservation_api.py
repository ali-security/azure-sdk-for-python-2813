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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling
import uuid
from .operations.reservation_order_operations import ReservationOrderOperations
from .operations.reservation_operations import ReservationOperations
from .operations.operation_operations import OperationOperations
from . import models


class AzureReservationAPIConfiguration(AzureConfiguration):
    """Configuration for AzureReservationAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AzureReservationAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-reservations/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class AzureReservationAPI(SDKClient):
    """This API describe Azure Reservation

    :ivar config: Configuration for client.
    :vartype config: AzureReservationAPIConfiguration

    :ivar reservation_order: ReservationOrder operations
    :vartype reservation_order: azure.mgmt.reservations.operations.ReservationOrderOperations
    :ivar reservation: Reservation operations
    :vartype reservation: azure.mgmt.reservations.operations.ReservationOperations
    :ivar operation: Operation operations
    :vartype operation: azure.mgmt.reservations.operations.OperationOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = AzureReservationAPIConfiguration(credentials, base_url)
        super(AzureReservationAPI, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.reservation_order = ReservationOrderOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reservation = ReservationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def get_catalog(
            self, subscription_id, reserved_resource_type, location=None, custom_headers=None, raw=False, **operation_config):
        """Get the regions and skus that are available for RI purchase for the
        specified Azure subscription.

        :param subscription_id: Id of the subscription
        :type subscription_id: str
        :param reserved_resource_type: The type of the resource for which the
         skus should be provided.
        :type reserved_resource_type: str
        :param location: Filters the skus based on the location specified in
         this parameter. This can be an azure region or global
        :type location: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.mgmt.reservations.models.Catalog] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.reservations.models.ErrorException>`
        """
        # Construct URL
        url = self.get_catalog.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['reservedResourceType'] = self._serialize.query("reserved_resource_type", reserved_resource_type, 'str')
        if location is not None:
            query_parameters['location'] = self._serialize.query("location", location, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[Catalog]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_catalog.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/catalogs'}

    def get_applied_reservation_list(
            self, subscription_id, custom_headers=None, raw=False, **operation_config):
        """Get list of applicable `Reservation`s.

        Get applicable `Reservation`s that are applied to this subscription.

        :param subscription_id: Id of the subscription
        :type subscription_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AppliedReservations or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.reservations.models.AppliedReservations or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.reservations.models.ErrorException>`
        """
        # Construct URL
        url = self.get_applied_reservation_list.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AppliedReservations', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_applied_reservation_list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/appliedReservations'}
