List of available extensions
============================

The following PostgreSQL extensions are available. Please note that some of the extensions have dependencies and they need to be created in the proper order. Also some extensions may require disconnecting the client connection and reconnecting before they are fully available.

Data types
----------

``hll`` - https://github.com/citusdata/postgresql-hll
    Data type ``hll`` is a HyperLogLog data structure

``hstore`` - https://www.postgresql.org/docs/current/hstore.html
    Store sets of key/value pairs as a single PostgreSQL value

``citext`` - https://www.postgresql.org/docs/current/citext.html
    Data type ``citext`` is a case-insensitive character string type

``unit`` - https://github.com/df7cb/postgresql-unit
    Data type for SI units

``cube`` - https://www.postgresql.org/docs/current/cube.html
    Data type ``cube`` to represent multidimensional cubes

``isn`` - https://www.postgresql.org/docs/current/isn.html
    Data types for international product numbering standards

``ltree`` - https://www.postgresql.org/docs/current/ltree.html
    Data type ``ltree`` for representing labels of data

``timescaledb`` - https://github.com/timescale/timescaledb
    Support for time series data types and functions

``uuid-ossp`` - https://www.postgresql.org/docs/current/uuid-ossp.html
    Additional support for generating UUIDs and special UUID constants


Search and text handling
------------------------

``fuzzystrmatch`` - https://www.postgresql.org/docs/current/fuzzystrmatch.html
    Determine similarities and differences between strings

``pg_similarity`` - https://github.com/eulerto/pg_similarity
    PostgreSQL 13 and newer. Support for similarity queries on PostgreSQL

``bloom`` - https://www.postgresql.org/docs/current/bloom.html
    Provides an index access method based on Bloom filters

``unaccent`` - https://www.postgresql.org/docs/current/unaccent.html
    Filtering dictionary to remove accented characters and enable accent-insensitive text processing 

``btree_gin`` - https://www.postgresql.org/docs/current/btree-gin.html
    Support for GIN-based indexes to speed up full text searches

``rum`` - https://github.com/postgrespro/rum
    Support for RUM-based indexes to improve full text search

``btree_gist`` - https://www.postgresql.org/docs/current/btree-gist.html
    Support for GIST-based indexes to speed up full text searches

``dict_int`` - https://www.postgresql.org/docs/current/dict-int.html
    Add-on dictionary to allow integers to be indexed for full-text search

``pg_trgm`` - https://www.postgresql.org/docs/current/pgtrgm.html
    Determine similarity of text based on trigram matching

``pgcrypto`` - https://www.postgresql.org/docs/current/pgcrypto.html
    Cryptographic functions for PostgreSQL

Geographical features
---------------------

``postgis`` - https://postgis.net/
    Support for geographic objects and spatial database features such as location awareness

``postgis_address_standardizer`` - https://postgis.net/docs/standardize_address.html
    PostgreSQL 10 and newer, a PostGIS-powered feature to produce a standard address format

``postgis_sfcgal`` - http://postgis.net/docs/reference.html#reference_sfcgal
    Computational geometry support for spatial database features

``postgis_tiger_geocoder`` - https://postgis.net/docs/Extras.html#Tiger_Geocoder
    Geocoder and reverse geocoder to work with the TIGER database

``postgis_topology`` - https://postgis.net/docs/Topology.html
    Data types and functions to work with topological objects

``postgis_legacy`` 
    The extension is not packaged or supported as an extension by the PostGIS project. The extension package is provided by Aiven for Aiven users.

``postgres_fdw`` - https://www.postgresql.org/docs/current/postgres-fdw.html
    Foreign data wrapper to enable access to data stored in external PostgreSQL servers
``address_standardizer`` - https://postgis.net/docs/standardize_address.html
    Returns a standard address format from certain rules

``address_standardizer_data_us`` - https://postgis.net/docs/standardize_address.html
    Returns a standard US address format from certain rules

``earthdistance`` - https://www.postgresql.org/docs/current/earthdistance.html
    Calculate great circle distances on the surface of the earth

``pgrouting`` - https://github.com/pgRouting/pgrouting
    Geospatial routing and network analysis, extends PostGIS


Utilities
---------

``aiven_extras`` - https://github.com/aiven/aiven-extras
    Aiven-created extension to enable non-superusers to access certain database features, such as logical replication support

``dblink`` - https://www.postgresql.org/docs/current/contrib-dblink-function.html
    Allow execution of queries on a remote database

``intagg`` - https://www.postgresql.org/docs/current/intagg.html
    Integer aggregator and enumerator (note that built-in functions provide these capabilities; the extension is still supported for compatibility)

``intarray`` - https://www.postgresql.org/docs/current/intarray.html
    Functions and operators for manipulating arrays of integers

``pg_buffercache`` - https://www.postgresql.org/docs/current/pgbuffercache.html
    Examine the shared buffer cache in real time

``pg_cron`` - https://github.com/citusdata/pg_cron
    Simple cron-based support for running period jobs in PostgreSQL

``pg_prometheus`` - https://github.com/timescale/pg_prometheus
    PostgreSQL 12 and older, the extension has been sunset by Timescale in favor of ``promscale``

``pg_repack`` - https://pgxn.org/dist/pg_repack/1.4.6/
    Reorganize tables and indexes in PostgreSQL with the database online, with minimal locking

``pg_stat_statements`` - https://www.postgresql.org/docs/current/pgstatstatements.html
    Track and plan execution statistics of SQL statements

``pgrowlocks`` - https://www.postgresql.org/docs/current/pgrowlocks.html
    Show row locking information for a table

``pgstattuple`` - https://www.postgresql.org/docs/current/pgstattuple.html
    PostgreSQL 11 and later. Provides functions to obtain tuple-level statistics

``plperl`` - https://www.postgresql.org/docs/current/plperl.html
    Write your functions and procedures in Perl

``sslinfo`` - https://www.postgresql.org/docs/current/sslinfo.html
    Information about the SSL certificate used by the current client

``tablefunc`` - https://www.postgresql.org/docs/current/tablefunc.html
    Support for functions that return multiple rows

``tsm_system_rows`` - https://www.postgresql.org/docs/current/tsm-system-rows.html
    Table sampling method

``wal2json`` - https://github.com/eulerto/wal2json
    Output plugin to produce JSON objects for logical decoding

