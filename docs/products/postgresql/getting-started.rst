Getting started
===============

Aiven for PostgreSQL is available in the `Aiven console <https://console.aiven.io>`_.

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

Load a test dataset in PostgreSQL
---------------------------------

If you're checking out PostgreSQL, loading a test dataset will give you something to look at. This example uses
``dellstore2``, a standard store dataset with products, orders, inventory and customer information.

1. Download the ``dellstore2-normal-1.0.tar.gz`` file from the `PostgreSQL website <https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/dellstore2/dellstore2-normal-1.0/>`_ and unzip it.
2. Navigate to the ``dellstore2-normal-1.0`` folder on your terminal.
3. Connect to your PostgreSQL instance with ``psql`` as shown above.
4. Create a ``dellstore`` database and connect to it with the following command from ``psql``::

    CREATE DATABASE dellstore;
    \c dellstore


.. Tip::

    Your ``psql`` terminal prefix will change to ``dellstore==>`` when you are connected to the correct database.

5. Populate the database by executing the following command from ``psql``::

    \i dellstore2-normal-1.0.sql

6. Verify which objects have been created from ``psql``::

    \d

The output should look like this::

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

Further reading
----------------

Here are some more resources to help you on your PostgreSQL journey:

* Code examples for connecting to PostgreSQL from your application:
    * :doc:`Go <howto/connect-go>`
    * :doc:`Python <howto/connect-python>`
* How to :doc:`use PgAdmin <howto/connect-pgadmin>` with Aiven for PostgreSQL
* How to :doc:`migrate your PostgreSQL to Aiven <concepts/aiven-db-migrate>`
* Learn PostgreSQL with some `PostgreSQL Exercises <https://pgexercises.com/>`_
* The `awesome PostgreSQL ecosystem <https://github.com/dhamaniasad/awesome-postgres>`_ of tools and solutions
