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

from .job_properties import JobProperties


class USqlJobProperties(JobProperties):
    """USqlJobProperties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param runtime_version: Gets or sets the runtime version of the U-SQL
     engine to use
    :type runtime_version: str
    :param script: Gets or sets the U-SQL script to run
    :type script: str
    :param type: Polymorphic Discriminator
    :type type: str
    :param resources: Gets or sets the list of resources that are required by
     the job
    :type resources: list of :class:`JobResource
     <azure.mgmt.datalake.analytics.job.models.JobResource>`
    :param statistics: Gets or sets the job specific statistics.
    :type statistics: :class:`JobStatistics
     <azure.mgmt.datalake.analytics.job.models.JobStatistics>`
    :param debug_data: Gets or sets the job specific debug data locations.
    :type debug_data: :class:`JobDataPath
     <azure.mgmt.datalake.analytics.job.models.JobDataPath>`
    :ivar algebra_file_path: Gets the U-SQL algebra file path after the job
     has completed
    :vartype algebra_file_path: str
    :ivar total_compilation_time: Gets the total time this job spent
     compiling. This value should not be set by the user and will be ignored
     if it is.
    :vartype total_compilation_time: str
    :ivar total_pause_time: Gets the total time this job spent paused. This
     value should not be set by the user and will be ignored if it is.
    :vartype total_pause_time: str
    :ivar total_queued_time: Gets the total time this job spent queued. This
     value should not be set by the user and will be ignored if it is.
    :vartype total_queued_time: str
    :ivar total_running_time: Gets the total time this job spent executing.
     This value should not be set by the user and will be ignored if it is.
    :vartype total_running_time: str
    :ivar root_process_node_id: Gets the ID used to identify the job manager
     coordinating job execution. This value should not be set by the user and
     will be ignored if it is.
    :vartype root_process_node_id: str
    :ivar yarn_application_id: Gets the ID used to identify the yarn
     application executing the job. This value should not be set by the user
     and will be ignored if it is.
    :vartype yarn_application_id: str
    :ivar yarn_application_time_stamp: Gets the timestamp (in ticks) for the
     yarn application executing the job. This value should not be set by the
     user and will be ignored if it is.
    :vartype yarn_application_time_stamp: long
    :param compile_mode: Gets or sets the compile mode for the job. Possible
     values include: 'Semantic', 'Full', 'SingleBox'
    :type compile_mode: str or :class:`CompileMode
     <azure.mgmt.datalake.analytics.job.models.CompileMode>`
    """ 

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
        'algebra_file_path': {'readonly': True},
        'total_compilation_time': {'readonly': True},
        'total_pause_time': {'readonly': True},
        'total_queued_time': {'readonly': True},
        'total_running_time': {'readonly': True},
        'root_process_node_id': {'readonly': True},
        'yarn_application_id': {'readonly': True},
        'yarn_application_time_stamp': {'readonly': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[JobResource]'},
        'statistics': {'key': 'statistics', 'type': 'JobStatistics'},
        'debug_data': {'key': 'debugData', 'type': 'JobDataPath'},
        'algebra_file_path': {'key': 'algebraFilePath', 'type': 'str'},
        'total_compilation_time': {'key': 'totalCompilationTime', 'type': 'str'},
        'total_pause_time': {'key': 'totalPauseTime', 'type': 'str'},
        'total_queued_time': {'key': 'totalQueuedTime', 'type': 'str'},
        'total_running_time': {'key': 'totalRunningTime', 'type': 'str'},
        'root_process_node_id': {'key': 'rootProcessNodeId', 'type': 'str'},
        'yarn_application_id': {'key': 'yarnApplicationId', 'type': 'str'},
        'yarn_application_time_stamp': {'key': 'yarnApplicationTimeStamp', 'type': 'long'},
        'compile_mode': {'key': 'compileMode', 'type': 'CompileMode'},
    }

    def __init__(self, script, runtime_version=None, resources=None, statistics=None, debug_data=None, compile_mode=None):
        super(USqlJobProperties, self).__init__(runtime_version=runtime_version, script=script)
        self.resources = resources
        self.statistics = statistics
        self.debug_data = debug_data
        self.algebra_file_path = None
        self.total_compilation_time = None
        self.total_pause_time = None
        self.total_queued_time = None
        self.total_running_time = None
        self.root_process_node_id = None
        self.yarn_application_id = None
        self.yarn_application_time_stamp = None
        self.compile_mode = compile_mode
        self.type = 'USql'
