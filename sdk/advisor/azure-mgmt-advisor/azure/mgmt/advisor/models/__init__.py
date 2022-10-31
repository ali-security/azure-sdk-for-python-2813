# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ARMErrorResponseBody
from ._models_py3 import ArmErrorResponse
from ._models_py3 import ConfigData
from ._models_py3 import ConfigurationListResult
from ._models_py3 import DigestConfig
from ._models_py3 import MetadataEntity
from ._models_py3 import MetadataEntityListResult
from ._models_py3 import MetadataSupportedValueDetail
from ._models_py3 import OperationDisplayInfo
from ._models_py3 import OperationEntity
from ._models_py3 import OperationEntityListResult
from ._models_py3 import Resource
from ._models_py3 import ResourceMetadata
from ._models_py3 import ResourceRecommendationBase
from ._models_py3 import ResourceRecommendationBaseListResult
from ._models_py3 import ShortDescription
from ._models_py3 import SuppressionContract
from ._models_py3 import SuppressionContractListResult

from ._advisor_management_client_enums import Category
from ._advisor_management_client_enums import ConfigurationName
from ._advisor_management_client_enums import CpuThreshold
from ._advisor_management_client_enums import DigestConfigState
from ._advisor_management_client_enums import Impact
from ._advisor_management_client_enums import Scenario
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ARMErrorResponseBody",
    "ArmErrorResponse",
    "ConfigData",
    "ConfigurationListResult",
    "DigestConfig",
    "MetadataEntity",
    "MetadataEntityListResult",
    "MetadataSupportedValueDetail",
    "OperationDisplayInfo",
    "OperationEntity",
    "OperationEntityListResult",
    "Resource",
    "ResourceMetadata",
    "ResourceRecommendationBase",
    "ResourceRecommendationBaseListResult",
    "ShortDescription",
    "SuppressionContract",
    "SuppressionContractListResult",
    "Category",
    "ConfigurationName",
    "CpuThreshold",
    "DigestConfigState",
    "Impact",
    "Scenario",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
