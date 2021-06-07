Connect with ``psql``
========================

``psql`` is a command line tool for PostgreSQL, useful to manage and query your database.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``POSTGRESQL_URI``      URL for PostgreSQL connection, from the service overview page
==================      =============================================================

Pre-requisites
''''''''''''''

For this example you'll need ``psql`` already installed on your computer

Connect to PostgreSQL
'''''''''''''''''''''

From your terminal, execute the following code::

    psql POSTGRESQL_URI

The output should look like the following if the connection is successful::

    psql (13.2, server 13.3)
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.

    defaultdb=>

To confirm that the connection is working, issue the following code checking the PostgreSQL version::

    select version();

The result will be similar to the following::

                                        version
    --------------------------------------------------------------------------------------------
    PostgreSQL 13.3 on x86_64-pc-linux-gnu, compiled by gcc, a 68c5366192 p 6520304dc1, 64-bit
    (1 row)
