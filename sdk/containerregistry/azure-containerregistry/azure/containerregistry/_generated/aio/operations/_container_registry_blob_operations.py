# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.2.4, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ContainerRegistryBlobOperations:
    """ContainerRegistryBlobOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~container_registry.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_blob(
        self,
        name: str,
        digest: str,
        **kwargs
    ) -> Optional[IO]:
        """Retrieve the blob from the registry identified by digest.

        :param name: Name of the image (including the namespace).
        :type name: str
        :param digest: Digest of a BLOB.
        :type digest: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[IO]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream"

        # Construct URL
        url = self.get_blob.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            response_headers['Content-Length']=self._deserialize('long', response.headers.get('Content-Length'))
            response_headers['Docker-Content-Digest']=self._deserialize('str', response.headers.get('Docker-Content-Digest'))
            deserialized = response.stream_download(self._client._pipeline)

        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_blob.metadata = {'url': '/v2/{name}/blobs/{digest}'}  # type: ignore

    async def check_blob_exists(
        self,
        name: str,
        digest: str,
        **kwargs
    ) -> None:
        """Same as GET, except only the headers are returned.

        :param name: Name of the image (including the namespace).
        :type name: str
        :param digest: Digest of a BLOB.
        :type digest: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.check_blob_exists.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 200:
            response_headers['Content-Length']=self._deserialize('long', response.headers.get('Content-Length'))
            response_headers['Docker-Content-Digest']=self._deserialize('str', response.headers.get('Docker-Content-Digest'))

        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    check_blob_exists.metadata = {'url': '/v2/{name}/blobs/{digest}'}  # type: ignore

    async def delete_blob(
        self,
        name: str,
        digest: str,
        **kwargs
    ) -> IO:
        """Removes an already uploaded blob.

        :param name: Name of the image (including the namespace).
        :type name: str
        :param digest: Digest of a BLOB.
        :type digest: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream"

        # Construct URL
        url = self.delete_blob.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Docker-Content-Digest']=self._deserialize('str', response.headers.get('Docker-Content-Digest'))
        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    delete_blob.metadata = {'url': '/v2/{name}/blobs/{digest}'}  # type: ignore

    async def mount_blob(
        self,
        name: str,
        from_parameter: str,
        mount: str,
        **kwargs
    ) -> None:
        """Mount a blob identified by the ``mount`` parameter from another repository.

        :param name: Name of the image (including the namespace).
        :type name: str
        :param from_parameter: Name of the source repository.
        :type from_parameter: str
        :param mount: Digest of blob to mount from the source repository.
        :type mount: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.mount_blob.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['from'] = self._serialize.query("from_parameter", from_parameter, 'str')
        query_parameters['mount'] = self._serialize.query("mount", mount, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Docker-Upload-UUID']=self._deserialize('str', response.headers.get('Docker-Upload-UUID'))
        response_headers['Docker-Content-Digest']=self._deserialize('str', response.headers.get('Docker-Content-Digest'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    mount_blob.metadata = {'url': '/v2/{name}/blobs/uploads/'}  # type: ignore

    async def get_upload_status(
        self,
        location: str,
        **kwargs
    ) -> None:
        """Retrieve status of upload identified by uuid. The primary purpose of this endpoint is to
        resolve the current status of a resumable upload.

        :param location: Link acquired from upload start or previous chunk. Note, do not include
         initial / (must do substring(1) ).
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_upload_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Range']=self._deserialize('str', response.headers.get('Range'))
        response_headers['Docker-Upload-UUID']=self._deserialize('str', response.headers.get('Docker-Upload-UUID'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get_upload_status.metadata = {'url': '/{nextBlobUuidLink}'}  # type: ignore

    async def upload_chunk(
        self,
        location: str,
        value: IO,
        **kwargs
    ) -> None:
        """Upload a stream of data without completing the upload.

        :param location: Link acquired from upload start or previous chunk. Note, do not include
         initial / (must do substring(1) ).
        :type location: str
        :param value: Raw data of blob.
        :type value: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/json"

        # Construct URL
        url = self.upload_chunk.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['stream_content'] = value
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Range']=self._deserialize('str', response.headers.get('Range'))
        response_headers['Docker-Upload-UUID']=self._deserialize('str', response.headers.get('Docker-Upload-UUID'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    upload_chunk.metadata = {'url': '/{nextBlobUuidLink}'}  # type: ignore

    async def complete_upload(
        self,
        digest: str,
        location: str,
        value: Optional[IO] = None,
        **kwargs
    ) -> None:
        """Complete the upload, providing all the data in the body, if necessary. A request without a body
        will just complete the upload with previously uploaded content.

        :param digest: Digest of a BLOB.
        :type digest: str
        :param location: Link acquired from upload start or previous chunk. Note, do not include
         initial / (must do substring(1) ).
        :type location: str
        :param value: Optional raw data of blob.
        :type value: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/json"

        # Construct URL
        url = self.complete_upload.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['digest'] = self._serialize.query("digest", digest, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['stream_content'] = value
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Range']=self._deserialize('str', response.headers.get('Range'))
        response_headers['Docker-Content-Digest']=self._deserialize('str', response.headers.get('Docker-Content-Digest'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    complete_upload.metadata = {'url': '/{nextBlobUuidLink}'}  # type: ignore

    async def cancel_upload(
        self,
        location: str,
        **kwargs
    ) -> None:
        """Cancel outstanding upload processes, releasing associated resources. If this is not called, the
        unfinished uploads will eventually timeout.

        :param location: Link acquired from upload start or previous chunk. Note, do not include
         initial / (must do substring(1) ).
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.cancel_upload.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'nextBlobUuidLink': self._serialize.url("location", location, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_upload.metadata = {'url': '/{nextBlobUuidLink}'}  # type: ignore

    async def start_upload(
        self,
        name: str,
        **kwargs
    ) -> None:
        """Initiate a resumable blob upload with an empty request body.

        :param name: Name of the image (including the namespace).
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.start_upload.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Range']=self._deserialize('str', response.headers.get('Range'))
        response_headers['Docker-Upload-UUID']=self._deserialize('str', response.headers.get('Docker-Upload-UUID'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    start_upload.metadata = {'url': '/v2/{name}/blobs/uploads/'}  # type: ignore

    async def get_chunk(
        self,
        name: str,
        digest: str,
        range: str,
        **kwargs
    ) -> IO:
        """Retrieve the blob from the registry identified by ``digest``. This endpoint may also support
        RFC7233 compliant range requests. Support can be detected by issuing a HEAD request. If the
        header ``Accept-Range: bytes`` is returned, range requests can be used to fetch partial
        content.

        :param name: Name of the image (including the namespace).
        :type name: str
        :param digest: Digest of a BLOB.
        :type digest: str
        :param range: Format : bytes=:code:`<start>`-:code:`<end>`,  HTTP Range header specifying blob
         chunk.
        :type range: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream"

        # Construct URL
        url = self.get_chunk.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Range'] = self._serialize.header("range", range, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [206]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Content-Length']=self._deserialize('long', response.headers.get('Content-Length'))
        response_headers['Content-Range']=self._deserialize('str', response.headers.get('Content-Range'))
        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_chunk.metadata = {'url': '/v2/{name}/blobs/{digest}'}  # type: ignore

    async def check_chunk_exists(
        self,
        name: str,
        digest: str,
        range: str,
        **kwargs
    ) -> None:
        """Same as GET, except only the headers are returned.

        :param name: Name of the image (including the namespace).
        :type name: str
        :param digest: Digest of a BLOB.
        :type digest: str
        :param range: Format : bytes=:code:`<start>`-:code:`<end>`,  HTTP Range header specifying blob
         chunk.
        :type range: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.check_chunk_exists.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'digest': self._serialize.url("digest", digest, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Range'] = self._serialize.header("range", range, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Content-Length']=self._deserialize('long', response.headers.get('Content-Length'))
        response_headers['Content-Range']=self._deserialize('str', response.headers.get('Content-Range'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    check_chunk_exists.metadata = {'url': '/v2/{name}/blobs/{digest}'}  # type: ignore
