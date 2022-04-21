MySQL memory usage
==================

MySQL InnoDB buffer pools are **pre-allocated** and shown as **used memory** even without user activity or stored data in the database. Because of this pre-allocated memory, it's expected high memory usage within all Aiven MySQL plans. 

.. important::
    
    The high memory usage on MySQL Aiven services does not indicate any particular issue. 

InnoDB buffer pools are set to values between 15% to 80% of total available memory. Smaller plans use a smaller percentage of total memory for buffer pools because the operating system and management infrastructure components and other MySQL features may consume a considerable portion of the available memory. A sufficient amount of free memory is reserved to run extra utilities while backing up the database.

The MySQL documentation references buffer pool sizing explicitly:

    A buffer pool is the memory area that holds cached InnoDB data for both tables and indexes. A larger buffer pool requires less disk I/O to access the same table data more than once. On a dedicated database server, you might set the buffer pool size to 80% of the machine's physical memory size.

All nodes also have some base CPU consumption due to management overhead (about 5% of a single CPU core).