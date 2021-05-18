Manage Extensions
=================

Aiven PostgreSQL allows a series of pre-approved extensions to be installed.


List of Available extensions
----------------------------

The following PostgreSQL extensions are available. Please note that some of the extensions have dependencies and they need to be created in the proper order. Also some extensions may require disconnecting the client connection and reconnecting before they are fully available.

==================================  ============================================================
Extension Name                      Notes
==================================  ============================================================
address_standardizer
address_standardizer_data_us
aiven_extras                        Logical replication support
bloom
btree_gin
btree_gist
chkpass
citext
cube
dblink
dict_int
earthdistance
fuzzystrmatch
hll
hstore
intagg
intarray
isn
ltree
pg_buffercache
pg_cron
pg_partman                          PostgreSQL 10 and older
pg_prometheus                       PostgreSQL 10 to 12, the extension has been sunset
                                    by Timescale in favor of promscale and
                                    is not supported for PostgreSQL 13
pg_repack                           PostgreSQL 10 and newer
pg_similarity                       PostgreSQL 13 and newer
pg_stat_statements
pg_trgm
pgcrypto
pgrouting
pgrowlocks
pgstattuple
plcoffee
plls
plperl
plv8                                PostgreSQL 10 and older
postgis
postgis_address_standardizer
postgis_sfcgal
postgis_tiger_geocoder
postgis_topology
postgis_legacy                      The extension is not packaged or supported as an extension by
                                    the PostGIS project.
                                    The extension package is provided by Aiven for Aiven users.
postgres_fdw
rum
sslinfo
tablefunc
timescaledb                         PostgreSQL 10 and newer
tsearch2
tsm_system_rows
unaccent
unit
uuid-ossp
wal2json
==================================  ============================================================


Install Extension
-----------------

The available extensions can be installed from the `avnadmin` user with the following `CREATE EXTENSION <CREATE EXTENSION>`_ command::

  CREATE EXTENSION <EXTENSION_NAME> CASCADE;


Update Extension
----------------

When a maintenance update is executed, the update itself does not update the extension versions that are used automatically.

The reason for this is that user schemas and functions can and do often rely on specific versions of an extension being used, if we change the underlying assumption behind that we would be breaking user code.

Instead the users need to upgrade the extensions themselves explicitly. This sort of behaviour is commonly true even if you were to run PostgreSQL on your own and just upgrade the package version of an extension to be newer, that won't update the extension version in the database(s) automatically either.

So to actually run the update, please run as `avnadmin` user::

  ALTER EXTENSION <EXTENSION_NAME> UPDATE;

To update to the very latest version that is available.



Request a New Extension
-----------------------

Based on support requests, we may also install additional extension related files for your database. When requesting things not on the pre-approved list through a support ticket, be sure to remember to specify to which database service and to which particular user database you'd like to see us install them.

"Untrusted" language extensions such as ``plpythonu`` cannot be supported as they would compromise our ability to guarantee the highest possible service level.

If you have some other extensions you'd like to be supported, please give us a heads up on what you'd like to see in the future.
