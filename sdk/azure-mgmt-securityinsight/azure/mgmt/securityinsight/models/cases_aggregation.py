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

from .aggregations import Aggregations


class CasesAggregation(Aggregations):
    """Represents aggregations results for cases.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param aggregation_by_severity: Aggregations results by case severity.
    :type aggregation_by_severity:
     ~azure.mgmt.securityinsight.models.CasesAggregationBySeverityProperties
    :param aggregation_by_status: Aggregations results by case status.
    :type aggregation_by_status:
     ~azure.mgmt.securityinsight.models.CasesAggregationByStatusProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'aggregation_by_severity': {'key': 'properties.aggregationBySeverity', 'type': 'CasesAggregationBySeverityProperties'},
        'aggregation_by_status': {'key': 'properties.aggregationByStatus', 'type': 'CasesAggregationByStatusProperties'},
    }

    def __init__(self, **kwargs):
        super(CasesAggregation, self).__init__(**kwargs)
        self.aggregation_by_severity = kwargs.get('aggregation_by_severity', None)
        self.aggregation_by_status = kwargs.get('aggregation_by_status', None)
        self.kind = 'CasesAggregation'