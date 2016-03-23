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


class VirtualMachineScaleSetVMInstanceIDs(Model):
    """
    Specifies the list of virtual machine scale set instance IDs.

    :param list instance_ids: Gets or sets the virtual machine scale set
     instance ids.
    """ 

    _attribute_map = {
        'instance_ids': {'key': 'instanceIds', 'type': '[str]'},
    }

    def __init__(self, instance_ids=None, **kwargs):
        self.instance_ids = instance_ids
