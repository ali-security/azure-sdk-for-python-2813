# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta

class ApiVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    V2023_06_15_PREVIEW = "2023-06-15-preview"
    V2023_10_03_PREVIEW = "2023-10-03-preview"
    V2024_06_15_PREVIEW = "2024-06-15-preview"

DEFAULT_VERSION = ApiVersion.V2024_06_15_PREVIEW.value
