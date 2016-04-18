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


class HiveJobProperties(JobProperties):
    """HiveJobProperties

    :param runtime_version: Gets or sets the runtime version of the U-SQL
     engine to use
    :type runtime_version: str
    :param script: Gets or sets the U-SQL script to run
    :type script: str
    :param type: Polymorphic Discriminator
    :type type: str
    :param statement_info: Gets or sets the statement information for each
     statement in the script
    :type statement_info: list of :class:`HiveJobStatementInfo
     <datalakeanalyticsjobmanagementclient.models.HiveJobStatementInfo>`
    :param logs_location: Gets or sets the Hive logs location
    :type logs_location: str
    :param warehouse_location: Gets or sets the runtime version of the U-SQL
     engine to use
    :type warehouse_location: str
    :param statement_count: Gets or sets the number of statements that will
     be run based on the script
    :type statement_count: int
    :param executed_statement_count: Gets or sets the number of statements
     that have been run based on the script
    :type executed_statement_count: int
    """ 

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'statement_info': {'key': 'statementInfo', 'type': '[HiveJobStatementInfo]'},
        'logs_location': {'key': 'logsLocation', 'type': 'str'},
        'warehouse_location': {'key': 'warehouseLocation', 'type': 'str'},
        'statement_count': {'key': 'statementCount', 'type': 'int'},
        'executed_statement_count': {'key': 'executedStatementCount', 'type': 'int'},
    }

    def __init__(self, script, runtime_version=None, statement_info=None, logs_location=None, warehouse_location=None, statement_count=None, executed_statement_count=None):
        super(HiveJobProperties, self).__init__(runtime_version=runtime_version, script=script)
        self.statement_info = statement_info
        self.logs_location = logs_location
        self.warehouse_location = warehouse_location
        self.statement_count = statement_count
        self.executed_statement_count = executed_statement_count
        self.type = 'Hive'
