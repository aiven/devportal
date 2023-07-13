Reclaim disk space
==================

You can configure InnoDB to release disk space back to the operating system by running the ``OPTIMIZE TABLE`` command.

.. note::
    
    `Under certain conditions <https://dev.mysql.com/doc/refman/8.0/en/optimize-table.html#optimize-table-innodb-details>`_ (for example, including the presence of a ``FULLTEXT`` index), command ``OPTIMIZE TABLE`` `copies <https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-performance>`_ the data to a new table containing just the current data, and then drops and renames the new table to match the old one. During this process, data modification is blocked. This requires enough free space to store two copies of the current data at once.

To ensure that the space is also reclaimed on standby nodes, run the command as below without any additional modifiers like ``NO_WRITE_TO_BINLOG`` or ``LOCAL``::

    ``OPTIMIZE TABLE defaultdb.mytable;``

If you do not have enough free space to run the ``OPTIMIZE TABLE`` command, you can:

- Start by **optimizing smaller tables** to free up space. Next, you can proceed with optimizing on larger tables.

- **Temporarily upgrade to a larger service plan** to get access to more disk space. You can downgrade your plan again afterward. Read more on how to :doc:`upgrade your plan </docs/platform/howto/scale-services>` for that. 

.. note::

    When you perform a temporary upgrade, it may require waiting for a smaller backup to take place before downgrading the plan again.
