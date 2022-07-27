Service memory limits
=====================

**All services are subject to operating overhead:**

- A small amount of memory is required by the operating system kernel to manage system resources, including networking functions and disk buffers.
- Aiven's cloud data platform also requires memory to monitor availability, provide metrics, logging and manage backups.
- Some services utilize optional integrations, connection pooling, or plug-ins components that also consume system resources.

In most instances, the combined overhead is negligible; however, it is **critically important to maintain availability**.

If a service consumes too much memory, the operating system or management components, including backups and availability monitoring, may fail status checks or timed operations due to limited system resources. In severe instances, the node may fail completely with an ``Out of Memory`` condition. 

A memory limit is applied to the primary process of the following Aiven services:

- InfluxDB®
- MySQL
- PostgreSQL®

With all new instances, a limit of 80% of available memory (RAM - 350MB) is assigned to the primary process, with the remainder reserved for operating overhead and mitigation of potential ``Out of Memory`` conditions.

.. note:: Reserved memory for non-service use is capped to a maximum of 4GB.

.. note:: For MySQL, a minimum of 600MB is always guaranteed.

