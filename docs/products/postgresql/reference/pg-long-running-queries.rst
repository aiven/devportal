PostgreSQL long-running queries
===============================

Aiven does not terminate any customer PostgreSQL queries even if they run indefinitely.  Long-running queries often cause issues by locking resources and preventing database maintenance tasks.

To identify and terminate such long-running queries, you can do it from either:

* `Aiven console <http://console.aiven.io>`_ / web page
* `PostgreSQL shell <https://www.postgresql.org/docs/current/app-psql.html>`_ (psql)


Aiven console
-------------
In the Aiven web console, you can go to the **Current Queries** tab for your PostgreSQL service.

.. image:: /images/products/postgresql/pg-long-running-queries.png
    :alt: PostgreSQL service overview tab in Aiven's console


On this page, you can click **Terminate** to stop any queries directly.


PostgreSQL shell (psql)
-----------------------
You can login to your PostgreSQL service via `psql <service_uri>`.  Once connected, you can call the following function on the `psql` shell:

.. code:: bash

    => SELECT pg_terminate_backend(pid);


You can use the following query to monitor currently running queries:

.. code:: bash

    => SELECT * FROM pg_stat_activity WHERE state <> 'idle';


Client applications can use the statement_timeout session variable to voluntarily request the server to automatically cancel any query using the current connection that runs over a specified length of time. For example, the following would cancel any query that runs for more 15 seconds automatically:

.. code:: bash

    => SET statement_timeout = 15000


You may check the `Client Connection Defaults <https://www.postgresql.org/docs/9.6/runtime-config-client.html>`_ PostgreSQL documentation for more information on the available session variables.

.. note:: 

    There may be a scenario where you encounter an error when running the above commands.

If the database user is not a member of the database connected to, you may encounter the error:

.. code:: bash

    SELECT r.rolname as username,r1.rolname as "role"
    FROM pg_catalog.pg_roles r JOIN pg_catalog.pg_auth_members m
    ON (m.member = r.oid)
    JOIN pg_roles r1 ON (m.roleid=r1.oid)
    WHERE r.rolcanlogin
    ORDER BY 1;
    username |        role
    ----------+---------------------
    avnadmin | pg_read_all_stats
    avnadmin | pg_stat_scan_tables
    (3 rows)

To be able to check the database owner and grant the role, you can run the following:

.. code:: bash

    => \l
       Name    |  Owner   |
    -----------+----------+
     testdb    | testrole |
    
    => grant testrole to avnadmin;
    GRANT ROLE

For any additional questions, you can contact support@aiven.io.