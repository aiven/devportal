Manage Aiven for ClickHouse® data service integrations
======================================================

Aiven for ClickHouse supports two types of integrations:

Regular integrations
   Logs, metrics, dataflow/replication, and authentication integrations among your Aiven services and with external applications
Data service integrations
  Integrations with other Aiven services to use them as data sources

This article details how to set up and use data service integrations in Aiven for ClickHouse.

.. seealso::

    For information on how to set up and use regular integrations in Aiven for ClickHouse, see intregration guides in :doc:`Integrate your Aiven for ClickHouse® service </docs/products/clickhouse/howto/list-integrations>`.

About data service integrations
-------------------------------

By enabling data service integrations in Aiven for ClickHouse, you create streaming data pipelines across services. Aiven for ClickHouse supports data service integrations with Aiven for Kafka® and Aiven for PostgreSQL®.

You can create Aiven for ClickHouse® data service integrations in the `Aiven web console <https://console.aiven.io/>`_.

.. topic:: Integration databases
   
   When creating integrations in the **Data service integrations** wizard, you can also create integration databases connected to the services you are integrating with.

   If you prefer to create a data service integration without adding integration databases, you can create integration databases for your service any time later. See :doc:`Manage Aiven for ClickHouse® integration databases </docs/products/clickhouse/howto/integration-databases>` for guidance on how to do that.

Prerequisites
-------------

* Aiven account
* Access to `Aiven web console <https://console.aiven.io/>`_

.. _create-data-service-integration:

Create data service integrations
--------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. In the **Services** page, select an Aiven for ClickHouse service you want to integrate with a data service.
3. Select **Get started** from the **Integrate your Aiven for ClickHouse** section in the **Overview** page of your service.

4. In the **Data service integrations** wizard, select one of the following options:

* To create a new service and integrate it, make sure the checkboxes for both service types are unchecked.

  .. dropdown:: Expand for next steps

     1. In the **Data service integrations** view, select **Create service**.
     2. :doc:`Set up the new service </docs/platform/howto/create_new_service>`.
     3. Come back to your primary service and create an integration to the newly-created service. For that purpose, skip the steps that follow and start over with building your integration using this instruction but now follow the part on :ref:`integrating with an existing service <integrate-existing-service>`.

  or

.. _integrate-existing-service:

* To create an integration with an existing service, select a type of service you want to integrate with (Aiven for Apache Kafka or Aiven for PostgreSQL).

  .. dropdown:: Expand for next steps

    1. Select a service of the chosen type from the list of services available for integration.
    2. Select **Continue** and proceed to the :ref:`database setup part <integration-db>`.

.. _integration-db:

5. In the **Integration databases** view, select either **Enable without databases** or **Add databases** depending on whether you want to enable your integration with databases.

   .. dropdown:: Expand for enabling your integration with databases

      1. In the **Integration databases** view, select **Add databases**.
      2. In the **Add integration databases** section, enter database names and schema names and select **Enable** when ready.

      You can preview the created databases by selecting **Databases  tables** from the sidebar.

   .. dropdown:: Expand for enabling your integration without databases

      In the **Integration databases** view, select **Enable without databases**.
      
      You can preview the created integration by selecting **Overview** from the sidebar.

View data service integrations
------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. In the **Services** page, select an Aiven for ClickHouse service you want to check integrations for.
3. In the **Overview** page of your service, find the **Data service integration** section at the top and discover your integrations grouped according to service types (PostgreSQL or Apache Kafka).

4. Select the meatball menu for a particular service group to preview active data service integrations within that group.

Stop data service integrations
------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. In the **Services** page, select an Aiven for ClickHouse service you want to stop integrations for.
3. In the **Overview** page of your service, find the **Data service integration** section at the top and select the meatball menu for a service group that your unwanted integration belongs to.

4. From the **Active data service integrations** list, select the service integration that you no longer need and select **Disconnect integration**.

5. In the **Warning** popup, study the impact of disconnecting from a service and select **Disconnect integration** if you accept erasing all the databases and configuration information.

.. topic:: Result

   Your integration has been removed along with all the corresponding databases and configuration information.

Related reading
---------------

* :doc:`Manage Aiven for ClickHouse® integration databases </docs/products/clickhouse/howto/integration-databases>`
* :doc:`Integrate your Aiven for ClickHouse® service </docs/products/clickhouse/howto/list-integrations>`
