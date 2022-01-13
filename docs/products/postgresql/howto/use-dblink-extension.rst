Use the PostgreSQL ``dblink`` extension
==========================================

``dblink`` is a `PostgreSQL extension <https://www.postgresql.org/docs/current/dblink.html>`_  that allows you to connect to other PostgreSQL databases and to run arbitrary queries. 

With `Foreign Data Wrappers <https://www.postgresql.org/docs/current/postgres-fdw.html>`_ (FDW) you can uniquely define a remote **foreign server** in order to access its data. The database connection details like hostnames are kept in a single place, and you only need to create once a **user mapping** storing remote connections credentials.

Prerequisites
-------------

To create a ``dblink`` foreign data wrapper you need the following information about the PostgreSQL remote server:

* ``TARGET_PG_HOST``: The remote database hostname
* ``TARGET_PG_PORT``: The remote database port
* ``TARGET_PG_USER``: The remote database user to connect
* ``TARGET_PG_PASSWORD``: The remote database password for the ``TARGET_PG_USER``
* ``TARGET_PG_DATABASE_NAME``: The remote database name

.. Note::

    If you're using Aiven for PostgreSQL as remote server, the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.


Enable ``dblink`` extension on Aiven for PostgreSQL
-------------------------------------------------------

To enable the ``dblink`` extension on an Aiven for PostgreSQL service:

* Connect to the database with the ``avnadmin`` user, the following shows how to do it with ``psql``, the service URI can be found in the `Aiven console <https://console.aiven.io/>`_ service Overview page:

::

    psql "postgres://avnadmin:[AVNADMIN_PWD]@[PG_HOST]:[PG_PORT]/[PG_DB_NAME]?sslmode=require"

* Create the ``dblink`` extension

::

    CREATE EXTENSION dblink;

Create a foreign data wrapper using ``dblink_fdw``
--------------------------------------------------

To create a foreign data wrapper using the ``dblink_fwd`` you need to perform the following steps:

*  Connect to the database with the ``avnadmin`` user, the following shows how to do it with ``psql``, the service URI can be found in the `Aiven console <https://console.aiven.io/>`_ service Overview page:

::

    psql "postgres://avnadmin:[AVNADMIN_PWD]@[PG_HOST]:[PG_PORT]/[PG_DB_NAME]?sslmode=require"

.. Tip::

    If you're using Aiven for PostgreSQL as remote server, you can connect to a service with the ``avnadmin`` user with the ``avn service cli`` command with the :ref:`Aiven CLI <avn_service_cli>`.

* Create an user ``user1`` that will be access the ``dblink``

::

    CREATE USER user1 PASSWORD 'secret1'

* Create a remote server definition (named ``pg_remote``)  using ``dblink_fdw`` and the target PostgreSQL connection details 

::

    CREATE SERVER pg_remote
        FOREIGN DATA WRAPPER dblink_fdw
        OPTIONS (
                 host 'TARGET_PG_HOST',
                 dbname 'TARGET_PG_DATABASE_NAME', 
                 port 'TARGET_PG_PORT'
                 );

* Create a user mapping for the ``user1`` to automatically authenticate as the ``TARGET_PG_USER`` when using the ``dblink``

::

    CREATE USER MAPPING FOR user1
        SERVER pg_remote
        OPTIONS (
            user 'TARGET_PG_USER', 
            password 'TARGET_PG_PASSWORD'
            );

* Enable ``user1`` to use the remote PostgreSQL connection ``pg_remote``

::

    GRANT USAGE ON FOREIGN SERVER pg_remote TO user1;

Query data using a foreign data wrapper
---------------------------------------

To query a foreign data wrapper you must be use a database user having the necessary grants to the remote server definition. In the previous example the user ``user1``. To query the remote table ``inventory`` defined in the target PostgreSQL database pointed by the ``pg_remote`` server definition:

* Connect with the Aiven for PostgreSQL service with the database user (``user1``) having the necessary grants to the remote server definition

* Establish the ``dblink`` connection to the remote target

::

    SELECT dblink_connect('my_new_conn', 'pg_remote');

* Execute the query passing the foreign server definition as parameter

::

    SELECT * FROM dblink('pg_remote','SELECT item_id FROM inventory') 
        AS target_inventory(target_item_id int);

* Check the results

.. code:: text

    target_item_id
    ----------------
                1
                2
                3
    (3 rows)