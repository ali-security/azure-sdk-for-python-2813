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


class JobUpdateParameter(Model):
    """
    Parameters for a CloudJobOperations.Update request.

    :param priority: Sets the priority of the job. Priority values can range
     from -1000 to 1000, with -1000 being the lowest priority and 1000 being
     the highest priority. If omitted, the priority of the job is left
     unchanged.
    :type priority: int
    :param constraints: Sets the execution constraints for the job. If
     omitted, the existing execution constraints are left unchanged.
    :type constraints: :class:`JobConstraints
     <azure.batch.models.JobConstraints>`
    :param pool_info: Sets the pool on which the Batch service runs the job's
     tasks. If omitted, the job continues to run on its current pool.
    :type pool_info: :class:`PoolInformation
     <azure.batch.models.PoolInformation>`
    :param metadata: Sets a list of name-value pairs associated with the job
     as metadata. If omitted, the existing job metadata is left unchanged.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _validation = {
        'pool_info': {'required': True},
    }

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'constraints': {'key': 'constraints', 'type': 'JobConstraints'},
        'pool_info': {'key': 'poolInfo', 'type': 'PoolInformation'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, pool_info, priority=None, constraints=None, metadata=None, **kwargs):
        self.priority = priority
        self.constraints = constraints
        self.pool_info = pool_info
        self.metadata = metadata
