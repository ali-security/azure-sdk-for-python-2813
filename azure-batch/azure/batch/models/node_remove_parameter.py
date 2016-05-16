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


class NodeRemoveParameter(Model):
    """
    Parameters for a ComputeNodeOperations.Remove request.

    :param node_list: A list containing the id of the compute nodes to be
     removed from the specified pool.
    :type node_list: list of str
    :param resize_timeout: The timeout for removal of compute nodes to the
     pool. The default value is 10 minutes.
    :type resize_timeout: timedelta
    :param node_deallocation_option: When compute nodes may be removed from
     the pool. Possible values include: 'requeue', 'terminate',
     'taskcompletion', 'retaineddata'
    :type node_deallocation_option: str
    """ 

    _validation = {
        'node_list': {'required': True},
    }

    _attribute_map = {
        'node_list': {'key': 'nodeList', 'type': '[str]'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'node_deallocation_option': {'key': 'nodeDeallocationOption', 'type': 'ComputeNodeDeallocationOption'},
    }

    def __init__(self, node_list, resize_timeout=None, node_deallocation_option=None):
        self.node_list = node_list
        self.resize_timeout = resize_timeout
        self.node_deallocation_option = node_deallocation_option
