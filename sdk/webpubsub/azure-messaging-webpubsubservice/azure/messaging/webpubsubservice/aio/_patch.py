# coding=utf-8
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

from typing import TYPE_CHECKING
import importlib

from azure.core import AsyncPipelineClient
from msrest import Deserializer

from .._version import VERSION
from .._patch import JwtCredentialPolicy, ApiManagementProxy, _parse_connection_string, _get_token_by_key
from ._web_pub_sub_service_client import WebPubSubServiceClient as GeneratedWebPubSubServiceClient

from azure.core.configuration import Configuration
from azure.core.pipeline import policies
from azure.core.credentials import AzureKeyCredential
from msrest import Serializer
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict, TypeVar, Type
    ClientType = TypeVar("ClientType", bound="WebPubSubServiceClient")

    from azure.core.credentials_async import AsyncTokenCredential


class WebPubSubServiceClientConfiguration(Configuration):
    """Configuration for WebPubSubServiceClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: HTTP or HTTPS endpoint for the Web PubSub service instance.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: Union[~azure.core.credentials_async.AsyncTokenCredential, ~azure.core.credentials.AzureKeyCredential]
    :keyword api_version: Api Version. The default value is "2021-10-01". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        endpoint: str,
        credential: Union["AsyncTokenCredential", "AzureKeyCredential"],
        **kwargs: Any
    ) -> None:
        super(WebPubSubServiceClientConfiguration, self).__init__(**kwargs)
        api_version = kwargs.pop('api_version', "2021-10-01")  # type: str

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.endpoint = endpoint
        self.credential = credential
        self.api_version = api_version
        self.credential_scopes = kwargs.pop('credential_scopes', ['https://webpubsub.azure.com/.default'])
        kwargs.setdefault('sdk_moniker', 'messaging-webpubsubservice/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or ApiManagementProxy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
        if self.credential and not self.authentication_policy:
            if isinstance(self.credential, AzureKeyCredential):
                self.authentication_policy = JwtCredentialPolicy(self.credential, kwargs.get('user'))
            else:
                self.authentication_policy = policies.AsyncBearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)


class WebPubSubServiceClient(GeneratedWebPubSubServiceClient):
    """WebPubSubServiceClient.

    :param endpoint: HTTP or HTTPS endpoint for the Web PubSub service instance.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. The default value is "2021-10-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        endpoint: str,
        credential: Union["AsyncTokenCredential", "AzureKeyCredential"],
        **kwargs: Any
    ) -> None:
        kwargs['origin_endpoint'] = endpoint
        _endpoint = '{Endpoint}'
        self._config = WebPubSubServiceClientConfiguration(endpoint, credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    @classmethod
    def from_connection_string(cls, connection_string, **kwargs):
        # type: (Type[ClientType], str, Any) -> ClientType
        """Create a new WebPubSubServiceClient from a connection string.
        :param connection_string: Connection string
        :type connection_string: ~str
        :rtype: WebPubSubServiceClient
        """
        kwargs = _parse_connection_string(connection_string, **kwargs)

        credential = AzureKeyCredential(kwargs.pop("accesskey"))
        return cls(credential=credential, **kwargs)

    @distributed_trace_async
    async def get_client_access_token(self, hub, **kwargs):
        # type: (str, Any) -> Dict[Any]
        """Build an authentication token.

        :keyword hub: The hub to give access to.
        :type hub: str
        :keyword user_id: User Id.
        :paramtype user_id: str
        :keyword roles: Roles that the connection with the generated token will have.
        :paramtype roles: list[str]
        :keyword minutes_to_expire: The expire time of the generated token.
        :paramtype minutes_to_expire: int
        :returns: ~dict containing the web socket endpoint, the token and a url with the generated access token.
        :rtype: ~dict

        Example:
        >>> get_client_access_token(hub='theHub')
        {
            'baseUrl': 'wss://contoso.com/api/webpubsub/client/hubs/theHub',
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ...',
            'url': 'wss://contoso.com/api/webpubsub/client/hubs/theHub?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ...'
        }
        """
        endpoint = self._config.endpoint.lower()
        if not endpoint.startswith("http://") and not endpoint.startswith("https://"):
            raise ValueError(
                "Invalid endpoint: '{}' has unknown scheme - expected 'http://' or 'https://'".format(
                    endpoint
                )
            )

        # Ensure endpoint has no trailing slash
        endpoint = endpoint.rstrip("/")

        # Switch from http(s) to ws(s) scheme
        client_endpoint = "ws" + endpoint[4:]
        client_url = "{}/client/hubs/{}".format(client_endpoint, hub)
        if isinstance(self._config.credential, AzureKeyCredential):
            token = _get_token_by_key(endpoint, hub, self._config.credential.key, **kwargs)
        else:
            access_token = await super().get_client_access_token(hub, **kwargs)
            token = access_token.get('token')

        return {
            "baseUrl": client_url,
            "token": token,
            "url": "{}?access_token={}".format(client_url, token),
        }
    get_client_access_token.metadata = {'url': '/api/hubs/{hub}/:generateToken'}  # type: ignore


def patch_sdk():
    curr_package = importlib.import_module("azure.messaging.webpubsubservice.aio")
    curr_package.WebPubSubServiceClient = WebPubSubServiceClient
