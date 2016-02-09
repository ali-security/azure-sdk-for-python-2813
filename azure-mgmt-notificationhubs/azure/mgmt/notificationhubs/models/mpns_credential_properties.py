# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MpnsCredentialProperties(Model):
    """
    Description of a NotificationHub MpnsCredential.

    :param str mpns_certificate: Gets or sets the MPNS certificate.
    :param str certificate_key: Gets or sets the certificate key for this
     credential.
    :param str thumbprint: Gets or sets the Mpns certificate Thumbprint
    """

    _required = []

    _attribute_map = {
        'mpns_certificate': {'key': 'mpnsCertificate', 'type': 'str'},
        'certificate_key': {'key': 'certificateKey', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
    }

    def __init__(self, mpns_certificate=None, certificate_key=None, thumbprint=None):
        self.mpns_certificate = mpns_certificate
        self.certificate_key = certificate_key
        self.thumbprint = thumbprint
