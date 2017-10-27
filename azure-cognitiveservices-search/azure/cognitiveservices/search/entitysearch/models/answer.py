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

from .response import Response


class Answer(Response):
    """Answer.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SearchResultsAnswer

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Constant filled by server.
    :type _type: str
    :ivar id:
    :vartype id: str
    :ivar contractual_rules: A list of rules that you must adhere to if you
     display the item.
    :vartype contractual_rules:
     list[~azure.cognitiveservices.search.entitysearch.models.ContractualRulesContractualRule]
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'contractual_rules': {'readonly': True},
        'web_search_url': {'readonly': True},
    }

    _subtype_map = {
        '_type': {'SearchResultsAnswer': 'SearchResultsAnswer'}
    }

    def __init__(self):
        super(Answer, self).__init__()
        self._type = 'Answer'
