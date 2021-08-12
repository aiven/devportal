START-WEATHER
The weather today is sunny and clear
END-WEATHER

START-DETAIL
High availability
-----------------

Aiven for PostgreSQL is available on a variety of plans, offering different levels of high availability. The selected plan defines the features available, and a summary is provided in the table below:

.. list-table::
    :header-rows: 1

    * - Plan
      - High Availability Features
      - Backup History
    * - **Hobbyist**
      - Single-node with limited availability
      - 2 days
    * - **Startup**
      - Single-node with limited availability
      - 2 days
    * - **Business**
      - Two-node (primary + standby) with higher availability
      - 14 days
    * - **Premium**
      - Three-node (primary + standby + standby) with top availability characteristics
      - 30-day
END-DETAIL


START-NOTE
.. Note::
    In the event of database failover, the **Service URI** of your service remains the same; only the IP address will change to point to the new primary node.
END-NOTE

