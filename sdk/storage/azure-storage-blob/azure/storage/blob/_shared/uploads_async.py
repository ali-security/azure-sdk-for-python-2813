# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import asyncio
import inspect
import threading
from asyncio import Lock
from io import UnsupportedOperation
from itertools import islice
from math import ceil
from typing import AsyncGenerator, Union

from . import encode_base64, url_quote
from .request_handlers import get_length
from .response_handlers import return_response_headers
from .uploads import ChunkInfo, SubStream, IterStreamer  # pylint: disable=unused-import


async def _async_parallel_uploads(uploader, pending, running):
    range_ids = []
    while True:
        # Wait for some download to finish before adding a new one
        done, running = await asyncio.wait(running, return_when=asyncio.FIRST_COMPLETED)
        range_ids.extend([chunk.result() for chunk in done])
        try:
            for _ in range(0, len(done)):
                next_chunk = await pending.__anext__()
                running.add(asyncio.ensure_future(uploader(next_chunk)))
        except StopAsyncIteration:
            break

    # Wait for the remaining uploads to finish
    if running:
        done, _running = await asyncio.wait(running)
        range_ids.extend([chunk.result() for chunk in done])
    return range_ids


async def _parallel_uploads(uploader, pending, running):
    range_ids = []
    while True:
        # Wait for some download to finish before adding a new one
        done, running = await asyncio.wait(running, return_when=asyncio.FIRST_COMPLETED)
        range_ids.extend([chunk.result() for chunk in done])
        try:
            for _ in range(0, len(done)):
                next_chunk = next(pending)
                running.add(asyncio.ensure_future(uploader(next_chunk)))
        except StopIteration:
            break

    # Wait for the remaining uploads to finish
    if running:
        done, _running = await asyncio.wait(running)
        range_ids.extend([chunk.result() for chunk in done])
    return range_ids


async def upload_data_chunks(
        service=None,
        uploader_class=None,
        total_size=None,
        chunk_size=None,
        max_concurrency=None,
        stream=None,
        progress_hook=None,
        **kwargs):

    parallel = max_concurrency > 1
    if parallel and 'modified_access_conditions' in kwargs:
        # Access conditions do not work with parallelism
        kwargs['modified_access_conditions'] = None

    uploader = uploader_class(
        service=service,
        total_size=total_size,
        chunk_size=chunk_size,
        stream=stream,
        parallel=parallel,
        progress_hook=progress_hook,
        **kwargs)

    if parallel:
        upload_tasks = uploader.get_chunk_streams()
        running_futures = []
        for _ in range(max_concurrency):
            try:
                chunk = await upload_tasks.__anext__()
                running_futures.append(asyncio.ensure_future(uploader.process_chunk(chunk)))
            except StopAsyncIteration:
                break

        range_ids = await _async_parallel_uploads(uploader.process_chunk, upload_tasks, running_futures)
    else:
        range_ids = []
        async for chunk in uploader.get_chunk_streams():
            range_ids.append(await uploader.process_chunk(chunk))

    if any(range_ids):
        return [r[1] for r in sorted(range_ids, key=lambda r: r[0])]
    return uploader.response_headers


async def upload_substream_blocks(
        service=None,
        uploader_class=None,
        total_size=None,
        chunk_size=None,
        max_concurrency=None,
        stream=None,
        progress_hook=None,
        **kwargs):
    parallel = max_concurrency > 1
    if parallel and 'modified_access_conditions' in kwargs:
        # Access conditions do not work with parallelism
        kwargs['modified_access_conditions'] = None
    uploader = uploader_class(
        service=service,
        total_size=total_size,
        chunk_size=chunk_size,
        stream=stream,
        parallel=parallel,
        progress_hook=progress_hook,
        **kwargs)

    if parallel:
        upload_tasks = uploader.get_substream_blocks()
        running_futures = [
            asyncio.ensure_future(uploader.process_substream_block(u))
            for u in islice(upload_tasks, 0, max_concurrency)
        ]
        range_ids = await _parallel_uploads(uploader.process_substream_block, upload_tasks, running_futures)
    else:
        range_ids = []
        for block in uploader.get_substream_blocks():
            range_ids.append(await uploader.process_substream_block(block))
    if any(range_ids):
        return sorted(range_ids)
    return


class _ChunkUploader(object):  # pylint: disable=too-many-instance-attributes

    def __init__(
            self, service,
            total_size,
            chunk_size,
            stream,
            parallel,
            encryptor=None,
            padder=None,
            progress_hook=None,
            validate_content=None,
            **kwargs):
        self.service = service
        self.total_size = total_size
        self.chunk_size = chunk_size
        self.stream = stream
        self.parallel = parallel
        self.validate_content = validate_content

        # Stream management
        self.stream_lock = threading.Lock() if parallel else None

        # Progress feedback
        self.progress_total = 0
        self.progress_lock = Lock() if parallel else None
        self.progress_hook = progress_hook

        # Encryption
        self.encryptor = encryptor
        self.padder = padder
        self.response_headers = None
        self.etag = None
        self.last_modified = None
        self.request_options = kwargs
        # Legacy support for bool - Pass True through to pipeline
        self.request_options['validate_content'] = self.validate_content if self.validate_content is True else None

    async def get_chunk_streams(self):
        index = 0
        while True:
            data = b''
            read_size = self.chunk_size

            # Buffer until we either reach the end of the stream or get a whole chunk.
            while True:
                if self.total_size:
                    read_size = min(self.chunk_size - len(data), self.total_size - (index + len(data)))
                temp = self.stream.read(read_size)
                if inspect.isawaitable(temp):
                    temp = await temp
                if not isinstance(temp, bytes):
                    raise TypeError('Blob data should be of type bytes.')
                data += temp or b""

                # We have read an empty string and so are at the end
                # of the buffer or we have read a full chunk.
                if temp == b'' or len(data) == self.chunk_size:
                    break

            if len(data) == self.chunk_size:
                if self.padder:
                    data = self.padder.update(data)
                if self.encryptor:
                    data = self.encryptor.update(data)
                yield ChunkInfo(index, data, self.validate_content)
            else:
                if self.padder:
                    data = self.padder.update(data) + self.padder.finalize()
                if self.encryptor:
                    data = self.encryptor.update(data) + self.encryptor.finalize()
                if data:
                    yield ChunkInfo(index, data, self.validate_content)
                break
            index += len(data)

    async def process_chunk(self, chunk_info):
        range_id = await self._upload_chunk(chunk_info)
        await self._update_progress(chunk_info.length)
        return range_id

    async def _update_progress(self, length):
        if self.progress_lock is not None:
            async with self.progress_lock:
                self.progress_total += length
        else:
            self.progress_total += length

        if self.progress_hook:
            await self.progress_hook(self.progress_total, self.total_size)

    async def _upload_chunk(self, chunk_info):
        raise NotImplementedError("Must be implemented by child class.")

    def get_substream_blocks(self):
        assert self.chunk_size is not None
        lock = self.stream_lock
        blob_length = self.total_size

        if blob_length is None:
            blob_length = get_length(self.stream)
            if blob_length is None:
                raise ValueError("Unable to determine content length of upload data.")

        blocks = int(ceil(blob_length / (self.chunk_size * 1.0)))
        last_block_size = self.chunk_size if blob_length % self.chunk_size == 0 else blob_length % self.chunk_size

        for i in range(blocks):
            index = i * self.chunk_size
            length = last_block_size if i == blocks - 1 else self.chunk_size
            yield index, SubStream(self.stream, index, length, lock)

    async def process_substream_block(self, block_data):
        return await self._upload_substream_block_with_progress(block_data[0], block_data[1])

    async def _upload_substream_block(self, index, block_stream):
        raise NotImplementedError("Must be implemented by child class.")

    async def _upload_substream_block_with_progress(self, index, block_stream):
        range_id = await self._upload_substream_block(index, block_stream)
        await self._update_progress(len(block_stream))
        return range_id

    def set_response_properties(self, resp):
        self.etag = resp.etag
        self.last_modified = resp.last_modified


class BlockBlobChunkUploader(_ChunkUploader):

    def __init__(self, *args, **kwargs):
        kwargs.pop('modified_access_conditions', None)
        super(BlockBlobChunkUploader, self).__init__(*args, **kwargs)
        self.current_length = None

    async def _upload_chunk(self, chunk_info):
        # TODO: This is incorrect, but works with recording.
        index = f'{chunk_info.offset:032d}'
        block_id = encode_base64(url_quote(encode_base64(index)))
        await self.service.stage_block(
            block_id,
            chunk_info.length,
            chunk_info.data,
            transactional_content_md5=chunk_info.md5,
            transactional_content_crc64=chunk_info.crc64,
            data_stream_total=self.total_size,
            upload_stream_current=self.progress_total,
            **self.request_options)
        return index, block_id

    async def _upload_substream_block(self, index, block_stream):
        try:
            block_id = f'BlockId{(index//self.chunk_size):05}'
            await self.service.stage_block(
                block_id,
                len(block_stream),
                block_stream,
                data_stream_total=self.total_size,
                upload_stream_current=self.progress_total,
                **self.request_options)
        finally:
            block_stream.close()
        return block_id


class PageBlobChunkUploader(_ChunkUploader):  # pylint: disable=abstract-method

    def _is_chunk_empty(self, chunk_data):
        # read until non-zero byte is encountered
        # if reached the end without returning, then chunk_data is all 0's
        for each_byte in chunk_data:
            if each_byte not in [0, b'\x00']:
                return False
        return True

    async def _upload_chunk(self, chunk_info):
        # avoid uploading the empty pages
        if not self._is_chunk_empty(chunk_info.data):
            chunk_end = chunk_info.offset + chunk_info.length - 1
            content_range = f'bytes={chunk_info.offset}-{chunk_end}'
            self.response_headers = await self.service.upload_pages(
                body=chunk_info.data,
                content_length=chunk_info.length,
                range=content_range,
                transactional_content_md5=chunk_info.md5,
                transactional_content_crc64=chunk_info.crc64,
                cls=return_response_headers,
                data_stream_total=self.total_size,
                upload_stream_current=self.progress_total,
                **self.request_options)

            if not self.parallel and self.request_options.get('modified_access_conditions'):
                self.request_options['modified_access_conditions'].if_match = self.response_headers['etag']

    async def _upload_substream_block(self, index, block_stream):
        pass


class AppendBlobChunkUploader(_ChunkUploader):  # pylint: disable=abstract-method

    def __init__(self, *args, **kwargs):
        super(AppendBlobChunkUploader, self).__init__(*args, **kwargs)
        self.current_length = None

    async def _upload_chunk(self, chunk_info):
        if self.current_length is None:
            self.response_headers = await self.service.append_block(
                body=chunk_info.data,
                content_length=chunk_info.length,
                transactional_content_md5=chunk_info.md5,
                transactional_content_crc64=chunk_info.crc64,
                cls=return_response_headers,
                data_stream_total=self.total_size,
                upload_stream_current=self.progress_total,
                **self.request_options)
            self.current_length = int(self.response_headers['blob_append_offset'])
        else:
            self.request_options['append_position_access_conditions'].append_position = \
                self.current_length + chunk_info.offset
            self.response_headers = await self.service.append_block(
                body=chunk_info.data,
                content_length=chunk_info.length,
                transactional_content_md5=chunk_info.md5,
                transactional_content_crc64=chunk_info.crc64,
                cls=return_response_headers,
                data_stream_total=self.total_size,
                upload_stream_current=self.progress_total,
                **self.request_options)

    async def _upload_substream_block(self, index, block_stream):
        pass


class DataLakeFileChunkUploader(_ChunkUploader):  # pylint: disable=abstract-method

    async def _upload_chunk(self, chunk_info):
        self.response_headers = await self.service.append_data(
            body=chunk_info.data,
            position=chunk_info.offset,
            content_length=chunk_info.length,
            cls=return_response_headers,
            data_stream_total=self.total_size,
            upload_stream_current=self.progress_total,
            **self.request_options
        )

        if not self.parallel and self.request_options.get('modified_access_conditions'):
            self.request_options['modified_access_conditions'].if_match = self.response_headers['etag']

    async def _upload_substream_block(self, index, block_stream):
        try:
            await self.service.append_data(
                body=block_stream,
                position=index,
                content_length=len(block_stream),
                cls=return_response_headers,
                data_stream_total=self.total_size,
                upload_stream_current=self.progress_total,
                **self.request_options
            )
        finally:
            block_stream.close()


class FileChunkUploader(_ChunkUploader):  # pylint: disable=abstract-method

    async def _upload_chunk(self, chunk_info):
        chunk_end = chunk_info.offset + chunk_info.length - 1
        response = await self.service.upload_range(
            chunk_info.data,
            chunk_info.offset,
            chunk_info.length,
            data_stream_total=self.total_size,
            upload_stream_current=self.progress_total,
            **self.request_options
        )
        range_id = f'bytes={chunk_info.offset}-{chunk_end}'
        return range_id, response

    # TODO: Implement this method.
    async def _upload_substream_block(self, index, block_stream):
        pass


class AsyncIterStreamer():
    """
    File-like streaming object for AsyncGenerators.
    """
    def __init__(self, generator: AsyncGenerator[Union[bytes, str], None], encoding: str = "UTF-8"):
        self.iterator = generator.__aiter__()
        self.leftover = b""
        self.encoding = encoding

    def seekable(self):
        return False

    def tell(self, *args, **kwargs):
        raise UnsupportedOperation("Data generator does not support tell.")

    def seek(self, *args, **kwargs):
        raise UnsupportedOperation("Data generator is not seekable.")

    async def read(self, size: int) -> bytes:
        data = self.leftover
        count = len(self.leftover)
        try:
            while count < size:
                chunk = await self.iterator.__anext__()
                if isinstance(chunk, str):
                    chunk = chunk.encode(self.encoding)
                data += chunk
                count += len(chunk)
        # This means count < size and what's leftover will be returned in this call.
        except StopAsyncIteration:
            self.leftover = b""

        if count >= size:
            self.leftover = data[size:]

        return data[:size]
