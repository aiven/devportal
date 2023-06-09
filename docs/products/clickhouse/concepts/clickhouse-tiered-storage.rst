Tiered storage in Aiven for ClickHouse®
=======================================

Discover the tiered storage capability in Aiven for ClickHouse®. Learn how it works and explore its use cases. Check why you might need it and what benefits you get using it.

Overview
--------

The tiered storage feature introduces a method of organizing and storing data in two tiers for improved efficiency and cost optimization. The data is automatically moved to an appropriate tier based on your database's local disk usage. On top of this default data allocation mechanism, you can control the tier your data is stored in using custom data retention periods.

The tiered storage in Aiven for ClickHouse consists of the following two layers:

SSD - the first tier
  For fresh, frequently-accessed and valuable data, a fast but costly storage device

Object storage - the second tier
  For older, less valuable or rarely-accessed data, a slower but more affordable storage device

Why use it
----------

By :doc:`enabling </docs/products/clickhouse/howto/enable-tiered-storage>` and properly :doc:`configuring </docs/products/clickhouse/howto/configure-tiered-storage>` the tiered storage in Aiven for ClickHouse, you can use storage resources efficiently and, therefore, significantly reduce costs of storing data ingested into an Aiven for ClickHouse instance.

How it works
------------

With the tiered storage :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`, by default Aiven for ClickHouse stores data on your SSD until it reaches 80% of its capacity. After exceeding this size-based threshold, the data is stored in the object storage.

Optionally, you can :doc:`configure the time-based threshold </docs/products/clickhouse/howto/configure-tiered-storage>` in the tiered storage. Based on the time-based threshold, the data is moved for your SSD to the object storage after a specified time period.

.. mermaid:: 

    sequenceDiagram
        Application->>+SSD: writing data
        SSD->>Object storage: moving data based <br> on storage policies 
        par Application to SSD
            Application-->>SSD: querying data
        and Application to Object storage
            Application-->>Object storage: querying data
        end
        alt if stored in Object storage
            Object storage->>Application: reading data
        else if stored in SSD
            SSD->>Application: reading data
        end

.. note:: 
    
    Backups are taken for data that resides both on SSD and in object storage.

Typical use case
----------------

In your Aiven for ClickHouse service, there is a significant amount of data that is there for a while and is hardly ever accessed. It's stored on SSD and, thus, high-priced. You decide to :doc:`enable </docs/products/clickhouse/howto/enable-tiered-storage>` the tiered storage for your service to make your data storage more efficient and reduce the costs. For that purpose, you select a plan for your service that supports the tiered storage and you :doc:`enable </docs/products/clickhouse/howto/enable-tiered-storage>` the feature on particular tables. You :doc:`configure the time-based threshold </docs/products/clickhouse/howto/configure-tiered-storage>` the time-based threshold for controlling how your data is stored in the two layers.

.. _tiered-storage-limitations:

Limitations
-----------

* When :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`, the tiered storage feature cannot be deactivated.

  .. tip::

    As a workaround, you can create a new table (without enabling the tiered storage) and copy the data from the original table (with the tiered storage :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`) to the new table. As soon as the data is copied to the new table, you can remove the original table.

* With the tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`, it's not possible to connect to an external existing object storage or cloud storage bucket.

What's next
-----------

* :doc:`Enable tiered storage in Aiven for ClickHouse </docs/products/clickhouse/howto/enable-tiered-storage>`
* :doc:`Configure data retention thresholds for tiered storage </docs/products/clickhouse/howto/configure-tiered-storage>`

Related reading
---------------

* :doc:`Check data volume distribution between different disks </docs/products/clickhouse/howto/check-data-tiered-storage>`
* :doc:`Transfer data between SSD and object storage </docs/products/clickhouse/howto/transfer-data-tiered-storage>`
