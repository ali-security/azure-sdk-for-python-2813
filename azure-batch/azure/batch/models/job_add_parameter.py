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


class JobAddParameter(Model):
    """
    An Azure Batch job to add.

    :param id: Gets or sets a string that uniquely identifies the job within
     the account. The id can contain any combination of alphanumeric
     characters including hyphens and underscores, and cannot contain more
     than 64 characters. It is common to use a GUID for the id.
    :type id: str
    :param display_name: Gets or sets the display name for the job.
    :type display_name: str
    :param priority: Gets or sets the priority of the job. Priority values
     can range from -1000 to 1000, with -1000 being the lowest priority and
     1000 being the highest priority. The default value is 0.
    :type priority: int
    :param constraints: Gets or sets the execution constraints for the job.
    :type constraints: :class:`JobConstraints
     <azure.batch.models.JobConstraints>`
    :param job_manager_task: Gets or sets details of a Job Manager task to be
     launched when the job is started.
    :type job_manager_task: :class:`JobManagerTask
     <azure.batch.models.JobManagerTask>`
    :param job_preparation_task: Gets or sets the Job Preparation task.
    :type job_preparation_task: :class:`JobPreparationTask
     <azure.batch.models.JobPreparationTask>`
    :param job_release_task: Gets or sets the Job Release task.
    :type job_release_task: :class:`JobReleaseTask
     <azure.batch.models.JobReleaseTask>`
    :param common_environment_settings: Gets or sets the list of common
     environment variable settings.  These environment variables are set for
     all tasks in the job (including the Job Manager, Job Preparation and Job
     Release tasks).
    :type common_environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param pool_info: Gets or sets the pool on which the Batch service runs
     the jobâ€™s tasks.
    :type pool_info: :class:`PoolInformation
     <azure.batch.models.PoolInformation>`
    :param metadata: Gets or sets a list of name-value pairs associated with
     the job as metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    :param uses_task_dependencies: Gets or sets the flag that determines if
     this job will use tasks with dependencies.
    :type uses_task_dependencies: bool
    """ 

    _validation = {
        'id': {'required': True},
        'pool_info': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'constraints': {'key': 'constraints', 'type': 'JobConstraints'},
        'job_manager_task': {'key': 'jobManagerTask', 'type': 'JobManagerTask'},
        'job_preparation_task': {'key': 'jobPreparationTask', 'type': 'JobPreparationTask'},
        'job_release_task': {'key': 'jobReleaseTask', 'type': 'JobReleaseTask'},
        'common_environment_settings': {'key': 'commonEnvironmentSettings', 'type': '[EnvironmentSetting]'},
        'pool_info': {'key': 'poolInfo', 'type': 'PoolInformation'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'uses_task_dependencies': {'key': 'usesTaskDependencies', 'type': 'bool'},
    }

    def __init__(self, id, pool_info, display_name=None, priority=None, constraints=None, job_manager_task=None, job_preparation_task=None, job_release_task=None, common_environment_settings=None, metadata=None, uses_task_dependencies=None, **kwargs):
        self.id = id
        self.display_name = display_name
        self.priority = priority
        self.constraints = constraints
        self.job_manager_task = job_manager_task
        self.job_preparation_task = job_preparation_task
        self.job_release_task = job_release_task
        self.common_environment_settings = common_environment_settings
        self.pool_info = pool_info
        self.metadata = metadata
        self.uses_task_dependencies = uses_task_dependencies
