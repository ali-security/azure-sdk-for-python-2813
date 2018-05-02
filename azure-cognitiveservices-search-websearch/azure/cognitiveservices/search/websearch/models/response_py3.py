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

from .identifiable import Identifiable


class Response(Identifiable):
    """Defines a response. All schemas that could be returned at the root of a
    response should inherit from this.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SearchResponse, Thing, Answer, ErrorResponse

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'SearchResponse': 'SearchResponse', 'Thing': 'Thing', 'Answer': 'Answer', 'ErrorResponse': 'ErrorResponse'}
    }

    def __init__(self, **kwargs) -> None:
        super(Response, self).__init__(**kwargs)
        self.web_search_url = None
        self._type = 'Response'
