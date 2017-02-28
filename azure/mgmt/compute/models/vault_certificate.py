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

from msrest.serialization import Model


class VaultCertificate(Model):
    """Describes a single certificate reference in a Key Vault, and where the
    certificate should reside on the VM.

    :param certificate_url: The URL referencing a secret in a Key Vault which
     contains a properly formatted certificate.
    :type certificate_url: str
    :param certificate_store: The Certificate store in LocalMachine to add the
     certificate to on Windows, leave empty on Linux.
    :type certificate_store: str
    """ 

    _attribute_map = {
        'certificate_url': {'key': 'certificateUrl', 'type': 'str'},
        'certificate_store': {'key': 'certificateStore', 'type': 'str'},
    }

    def __init__(self, certificate_url=None, certificate_store=None):
        self.certificate_url = certificate_url
        self.certificate_store = certificate_store
