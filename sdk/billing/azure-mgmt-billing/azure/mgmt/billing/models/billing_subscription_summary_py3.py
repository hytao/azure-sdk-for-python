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


class BillingSubscriptionSummary(Resource):
    """A billing Subscription summary resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar display_name: display name.
    :vartype display_name: str
    :ivar subscription_id: Subscription Id.
    :vartype subscription_id: str
    :param subscription_billing_status: Subscription billing status. Possible
     values include: 'Active', 'Inactive', 'Abandoned', 'Deleted', 'Warning'
    :type subscription_billing_status: str or
     ~azure.mgmt.billing.models.BillingSubscriptionStatusType
    :ivar last_month_charges: Last month charges.
    :vartype last_month_charges: ~azure.mgmt.billing.models.Amount
    :ivar month_to_date_charges: Month to date charges.
    :vartype month_to_date_charges: ~azure.mgmt.billing.models.Amount
    :ivar billing_profile_id: Billing Profile id to which this product
     belongs.
    :vartype billing_profile_id: str
    :ivar billing_profile_name: Billing Profile name to which this product
     belongs.
    :vartype billing_profile_name: str
    :ivar customer_id: Customer id to which this product belongs.
    :vartype customer_id: str
    :ivar customer_display_name: Display name of customer to which this
     product belongs.
    :vartype customer_display_name: str
    :ivar invoice_section_id: Invoice section id to which this product
     belongs.
    :vartype invoice_section_id: str
    :ivar invoice_section_name: Invoice section name to which this product
     belongs.
    :vartype invoice_section_name: str
    :param sku_id: The sku id.
    :type sku_id: str
    :ivar sku_description: The sku description.
    :vartype sku_description: str
    :param service_provider_id: The service provider id.
    :type service_provider_id: str
    :ivar service_provider_description: The service provider description.
    :vartype service_provider_description: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'readonly': True},
        'subscription_id': {'readonly': True},
        'last_month_charges': {'readonly': True},
        'month_to_date_charges': {'readonly': True},
        'billing_profile_id': {'readonly': True},
        'billing_profile_name': {'readonly': True},
        'customer_id': {'readonly': True},
        'customer_display_name': {'readonly': True},
        'invoice_section_id': {'readonly': True},
        'invoice_section_name': {'readonly': True},
        'sku_description': {'readonly': True},
        'service_provider_description': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'subscription_billing_status': {'key': 'properties.subscriptionBillingStatus', 'type': 'str'},
        'last_month_charges': {'key': 'properties.lastMonthCharges', 'type': 'Amount'},
        'month_to_date_charges': {'key': 'properties.monthToDateCharges', 'type': 'Amount'},
        'billing_profile_id': {'key': 'properties.billingProfileId', 'type': 'str'},
        'billing_profile_name': {'key': 'properties.billingProfileName', 'type': 'str'},
        'customer_id': {'key': 'properties.customerId', 'type': 'str'},
        'customer_display_name': {'key': 'properties.customerDisplayName', 'type': 'str'},
        'invoice_section_id': {'key': 'properties.invoiceSectionId', 'type': 'str'},
        'invoice_section_name': {'key': 'properties.invoiceSectionName', 'type': 'str'},
        'sku_id': {'key': 'properties.skuId', 'type': 'str'},
        'sku_description': {'key': 'properties.skuDescription', 'type': 'str'},
        'service_provider_id': {'key': 'properties.serviceProviderId', 'type': 'str'},
        'service_provider_description': {'key': 'properties.serviceProviderDescription', 'type': 'str'},
    }

    def __init__(self, *, subscription_billing_status=None, sku_id: str=None, service_provider_id: str=None, **kwargs) -> None:
        super(BillingSubscriptionSummary, self).__init__(**kwargs)
        self.display_name = None
        self.subscription_id = None
        self.subscription_billing_status = subscription_billing_status
        self.last_month_charges = None
        self.month_to_date_charges = None
        self.billing_profile_id = None
        self.billing_profile_name = None
        self.customer_id = None
        self.customer_display_name = None
        self.invoice_section_id = None
        self.invoice_section_name = None
        self.sku_id = sku_id
        self.sku_description = None
        self.service_provider_id = service_provider_id
        self.service_provider_description = None
