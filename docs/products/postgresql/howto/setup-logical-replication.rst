Set up logical replication to Aiven for PostgreSQL
==================================================

Aiven for PostgreSQL represents the perfect managed solution for a variety of use cases; remote production systems can be completely migrated in Aiven using different methods including :doc:`using Aiven-db-migrate <migrate-aiven-db-migrate>` or the standard :doc:`dump and restore method <migrate-pg-dump-restore>`.

In some cases a complete migration from legacy systems is not possible, still Aiven for PostgreSQL can be used to keep an in-sync copy of the source dataset via **logical replica**. This article goes through the steps of replicating some tables from a self-managed PostgreSQL cluster to Aiven.

.. Note::
    These instructions work also with AWS RDS PostgreSQL 10+.

    Google Cloud Platform's PostgreSQL for CloudSQL does not currently support logical replication.


Variables
---------

These are the placeholders you will need to replace in the code sample:

==================      =======================================================================
Variable                Description
==================      =======================================================================
``SRC_HOST``            Hostname of the source PostgreSQL database
``SRC_PORT``            Port of the source PostgreSQL database
``SRC_DATABASE``        Database Name of the source PostgreSQL database
``SRC_USER``            Username of the source PostgreSQL database
``SRC_PASSWORD``        Password of the source PostgreSQL database
``SRC_CONN_URI``        Connection URI of the source PostgreSQL database
==================      =======================================================================

Requirements
------------

The following are the requirements to setup a **logical replica** to Aiven for PostgreSQL


* PostgreSQL version 10 or newer.
* Connection between the source cluster's PostgreSQL port and Aiven for PostgreSQL cluster.
* Access to an superuser role on the source cluster.
* ``wal_level`` setting to ``logical`` on the source cluster. To verify and change the ``wal_level`` setting check :ref:`this section <PG MigrateWAL>`.

.. Note::
    If you are using an AWS RDS PostgreSQL cluster as source, the ``rds.logical_replication`` parameter must be set to ``1`` (true) in the parameter group.

Set up the replication
----------------------

To create a logical replication, there is no need to install any extensions on the source cluster, but requires a superuser account.

.. Tip::
    The ``aiven_extras`` extension enables the creation of a publish/subscribe-style logical replication without a superuser account, and it is preinstalled on Aiven PostgreSQL servers. For more info on ``aiven_extras`` check the dedicated `GitHub repository <https://github.com/aiven/aiven-extras>`_. The following example will assume ``aiven_extras`` extension is not available in the source PostgreSQL database.

This example assumes a source database called ``origin_database`` on a self-managed PostgreSQL cluster. The replication will mirror three tables, named ``test_table``, ``test_table_2`` and ``test_table_3``, to the ``defaultdb`` database on Aiven for PostgreSQL. The process to setup the logical replication is the following:

1. On the source cluster, connect to the ``origin_database`` with ``psql``.

2. Create the ``PUBLICATION`` entry, named ``pub_source_tables``, for the test tables::

    CREATE PUBLICATION pub_source_tables
    FOR TABLE test_table,test_table_2,test_table_3
    WITH (publish='insert,update,delete');

.. Tip::
    In PostgreSQL 10 and above, ``PUBLICATION`` entries define the tables to be replicated, which are in turn ``SUBSCRIBED`` to by the receiving database.

    When creating a publication entry, the ``publish`` parameter defines the operations to transfer. In the above example, all the ``INSERT``, ``UPDATE`` or ``DELETE`` operations will be transferred.

3. PostgreSQL’s logical replication doesn’t copy table definitions, that can be extracted from the ``origin_database`` with ``pg_dump`` and included in a ``origin-database-schema.sql`` file with::

    pg_dump --schema-only --no-publications \
    SRC_CONN_URI                            \
    -t test_table -t test_table_2 -t test_table_3 > origin-database-schema.sql

4. The default ``postgres`` superuser :doc:`is not available in Aiven for PostgreSQL <../concepts/dba-tasks-pg>`, thus the user defined in the ``ALTER TABLE`` invocations within ``origin-database-schema.sql`` must be changed from ``postgres`` to the default ``avnadmin``.

5. Connect via ``psql`` to the destination Aiven for PostgreSQL database and create the new ``aiven_extras`` extension::

    CREATE EXTENSION aiven_extras CASCADE;

6. Create the table definitions in the Aiven for PostgreSQL destination database within ``psql``::

    \i origin-database-schema.sql

7. Create a ``SUBSCRIPTION`` entry, named ``dest_subscription``, in the Aiven for PostgreSQL destination database to start replicating changes from the source ``pub_source_tables`` publication::

    SELECT * FROM
    aiven_extras.pg_create_subscription(
        'dest_subscription',
        'host=SRC_HOST password=SRC_PASSWORD port=SRC_PORT dbname=SRC_DATABASE user=SRC_USER',
        'pub_source_tables',
        'slot',
        TRUE,
        TRUE);


8. Verify that the subscription has been created successfully. As the ``pg_subscription`` catalog is superuser-only, you can use the ``aiven_extras.pg_list_all_subscriptions()`` function from ``aiven_extras`` extension::

     SELECT subdbid, subname, subowner, subenabled, subslotname
     FROM aiven_extras.pg_list_all_subscriptions();

      subdbid |      subname      | subowner | subenabled | subslotname
     ---------+-------------------+----------+------------+-------------
        16401 | dest_subscription |       10 | t          | slot
     (1 row)

9. Verify the subscription status::

    SELECT * FROM pg_stat_subscription;

     subid |      subname      | pid | relid | received_lsn |      last_msg_send_time       |     last_msg_receipt_time     | latest_end_lsn |        latest_end_time
    -------+-------------------+-----+-------+--------------+-------------------------------+-------------------------------+----------------+-------------------------------
     16444 | dest_subscription | 869 |       | 0/C002360    | 2021-06-25 12:06:59.570865+00 | 2021-06-25 12:06:59.571295+00 | 0/C002360      | 2021-06-25 12:06:59.570865+00
    (1 row)

10. Verify the data is correctly copied over the Aiven for PostgreSQL target tables


Remove unused replication setup
-------------------------------

It is important to remove unused replication setups, since the underlying replication slots in PostgreSQL forces the server to keep all the data needed to replicate since the publication creation time. If the data stream has no readers, there will be an ever-growing amount of data on disk until it becomes full.

To remove an unused subscription, essentially stopping the replication, run the following command in the Aiven for PostgreSQL target database::

    SELECT * FROM aiven_extras.pg_drop_subscription('dest_subscription');


Verify the replication removal with::

    SELECT * FROM aiven_extras.pg_list_all_subscriptions();

     subdbid | subname | subowner | subenabled | subconninfo | subslotname | subsynccommit | subpublications
    ---------+---------+----------+------------+-------------+-------------+---------------+-----------------
    (0 rows)
