Secure a managed ClickHouse® service
====================================

Restrict network access to your service
---------------------------------------

    .. include:: /docs/platform/howto/restrict-access.rst

Manage Virtual Private Cloud (VPC) peering
------------------------------------------

    .. include:: /docs/platform/howto//manage-vpc-peering.rst

Protect a service from termination
----------------------------------

Aiven services can be protected against accidental deletion or powering off by enabling the Termination Protection feature.

.. note::

    Termination Protection has no effect on service migrations or upgrades.

Enable the termination protection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Log in to the `Aiven web console <https://console.aiven.io/>`_ and select your ClickHouse® service from the *Services* view.

2. In the *Overview* tab of your service, enable Termination Protection by using the toggle switch.

.. image:: /images/products/clickhouse/termination-prevention.png
   :width: 800px
   :alt: Termination protection

.. topic:: Result

    Termination Protection is enabled for your service: It cannot be terminated or powered down from the Aiven web console, via the Aiven REST API, or by using the Aiven command-line client.

Terminate a protected service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before terminating or powering off a protected service, you need to disable Termination Protection for this service.

.. note::
    
    Running out of free Aiven sign-up credits causes the service to be powered down unless a credit card has been entered for the project.
