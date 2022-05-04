Understand MySQL high memory usage
==================================
Aiven for MySQL users can expect a high memory usage. It is important to notice that the high memory usage on MySQL Aiven services does not indicate any particular issue. 

In this article, we explain the reasons for the **high memory usage** on Aiven for MySQL services.

InnoDB buffer pools
-------------------
According to the `MySQL official documentation <https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html>`_:

    The buffer pool is an area in main memory where InnoDB caches table and index data as it is accessed. The buffer pool permits frequently used data to be accessed directly from memory, which speeds up processing. On dedicated servers, up to 80% of physical memory is often assigned to the buffer pool.

As you can see the MySQL InnoDB buffer pools are **pre-allocated** and shown as **used memory** even without user activity or stored data in the database. This pre-allocated memory contributes to the high memory usage for Aiven for MySQL services.

Management overhead and backup memory
-------------------------------------
Another factor that contributes to the high memory usage is that all nodes have some base CPU consumption due to management overhead (about 5% of a single CPU core). In addition to the overhead management, a sufficient amount of memory is reserved to run extra utilities for database backups. 
