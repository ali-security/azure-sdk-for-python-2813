# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
import queue
import time
import re
import json

from typing import List, Union, AsyncIterator, Iterator, cast
from azure.core.rest import HttpResponse, AsyncHttpResponse
from .. import models as _models


class StreamingChatCompletions:
    """Represents an interator over ChatCompletionsUpdate objects. It can be used for either synchronous or
    asynchronous iterations. The class deserializes the Server Sent Events (SSE) response stream
    into chat completions updates, each one represented by a ChatCompletionsUpdate object.
    """

    # Enable console logs for debugging. For development only, will be removed before release.
    ENABLE_CLASS_LOGS = False

    # The prefix of each line in the SSE stream that contains a JSON string
    # to deserialize into a ChatCompletionsUpdate object
    SSE_DATA_EVENT_PREFIX = "data: "

    # The line indicating the end of the SSE stream
    SSE_DATA_EVENT_DONE = "data: [DONE]"

    def __init__(self, response: Union[HttpResponse, AsyncHttpResponse]):
        self._response = response
        self._bytes_iterator: Union[AsyncIterator[bytes], Iterator[bytes]] = response.iter_bytes()
        self._is_async_iterator = isinstance(self._response, AsyncHttpResponse)
        self._queue: "queue.Queue[_models.ChatCompletionsUpdate]" = queue.Queue()
        self._incomplete_json = ""
        self._done = False  # Will be set to True when reading 'data: [DONE]' line

    def __iter__(self):
        if self._is_async_iterator:
            raise ValueError("This method is not supported for async iterators")
        return self

    def __next__(self) -> _models.ChatCompletionsUpdate:
        if self._is_async_iterator:
            raise ValueError("This method is not supported for async iterators")
        while self._queue.empty() and not self._done:
            self._done = self._read_next_block()
        if self._queue.empty():
            raise StopIteration
        return self._queue.get()

    def _read_next_block(self) -> bool:
        try:
            # Use 'cast' to make 'pyright' error go away
            element = cast(Iterator[bytes], self._bytes_iterator).__next__()
        except StopIteration:
            self.close()
            return True
        return self._deserialize_and_add_to_queue(element)

    def __aiter__(self):
        if not self._is_async_iterator:
            raise ValueError("This method is only supported for async iterators")
        return self

    async def __anext__(self) -> _models.ChatCompletionsUpdate:
        if not self._is_async_iterator:
            raise ValueError("This method is only supported for async iterators")
        while self._queue.empty() and not self._done:
            self._done = await self._read_next_block_async()
        if self._queue.empty():
            raise StopAsyncIteration
        return self._queue.get()

    async def _read_next_block_async(self) -> bool:
        try:
            # Use 'cast' to make 'pyright' error go away
            element = await cast(AsyncIterator[bytes], self._bytes_iterator).__anext__()
        except StopAsyncIteration:
            await self.aclose()
            return True
        return self._deserialize_and_add_to_queue(element)

    def _deserialize_and_add_to_queue(self, element: bytes) -> bool:

        # Clear the queue of ChatCompletionsUpdate before processing the next block
        self._queue.queue.clear()

        # Convert `bytes` to string and split the string by newline, while keeping the new line char.
        # the last may be a partial "line" that does not contain a newline char at the end.
        line_list: List[str] = re.split(r"(?<=\n)", element.decode("utf-8"))
        for index, line in enumerate(line_list):

            if self.ENABLE_CLASS_LOGS:
                print(f"[original] {repr(line)}")

            if index == 0:
                line = self._incomplete_json + line
                self._incomplete_json = ""

            if index == len(line_list) - 1 and not line.endswith("\n"):
                self._incomplete_json = line
                return False

            if self.ENABLE_CLASS_LOGS:
                print(f"[modified] {repr(line)}")

            if line == "\n":  # Empty line, indicating flush output to client
                continue

            if not line.startswith(self.SSE_DATA_EVENT_PREFIX):
                raise ValueError(f"SSE event not supported (line `{line}`)")

            if line.startswith(self.SSE_DATA_EVENT_DONE):
                if self.ENABLE_CLASS_LOGS:
                    print("done]")
                return True

            # If you reached here, the line should contain `data: {...}\n`
            # where the curly braces contain a valid JSON object. Deserialize it into a ChatCompletionsUpdate object
            # and add it to the queue.
            self._queue.put(
                # pylint: disable=W0212 # Access to a protected member _deserialize of a client class
                _models.ChatCompletionsUpdate._deserialize(json.loads(line[len(self.SSE_DATA_EVENT_PREFIX) : -1]), [])
            )

            if self.ENABLE_CLASS_LOGS:
                print("[added]")

        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def close(self) -> None:
        if isinstance(self._response, HttpResponse):
            self._response.close()

    async def aclose(self) -> None:
        # `if`` statement added to avoid mypy error: Incompatible types in "await" (actual type "Optional[Coroutine[Any, Any, None]]", expected type "Awaitable[Any]")
        if isinstance(self._response, AsyncHttpResponse):
            await self._response.close()


__all__: List[str] = [
    "StreamingChatCompletions"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
