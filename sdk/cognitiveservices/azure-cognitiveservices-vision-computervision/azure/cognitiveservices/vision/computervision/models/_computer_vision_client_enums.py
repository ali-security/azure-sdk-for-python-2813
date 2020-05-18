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


class Gender(str, Enum):

    male = "Male"
    female = "Female"


class OperationStatusCodes(str, Enum):

    not_started = "notStarted"
    running = "running"
    failed = "failed"
    succeeded = "succeeded"


class TextRecognitionResultDimensionUnit(str, Enum):

    pixel = "pixel"
    inch = "inch"


class DescriptionExclude(str, Enum):

    celebrities = "Celebrities"
    landmarks = "Landmarks"


class OcrLanguages(str, Enum):

    unk = "unk"
    zh_hans = "zh-Hans"
    zh_hant = "zh-Hant"
    cs = "cs"
    da = "da"
    nl = "nl"
    en = "en"
    fi = "fi"
    fr = "fr"
    de = "de"
    el = "el"
    hu = "hu"
    it = "it"
    ja = "ja"
    ko = "ko"
    nb = "nb"
    pl = "pl"
    pt = "pt"
    ru = "ru"
    es = "es"
    sv = "sv"
    tr = "tr"
    ar = "ar"
    ro = "ro"
    sr_cyrl = "sr-Cyrl"
    sr_latn = "sr-Latn"
    sk = "sk"


class VisualFeatureTypes(str, Enum):

    image_type = "ImageType"
    faces = "Faces"
    adult = "Adult"
    categories = "Categories"
    color = "Color"
    tags = "Tags"
    description = "Description"
    objects = "Objects"
    brands = "Brands"


class OcrDetectionLanguage(str, Enum):

    en = "en"
    es = "es"
    fr = "fr"
    de = "de"
    it = "it"
    nl = "nl"
    pt = "pt"


class Details(str, Enum):

    celebrities = "Celebrities"
    landmarks = "Landmarks"
