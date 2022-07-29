`_mysql_reclaim_disk_space`

Reclaim disk space
==================

You can configure Innodb to release disk space back to the operating system by running the ``OPTIMIZE TABLE`` command.

.. note::
    Note that `under certain conditions <https://dev.mysql.com/doc/refman/8.0/en/optimize-table.html#optimize-table-innodb-details>`_ (e.g. including the presence of a ``FULLTEXT`` index), the command ``OPTIMIZE TABLE`` will `copy <https://dev.mysql.com/doc/refman/8.0/en/alter-table.html#alter-table-performance>`_ the data to a new table containing just the current data, and then drop and rename the new table to match the old one. During this process, data modification will be blocked. This will require enough free space to store two copies of the current data at once.

To ensure that the space is also reclaimed on standby nodes, run the command as below without any additional modifiers like ``NO_WRITE_TO_BINLOG`` or ``LOCAL``::

    ``OPTIMIZE TABLE defaultdb.mytable;``

If you do not have enough free space to run the ``OPTIMIZE TABLE`` command, then you can:

- Start by optimizing smaller tables to free up space. After, you can proceed with optimizing on larger tables.

- Temporarily upgrade to a larger service plan to get access to more disk space. You can downgrade your plan again afterward. Read more on how  :ref:`_scale_your_service` for that.

.. note::

    When you perform a temporary upgrade, it may require waiting for a smaller backup to be taken place before downgrading the plan again.



