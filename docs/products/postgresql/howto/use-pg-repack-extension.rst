Use the PostgreSQL® ``pg_repack`` extension
===========================================

``pg_repack`` is a PostgreSQL® extension that allows you to efficiently reorganize tables to remove any excess bloat the tables have accumulated. Reorganizing a table may take some time, but ``pg_repack`` tries to minimize the locks required to continue online operations.

.. note:: 
  Before you install the ``pg_repack`` extension, verify the version of the extension is supported on the PostgreSQL version you are using. For information on supported versions, see `pg_repack <https://reorg.github.io/pg_repack/>`_ documentation.   

To use the ``pg_repack`` extension: 

1. Connect to the database as ``avnadmin`` user, and run the following command to create the extension: 
:: 
  CREATE EXTENSION pg_repack;

2. Run the ``pg_repack`` command on the table to reorganize it. 
::
  pg_repack -k -U <username> -h <hostname> -p <port> -d <database name> -t <table name>;   

.. note:: 
  - Using ``-k`` skips the superuser checks in the client. This setting is useful when using pg_repack on platforms that support running it as non-superusers.
  - The target table must have a PRIMARY KEY, or at least a UNIQUE total index on a NOT NULL column.


.. seealso::
  - For more information, see `pg_repack <https://reorg.github.io/pg_repack/>`_ documentation.
  - For more information on managing extensions, see :doc:`Install or update extension <../howto/manage-extensions>`.
  

