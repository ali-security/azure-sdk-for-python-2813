# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class JobResourceType(Enum):

    vertex_resource = "VertexResource"
    job_manager_resource = "JobManagerResource"
    statistics_resource = "StatisticsResource"
    vertex_resource_in_user_folder = "VertexResourceInUserFolder"
    job_manager_resource_in_user_folder = "JobManagerResourceInUserFolder"
    statistics_resource_in_user_folder = "StatisticsResourceInUserFolder"


class SeverityTypes(Enum):

    warning = "Warning"
    error = "Error"
    info = "Info"


class CompileMode(Enum):

    semantic = "Semantic"
    full = "Full"
    single_box = "SingleBox"


class JobType(Enum):

    usql = "USql"
    hive = "Hive"


class JobState(Enum):

    accepted = "Accepted"
    compiling = "Compiling"
    ended = "Ended"
    new = "New"
    queued = "Queued"
    running = "Running"
    scheduling = "Scheduling"
    starting = "Starting"
    paused = "Paused"
    waiting_for_capacity = "WaitingForCapacity"


class JobResult(Enum):

    none = "None"
    succeeded = "Succeeded"
    cancelled = "Cancelled"
    failed = "Failed"
