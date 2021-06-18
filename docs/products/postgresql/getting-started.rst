Getting Started
===============

PostgreSQL is available in the `Aiven console <https://console.aiven.io>`_.

Choose the PostgreSQL version, your cloud provider and location to deploy to, then choose which plan to use.

.. note::
    If you're just trying out PostgreSQL, a single-node setup is available with our startup and hobbyist plans. This isn't recommended for production use however; for that you should try the high availability pairs provided on the business plans, or a premium plan to meet your needs.

Finally, give the service a name and then select "Create Service", and your shiny new PostgreSQL database will start building. While it does that, you can already visit the service overview page to see the details of the service.

.. image:: /images/products/postgresql/pg-connection-details.png
    :alt: PostgreSQL service overview tab in Aiven's console


Connect to PostgreSQL with ``psql``
-----------------------------------

The direct PostgreSQL connection endpoint can be found under the **Service URI** connection information on the main service overview tab. To understand more about direct connections and connection pooling visit the dedicated :doc:`page <concepts/pg-connection-pooling>`

With :doc:`psql <howto/connect-psql>` you can connect to the PostgreSQL instance with the following command, by replacing the ``SERVICE_URI`` parameter::

    psql SERVICE_URI

Load a Test Dataset in PostgreSQL
---------------------------------

If you're checking out PostgreSQL, loading a test dataset will help you speeding up your knowledge. This example uses
``dellstore2``, a standard store dataset with products, orders, inventory and customer information.

1. Download the ``dellstore2-normal-1.0.tar.gz`` file from the `PostgreSQL website <https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/dellstore2/dellstore2-normal-1.0/>`_ and unzip it.
2. Navigate to the ``dellstore2-normal-1.0`` folder on your terminal
3. Connect to your PostgreSQL instance with :doc:`psql <howto/connect-psql>`
4. Create a ``dellstore`` database and connect to it with the following command from ``psql``::

    CREATE DATABASE dellstore;
    \c dellstore


.. Tip::

    You can verify you're connected to the correct database if your ``psql`` terminal prefix is ``dellstore==>``

5. Populate the database by executing the following command from ``psql``::

    \i dellstore2-normal-1.0.sql

6. Verify which objects have been created from ``psql``::

    \d

The output should look like::

    List of relations
    Schema |           Name           |   Type   |  Owner
    --------+--------------------------+----------+----------
    public | categories               | table    | avnadmin
    public | categories_category_seq  | sequence | avnadmin
    public | cust_hist                | table    | avnadmin
    public | customers                | table    | avnadmin
    public | customers_customerid_seq | sequence | avnadmin
    public | inventory                | table    | avnadmin
    public | orderlines               | table    | avnadmin
    public | orders                   | table    | avnadmin
    public | orders_orderid_seq       | sequence | avnadmin
    public | products                 | table    | avnadmin
    public | products_prod_id_seq     | sequence | avnadmin
    public | reorder                  | table    | avnadmin
    (12 rows)

Further Readings
----------------

If you're learning PostgreSQL, you might find the following resources interesting:

* How to connect to PostgreSQL across various languages
    * :doc:`Go <howto/connect-go>`
    * :doc:`Python <howto/connect-python>`
* How to use :doc:`PgAdmin <howto/connect-pgadmin>` with Aiven for PostgreSQL
* How to :doc:`Migrate from your PostgreSQL to Aiven <concepts/aiven-db-migrate>`
* Learn PostgreSQL by doing exercises at `PostgreSQL Exercises <https://pgexercises.com/>`_
* The `awesome PostgreSQL ecosystem <https://github.com/dhamaniasad/awesome-postgres>`_ of tools and solutions
