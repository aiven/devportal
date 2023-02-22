Manage Aiven for ClickHouse® integration databases
==================================================

Aiven for ClickHouse supports :doc:`regular integrations </docs/products/clickhouse/howto/list-integrations>` and :doc:`data service integrations </docs/products/clickhouse/howto/data-service-integration>`.

You can create Aiven for ClickHouse® integrations databases in the `Aiven web console <https://console.aiven.io/>`_ either when :ref:`creating a new data service integration <integration-db>` or from the the **Databases & Tables** view of your service.

This article details how to set up and manage integration databases from the the **Databases & Tables** view of your Aiven for ClickHouse service.

.. seealso::

    For information on how to set up integration databases when creating a new data service integration, see :doc:`Manage Aiven for ClickHouse® data service integrations </docs/products/clickhouse/howto/data-service-integration>`. 

About integration databases
---------------------------

By adding integrations databases in Aiven for ClickHouse, you create streaming data pipelines across services. From Aiven for ClickHouse, you can add integration databases connecting to Aiven for Kafka® and Aiven for PostgreSQL®.

Prerequisites
-------------

* Aiven account
* Access to `Aiven web console <https://console.aiven.io/>`_

Create integration databases
----------------------------

.. note::

    You can create both PostgrSQL and Apache Kafka integration databases for Aiven for ClickHouse. This instruction uses *PostgreSQL* as an example.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. From the **Current services** list, select an Aiven for ClickHouse service you want to add integration databases to.
3. In your service homepage, navigate to the **Databases & Tables** tab and select **Create database** > **PostgreSQL integration database**.

   .. image:: /images/products/clickhouse/data-integration/create-integration-db.png
      :width: 700px
      :alt: Create database

4. In **Create PostgreSQL integration database** wizard, select one of the following options:

   * To add an integration database to a service that is not yet integrated, go to the **Create new integration** tab.

     .. dropdown:: Expand for next steps

        1. Select a service from the list of services available for integration.
        2. Select **Continue**.
        3. In the **Integration databases** view, select **Add databases**.

        .. image:: /images/products/clickhouse/data-integration/enable-data-integration.png
           :width: 700px
           :alt: Add database

        1. In the **Add integration databases** section, enter database names and schema names and select **Enable** when ready.

        .. image:: /images/products/clickhouse/data-integration/enable-with-database.png
           :width: 700px
           :alt: Enable database

        As a result, you can see the created databases in the **Databases & Tables** tab.

        .. image:: /images/products/clickhouse/data-integration/preview-integration-database.png
           :width: 700px
           :alt: Database created

   * To add an integration database to an already integrated service, go to the **Manage integrations** tab.

     .. dropdown:: Expand for next steps

        1. Select a service from the list of integrated services.
        2. Select **Continue**.
        3. In the **Add integration databases** section, enter database names and schema names and select **Save changes** when ready.

        .. image:: /images/products/clickhouse/data-integration/enable-with-database.png
           :width: 700px
           :alt: Enable database

        As a result, you can see the created databases in the **Databases & Tables** tab.

        .. image:: /images/products/clickhouse/data-integration/preview-integration-database.png
           :width: 700px
           :alt: Database created

   * To create a new service, integrate it, and add integration databases, go to the **Manage integrations** tab.

     .. dropdown:: Expand for next steps

        1. In the **Manage integrations** view, select **Create service**.
        2. Set up the new service.
        3. Come back to your primary service and create an integration to the new service along with new integration databases.

        .. image:: /images/products/clickhouse/data-integration/integrate-db-new-service.png
           :width: 700px
           :alt: Create new service for integration

View integration databases
--------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. From the **Current services** list, select an Aiven for ClickHouse service you want to check integration databases for.
3. In your service homepage, navigate to the **Databases & Tables** tab to discover your integration databases in the **Databases** list.

.. image:: /images/products/clickhouse/data-integration/preview-integration-database.png
   :width: 700px
   :alt: Preview integration databases

.. note::
   
   PostgreSQL is currently only supported as a source.

Edit integration databases
--------------------------

.. note::

   You can only edit Apache Kafka integration databases and tables.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. From the **Current services** list, select an Aiven for ClickHouse service you want to edit integration databases for.
3. In your service homepage, navigate to the **Databases & Tables** tab > the **Databases** list.
4. From the **Databases** list, select a pencil icon for an Apache Kafka integration database you want to edit.

   .. image:: /images/products/clickhouse/data-integration/integration-db-edit.png
      :width: 700px
      :alt: Edit database

5. In the **Edit database** wizard, find a table that you want to edit in the **Configured tables** list and expand its details by selecting the angle brackets icon.

   .. note::

      You can also create a new table for the database you are editing by selecting **Add another table**.

   .. image:: /images/products/clickhouse/data-integration/integration-db-details.png
      :width: 700px
      :alt: Edit database details

6. In the table details section, update any of the following fields:

   * Table name
   * Consumer group name
   * Topics
   * Data format
   * Table columns

   .. image:: /images/products/clickhouse/data-integration/integration-db-save.png
      :width: 700px
      :alt: Save updated database

7. Select **Update table details** > **Save changes**.

.. topic:: Result

   Your integration database and/or its tables have been updated.

Delete integration databases
----------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. From the **Current services** list, select an Aiven for ClickHouse service you want to delete integration databases for.
3. In your service homepage, navigate to the **Databases & Tables** tab > the **Databases** list.
4. From the **Databases** list, select the trash bin icon for the integration database you want to remove.

   .. image:: /images/products/clickhouse/data-integration/delete-integration-database.png
      :width: 700px
      :alt: Delete integration database

5. In the **Delete database confirmation** popup, study the impact and select **Confirm** if you accept removing the database along with the tables inside it.

.. topic:: Result

   Your integration database has been removed from the **Databases** list.

Related reading
---------------

* :doc:`Manage Aiven for ClickHouse® data service integrations </docs/products/clickhouse/howto/data-service-integration>`
* :doc:`Integrate your Aiven for ClickHouse® service </docs/products/clickhouse/howto/list-integrations>`

