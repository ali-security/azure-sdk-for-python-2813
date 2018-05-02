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

from msrest.serialization import Model


class TrendingVideosSubcategory(Model):
    """TrendingVideosSubcategory.

    All required parameters must be populated in order to send to Azure.

    :param title: Required.
    :type title: str
    :param tiles: Required.
    :type tiles:
     list[~azure.cognitiveservices.search.videosearch.models.TrendingVideosTile]
    """

    _validation = {
        'title': {'required': True},
        'tiles': {'required': True},
    }

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'tiles': {'key': 'tiles', 'type': '[TrendingVideosTile]'},
    }

    def __init__(self, *, title: str, tiles, **kwargs) -> None:
        super(TrendingVideosSubcategory, self).__init__(**kwargs)
        self.title = title
        self.tiles = tiles
