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


class DeploymentOperationProperties(Model):
    """Deployment operation properties.

    :param provisioning_state: Gets or sets the state of the provisioning.
    :type provisioning_state: str
    :param timestamp: Gets or sets the date and time of the operation.
    :type timestamp: datetime
    :param service_request_id: Gets or sets deployment operation service
     request id.
    :type service_request_id: str
    :param status_code: Gets or sets operation status code.
    :type status_code: str
    :param status_message: Gets or sets operation status message.
    :type status_message: object
    :param target_resource: Gets or sets the target resource.
    :type target_resource: :class:`TargetResource
     <azure.mgmt.resource.resources.models.TargetResource>`
    :param request: Gets or sets the HTTP request message.
    :type request: :class:`HttpMessage
     <azure.mgmt.resource.resources.models.HttpMessage>`
    :param response: Gets or sets the HTTP response message.
    :type response: :class:`HttpMessage
     <azure.mgmt.resource.resources.models.HttpMessage>`
    """ 

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'service_request_id': {'key': 'serviceRequestId', 'type': 'str'},
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'object'},
        'target_resource': {'key': 'targetResource', 'type': 'TargetResource'},
        'request': {'key': 'request', 'type': 'HttpMessage'},
        'response': {'key': 'response', 'type': 'HttpMessage'},
    }

    def __init__(self, provisioning_state=None, timestamp=None, service_request_id=None, status_code=None, status_message=None, target_resource=None, request=None, response=None):
        self.provisioning_state = provisioning_state
        self.timestamp = timestamp
        self.service_request_id = service_request_id
        self.status_code = status_code
        self.status_message = status_message
        self.target_resource = target_resource
        self.request = request
        self.response = response
