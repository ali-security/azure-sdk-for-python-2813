# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SupportTicketsOperations(object):
    """SupportTicketsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.support.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def check_name_availability(
        self,
        check_name_availability_input,  # type: "_models.CheckNameAvailabilityInput"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.CheckNameAvailabilityOutput"
        """Check the availability of a resource name. This API should be used to check the uniqueness of
        the name for support ticket creation for the selected subscription.

        :param check_name_availability_input: Input to check.
        :type check_name_availability_input: ~azure.mgmt.support.models.CheckNameAvailabilityInput
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput, or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.CheckNameAvailabilityOutput
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CheckNameAvailabilityOutput"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.check_name_availability.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(check_name_availability_input, 'CheckNameAvailabilityInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ExceptionResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CheckNameAvailabilityOutput', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    check_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/checkNameAvailability'}  # type: ignore

    def list(
        self,
        top=None,  # type: Optional[int]
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.SupportTicketsListResult"]
        """Lists all the support tickets for an Azure subscription. You can also filter the support
        tickets by *Status* or *CreatedDate* using the $filter parameter. Output will be a paged result
        with *nextLink*\ , using which you can retrieve the next set of support tickets.
        :code:`<br/>`:code:`<br/>`Support ticket data is available for 18 months after ticket creation.
        If a ticket was created more than 18 months ago, a request for data might cause an error.

        :param top: The number of values to return in the collection. Default is 25 and max is 100.
        :type top: int
        :param filter: The filter to apply on the operation. We support 'odata v4.0' filter semantics.
         `Learn more <https://docs.microsoft.com/odata/concepts/queryoptions-overview>`_. *Status*
         filter can only be used with Equals ('eq') operator. For *CreatedDate* filter, the supported
         operators are Greater Than ('gt') and Greater Than or Equals ('ge'). When using both filters,
         combine them using the logical 'AND'.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SupportTicketsListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.support.models.SupportTicketsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SupportTicketsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('SupportTicketsListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(_models.ExceptionResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets'}  # type: ignore

    def get(
        self,
        support_ticket_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SupportTicketDetails"
        """Get ticket details for an Azure subscription. Support ticket data is available for 18 months
        after ticket creation. If a ticket was created more than 18 months ago, a request for data
        might cause an error.

        :param support_ticket_name: Support ticket name.
        :type support_ticket_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SupportTicketDetails, or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SupportTicketDetails"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ExceptionResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SupportTicketDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}  # type: ignore

    def update(
        self,
        support_ticket_name,  # type: str
        update_support_ticket,  # type: "_models.UpdateSupportTicket"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SupportTicketDetails"
        """This API allows you to update the severity level, ticket status, and your contact information
        in the support ticket.:code:`<br/>`:code:`<br/>`Note: The severity levels cannot be changed if
        a support ticket is actively being worked upon by an Azure support engineer. In such a case,
        contact your support engineer to request severity update by adding a new communication using
        the Communications API.:code:`<br/>`:code:`<br/>`Changing the ticket status to *closed* is
        allowed only on an unassigned case. When an engineer is actively working on the ticket, send
        your ticket closure request by sending a note to your engineer.

        :param support_ticket_name: Support ticket name.
        :type support_ticket_name: str
        :param update_support_ticket: UpdateSupportTicket object.
        :type update_support_ticket: ~azure.mgmt.support.models.UpdateSupportTicket
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SupportTicketDetails, or the result of cls(response)
        :rtype: ~azure.mgmt.support.models.SupportTicketDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SupportTicketDetails"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(update_support_ticket, 'UpdateSupportTicket')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ExceptionResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SupportTicketDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}  # type: ignore

    def _create_initial(
        self,
        support_ticket_name,  # type: str
        create_support_ticket_parameters,  # type: "_models.SupportTicketDetails"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.SupportTicketDetails"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.SupportTicketDetails"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-04-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._create_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(create_support_ticket_parameters, 'SupportTicketDetails')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ExceptionResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SupportTicketDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}  # type: ignore

    def begin_create(
        self,
        support_ticket_name,  # type: str
        create_support_ticket_parameters,  # type: "_models.SupportTicketDetails"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.SupportTicketDetails"]
        """Creates a new support ticket for Subscription and Service limits (Quota), Technical, Billing,
        and Subscription Management issues for the specified subscription. Learn the `prerequisites
        <https://aka.ms/supportAPI>`_ required to create a support
        ticket.:code:`<br/>`:code:`<br/>`Always call the Services and ProblemClassifications API to get
        the most recent set of services and problem categories required for support ticket
        creation.:code:`<br/>`:code:`<br/>`Adding attachments is not currently supported via the API.
        To add a file to an existing support ticket, visit the `Manage support ticket
        <https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest>`_
        page in the Azure portal, select the support ticket, and use the file upload control to add a
        new file.:code:`<br/>`:code:`<br/>`Providing consent to share diagnostic information with Azure
        support is currently not supported via the API. The Azure support engineer working on your
        ticket will reach out to you for consent if your issue requires gathering diagnostic
        information from your Azure resources.:code:`<br/>`:code:`<br/>`\ **Creating a support ticket
        for on-behalf-of**\ : Include *x-ms-authorization-auxiliary* header to provide an auxiliary
        token as per `documentation <https://docs.microsoft.com/azure/azure-resource-
        manager/management/authenticate-multi-tenant>`_. The primary token will be from the tenant for
        whom a support ticket is being raised against the subscription, i.e. Cloud solution provider
        (CSP) customer tenant. The auxiliary token will be from the Cloud solution provider (CSP)
        partner tenant.

        :param support_ticket_name: Support ticket name.
        :type support_ticket_name: str
        :param create_support_ticket_parameters: Support ticket request payload.
        :type create_support_ticket_parameters: ~azure.mgmt.support.models.SupportTicketDetails
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either SupportTicketDetails or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.support.models.SupportTicketDetails]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SupportTicketDetails"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_initial(
                support_ticket_name=support_ticket_name,
                create_support_ticket_parameters=create_support_ticket_parameters,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('SupportTicketDetails', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'supportTicketName': self._serialize.url("support_ticket_name", support_ticket_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }

        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}'}  # type: ignore
