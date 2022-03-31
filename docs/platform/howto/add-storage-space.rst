Add storage space
=================

With **Aiven for Apache Kafka®**, **Aiven for PostgreSQL®**, and **Aiven for MySQL** services, you can configure additional disk storage on top of what is included in your service plan.

Compared to service plan upgrades, setting additional disk storage is mainly intended for cases where you do not need additional computing power.

.. note::
   This feature is not available for all service plans. For example, **Aiven for Apache Kafka®** *Startup* and **Aiven for PostgreSQL®** *Hobbyist* service plans do not support adding storage space.

1. Log in to the `Aiven web console <https://console.aiven.io>`_ and select your service.

#. On the *Overview* page, scroll down to *Service plan* and click **Add Storage**.

#. Select **Add disk storage**  and use the slider to select the amount of storage that you want to add, up to a maximum of twice the storage defined in your service plan.

   The cost of the additional storage is shown to the right of the slider.

   * For **Aiven for Apache Kafka®** services, you can set the amount in increments of 30GB

   * For **Aiven for PostgreSQL®** and **Aiven for MySQL** services, you can set the amount in increments of 10GB

#. Click **Save changes**.

   This adds the storage to your service, and you can see the change next to *Service plan* on the *Overview* page for your service.
