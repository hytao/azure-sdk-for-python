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

from msrest.paging import Paged


class DatabaseAccountGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DatabaseAccountGetResults <azure.mgmt.cosmosdb.models.DatabaseAccountGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DatabaseAccountGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabaseAccountGetResultsPaged, self).__init__(*args, **kwargs)
class MetricPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Metric <azure.mgmt.cosmosdb.models.Metric>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Metric]'}
    }

    def __init__(self, *args, **kwargs):

        super(MetricPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.cosmosdb.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class MetricDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`MetricDefinition <azure.mgmt.cosmosdb.models.MetricDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[MetricDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(MetricDefinitionPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.cosmosdb.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class PercentileMetricPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PercentileMetric <azure.mgmt.cosmosdb.models.PercentileMetric>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PercentileMetric]'}
    }

    def __init__(self, *args, **kwargs):

        super(PercentileMetricPaged, self).__init__(*args, **kwargs)
class PartitionMetricPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PartitionMetric <azure.mgmt.cosmosdb.models.PartitionMetric>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PartitionMetric]'}
    }

    def __init__(self, *args, **kwargs):

        super(PartitionMetricPaged, self).__init__(*args, **kwargs)
class PartitionUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PartitionUsage <azure.mgmt.cosmosdb.models.PartitionUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PartitionUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(PartitionUsagePaged, self).__init__(*args, **kwargs)
class SqlDatabaseGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlDatabaseGetResults <azure.mgmt.cosmosdb.models.SqlDatabaseGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlDatabaseGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlDatabaseGetResultsPaged, self).__init__(*args, **kwargs)
class SqlContainerGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlContainerGetResults <azure.mgmt.cosmosdb.models.SqlContainerGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlContainerGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlContainerGetResultsPaged, self).__init__(*args, **kwargs)
class SqlStoredProcedureGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlStoredProcedureGetResults <azure.mgmt.cosmosdb.models.SqlStoredProcedureGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlStoredProcedureGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlStoredProcedureGetResultsPaged, self).__init__(*args, **kwargs)
class SqlUserDefinedFunctionGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlUserDefinedFunctionGetResults <azure.mgmt.cosmosdb.models.SqlUserDefinedFunctionGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlUserDefinedFunctionGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlUserDefinedFunctionGetResultsPaged, self).__init__(*args, **kwargs)
class SqlTriggerGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SqlTriggerGetResults <azure.mgmt.cosmosdb.models.SqlTriggerGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SqlTriggerGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(SqlTriggerGetResultsPaged, self).__init__(*args, **kwargs)
class MongoDBDatabaseGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`MongoDBDatabaseGetResults <azure.mgmt.cosmosdb.models.MongoDBDatabaseGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[MongoDBDatabaseGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(MongoDBDatabaseGetResultsPaged, self).__init__(*args, **kwargs)
class MongoDBCollectionGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`MongoDBCollectionGetResults <azure.mgmt.cosmosdb.models.MongoDBCollectionGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[MongoDBCollectionGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(MongoDBCollectionGetResultsPaged, self).__init__(*args, **kwargs)
class TableGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TableGetResults <azure.mgmt.cosmosdb.models.TableGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TableGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(TableGetResultsPaged, self).__init__(*args, **kwargs)
class CassandraKeyspaceGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CassandraKeyspaceGetResults <azure.mgmt.cosmosdb.models.CassandraKeyspaceGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CassandraKeyspaceGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(CassandraKeyspaceGetResultsPaged, self).__init__(*args, **kwargs)
class CassandraTableGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CassandraTableGetResults <azure.mgmt.cosmosdb.models.CassandraTableGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CassandraTableGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(CassandraTableGetResultsPaged, self).__init__(*args, **kwargs)
class GremlinDatabaseGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GremlinDatabaseGetResults <azure.mgmt.cosmosdb.models.GremlinDatabaseGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GremlinDatabaseGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(GremlinDatabaseGetResultsPaged, self).__init__(*args, **kwargs)
class GremlinGraphGetResultsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GremlinGraphGetResults <azure.mgmt.cosmosdb.models.GremlinGraphGetResults>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GremlinGraphGetResults]'}
    }

    def __init__(self, *args, **kwargs):

        super(GremlinGraphGetResultsPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.cosmosdb.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.cosmosdb.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
