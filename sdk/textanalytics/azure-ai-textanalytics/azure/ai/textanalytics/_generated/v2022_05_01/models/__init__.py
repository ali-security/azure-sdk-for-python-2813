# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AnalyzeTextEntityLinkingInput
from ._models_py3 import AnalyzeTextEntityRecognitionInput
from ._models_py3 import AnalyzeTextJobState
from ._models_py3 import AnalyzeTextJobStatistics
from ._models_py3 import AnalyzeTextJobsInput
from ._models_py3 import AnalyzeTextKeyPhraseExtractionInput
from ._models_py3 import AnalyzeTextLROResult
from ._models_py3 import AnalyzeTextLROTask
from ._models_py3 import AnalyzeTextLanguageDetectionInput
from ._models_py3 import AnalyzeTextPiiEntitiesRecognitionInput
from ._models_py3 import AnalyzeTextSentimentAnalysisInput
from ._models_py3 import AnalyzeTextTask
from ._models_py3 import AnalyzeTextTaskResult
from ._models_py3 import ClassificationDocumentResult
from ._models_py3 import ClassificationResult
from ._models_py3 import CustomEntitiesLROTask
from ._models_py3 import CustomEntitiesResult
from ._models_py3 import CustomEntitiesResultDocumentsItem
from ._models_py3 import CustomEntitiesTaskParameters
from ._models_py3 import CustomEntityRecognitionLROResult
from ._models_py3 import CustomLabelClassificationResult
from ._models_py3 import CustomLabelClassificationResultDocumentsItem
from ._models_py3 import CustomMultiLabelClassificationLROResult
from ._models_py3 import CustomMultiLabelClassificationLROTask
from ._models_py3 import CustomMultiLabelClassificationTaskParameters
from ._models_py3 import CustomResult
from ._models_py3 import CustomSingleLabelClassificationLROResult
from ._models_py3 import CustomSingleLabelClassificationLROTask
from ._models_py3 import CustomSingleLabelClassificationTaskParameters
from ._models_py3 import CustomTaskParameters
from ._models_py3 import DetectedLanguage
from ._models_py3 import DocumentError
from ._models_py3 import DocumentResult
from ._models_py3 import DocumentStatistics
from ._models_py3 import DocumentWarning
from ._models_py3 import EntitiesDocumentResult
from ._models_py3 import EntitiesLROTask
from ._models_py3 import EntitiesResult
from ._models_py3 import EntitiesResultDocumentsItem
from ._models_py3 import EntitiesTaskParameters
from ._models_py3 import EntitiesTaskResult
from ._models_py3 import Entity
from ._models_py3 import EntityLinkingLROResult
from ._models_py3 import EntityLinkingLROTask
from ._models_py3 import EntityLinkingResult
from ._models_py3 import EntityLinkingResultDocumentsItem
from ._models_py3 import EntityLinkingTaskParameters
from ._models_py3 import EntityLinkingTaskResult
from ._models_py3 import EntityRecognitionLROResult
from ._models_py3 import Error
from ._models_py3 import ErrorResponse
from ._models_py3 import HealthcareAssertion
from ._models_py3 import HealthcareEntitiesDocumentResult
from ._models_py3 import HealthcareEntity
from ._models_py3 import HealthcareEntityLink
from ._models_py3 import HealthcareLROResult
from ._models_py3 import HealthcareLROTask
from ._models_py3 import HealthcareRelation
from ._models_py3 import HealthcareRelationEntity
from ._models_py3 import HealthcareResult
from ._models_py3 import HealthcareResultDocumentsItem
from ._models_py3 import HealthcareTaskParameters
from ._models_py3 import InnerErrorModel
from ._models_py3 import JobErrors
from ._models_py3 import JobState
from ._models_py3 import KeyPhraseExtractionLROResult
from ._models_py3 import KeyPhraseLROTask
from ._models_py3 import KeyPhraseResult
from ._models_py3 import KeyPhraseResultDocumentsItem
from ._models_py3 import KeyPhraseTaskParameters
from ._models_py3 import KeyPhraseTaskResult
from ._models_py3 import KeyPhrasesDocumentResult
from ._models_py3 import LanguageDetectionAnalysisInput
from ._models_py3 import LanguageDetectionDocumentResult
from ._models_py3 import LanguageDetectionResult
from ._models_py3 import LanguageDetectionTaskParameters
from ._models_py3 import LanguageDetectionTaskResult
from ._models_py3 import LanguageInput
from ._models_py3 import LinkedEntitiesDocumentResult
from ._models_py3 import LinkedEntity
from ._models_py3 import Match
from ._models_py3 import MultiLanguageAnalysisInput
from ._models_py3 import MultiLanguageInput
from ._models_py3 import Pagination
from ._models_py3 import PiiEntitiesDocumentResult
from ._models_py3 import PiiEntityRecognitionLROResult
from ._models_py3 import PiiLROTask
from ._models_py3 import PiiResult
from ._models_py3 import PiiResultDocumentsItem
from ._models_py3 import PiiTaskParameters
from ._models_py3 import PiiTaskResult
from ._models_py3 import PreBuiltResult
from ._models_py3 import PreBuiltTaskParameters
from ._models_py3 import RequestStatistics
from ._models_py3 import SentenceAssessment
from ._models_py3 import SentenceSentiment
from ._models_py3 import SentenceTarget
from ._models_py3 import SentimentAnalysisLROTask
from ._models_py3 import SentimentAnalysisTaskParameters
from ._models_py3 import SentimentConfidenceScorePerLabel
from ._models_py3 import SentimentDocumentResult
from ._models_py3 import SentimentLROResult
from ._models_py3 import SentimentResponse
from ._models_py3 import SentimentResponseDocumentsItem
from ._models_py3 import SentimentTaskResult
from ._models_py3 import TargetConfidenceScoreLabel
from ._models_py3 import TargetRelation
from ._models_py3 import TaskIdentifier
from ._models_py3 import TaskParameters
from ._models_py3 import TaskState
from ._models_py3 import TasksState
from ._models_py3 import TasksStateTasks


from ._text_analytics_client_enums import AnalyzeTextLROResultsKind
from ._text_analytics_client_enums import AnalyzeTextLROTaskKind
from ._text_analytics_client_enums import AnalyzeTextTaskKind
from ._text_analytics_client_enums import AnalyzeTextTaskResultsKind
from ._text_analytics_client_enums import DocumentSentimentValue
from ._text_analytics_client_enums import EntityAssociation
from ._text_analytics_client_enums import EntityCertainty
from ._text_analytics_client_enums import EntityConditionality
from ._text_analytics_client_enums import ErrorCode
from ._text_analytics_client_enums import HealthcareEntityCategory
from ._text_analytics_client_enums import HealthcareEntityRelation
from ._text_analytics_client_enums import InnerErrorCode
from ._text_analytics_client_enums import PiiDomain
from ._text_analytics_client_enums import PiiEntityCategory
from ._text_analytics_client_enums import SentenceSentimentValue
from ._text_analytics_client_enums import State
from ._text_analytics_client_enums import StringIndexType
from ._text_analytics_client_enums import TargetRelationType
from ._text_analytics_client_enums import TokenSentimentValue
from ._text_analytics_client_enums import WarningCodeValue
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AnalyzeTextEntityLinkingInput',
    'AnalyzeTextEntityRecognitionInput',
    'AnalyzeTextJobState',
    'AnalyzeTextJobStatistics',
    'AnalyzeTextJobsInput',
    'AnalyzeTextKeyPhraseExtractionInput',
    'AnalyzeTextLROResult',
    'AnalyzeTextLROTask',
    'AnalyzeTextLanguageDetectionInput',
    'AnalyzeTextPiiEntitiesRecognitionInput',
    'AnalyzeTextSentimentAnalysisInput',
    'AnalyzeTextTask',
    'AnalyzeTextTaskResult',
    'ClassificationDocumentResult',
    'ClassificationResult',
    'CustomEntitiesLROTask',
    'CustomEntitiesResult',
    'CustomEntitiesResultDocumentsItem',
    'CustomEntitiesTaskParameters',
    'CustomEntityRecognitionLROResult',
    'CustomLabelClassificationResult',
    'CustomLabelClassificationResultDocumentsItem',
    'CustomMultiLabelClassificationLROResult',
    'CustomMultiLabelClassificationLROTask',
    'CustomMultiLabelClassificationTaskParameters',
    'CustomResult',
    'CustomSingleLabelClassificationLROResult',
    'CustomSingleLabelClassificationLROTask',
    'CustomSingleLabelClassificationTaskParameters',
    'CustomTaskParameters',
    'DetectedLanguage',
    'DocumentError',
    'DocumentResult',
    'DocumentStatistics',
    'DocumentWarning',
    'EntitiesDocumentResult',
    'EntitiesLROTask',
    'EntitiesResult',
    'EntitiesResultDocumentsItem',
    'EntitiesTaskParameters',
    'EntitiesTaskResult',
    'Entity',
    'EntityLinkingLROResult',
    'EntityLinkingLROTask',
    'EntityLinkingResult',
    'EntityLinkingResultDocumentsItem',
    'EntityLinkingTaskParameters',
    'EntityLinkingTaskResult',
    'EntityRecognitionLROResult',
    'Error',
    'ErrorResponse',
    'HealthcareAssertion',
    'HealthcareEntitiesDocumentResult',
    'HealthcareEntity',
    'HealthcareEntityLink',
    'HealthcareLROResult',
    'HealthcareLROTask',
    'HealthcareRelation',
    'HealthcareRelationEntity',
    'HealthcareResult',
    'HealthcareResultDocumentsItem',
    'HealthcareTaskParameters',
    'InnerErrorModel',
    'JobErrors',
    'JobState',
    'KeyPhraseExtractionLROResult',
    'KeyPhraseLROTask',
    'KeyPhraseResult',
    'KeyPhraseResultDocumentsItem',
    'KeyPhraseTaskParameters',
    'KeyPhraseTaskResult',
    'KeyPhrasesDocumentResult',
    'LanguageDetectionAnalysisInput',
    'LanguageDetectionDocumentResult',
    'LanguageDetectionResult',
    'LanguageDetectionTaskParameters',
    'LanguageDetectionTaskResult',
    'LanguageInput',
    'LinkedEntitiesDocumentResult',
    'LinkedEntity',
    'Match',
    'MultiLanguageAnalysisInput',
    'MultiLanguageInput',
    'Pagination',
    'PiiEntitiesDocumentResult',
    'PiiEntityRecognitionLROResult',
    'PiiLROTask',
    'PiiResult',
    'PiiResultDocumentsItem',
    'PiiTaskParameters',
    'PiiTaskResult',
    'PreBuiltResult',
    'PreBuiltTaskParameters',
    'RequestStatistics',
    'SentenceAssessment',
    'SentenceSentiment',
    'SentenceTarget',
    'SentimentAnalysisLROTask',
    'SentimentAnalysisTaskParameters',
    'SentimentConfidenceScorePerLabel',
    'SentimentDocumentResult',
    'SentimentLROResult',
    'SentimentResponse',
    'SentimentResponseDocumentsItem',
    'SentimentTaskResult',
    'TargetConfidenceScoreLabel',
    'TargetRelation',
    'TaskIdentifier',
    'TaskParameters',
    'TaskState',
    'TasksState',
    'TasksStateTasks',
    'AnalyzeTextLROResultsKind',
    'AnalyzeTextLROTaskKind',
    'AnalyzeTextTaskKind',
    'AnalyzeTextTaskResultsKind',
    'DocumentSentimentValue',
    'EntityAssociation',
    'EntityCertainty',
    'EntityConditionality',
    'ErrorCode',
    'HealthcareEntityCategory',
    'HealthcareEntityRelation',
    'InnerErrorCode',
    'PiiDomain',
    'PiiEntityCategory',
    'SentenceSentimentValue',
    'State',
    'StringIndexType',
    'TargetRelationType',
    'TokenSentimentValue',
    'WarningCodeValue',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()