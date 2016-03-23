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


class VaultCertificate(Model):
    """
    Describes a single certificate reference in a Key Vault, and where the
    certificate should reside on the VM.

    :param str certificate_url: Gets or sets the URL referencing a secret in
     a Key Vault which contains a properly formatted certificate.
    :param str certificate_store: Gets or sets the Certificate store in
     LocalMachine to add the certificate to on Windows, leave empty on Linux.
    """ 

    _attribute_map = {
        'certificate_url': {'key': 'certificateUrl', 'type': 'str'},
        'certificate_store': {'key': 'certificateStore', 'type': 'str'},
    }

    def __init__(self, certificate_url=None, certificate_store=None, **kwargs):
        self.certificate_url = certificate_url
        self.certificate_store = certificate_store
