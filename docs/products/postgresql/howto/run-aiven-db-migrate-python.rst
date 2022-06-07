Migrate between PostgreSQL® instances using ``aiven-db-migrate`` in Python
==========================================================================

The ``aiven-db-migrate`` tool is an open source project available on `GitHub <https://github.com/aiven/aiven-db-migrate>`_, useful to perform PostgreSQL migrations. It's written in Python and therefore you can start any migration by directly calling the correct module.

The list of source and target database requirements is available in the :doc:`dedicated documentation <migrate-aiven-db-migrate>`.

Variables
---------

The following variables need to be substituted in the ``aiven-db-migrate`` calls

==================      =======================================================================
Variable                Description
==================      =======================================================================
``SRC_USERNAME``        Username for source PostgreSQL connection
``SRC_PASSWORD``        Password for source PostgreSQL connection
``SRC_HOSTNAME``        Hostname for source PostgreSQL connection
``SRC_PORT``            Port for source PostgreSQL connection
``DST_USERNAME``        Username for destination PostgreSQL connection
``DST_PASSWORD``        Password for destination PostgreSQL connection
``DST_HOSTNAME``        Hostname for destination PostgreSQL connection
``DST_PORT``            Port for destination PostgreSQL connection
``DST_DBNAME``          Bootstrap database name for destination PostgreSQL connection
==================      =======================================================================

Execute the ``aiven-db-migrate`` in Python
------------------------------------------

You can run perform a PostgreSQL® migration using ``aiven-db-migrate`` by:

* Cloning the ``aiven-db-migrate`` `GitHub repository <https://github.com/aiven/aiven-db-migrate>`_ and follow the installation instructions
* Executing the following script

  .. code:: bash

    python3 -m aiven_db_migrate.migrate pg -d \
        -s postgres://SRC_USERNAME:SRC_PASSWORD@SRC_HOSTNAME:SRC_PORT \
        -t postgres://DST_USERNAME:DST_PASSWORD@DST_HOSTNAME:DST_PORT/DST_DBNAME?sslmode=require \
        --max-replication-lag 1 \
        --stop-replication \
        -f DB_TO_SKIP

The following flags can be set:

* ``-d`` or ``--debug``: enables debug logging, highly recommended when running migration to see details of the migration process
* ``-f`` or ``--filtered-db``: comma separated list of databases to filter out during migrations
* ``--stop-replication``: by default logical replication will be left running on both source and target database. If set to true, it requires also ``--max-replication-lag >= 0`` to wait until a fixed replication lag before stopping the replication
* ``--max-replication-lag``: max replication lag in bytes to wait for, by default no wait, this parameter is required when using ``--stop-replication``
* ``--skip-table``: comma separated list of tables to filter out during migrations, useful when willing to skip extension tables like ``spatial_ref_sys`` from ``postgis`` extension.

.. Tip::

    For live migration ``--stop-replication`` and ``--max-replication-lag`` flags are not needed to keep logical replication running.

The full list of parameters and related descriptions is available by running the following command:

.. code:: bash

    python3 -m aiven_db_migrate.migrate pg -h