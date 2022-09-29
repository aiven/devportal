Use the PostgreSQL® ``pg_repack`` extension
===========================================

``pg_repack`` is a PostgreSQL® extension that allows you to efficiently reorganize tables to remove any excess bloat the tables have accumulated.  

.. note:: 
  Reorganizing a table may take some time, but ``pg_repack`` tries to minimize the locks required to continue online operations.

To use the ``pg_repack`` extension: 

1. Run the following command as ``avnadmin`` user: 
:: 
  CREATE EXTENSION pg_repack;

2. Run the command-line tool that comes with the extension on your machine. The command to reorganize a single table looks like the following:
::
  pg_repack -d connstr --no-superuser-check -t tablename   

This reorganizes the ``tablename`` table.

