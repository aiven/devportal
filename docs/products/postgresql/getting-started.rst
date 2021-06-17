Getting Started
===============

PostgreSQL is available in the `Aiven console <https://console.aiven.io>`_.

Choose the PostgreSQL version, your cloud provider and location to deploy to, then choose which plan to use.

.. note::
    If you're just trying out PostgreSQL, a single-node setup is available with our startup and hobbyist plans. This isn't recommended for production use however; for that you should try the high availability pairs provided on the business plans, or a premium plan to meet your needs.

Finally, give the service a name and then select "Create Service", and your shiny new PostgreSQL database will start building. While it does that, you can already visit the service overview page to see the details of the service.

.. image:: /images/products/postgresql/pg-connection-details.png

.. _pg-connect:
Connect to PostgreSQL
---------------------

The direct PostgreSQL connection endpoint can be found under the **Service URI** connection information on the main service overview tab. To understand more about direct connections and connection pooling visit the dedicated :doc:`page <concepts/pg-connection-pooling>`

If you have `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ already installed you can connect to the PostgreSQL instance with the following command, by replacing the ``SERVICE_URI`` parameter::

    psql SERVICE_URI

Load a Test Dataset in PostgreSQL
---------------------------------

If you're testing PostgreSQL, loading a test dataset <ADD TEXT HERE>. This example uses `Pagila <https://github.com/devrimgunduz/pagila>`_ and provides a standard schema.

1. Clone the `Pagila <https://github.com/devrimgunduz/pagila>`_ Github repository and navigate to the ``pagila`` folder on your terminal
2. Connect to your PostgreSQL instance with :ref:`psql <pg-connect>`
3. Create a ``pagila`` database and connect to it with the following command from ``psql``::

    CREATE DATABASE pagila;
    \c pagila

.. Tip::

    You can verify you're connected to the correct database if your ``psql`` terminal prefix is ``pagila==>``

4.
