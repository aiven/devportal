Visualise PostgreSQL Data with Grafana
======================================

PostgreSQL can hold a wide variety of types of data, and creating visualisations helps gather insights on top of raw figures. Luckily, Aiven can set up the Grafana and the integration between the two services for you.


Integrate PostgreSQL and Grafana
--------------------------------

1. On the service overview page for your PostgreSQL service, go to **Manage Integrations** and choose the **datasource** option.

2. Choose either a new or existing Grafana service.

   - A new service will ask you to select the cloud, region and plan to use. You should also give your service a name. The service overview page shows the nodes rebuilding, and then indicates when they are ready.
   - If you're already using Grafana on Aiven, you can integrate your PostgreSQL as a data source for that existing Grafana.

3. On the service overview page for your Grafana service, click the "Service URI" link. The username and password for your Grafana service is also available on the service overview page.

Now your Grafana service is connected to PostgreSQL as a data source and you can go ahead and visualise your data.

Visualize PostgreSQL data in Grafana
------------------------------------

In Grafana, create a new dashboard and add a panel to it.

The datasource dropdown shows ``--Grafana--`` by default, but your PostgreSQL service will be listed here with a Prometheus logo. Prometheus is managing the communication between PostgreSQL and Grafana.

With your PostgreSQL service selected, the "Query" section will show the metrics from the database in its dropdown.

.. tip::
   If no metrics are shown, check that there is data in the database

Once you are happy with your panel, give it a title and click "Save" in the top right hand corner.

.. image:: /images/products/postgresql/view-data-postgresql-grafana.png
   :alt: Screenshot of a Grafana panel

.. tip::
    Grafana expects a Time column in the query, if you don't have any, use the function ``NOW()`` which generates the up-to-date timestamp.

To get to know Grafana better, try the `Grafana Fundamentals <https://grafana.com/tutorials/grafana-fundamentals/?pg=docs>`_ page on the Grafana project site.
