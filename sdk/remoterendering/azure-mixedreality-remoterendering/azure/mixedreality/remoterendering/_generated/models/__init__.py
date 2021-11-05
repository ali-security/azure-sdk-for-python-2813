# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AssetConversion
    from ._models_py3 import AssetConversionInputSettings
    from ._models_py3 import AssetConversionOutput
    from ._models_py3 import AssetConversionOutputSettings
    from ._models_py3 import AssetConversionSettings
    from ._models_py3 import ConversionList
    from ._models_py3 import CreateAssetConversionSettings
    from ._models_py3 import CreateRenderingSessionSettings
    from ._models_py3 import ErrorResponse
    from ._models_py3 import RemoteRenderingError
    from ._models_py3 import RenderingSession
    from ._models_py3 import SessionsList
    from ._models_py3 import UpdateSessionSettings
except (SyntaxError, ImportError):
    from ._models import AssetConversion  # type: ignore
    from ._models import AssetConversionInputSettings  # type: ignore
    from ._models import AssetConversionOutput  # type: ignore
    from ._models import AssetConversionOutputSettings  # type: ignore
    from ._models import AssetConversionSettings  # type: ignore
    from ._models import ConversionList  # type: ignore
    from ._models import CreateAssetConversionSettings  # type: ignore
    from ._models import CreateRenderingSessionSettings  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import RemoteRenderingError  # type: ignore
    from ._models import RenderingSession  # type: ignore
    from ._models import SessionsList  # type: ignore
    from ._models import UpdateSessionSettings  # type: ignore

from ._remote_rendering_rest_client_enums import (
    AssetConversionStatus,
    RenderingSessionSize,
    RenderingSessionStatus,
)

__all__ = [
    'AssetConversion',
    'AssetConversionInputSettings',
    'AssetConversionOutput',
    'AssetConversionOutputSettings',
    'AssetConversionSettings',
    'ConversionList',
    'CreateAssetConversionSettings',
    'CreateRenderingSessionSettings',
    'ErrorResponse',
    'RemoteRenderingError',
    'RenderingSession',
    'SessionsList',
    'UpdateSessionSettings',
    'AssetConversionStatus',
    'RenderingSessionSize',
    'RenderingSessionStatus',
]
