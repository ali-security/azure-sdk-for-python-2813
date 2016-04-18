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

from .sub_resource import SubResource


class WorkflowTriggerHistory(SubResource):
    """WorkflowTriggerHistory

    :param id: Gets or sets the resource id.
    :type id: str
    :param start_time: Gets the start time.
    :type start_time: datetime
    :param end_time: Gets the end time.
    :type end_time: datetime
    :param status: Gets the status. Possible values include: 'NotSpecified',
     'Paused', 'Running', 'Waiting', 'Succeeded', 'Skipped', 'Suspended',
     'Cancelled', 'Failed', 'Faulted', 'TimedOut', 'Aborted'
    :type status: str
    :param code: Gets the code.
    :type code: str
    :param error: Gets the error.
    :type error: object
    :param tracking_id: Gets the tracking id.
    :type tracking_id: str
    :param inputs_link: Gets the link to input parameters.
    :type inputs_link: :class:`ContentLink
     <logicmanagementclient.models.ContentLink>`
    :param outputs_link: Gets the link to output parameters.
    :type outputs_link: :class:`ContentLink
     <logicmanagementclient.models.ContentLink>`
    :param fired: Gets a value indicating whether trigger was fired.
    :type fired: bool
    :param run: Gets the reference to workflow run.
    :type run: :class:`ResourceReference
     <logicmanagementclient.models.ResourceReference>`
    :param name: Gets the workflow trigger history name.
    :type name: str
    :param type: Gets the workflow trigger history type.
    :type type: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'status': {'key': 'properties.status', 'type': 'WorkflowStatus'},
        'code': {'key': 'properties.code', 'type': 'str'},
        'error': {'key': 'properties.error', 'type': 'object'},
        'tracking_id': {'key': 'properties.trackingId', 'type': 'str'},
        'inputs_link': {'key': 'properties.inputsLink', 'type': 'ContentLink'},
        'outputs_link': {'key': 'properties.outputsLink', 'type': 'ContentLink'},
        'fired': {'key': 'properties.fired', 'type': 'bool'},
        'run': {'key': 'properties.run', 'type': 'ResourceReference'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, start_time=None, end_time=None, status=None, code=None, error=None, tracking_id=None, inputs_link=None, outputs_link=None, fired=None, run=None, name=None, type=None):
        super(WorkflowTriggerHistory, self).__init__(id=id)
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.code = code
        self.error = error
        self.tracking_id = tracking_id
        self.inputs_link = inputs_link
        self.outputs_link = outputs_link
        self.fired = fired
        self.run = run
        self.name = name
        self.type = type
