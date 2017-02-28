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


class WinRMListener(Model):
    """Describes Protocol and thumbprint of Windows Remote Management listener.

    :param protocol: The Protocol used by the WinRM listener. Http and Https
     are supported. Possible values include: 'Http', 'Https'
    :type protocol: str or :class:`ProtocolTypes
     <azure.mgmt.compute.models.ProtocolTypes>`
    :param certificate_url: The Certificate URL in KMS for Https listeners.
     Should be null for Http listeners.
    :type certificate_url: str
    """ 

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'ProtocolTypes'},
        'certificate_url': {'key': 'certificateUrl', 'type': 'str'},
    }

    def __init__(self, protocol=None, certificate_url=None):
        self.protocol = protocol
        self.certificate_url = certificate_url
