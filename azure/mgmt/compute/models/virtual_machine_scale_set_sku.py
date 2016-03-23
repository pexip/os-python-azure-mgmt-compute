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


class VirtualMachineScaleSetSku(Model):
    """
    Describes an available virtual machine scale set sku.

    :param str resource_type: Gets the type of resource the sku applies to.
    :param Sku sku: Gets the Sku.
    :param VirtualMachineScaleSetSkuCapacity capacity: Gets available scaling
     information.
    """ 

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'capacity': {'key': 'capacity', 'type': 'VirtualMachineScaleSetSkuCapacity'},
    }

    def __init__(self, resource_type=None, sku=None, capacity=None, **kwargs):
        self.resource_type = resource_type
        self.sku = sku
        self.capacity = capacity
