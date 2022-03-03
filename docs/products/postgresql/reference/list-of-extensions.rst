List of available extensions
============================

The following PostgreSQL extensions are available. Please note that some of the extensions have dependencies and they need to be created in the proper order. Some extensions may require disconnecting the client connection and reconnecting before they are fully available.  The version columns show which extension version is available on each version of Aiven for PostgreSQL.

Data types
----------

.. csv-table:: Data types extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`chkpass <https://www.postgresql.org/docs/10/chkpass.html>`_","data type for auto-encrypted passwords","","","","","1"
   "`citext <https://www.postgresql.org/docs/current/citext.html>`_","data type for case-insensitive character strings","1.6","1.6","1.6","1.5","1.4"
   "`cube <https://www.postgresql.org/docs/current/cube.html>`_","data type for multidimensional cubes","1.5","1.4","1.4","1.4","1.2"
   "`hll <https://github.com/citusdata/postgresql-hll>`_","type for storing hyperloglog data","2.16","2.16","2.16","2.16"
   "`hstore <https://www.postgresql.org/docs/current/hstore.html>`_","data type for storing sets of (key, value) pairs","1.8","1.7","1.6","1.5","1.4"
   "`isn <https://www.postgresql.org/docs/current/isn.html>`_","data types for international product numbering standards","1.2","1.2","1.2","1.2","1.1"
   "`ltree <https://www.postgresql.org/docs/current/ltree.html>`_","data type for hierarchical tree-like structures","1.2","1.2","1.1","1.1","1.1"
   "`seg <https://www.postgresql.org/docs/current/seg.html>`_","data type for representing line segments or floating-point intervals","1.4","1.3","1.3","1.3","1.1"
   "`timescaledb <https://github.com/timescale/timescaledb>`_","Enables scalable inserts and complex queries for time-series data","2.5.2","2.6.0","2.6.0","2.3.1","1.7.5"
   "`unit <https://github.com/df7cb/postgresql-unit>`_","SI units extension","7","7","7","7","7"
   "`uuid-ossp <https://www.postgresql.org/docs/current/uuid-ossp.html>`_","generate universally unique identifiers (UUIDs)","1.1","1.1","1.1","1.1","1.1"

Search and text handling
------------------------

.. csv-table:: Search and text handling extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`bloom <https://www.postgresql.org/docs/current/bloom.html>`_","bloom access method - signature file based index","1","1","1","1","1"
   "`btree_gin <https://www.postgresql.org/docs/current/btree-gin.html>`_","support for indexing common datatypes in GIN","1.3","1.3","1.3","1.3","1.2"
   "`btree_gist <https://www.postgresql.org/docs/current/btree-gist.html>`_","support for indexing common datatypes in GiST","1.6","1.5","1.5","1.5","1.5"
   "`dict_int <https://www.postgresql.org/docs/current/dict-int.html>`_","text search dictionary template for integers","1","1","1","1","1"
   "`dict_xsyn <https://www.postgresql.org/docs/current/dict-xsyn.html>`_","text search dictionary template for extended synonym processing","1","1","1","1","1"
   "`fuzzystrmatch <https://www.postgresql.org/docs/current/fuzzystrmatch.html>`_","determine similarities and distance between strings","1.1","1.1","1.1","1.1","1.1"
   "`pg_similarity <https://github.com/eulerto/pg_similarity>`_","support similarity queries","1","1","1.4.7","1.4.7","1.4.7"
   "`pg_trgm <https://www.postgresql.org/docs/current/pgtrgm.html>`_","text similarity measurement and index searching based on trigrams","1.6","1.5","1.4","1.4","1.3"
   "`pgcrypto <https://www.postgresql.org/docs/current/pgcrypto.html>`_","cryptographic functions","1.3","1.3","1.3","1.3","1.3"
   "`rum <https://github.com/postgrespro/rum>`_","RUM index access method","1.3","1.3","1.3","1.3","1.3"
   "`unaccent <https://www.postgresql.org/docs/current/unaccent.html>`_","text search dictionary that removes accents","1.1","1.1","1.1","1.1","1.1"

Auditing
------------------------

.. csv-table:: Auditing extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`insert_username <https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.47.7>`_","functions for tracking who changed a table","1","1","1","1","1"
   "`moddatetime <https://www.postgresql.org/docs/10/contrib-spi.html#id-1.11.7.46.9>`_","functions for tracking last modification time","1","1","1","1","1"
   "`pgaudit <https://www.pgaudit.org/>`_","provides auditing functionality","1.6.1","1.5.1","1.4.2","1.3.3"
   "`tcn <https://www.postgresql.org/docs/current/tcn.html>`_","Triggered change notifications","1","1","1","1","1"

Geographical features
---------------------

.. csv-table:: Geographical features extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`address_standardizer <https://postgis.net/docs/standardize_address.html>`_","Used to parse an address into constituent elements. Generally used to support geocoding address normalization step.","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"
   "`address_standardizer_data_us <https://postgis.net/docs/standardize_address.html>`_","Address Standardizer US dataset example","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"
   "`earthdistance <https://www.postgresql.org/docs/current/earthdistance.html>`_","calculate great-circle distances on the surface of the Earth","1.1","1.1","1.1","1.1","1.1"
   "`pgrouting <https://github.com/pgRouting/pgrouting>`_","pgRouting Extension","3.1.3","3.1.3","3.1.3","3.1.3","3.1.3"
   "`postgis <https://postgis.net/>`_","PostGIS geometry and geography spatial types and functions","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"
   "`postgis_legacy <https://postgis.net/>`_","Legacy functions for PostGIS","3.1","3.1","3.1","3.1","3.1"
   "`postgis_raster <https://postgis.net/docs/RT_reference.html>`_","PostGIS raster types and functions","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"
   "`postgis_sfcgal <http://postgis.net/docs/reference.html#reference_sfcgal>`_","PostGIS SFCGAL functions","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"
   "`postgis_tiger_geocoder <https://postgis.net/docs/Extras.html#Tiger_Geocoder>`_","PostGIS tiger geocoder and reverse geocoder","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"
   "`postgis_topology <https://postgis.net/docs/Topology.html>`_","PostGIS topology spatial types and functions","3.1.4","3.1.4","3.1.4","3.1.4","3.1.4"

Procedural language
-------------------

.. csv-table:: Procedural language extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`plcoffee <https://github.com/plv8/plv8>`_","PL/CoffeeScript (v8) trusted procedural language","","","","","1.4.4"
   "`plls <https://github.com/plv8/plv8>`_","PL/LiveScript (v8) trusted procedural language","","","","","1.4.4"
   "`plperl <https://www.postgresql.org/docs/current/plperl.html>`_","PL/Perl procedural language","1","1","1","1","1"
   "`plperlu <https://www.postgresql.org/docs/current/plperl-trusted.html>`_","PL/PerlU untrusted procedural language","1","1","1","1","1"
   "`plpgsql <https://www.postgresql.org/docs/current/plpgsql.html>`_","PL/pgSQL procedural language","1","1","1","1","1"
   "`plv8 <https://github.com/plv8/plv8>`_","PL/JavaScript (v8) trusted procedural language","","","","","1.4.4"

Connectivity
------------

.. csv-table:: Connectivity extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`dblink <https://www.postgresql.org/docs/current/contrib-dblink-function.html>`_","connect to other PostgreSQL databases from within a database","1.2","1.2","1.2","1.2","1.2"
   "`file_fdw <https://www.postgresql.org/docs/current/file-fdw.html>`_","foreign-data wrapper for flat file access","1","1","1","1","1"
   "`postgres_fdw <https://www.postgresql.org/docs/current/postgres-fdw.html>`_","foreign-data wrapper for remote PostgreSQL servers","1.1","1","1","1","1"

Utilities
---------

.. csv-table:: Utilities extensions available in Aiven for PostgreSQL
   :header: "Name", "Description", "Version (14)", "Version (13)", "Version (12)", "Version (11)", "Version (10)"

   "`aiven_extras <https://github.com/aiven/aiven-extras>`_","aiven_extras","1.1.5","1.1.5","1.1.5","1.1.5","1.1.5"
   "`amcheck <https://www.postgresql.org/docs/current/amcheck.html>`_","functions for verifying relation integrity","1.3","1.2","1.2","1.1","1"
   "`autoinc <https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.47.6>`_","functions for autoincrementing fields","1","1","1","1","1"
   "`bool_plperl <https://www.postgresql.org/docs/current/plperl-funcs.html>`_","transform between bool and plperl","1","1"
   "`bool_plperlu <https://www.postgresql.org/docs/current/plperl-funcs.html>`_","transform between bool and plperlu","1","1"
   "`hstore_plperl <https://www.postgresql.org/docs/current/hstore.html>`_","transform between hstore and plperl","1","1","1","1","1"
   "`hstore_plperlu <https://www.postgresql.org/docs/current/hstore.html>`_","transform between hstore and plperlu","1","1","1","1","1"
   "`intagg <https://www.postgresql.org/docs/current/intagg.html>`_","integer aggregator and enumerator (obsolete)","1.1","1.1","1.1","1.1","1.1"
   "`intarray <https://www.postgresql.org/docs/current/intarray.html>`_","functions, operators, and index support for 1-D arrays of integers","1.5","1.3","1.2","1.2","1.2"
   "`jsonb_plperl <https://www.postgresql.org/docs/current/datatype-json.html>`_","transform between jsonb and plperl","1","1","1","1"
   "`jsonb_plperlu <https://www.postgresql.org/docs/current/datatype-json.html>`_","transform between jsonb and plperlu","1","1","1","1"
   "`lo <https://www.postgresql.org/docs/current/lo.html>`_","Large Object maintenance","1.1","1.1","1.1","1.1","1.1"
   "`old_snapshot <https://www.postgresql.org/docs/current/oldsnapshot.html>`_","utilities in support of old_snapshot_threshold","1"
   "`pageinspect <https://www.postgresql.org/docs/current/pageinspect.html>`_","inspect the contents of database pages at a low level","1.9","1.8","1.7","1.7","1.6"
   "`pg_buffercache <https://www.postgresql.org/docs/current/pgbuffercache.html>`_","examine the shared buffer cache","1.3","1.3","1.3","1.3","1.3"
   "`pg_cron <https://github.com/citusdata/pg_cron>`_","Job scheduler for PostgreSQL","1.3","1.3","1.3","1.3","1.3"
   "`pg_freespacemap <https://www.postgresql.org/docs/current/pgfreespacemap.html>`_","examine the free space map (FSM)","1.2","1.2","1.2","1.2","1.2"
   "`pg_partman <https://github.com/pgpartman/pg_partman>`_","Extension to manage partitioned tables by time or ID","4.6.0","4.6.0","4.6.0","4.6.0","4.6.0"
   "`pg_prewarm <https://www.postgresql.org/docs/current/pgprewarm.html>`_","prewarm relation data","1.2","1.2","1.2","1.2","1.1"
   "`pg_repack <https://pgxn.org/dist/pg_repack/1.4.6/>`_","Reorganize tables in PostgreSQL databases with minimal locks","1.4.7","1.4.7","0.2.1","0.2.1","0.2.1"
   "`pg_stat_statements <https://www.postgresql.org/docs/current/pgstatstatements.html>`_","track planning and execution statistics of all SQL statements executed","1.9","1.8","1.7","1.6","1.6"
   "`pg_surgery <https://www.postgresql.org/docs/current/pgsurgery.html>`_","extension to perform surgery on a damaged relation","1"
   "`pg_visibility <https://www.postgresql.org/docs/current/pgvisibility.html>`_","examine the visibility map (VM) and page-level visibility info","1.2","1.2","1.2","1.2","1.2"
   "`pgrowlocks <https://www.postgresql.org/docs/current/pgrowlocks.html>`_","show row-level locking information","1.2","1.2","1.2","1.2","1.2"
   "`pgstattuple <https://www.postgresql.org/docs/current/pgstattuple.html>`_","show tuple-level statistics","1.5","1.5","1.5","1.5","1.5"
   "`refint <https://www.postgresql.org/docs/current/contrib-spi.html#id-1.11.7.47.5>`_","functions for implementing referential integrity (obsolete)","1","1","1","1","1"
   "`sslinfo <https://www.postgresql.org/docs/current/sslinfo.html>`_","information about SSL certificates","1.2","1.2","1.2","1.2","1.2"
   "`tablefunc <https://www.postgresql.org/docs/current/tablefunc.html>`_","functions that manipulate whole tables, including crosstab","1","1","1","1","1"
   "`timetravel <https://www.postgresql.org/docs/6.3/c0503.htm>`_","functions for implementing time travel","","","","1","1"
   "`tsm_system_rows <https://www.postgresql.org/docs/current/tsm-system-rows.html>`_","TABLESAMPLE method which accepts number of rows as a limit","1","1","1","1","1"
   "`tsm_system_time <https://www.postgresql.org/docs/current/tsm-system-time.html>`_","TABLESAMPLE method which accepts time in milliseconds as a limit","1","1","1","1","1"
   "`xml2 <https://www.postgresql.org/docs/current/xml2.html>`_","XPath querying and XSLT","1.1","1.1","1.1","1.1","1.1"

