Billing overview
=================

In the **Billing** section of `Aiven Console <https://console.aiven.io>`_, you can manage your :doc:`billing groups </docs/platform/concepts/billing-groups>`, :doc:`payment cards </docs/platform/howto/manage-payment-card>`, and view and download your invoices.


Service charges
----------------

The prices shown in the Aiven console are all-inclusive, meaning that all of the following are included in the hourly service price:

* Virtual machine costs
* Network costs
* Backup costs
* Setup costs

.. note::
    While network traffic is not charged separately, your application cloud service provider may charge you for the network traffic going to or from their services.

    Use of PrivateLink and additional storage will incur additional costs on top of the hourly service usage rate.

The minimum hourly charge unit is one hour. For example, when you launch an Aiven service and terminate it after 40 minutes, you will be charged for one full hour.  Likewise, if you terminate a service after 40.5 hours, you will be charged for 41 hours.

:doc:`Terminating or pausing a service <../howto/pause-from-cli>` will stop the accumulation of new charges immediately.  However, please note that the minimum hourly charge unit still applies prior to terminating or pausing a service.

Migrating a service to another cloud region or to a different cloud provider does not incur any additional costs.