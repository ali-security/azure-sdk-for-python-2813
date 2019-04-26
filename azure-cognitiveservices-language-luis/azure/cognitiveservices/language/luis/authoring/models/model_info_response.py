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


class ModelInfoResponse(Model):
    """An application model info.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The ID of the Entity Model.
    :type id: str
    :param name: Name of the Entity Model.
    :type name: str
    :param type_id: The type ID of the Entity Model.
    :type type_id: int
    :param readable_type: Required. Possible values include: 'Entity
     Extractor', 'Hierarchical Entity Extractor', 'Hierarchical Child Entity
     Extractor', 'Composite Entity Extractor', 'List Entity Extractor',
     'Prebuilt Entity Extractor', 'Intent Classifier', 'Pattern.Any Entity
     Extractor', 'Closed List Entity Extractor', 'Regex Entity Extractor'
    :type readable_type: str or
     ~azure.cognitiveservices.language.luis.authoring.models.enum
    :param roles:
    :type roles:
     list[~azure.cognitiveservices.language.luis.authoring.models.EntityRole]
    :param children: List of child entities.
    :type children:
     list[~azure.cognitiveservices.language.luis.authoring.models.ChildEntity]
    :param sub_lists: List of sublists.
    :type sub_lists:
     list[~azure.cognitiveservices.language.luis.authoring.models.SubClosedListResponse]
    :param custom_prebuilt_domain_name: The domain name.
    :type custom_prebuilt_domain_name: str
    :param custom_prebuilt_model_name: The intent name or entity name.
    :type custom_prebuilt_model_name: str
    :param regex_pattern: The Regular Expression entity pattern.
    :type regex_pattern: str
    :param explicit_list:
    :type explicit_list:
     list[~azure.cognitiveservices.language.luis.authoring.models.ExplicitListItem]
    """

    _validation = {
        'id': {'required': True},
        'readable_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'int'},
        'readable_type': {'key': 'readableType', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[EntityRole]'},
        'children': {'key': 'children', 'type': '[ChildEntity]'},
        'sub_lists': {'key': 'subLists', 'type': '[SubClosedListResponse]'},
        'custom_prebuilt_domain_name': {'key': 'customPrebuiltDomainName', 'type': 'str'},
        'custom_prebuilt_model_name': {'key': 'customPrebuiltModelName', 'type': 'str'},
        'regex_pattern': {'key': 'regexPattern', 'type': 'str'},
        'explicit_list': {'key': 'explicitList', 'type': '[ExplicitListItem]'},
    }

    def __init__(self, **kwargs):
        super(ModelInfoResponse, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type_id = kwargs.get('type_id', None)
        self.readable_type = kwargs.get('readable_type', None)
        self.roles = kwargs.get('roles', None)
        self.children = kwargs.get('children', None)
        self.sub_lists = kwargs.get('sub_lists', None)
        self.custom_prebuilt_domain_name = kwargs.get('custom_prebuilt_domain_name', None)
        self.custom_prebuilt_model_name = kwargs.get('custom_prebuilt_model_name', None)
        self.regex_pattern = kwargs.get('regex_pattern', None)
        self.explicit_list = kwargs.get('explicit_list', None)
