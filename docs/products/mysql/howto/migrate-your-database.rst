Migrate your MySQL data to Aiven for MySQL
==========================================

This article explains how to to migrate your data to Aiven with the `<mysqldump> https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html`_ utility.

The mysqldump client is a utility that performs logical backups, producing a set of SQL statements that can be run to reproduce the original schema objects, table data, or both. It dumps one or more MySQL database for backup or transfer to another SQL server. The mysqldump command can also generate output in CSV, other delimited text, or XML format.


.. tip::

    For the dumping process, we recommend you to pick a plan size that is large and powerful enough, so you can limit the downtime during migration.

Prerequisites
-------------

* An Aiven account with a Aiven for MySQL running.

* `<mysqldump> https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html`_ installed
  
* A MySQL database that we aim to copy our data from. We will refer to it as ``source-db``
  
* A target MySQL database that we aim to dump our ``source-db`` data to. We will refer to it as ``target-db``
  
.. note::

    To simplify the test, we will create Aiven for MySQL databases for both, ``source-db`` and ``target-db``. You can create the databases by going to your running service for **Aiven for MySQL** > **Databases** > **Create a new database**.


Variables
'''''''''

To migrate or copy data:

#. Create a hosted Aiven for OpenSearch service.