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

from .resource_py3 import Resource


class CaseComment(Resource):
    """Represents a case comment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar created_time_utc: The time the comment was created
    :vartype created_time_utc: datetime
    :param message: Required. The comment message
    :type message: str
    :ivar user_info: Describes the user that created the comment
    :vartype user_info: ~azure.mgmt.securityinsight.models.UserInfo
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_time_utc': {'readonly': True},
        'message': {'required': True},
        'user_info': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'created_time_utc': {'key': 'properties.createdTimeUtc', 'type': 'iso-8601'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'user_info': {'key': 'properties.userInfo', 'type': 'UserInfo'},
    }

    def __init__(self, *, message: str, **kwargs) -> None:
        super(CaseComment, self).__init__(**kwargs)
        self.created_time_utc = None
        self.message = message
        self.user_info = None
