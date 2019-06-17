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

from .proxy_only_resource_py3 import ProxyOnlyResource


class TriggeredJobRun(ProxyOnlyResource):
    """Triggered Web Job Run Information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param web_job_id: Job ID.
    :type web_job_id: str
    :param web_job_name: Job name.
    :type web_job_name: str
    :param status: Job status. Possible values include: 'Success', 'Failed',
     'Error'
    :type status: str or ~azure.mgmt.web.models.TriggeredWebJobStatus
    :param start_time: Start time.
    :type start_time: datetime
    :param end_time: End time.
    :type end_time: datetime
    :param duration: Job duration.
    :type duration: str
    :param output_url: Output URL.
    :type output_url: str
    :param error_url: Error URL.
    :type error_url: str
    :param url: Job URL.
    :type url: str
    :param job_name: Job name.
    :type job_name: str
    :param trigger: Job trigger.
    :type trigger: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'web_job_id': {'key': 'properties.web_job_id', 'type': 'str'},
        'web_job_name': {'key': 'properties.web_job_name', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'TriggeredWebJobStatus'},
        'start_time': {'key': 'properties.start_time', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.end_time', 'type': 'iso-8601'},
        'duration': {'key': 'properties.duration', 'type': 'str'},
        'output_url': {'key': 'properties.output_url', 'type': 'str'},
        'error_url': {'key': 'properties.error_url', 'type': 'str'},
        'url': {'key': 'properties.url', 'type': 'str'},
        'job_name': {'key': 'properties.job_name', 'type': 'str'},
        'trigger': {'key': 'properties.trigger', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, web_job_id: str=None, web_job_name: str=None, status=None, start_time=None, end_time=None, duration: str=None, output_url: str=None, error_url: str=None, url: str=None, job_name: str=None, trigger: str=None, **kwargs) -> None:
        super(TriggeredJobRun, self).__init__(kind=kind, **kwargs)
        self.web_job_id = web_job_id
        self.web_job_name = web_job_name
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.output_url = output_url
        self.error_url = error_url
        self.url = url
        self.job_name = job_name
        self.trigger = trigger