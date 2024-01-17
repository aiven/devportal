Set up Aiven for ClickHouse® data service integrations
======================================================

Connect an Aiven for ClickHouse® service with another Aiven service or external data source to make your data available in the Aiven for ClickHouse service. Depending on your use case, select either the managed-database integration or the managed-credentials integration.

.. seealso::

   For information on data service integraton types and methods available with Aiven for ClickHouse®, check out :doc:`About Aiven for ClickHouse® data service integrations </docs/products/clickhouse/concepts/data-integration-overview>`.

Prerequisites
-------------

* Make sure you are aware of and understand :ref:`Limitations <integration-limitations>`.
* Make sure you have an Aiven organization, project, and Aiven for ClickHouse service.
* Make sure you have access to the `Aiven Console <https://console.aiven.io/>`_.

.. _create-data-service-integration:

Create data service integrations
--------------------------------

#. Log in to the `Aiven Console <https://console.aiven.io/>`_.
#. On the **Services** page, select an Aiven for ClickHouse service you want to integrate with a data service.
#. From the **Integrate your Aiven for ClickHouse** section on the **Overview** page of your service, select **Get started** (to create your first integration) or the **+** icon (to add another integration).

As a result, the **Data service integrations** wizard opens, showing the **Select data service type** dropdown menu and the list of all data sources available for integration. At this point you need to decide if you want to integrate with an Aiven service or an external endpoint and continue as instructed in either :ref:`Integrate with Aiven services <integrate-aiven-services>` or :ref:`Integrate with external data sources <integrate-external-services>` respectively.

.. _integrate-aiven-services:

Integrate with Aiven services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
Integrate with a new Aiven service
''''''''''''''''''''''''''''''''''
   
To create an integration with a new service, take the following steps in the **Data service integrations** wizard:
   
#. Use the **Select data service type** dropdown menu to select the option for no data service type.
#. In the **Data service integrations** view, select **Create service**.
#. :doc:`Set up the new service </docs/platform/howto/create_new_service>`.
#. Come back to your primary service and create an integration to the newly-created service.
   For that purpose, skip the steps that follow and start over with building your integration using this
   instruction but now follow the steps in :ref:`Integrate with an existing Aiven service <integrate-existing-aiven-services>`.

.. _integrate-existing-aiven-services:

Integrate with an existing Aiven service
''''''''''''''''''''''''''''''''''''''''

To create an integration with an existing service, take the following steps in the **Data service integrations** wizard:
   
#. Select a type of an Aiven service you want to integrate with using the **Select data service type** dropdown menu.
#. Select a service of the chosen type from the list of services available for integration.
#. Select **Continue** and proceed to the next step to integrate the database.
#. Select either **Enable without databases** or **Add databases** depending on whether you want to enable your integration with databases:

.. note::

   If you prefer to create a data service integration without adding integration databases, you can create integration databases for your service any time later. See :doc:`Manage Aiven for ClickHouse® integration databases </docs/products/clickhouse/howto/integration-databases>` for guidance on how to do that.

- Enable your integration with databases:

  #. Select **Add databases**.
  #. Enter database names and schema names and select **Enable**.

     You can preview the created databases by selecting **Databases and tables** from the sidebar.

- Enable your integration without databases:

  #. Select **Enable without databases**.
      
     You can preview the created integration by selecting **Overview** from the sidebar.

.. _integrate-external-services:

Integrate with external data sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For integration with external data sources, Aiven for ClickHouse offers two methods:

* :ref:`Managed databases <managed-databases-integration>`
* :ref:`Managed credentials <managed-credentials-integration>`

To create an integration with an external data source, take the following steps in the **Data service integrations** wizard:

#. Select a type of an external service you want to integrate with using the **Select data service type** dropdown menu.
#. Select an external service of the chosen type from the list of services available for integration.
#. Select an integration method: either **Managed databases**  or **Managed credentials**.
#. Continue as instructed either in :ref:`Integrate using managed databases <integrate-managed-databases>` or in :ref:`Integrate using managed credentials <integrate-managed-credentials>` depending on a chosen method.

.. _integrate-managed-databases:

Integrate using managed databases
'''''''''''''''''''''''''''''''''

The **Managed databases** integration uses databases engines and, when enabled, automatically creates databases in your Aiven for ClickHouse, where you can ingest your external data.

1. Enable the **Managed databases** integration by selecting **Managed databases** and confirming your choice by selecting **Continue**.
2. Populate your automatically created databases with your external data using the following query:

.. code:: bash

   SELECT data 
   FROM ext-postgresql-resource-name.your-pg-table-name

.. _integrate-managed-credentials:

Integrate using managed credentials
'''''''''''''''''''''''''''''''''''

The **Managed credentials** integration supports storing connection parameters in Aiven and allows you to create tables for your external data.

1. Enable the **Managed credentials** integration by selecting **Managed credentials** and confirming your choice by selecting **Continue**.
2. Create tables using :doc:`table engines </docs/products/clickhouse/reference/supported-table-engines>`:

.. code:: bash

   SELECT data 
   FROM postgresql(ext-postgresql-resource-name,
        database='defaultdb',
        table='your-pg-table-name')

.. note::

   The connection parameters for your integration are stored in Aiven and automatically seeded in your external data queries.

You can access your credentials storage by passing your external service name in the following query:

.. code:: bash

   SELECT * 
   FROM postgresql(ext-postgresql-resource-name);

View data service integrations
------------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. On the **Services** page, select an Aiven for ClickHouse service you want to check integrations for.
3. On the **Overview** page of your service, find the **Data service integration** section and discover your integrations grouped according to service types.
4. Select the **>** icon for a particular service group to preview active data service integrations within that group.

Stop data service integrations
------------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. In the **Services** page, select an Aiven for ClickHouse service you want to stop integrations for.
3. In the **Overview** page of your service, find the **Data service integration** section and select the **>** icon for a service group that your unwanted integration belongs to.
4. From the **Active data service integrations** list, select the service integration that you no longer need and select **Disconnect integration**.
5. Make sure you understand the impact of disconnecting from a service explained in the **Warning** popup, and select **Disconnect integration** if you accept erasing all the databases and configuration information.

Your integration has been terminated, and all the corresponding databases and configuration information has been deleted.

Related pages
---------------

* :doc:`About Aiven for ClickHouse® data service integrations </docs/products/clickhouse/concepts/data-integration-overview>`
* :doc:`Manage Aiven for ClickHouse® integration databases </docs/products/clickhouse/howto/integration-databases>`
* :doc:`Integrate your Aiven for ClickHouse® service </docs/products/clickhouse/howto/list-integrations>`
