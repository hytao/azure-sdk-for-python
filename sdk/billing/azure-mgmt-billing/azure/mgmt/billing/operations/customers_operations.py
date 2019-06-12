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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class CustomersOperations(object):
    """CustomersOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview. Constant value: "2018-11-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-11-01-preview"

        self.config = config

    def list_by_billing_account_name(
            self, billing_account_name, filter=None, skiptoken=None, custom_headers=None, raw=False, **operation_config):
        """Lists all customers which the current user can work with on-behalf of a
        partner.

        :param billing_account_name: Billing Account Id.
        :type billing_account_name: str
        :param filter: May be used to filter using
         hasPermission('{permissionId}') to only return customers for which the
         caller has the specified permission.
        :type filter: str
        :param skiptoken: Skiptoken is only used if a previous operation
         returned a partial result. If a previous response contains a nextLink
         element, the value of the nextLink element will include a skiptoken
         parameter that specifies a starting point to use for subsequent calls.
        :type skiptoken: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CustomerListResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.CustomerListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_by_billing_account_name.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if skiptoken is not None:
            query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CustomerListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_by_billing_account_name.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers'}

    def get(
            self, billing_account_name, customer_name, expand=None, custom_headers=None, raw=False, **operation_config):
        """Get the customer by id.

        :param billing_account_name: Billing Account Id.
        :type billing_account_name: str
        :param customer_name: Customer Id.
        :type customer_name: str
        :param expand: May be used to expand enabledAzureSkus,
         serviceProviders.
        :type expand: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Customer or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.Customer or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'customerName': self._serialize.url("customer_name", customer_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Customer', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}'}
