# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import abc
import copy
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Iterable, Iterator,
    Optional,
    Union,
    MutableMapping,
)

from ..utils._utils import _case_insensitive_dict

from ._helpers import (
    ParamsType,
    FilesType,
    set_json_body,
    set_multipart_body,
    set_urlencoded_body,
    _format_parameters_helper,
    HttpRequestBackcompatMixin,
)
from ._helpers_py3 import set_content_body

ContentType = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]

################################## CLASSES ######################################

class HttpRequest(HttpRequestBackcompatMixin):
    """**Provisional** object that represents an HTTP request.

    **This object is provisional**, meaning it may be changed in a future release.

    It should be passed to your client's `send_request` method.

    >>> from azure.core.rest import HttpRequest
    >>> request = HttpRequest('GET', 'http://www.example.com')
    <HttpRequest [GET], url: 'http://www.example.com'>
    >>> response = client.send_request(request)
    <HttpResponse: 200 OK>

    :param str method: HTTP method (GET, HEAD, etc.)
    :param str url: The url for your request
    :keyword mapping params: Query parameters to be mapped into your URL. Your input
     should be a mapping of query name to query value(s).
    :keyword mapping headers: HTTP headers you want in your request. Your input should
     be a mapping of header name to header value.
    :keyword any json: A JSON serializable object. We handle JSON-serialization for your
     object, so use this for more complicated data structures than `data`.
    :keyword content: Content you want in your request body. Think of it as the kwarg you should input
     if your data doesn't fit into `json`, `data`, or `files`. Accepts a bytes type, or a generator
     that yields bytes.
    :paramtype content: str or bytes or iterable[bytes] or asynciterable[bytes]
    :keyword dict data: Form data you want in your request body. Use for form-encoded data, i.e.
     HTML forms.
    :keyword mapping files: Files you want to in your request body. Use for uploading files with
     multipart encoding. Your input should be a mapping of file name to file content.
     Use the `data` kwarg in addition if you want to include non-file data files as part of your request.
    :ivar str url: The URL this request is against.
    :ivar str method: The method type of this request.
    :ivar mapping headers: The HTTP headers you passed in to your request
    :ivar any content: The content passed in for the request
    """

    def __init__(
        self,
        method: str,
        url: str,
        *,
        params: Optional[ParamsType] = None,
        headers: Optional[MutableMapping[str, str]] = None,
        json: Any = None,
        content: Optional[ContentType] = None,
        data: Optional[dict] = None,
        files: Optional[FilesType] = None,
        **kwargs
    ):
        self.url = url
        self.method = method

        if params:
            _format_parameters_helper(self, params)
        self._files = None
        self._data = None  # type: Any

        default_headers = self._set_body(
            content=content,
            data=data,
            files=files,
            json=json,
        )
        self.headers = _case_insensitive_dict(default_headers)
        self.headers.update(headers or {})

        if kwargs:
            raise TypeError(
                "You have passed in kwargs '{}' that are not valid kwargs.".format(
                    "', '".join(list(kwargs.keys()))
                )
            )

    def _set_body(
        self,
        content: Optional[ContentType] = None,
        data: Optional[dict] = None,
        files: Optional[FilesType] = None,
        json: Any = None,
    ) -> MutableMapping[str, str]:
        """Sets the body of the request, and returns the default headers
        """
        default_headers = {}  # type: MutableMapping[str, str]
        if data is not None and not isinstance(data, dict):
            # should we warn?
            content = data
        if content is not None:
            default_headers, self._data = set_content_body(content)
            return default_headers
        if json is not None:
            default_headers, self._data = set_json_body(json)
            return default_headers
        if files:
            default_headers, self._files = set_multipart_body(files)
        if data:
            default_headers, self._data = set_urlencoded_body(data, has_files=bool(files))
        return default_headers

    @property
    def content(self) -> Any:
        """Get's the request's content

        :return: The request's content
        :rtype: any
        """
        return self._data or self._files

    def __repr__(self) -> str:
        return "<HttpRequest [{}], url: '{}'>".format(
            self.method, self.url
        )

    def __deepcopy__(self, memo=None) -> "HttpRequest":
        try:
            request = HttpRequest(
                method=self.method,
                url=self.url,
                headers=self.headers,
            )
            request._data = copy.deepcopy(self._data, memo)
            request._files = copy.deepcopy(self._files, memo)
            self._add_backcompat_properties(request, memo)
            return request
        except (ValueError, TypeError):
            return copy.copy(self)

class _HttpResponseBase(abc.ABC):
    """Base abstract base class for HttpResponses.
    """

    @property
    @abc.abstractmethod
    def request(self) -> HttpRequest:
        """The request that resulted in this response.

        :rtype: ~azure.core.rest.HttpRequest
        """
        ...

    @property
    @abc.abstractmethod
    def status_code(self) -> int:
        """The status code of this response.

        :rtype: int
        """
        ...

    @property
    @abc.abstractmethod
    def headers(self) -> MutableMapping[str, str]:
        """The response headers. Must be case-insensitive.

        :rtype: MutableMapping[str, str]
        """
        ...

    @property
    @abc.abstractmethod
    def reason(self) -> str:
        """The reason phrase for this response.

        :rtype: str
        """
        ...

    @property
    @abc.abstractmethod
    def content_type(self) -> Optional[str]:
        """The content type of the response.

        :rtype: str
        """
        ...

    @property
    @abc.abstractmethod
    def is_closed(self) -> bool:
        """Whether the network connection has been closed yet.

        :rtype: bool
        """
        ...

    @property
    @abc.abstractmethod
    def is_stream_consumed(self) -> bool:
        """Whether the stream has been consumed.

        :rtype: bool
        """
        ...

    @property
    @abc.abstractmethod
    def encoding(self) -> Optional[str]:
        """Returns the response encoding.

        :return: The response encoding. We either return the encoding set by the user,
         or try extracting the encoding from the response's content type. If all fails,
         we return `None`.
        :rtype: optional[str]
        """
        ...

    @encoding.setter
    def encoding(self, value: Optional[str]) -> None:
        """Sets the response encoding.

        :rtype: None
        """

    @property
    @abc.abstractmethod
    def url(self) -> str:
        """The URL that resulted in this response.

        :rtype: str
        """
        ...

    @property
    @abc.abstractmethod
    def content(self) -> bytes:
        """Return the response's content in bytes.

        :rtype: bytes
        """
        ...

    @abc.abstractmethod
    def text(self, encoding: Optional[str] = None) -> str:
        """Returns the response body as a string.

        :param optional[str] encoding: The encoding you want to decode the text with. Can
         also be set independently through our encoding property
        :return: The response's content decoded as a string.
        :rtype: str
        """
        ...

    @abc.abstractmethod
    def json(self) -> Any:
        """Returns the whole body as a json object.

        :return: The JSON deserialized response body
        :rtype: any
        :raises json.decoder.JSONDecodeError or ValueError (in python 2.7) if object is not JSON decodable:
        """
        ...

    @abc.abstractmethod
    def raise_for_status(self) -> None:
        """Raises an HttpResponseError if the response has an error status code.

        If response is good, does nothing.

        :rtype: None
        :raises ~azure.core.HttpResponseError if the object has an error status code.:
        """
        ...

class HttpResponse(_HttpResponseBase):
    """**Provisional** abstract base class for HTTP responses.

    **This object is provisional**, meaning it may be changed in a future release.
    Use this abstract base class to create your own transport responses.

    Responses implementing this ABC are returned from your client's `send_request` method
    if you pass in an :class:`~azure.core.rest.HttpRequest`

    >>> from azure.core.rest import HttpRequest
    >>> request = HttpRequest('GET', 'http://www.example.com')
    <HttpRequest [GET], url: 'http://www.example.com'>
    >>> response = client.send_request(request)
    <HttpResponse: 200 OK>
    """

    @abc.abstractmethod
    def __enter__(self) -> "HttpResponse":
        ...

    @abc.abstractmethod
    def __exit__(self, *args) -> None:
        ...

    @abc.abstractmethod
    def close(self) -> None:
        ...

    @abc.abstractmethod
    def read(self) -> bytes:
        """Read the response's bytes.

        :return: The read in bytes
        :rtype: bytes
        """
        ...

    @abc.abstractmethod
    def iter_raw(self, **kwargs: Any) -> Iterator[bytes]:
        """Iterates over the response's bytes. Will not decompress in the process.

        :return: An iterator of bytes from the response
        :rtype: Iterator[str]
        """
        ...

    @abc.abstractmethod
    def iter_bytes(self, **kwargs: Any) -> Iterator[bytes]:
        """Iterates over the response's bytes. Will decompress in the process.

        :return: An iterator of bytes from the response
        :rtype: Iterator[str]
        """
        ...

    def __repr__(self) -> str:
        content_type_str = (
            ", Content-Type: {}".format(self.content_type) if self.content_type else ""
        )
        return "<HttpResponse: {} {}{}>".format(
            self.status_code, self.reason, content_type_str
        )

class AsyncHttpResponse(_HttpResponseBase):
    """**Provisional** abstract base class for Async HTTP responses.

    **This object is provisional**, meaning it may be changed in a future release.
    Use this abstract base class to create your own transport responses.

    Responses implementing this ABC are returned from your async client's `send_request`
    method if you pass in an :class:`~azure.core.rest.HttpRequest`

    >>> from azure.core.rest import HttpRequest
    >>> request = HttpRequest('GET', 'http://www.example.com')
    <HttpRequest [GET], url: 'http://www.example.com'>
    >>> response = await client.send_request(request)
    <AsyncHttpResponse: 200 OK>
    """

    @abc.abstractmethod
    async def read(self) -> bytes:
        """Read the response's bytes into memory.

        :return: The response's bytes
        :rtype: bytes
        """
        ...

    @abc.abstractmethod
    async def iter_raw(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """Asynchronously iterates over the response's bytes. Will not decompress in the process.

        :return: An async iterator of bytes from the response
        :rtype: AsyncIterator[bytes]
        """
        raise NotImplementedError()
        # getting around mypy behavior, see https://github.com/python/mypy/issues/10732
        yield  # pylint: disable=unreachable

    @abc.abstractmethod
    async def iter_bytes(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """Asynchronously iterates over the response's bytes. Will decompress in the process.

        :return: An async iterator of bytes from the response
        :rtype: AsyncIterator[bytes]
        """
        raise NotImplementedError()
        # getting around mypy behavior, see https://github.com/python/mypy/issues/10732
        yield  # pylint: disable=unreachable

    @abc.abstractmethod
    async def close(self) -> None:
        ...

    @abc.abstractmethod
    async def __aexit__(self, *args) -> None:
        ...
