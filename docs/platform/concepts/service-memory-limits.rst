Service memory limits
=====================

The practical memory limit will always be less than the service physical memory limit.

**All services are subject to operating overhead:**

- A small amount of memory is required by the operating system kernel to manage system resources, including networking functions and disk buffers.
- Aiven's cloud data platform requires memory to monitor availability, provide metrics, logging and manage backups.
- Services may utilize optional components, service integrations, connection pooling, or plug-ins that also consume system resources.

In most instances, the combined overhead is negligible; however, it is **critically important to maintain availability**.

If a service consumes too much memory, the operating system, or management layer, including backups and availability monitoring, may fail status checks or operations due to resource contention.
In severe instances, the node may fail completely with an :doc:`Out Of Memory <out-of-memory-conditions>` condition. 

For database services with unbounded memory allocation, a memory limit is placed on the primary service.

.. include:: /includes/services-memory-capped.rst
