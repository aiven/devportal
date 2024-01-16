Billing overview
=================

Super admin and account owners can manage :doc:`billing groups </docs/platform/concepts/billing-groups>`, :doc:`payment methods </docs/platform/concepts/corporate-billing>`, and view and download invoices in the **Billing** section of the `Aiven Console <https://console.aiven.io>`_.


Service charges
----------------

Services are billed by the hour. The costs are automatically calculated based on the services running in a project. Each project is charged separately, but the charges for multiple projects can be consolidated by assigning them to a billing group.

The prices shown in the Aiven Console are all-inclusive, meaning that all of the following are included in the hourly service price:

* Virtual machine costs
* Network costs
* Backup costs
* Setup costs

.. note::
    While network traffic is not charged separately, your application cloud service provider may charge you for the network traffic going to or from their services.

    Use of PrivateLink and additional storage will incur additional costs on top of the hourly service usage rate.

The minimum hourly charge unit is one hour. For example, when you launch an Aiven service and terminate it after 40 minutes, you are charged for one full hour. Likewise, if you terminate a service after 40.5 hours, you will be charged for 41 hours.

:doc:`Terminating or pausing a service <../howto/pause-from-cli>` will stop the accumulation of new charges immediately. However, the minimum hourly charge unit still applies before the service is terminated or paused.

Migrating a service to another cloud region or to a different cloud provider does not incur any additional costs.

Taxes for Aiven services
-------------------------

Aiven services are provided by Aiven Ltd, a private limited company incorporated in Finland. Aiven's tax status varies by regions. None of the marketed prices include value-added or other taxes.

European Union
~~~~~~~~~~~~~~~

Finnish law requires Aiven to charge a value-added tax for services provided within the European Union (EU). The value-added tax percentage depends on the domicile of the customer.

For business customers in EU countries other than Finland, we can apply the reverse charge mechanism of 2006/112/EC article 196 when a valid VAT ID :doc:`is added to the billing information </docs/platform/howto/use-billing-groups>` for a billing group.

United States
~~~~~~~~~~~~~

According to the tax treaty between Finland and the United States (US), no direct tax needs to be withheld from payments by US entities to Aiven. Although a W-8 form is not required to confirm this status, Aiven can provide a W-8BEN-E form describing its status. Contact the sales team at sales@Aiven.io to request one. 

Aiven does charge US sales taxes in several states. The applicability of these taxes depends on various factors, such as the taxability of Aiven services and tax thresholds.

Rest of the world
~~~~~~~~~~~~~~~~~~

No EU value-added tax is applied to services sold outside the EU as described in the Value-Added Tax Act of Finland section 69h. Finland has tax treaties with most countries in the world affirming this status. Aiven reserves the right to charge any  taxes required by the customer's local tax legislation.
