# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountListNodeAgentSkusOptions(Model):
    """
    Additional parameters for the Account_ListNodeAgentSkus operation.

    :param filter: An OData $filter clause.
    :type filter: str
    :param max_results: The maximum number of items to return in the response.
    :type max_results: int
    :param timeout: The maximum time that the server can spend processing the
     request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the
     form of a GUID with no decoration such as curly braces, e.g.
     9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the
     client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this
     header will be automatically populated with the current system clock
     time.
    :type ocp_date: datetime
    """ 

    def __init__(self, filter=None, max_results=None, timeout=30, client_request_id=None, return_client_request_id=None, ocp_date=None):
        self.filter = filter
        self.max_results = max_results
        self.timeout = timeout
        self.client_request_id = client_request_id
        self.return_client_request_id = return_client_request_id
        self.ocp_date = ocp_date
