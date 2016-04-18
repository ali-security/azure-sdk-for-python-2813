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


class AzureAsyncOperationResult(Model):
    """
    The response body contains the status of the specified asynchronous
    operation, indicating whether it has succeeded, is in progress, or has
    failed. Note that this status is distinct from the HTTP status code
    returned for the Get Operation Status operation itself. If the
    asynchronous operation succeeded, the response body includes the HTTP
    status code for the successful request. If the asynchronous operation
    failed, the response body includes the HTTP status code for the failed
    request and error information regarding the failure.

    :param status: Gets the status of the AzureAsuncOperation. Possible
     values include: 'InProgress', 'Succeeded', 'Failed'
    :type status: str
    :param error:
    :type error: :class:`Error
     <datalakestoreaccountmanagementclient.models.Error>`
    """ 

    _attribute_map = {
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(self, status=None, error=None):
        self.status = status
        self.error = error
