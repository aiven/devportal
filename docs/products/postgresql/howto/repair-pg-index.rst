Identify and repair issues with PostgreSQL indexes with ``REINDEX``
===================================================================

PostgreSQL indexes can become corrupted due to a variety of reasons including software bugs, hardware failures or unexpected duplicated data. ``REINDEX`` allows you to rebuild the index in such situations.

Rebuild non-unique indexes
--------------------------

You can rebuild corrupted indexes that do not have ``UNIQUE`` in their definition using the following command, that creates a new index replacing the old one:

::

    REINDEX INDEX <index-name>;

.. Warning::

    Re-indexing applies locks to the table and may interfere with normal use of the database. 
    In some cases, it can be useful to manually build a second index concurrently alongside the old index and then remove the old index:

    ::

        CREATE INDEX CONCURRENTLY foo_index_new ON table_a (...);
        DROP INDEX CONCURRENTLY foo_index_old;
        ALTER INDEX foo_index_new RENAME TO foo_index;

You can run the ``REINDEX`` command for:

* all indexes of a table (``REINDEX TABLE``)
* all indexes in the entire database (``REINDEX DATABASE``).

For more information on the ``REINDEX`` command, see the `PostgreSQL documentation page <https://www.postgresql.org/docs/current/sql-reindex.html>`_. 

Rebuild unique indexes
----------------------

A ``UNIQUE`` index works on top of one or more columns whose combination is unique in a table. In situations when the index is corrupted or disabled and duplicated physical rows appear in the table, breaking the uniqueness constraint of the index, then index rebuilding with ``REINDEX`` will fail. To solve such problem, you'll first need to remove the duplicated rows from the table before attempting to rebuild the index.

Identify conflicting duplicated rows
''''''''''''''''''''''''''''''''''''

To identify conflicting duplicate rows, you need to run a query that counts the number of rows for each combination of columns included in the index definition. 

For example, the following ``route`` table has an ``unique_route_index`` index defining unique rows based on the combination of the ``source`` and ``destination`` columns:

::

    CREATE TABLE route(
        source TEXT, 
        destination TEXT, 
        description TEXT
        );

    CREATE UNIQUE INDEX unique_route_index 
        ON route (source, destination);

If the ``unique_route_index`` is corrupted, you can find duplicated rows in the ``route`` table by issuing the following query:

::

    SELECT 
        source, 
        destination, 
        count 
    FROM 
        (SELECT 
            source, 
            destination, 
            COUNT(*) AS count 
        FROM route 
        GROUP BY 
            source, 
            destination) AS foo 
    WHERE count > 1;    

The above query groups the data by the same ``source`` and ``destination`` fields defined in the index, and filters any entries with more than one occurrence.

The resulting rows identify the problematic entries, which must be resolved manually by deleting or merging the entries until no duplicates exist. 
Once duplicated entries are removed, you can use the ``REINDEX`` command to rebuild the index.
