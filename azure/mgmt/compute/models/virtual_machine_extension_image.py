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

from .resource import Resource


class VirtualMachineExtensionImage(Resource):
    """Describes a Virtual Machine Extension Image.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict
    :param operating_system: the operating system this extension supports.
    :type operating_system: str
    :param compute_role: the type of role (IaaS or PaaS) this extension
     supports.
    :type compute_role: str
    :param handler_schema: the schema defined by publisher, where extension
     consumers should provide settings in a matching schema.
    :type handler_schema: str
    :param vm_scale_set_enabled: whether the extension can be used on xRP
     VMScaleSets. By default existing extensions are usable on scalesets, but
     there might be cases where a publisher wants to explicitly indicate the
     extension is only enabled for CRP VMs but not VMSS.
    :type vm_scale_set_enabled: bool
    :param supports_multiple_extensions: whether the handler can support
     multiple extensions.
    :type supports_multiple_extensions: bool
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'operating_system': {'required': True},
        'compute_role': {'required': True},
        'handler_schema': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'operating_system': {'key': 'properties.operatingSystem', 'type': 'str'},
        'compute_role': {'key': 'properties.computeRole', 'type': 'str'},
        'handler_schema': {'key': 'properties.handlerSchema', 'type': 'str'},
        'vm_scale_set_enabled': {'key': 'properties.vmScaleSetEnabled', 'type': 'bool'},
        'supports_multiple_extensions': {'key': 'properties.supportsMultipleExtensions', 'type': 'bool'},
    }

    def __init__(self, location, operating_system, compute_role, handler_schema, tags=None, vm_scale_set_enabled=None, supports_multiple_extensions=None):
        super(VirtualMachineExtensionImage, self).__init__(location=location, tags=tags)
        self.operating_system = operating_system
        self.compute_role = compute_role
        self.handler_schema = handler_schema
        self.vm_scale_set_enabled = vm_scale_set_enabled
        self.supports_multiple_extensions = supports_multiple_extensions
