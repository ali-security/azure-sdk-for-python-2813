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


class PoolStatistics(Model):
    """Contains utilization and resource usage statistics for the lifetime of a
    pool.

    :param url: The URL for the statistics.
    :type url: str
    :param start_time: The start time of the time range covered by the
     statistics.
    :type start_time: datetime
    :param last_update_time: The time at which the statistics were last
     updated. All statistics are limited to the range between startTime and
     lastUpdateTime.
    :type last_update_time: datetime
    :param usage_stats: Statistics related to pool usage, such as the amount
     of core-time used.
    :type usage_stats: :class:`UsageStatistics
     <azure.batch.models.UsageStatistics>`
    :param resource_stats: Statistics related to resource consumption by
     compute nodes in the pool.
    :type resource_stats: :class:`ResourceStatistics
     <azure.batch.models.ResourceStatistics>`
    """ 

    _validation = {
        'url': {'required': True},
        'start_time': {'required': True},
        'last_update_time': {'required': True},
    }

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'usage_stats': {'key': 'usageStats', 'type': 'UsageStatistics'},
        'resource_stats': {'key': 'resourceStats', 'type': 'ResourceStatistics'},
    }

    def __init__(self, url, start_time, last_update_time, usage_stats=None, resource_stats=None):
        self.url = url
        self.start_time = start_time
        self.last_update_time = last_update_time
        self.usage_stats = usage_stats
        self.resource_stats = resource_stats
