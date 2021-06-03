Manage Extensions
=================

Aiven PostgreSQL allows a series of pre-approved extensions to be installed.


List of Available extensions
----------------------------

The following PostgreSQL extensions are available. Please note that some of the extensions have dependencies and they need to be created in the proper order. Also some extensions may require disconnecting the client connection and reconnecting before they are fully available.


.. list-table::
  :header-rows: 1
  :align: left

  * - Extension Name
    - Notes
  * - `address_standardizer <https://postgis.net/docs/Address_Standardizer.html>`_
    -
  * - `address_standardizer_data_us <https://postgis.net/docs/Address_Standardizer.html>`_
    -
  * - `aiven_extras <https://github.com/aiven/aiven-extras>`_
    - Logical replication support
  * - `bloom <https://www.postgresql.org/docs/current/bloom.html>`_
    -
  * - `btree_gin <https://www.postgresql.org/docs/current/btree-gin.html>`_
    -
  * - `btree_gist <https://www.postgresql.org/docs/current/btree-gist.html>`_
    -
  * - `chkpass <https://www.postgresql.org/docs/10/chkpass.html>`_
    - Available only up to PostgreSQL v10
  * - `citext <https://www.postgresql.org/docs/current/citext.html>`_
    -
  * - `cube <https://www.postgresql.org/docs/current/cube.html>`_
    -
  * - `dblink <https://www.postgresql.org/docs/current/contrib-dblink-function.html>`_
    -
  * - `dict_int <https://www.postgresql.org/docs/current/dict-int.html>`_
    -
  * - `earthdistance <https://www.postgresql.org/docs/current/earthdistance.html>`_
    -
  * - `fuzzystrmatch <https://www.postgresql.org/docs/current/fuzzystrmatch.html>`_
    -
  * - `hll <https://github.com/citusdata/postgresql-hll>`_
    - PostgreSQL 11 and newer
  * - `hstore <https://www.postgresql.org/docs/current/hstore.html>`_
    -
  * - `intagg <https://www.postgresql.org/docs/current/intagg.html>`_
    -
  * - `intarray <https://www.postgresql.org/docs/current/intarray.html>`_
    -
  * - `isn <https://www.postgresql.org/docs/current/isn.html>`_
    -
  * - `ltree <https://www.postgresql.org/docs/current/ltree.html>`_
    -
  * - `pg_buffercache <https://www.postgresql.org/docs/current/pgbuffercache.html>`_
    -
  * - `pg_cron <https://github.com/citusdata/pg_cron>`_
    -
  * - `pg_partman <https://github.com/pgpartman/pg_partman>`_
    - PostgreSQL 10 and older
  * - `pg_prometheus <https://github.com/timescale/pg_prometheus>`_
    - PostgreSQL 10 to 12, the extension has been sunset by Timescale in favor of ``promscale`` and is not supported for PostgreSQL 13
  * - `pg_repack <https://pgxn.org/dist/pg_repack/1.4.6/>`_
    - PostgreSQL 10 and newer
  * - `pg_similarity <https://github.com/eulerto/pg_similarity>`_
    - PostgreSQL 13 and newer
  * - `pg_stat_statements <https://www.postgresql.org/docs/current/pgstatstatements.html>`_
    -
  * - `pg_trgm <https://www.postgresql.org/docs/current/pgtrgm.html>`_
    -
  * - `pgcrypto <https://www.postgresql.org/docs/current/pgcrypto.html>`_
    -
  * - `pgrouting <https://github.com/pgRouting/pgrouting>`_
    -
  * - `pgrowlocks <https://www.postgresql.org/docs/current/pgrowlocks.html>`_
    -
  * - `pgstattuple <https://www.postgresql.org/docs/current/pgstattuple.html>`_
    - PostgreSQL 11 and later
  * - `plcoffee <https://pgxn.org/dist/plv8/>`_
    - Available only up to PostgreSQL v10
  * - `plls <https://pgxn.org/dist/plv8/>`_
    - Available only up to PostgreSQL v10
  * - `plperl <https://www.postgresql.org/docs/current/plperl.html>`_
    -
  * - `plv8 <https://pgxn.org/dist/plv8/>`_
    - Available only up to PostgreSQL v10
  * - `postgis <https://postgis.net/>`_
    -
  * - `postgis_address_standardizer <https://postgis.net/docs/Address_Standardizer.html>`_
    -
  * - `postgis_sfcgal <http://postgis.net/docs/reference.html#reference_sfcgal>`_
    -
  * - `postgis_tiger_geocoder <https://postgis.net/docs/Geocode.html>`_
    -
  * - `postgis_topology <https://postgis.net/docs/Topology.html>`_
    -
  * - postgis_legacy
    - The extension is not packaged or supported as an extension by the PostGIS project. The extension package is provided by Aiven for Aiven users.
  * - `postgres_fdw <https://www.postgresql.org/docs/current/postgres-fdw.html>`_
    -
  * - `rum <https://github.com/postgrespro/rum>`_
    -
  * - `sslinfo <https://www.postgresql.org/docs/current/sslinfo.html>`_
    -
  * - `tablefunc <https://www.postgresql.org/docs/current/tablefunc.html>`_
    -
  * - `timescaledb <https://github.com/timescale/timescaledb>`_
    - PostgreSQL 10 and newer
  * - `tsearch2 <https://www.postgresql.org/docs/9.2/tsearch2.html>`_
    - Available only up to PostgreSQL v9.6
  * - `tsm_system_rows <https://www.postgresql.org/docs/current/tsm-system-rows.html>`_
    -
  * - `unaccent <https://www.postgresql.org/docs/current/unaccent.html>`_
    -
  * - `unit <https://github.com/df7cb/postgresql-unit>`_
    - PostgreSQL 10 and newer
  * - `uuid-ossp <https://www.postgresql.org/docs/current/uuid-ossp.html>`_
    -
  * - `wal2json <https://github.com/eulerto/wal2json>`_
    - PostgreSQL 10 and newer



Install Extension
-----------------

The available extensions can be installed from the ``avnadmin`` user with the following ``CREATE EXTENSION`` command::

  CREATE EXTENSION <EXTENSION_NAME> CASCADE;


Update Extension
----------------

When a maintenance update is executed, the update itself does not update the extension versions that are used automatically.

The reason for this is that user schemas and functions can and do often rely on specific versions of an extension being used, if we change the underlying assumption behind that we would be breaking user code.

Instead the users need to upgrade the extensions themselves explicitly. This sort of behaviour is commonly true even if you were to run PostgreSQL on your own and just upgrade the package version of an extension to be newer, that won't update the extension version in the database(s) automatically either.

So to actually run the update, please run as ``avnadmin`` user::

  ALTER EXTENSION <EXTENSION_NAME> UPDATE;

To update to the very latest version that is available.



Request a New Extension
-----------------------

Based on support requests, we may also install additional extension related files for your database. When requesting things not on the pre-approved list through a support ticket, be sure to remember to specify to which database service and to which particular user database you'd like to see us install them.

.. warning::
    "Untrusted" language extensions such as ``plpythonu`` cannot be supported as they would compromise our ability to guarantee the highest possible service level.

If you have some other extensions you'd like to be supported, please give us a heads up on what you'd like to see in the future.
