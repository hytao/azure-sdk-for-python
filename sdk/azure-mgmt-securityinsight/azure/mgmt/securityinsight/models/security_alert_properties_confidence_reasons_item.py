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


class SecurityAlertPropertiesConfidenceReasonsItem(Model):
    """confidence reason item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar reason: The reason's description
    :vartype reason: str
    :ivar reason_type: The type (category) of the reason
    :vartype reason_type: str
    """

    _validation = {
        'reason': {'readonly': True},
        'reason_type': {'readonly': True},
    }

    _attribute_map = {
        'reason': {'key': 'reason', 'type': 'str'},
        'reason_type': {'key': 'reasonType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SecurityAlertPropertiesConfidenceReasonsItem, self).__init__(**kwargs)
        self.reason = None
        self.reason_type = None
