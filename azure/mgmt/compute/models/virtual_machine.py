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

from .resource import Resource


class VirtualMachine(Resource):
    """
    Describes a Virtual Machine.

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    :param Plan plan: Gets or sets the purchase plan when deploying virtual
     machine from VM Marketplace images.
    :param HardwareProfile hardware_profile: Gets or sets the hardware
     profile.
    :param StorageProfile storage_profile: Gets or sets the storage profile.
    :param OSProfile os_profile: Gets or sets the OS profile.
    :param NetworkProfile network_profile: Gets or sets the network profile.
    :param DiagnosticsProfile diagnostics_profile: Gets or sets the
     diagnostics profile.
    :param SubResource availability_set: Gets or sets the reference Id of the
     availability set to which this virtual machine belongs.
    :param str provisioning_state: Gets or sets the provisioning state, which
     only appears in the response.
    :param VirtualMachineInstanceView instance_view: Gets the virtual machine
     instance view.
    :param str license_type: Gets or sets the license type, which is for
     bring your own license scenario.
    :param list resources: Gets the virtual machine child extension resources.
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'hardware_profile': {'key': 'properties.hardwareProfile', 'type': 'HardwareProfile'},
        'storage_profile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'os_profile': {'key': 'properties.osProfile', 'type': 'OSProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'diagnostics_profile': {'key': 'properties.diagnosticsProfile', 'type': 'DiagnosticsProfile'},
        'availability_set': {'key': 'properties.availabilitySet', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'instance_view': {'key': 'properties.instanceView', 'type': 'VirtualMachineInstanceView'},
        'license_type': {'key': 'properties.licenseType', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[VirtualMachineExtension]'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, plan=None, hardware_profile=None, storage_profile=None, os_profile=None, network_profile=None, diagnostics_profile=None, availability_set=None, provisioning_state=None, instance_view=None, license_type=None, resources=None, **kwargs):
        super(VirtualMachine, self).__init__(id=id, name=name, type=type, location=location, tags=tags, **kwargs)
        self.plan = plan
        self.hardware_profile = hardware_profile
        self.storage_profile = storage_profile
        self.os_profile = os_profile
        self.network_profile = network_profile
        self.diagnostics_profile = diagnostics_profile
        self.availability_set = availability_set
        self.provisioning_state = provisioning_state
        self.instance_view = instance_view
        self.license_type = license_type
        self.resources = resources
