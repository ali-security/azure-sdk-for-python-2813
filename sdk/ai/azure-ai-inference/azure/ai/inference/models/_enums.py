# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CapacityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether your capacity has been affected by the usage amount (token count) reported here."""

    USAGE = "usage"
    """Your capacity has been affected by the usage amount (token count) reported here."""
    FIXED = "fixed"
    """Your capacity has not been affected by the usage amount (token count) reported here."""


class ChatCompletionsResponseFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An representation of a response format configuration usable by Chat Completions. Can be used to
    enable JSON
    mode.
    """

    TEXT = "text"
    """The standard Chat Completions response format that can freely generate text and is not
    guaranteed to produce response
    content that adheres to a specific schema."""
    JSON_OBJECT = "json_object"
    """A response format for Chat Completions that restricts responses to emitting valid JSON objects."""


class ChatCompletionsToolSelectionPreset(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents a generic policy for how a chat completions tool may be selected."""

    AUTO = "auto"
    """Specifies that the model may either use any of the tools provided in this chat completions
    request or
    instead return a standard chat completions response as if no tools were provided."""
    NONE = "none"
    """Specifies that the model should not respond with a tool call and should instead provide a
    standard chat
    completions response. Response content may still be influenced by the provided tool
    definitions."""


class ChatRole(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A description of the intended purpose of a message within a chat completions interaction."""

    SYSTEM = "system"
    """The role that instructs or sets the behavior of the assistant."""
    USER = "user"
    """The role that provides input for chat completions."""
    ASSISTANT = "assistant"
    """The role that provides responses to system-instructed, user-prompted input."""
    TOOL = "tool"
    """The role that represents extension tool activity within a chat completions operation."""


class CompletionsFinishReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Representation of the manner in which a completions response concluded."""

    STOPPED = "stop"
    """Completions ended normally and reached its end of token generation."""
    TOKEN_LIMIT_REACHED = "length"
    """Completions exhausted available token limits before generation could complete."""
    CONTENT_FILTERED = "content_filter"
    """Completions generated a response that was identified as potentially sensitive per content
    moderation policies."""
    TOOL_CALLS = "tool_calls"
    """Completion ended with the model calling a provided tool for output."""


class EmbeddingInputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the input types used for embedding search."""

    TEXT = "text"
    """to do"""
    QUERY = "query"
    """to do"""
    DOCUMENT = "document"
    """to do"""


class ImageGenerationQuality(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An image generation configuration that specifies how the model should prioritize quality, cost,
    and speed.
    """

    STANDARD = "standard"
    """Requests image generation with standard, balanced characteristics of quality, cost, and speed."""
    HD = "hd"
    """Requests image generation with higher quality, higher cost and lower speed relative to
    standard."""


class ImageGenerationResponseFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format in which the generated images are returned."""

    URL = "url"
    """Image generation response items should provide a URL from which the image may be retrieved."""
    BASE64 = "b64_json"
    """Image generation response items should provide image data as a base64-encoded string."""


class ModelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of AI model."""

    EMBEDDINGS = "embeddings"
    """Embeddings."""
    IMAGE_GENERATION = "image_generation"
    """Image generation."""
    TEXT_GENERATION = "text_generation"
    """Text generation"""
    IMAGE_EMBEDDINGS = "image_embeddings"
    """Image embeddings."""
    AUDIO_GENERATION = "audio_generation"
    """Audio generation"""
    CHAT = "chat"
    """Chat completions"""
