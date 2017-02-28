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


class Plan(Model):
    """Plan for the resource.

    :param name: The plan ID.
    :type name: str
    :param publisher: The publisher ID.
    :type publisher: str
    :param product: The offer ID.
    :type product: str
    :param promotion_code: The promotion code.
    :type promotion_code: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
    }

    def __init__(self, name=None, publisher=None, product=None, promotion_code=None):
        self.name = name
        self.publisher = publisher
        self.product = product
        self.promotion_code = promotion_code
