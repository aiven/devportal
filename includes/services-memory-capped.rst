Services with memory limits
-----------------------------------------------------

A memory limit is applied to the primary process of the following Aiven services:

- InfluxDB®
- MySQL
- PostgreSQL®

With all new instances, a limit of 80% of available memory (RAM - 350MB) is assigned to the primary process, with the remainder reserved for operating overhead and page cache.

.. note:: Reserved memory for non-service use is capped to a maximum of 4GB.

.. note:: For MySQL, a minimum of 600MB is always guaranteed.
