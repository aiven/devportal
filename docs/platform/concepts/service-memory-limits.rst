Service memory limits
=====================

The practical memory limit will always be less than the service physical memory limit.

**All services are subject to operating overhead:**

- A small amount of memory is required by the operating system kernel to manage system resources, including networking functions and disk cache.
- Aiven's cloud data platform requires memory to monitor availability, provide metrics, logging and manage backups.

A server (or node) **usable memory** can be calculated as: 
  
  |vm_usable_memory| 

.. important:: This ``overhead`` is currently calculated as: |vm_overhead|

Services may utilize optional components, service integrations, connection pooling, or plug-ins, which are not included in overhead calculations.

If a service is overcommitted, the operating system, management layer, backups or availability monitoring, may fail status checks or operations due to resource contention. In severe instances, the node may fail completely with an :doc:`Out Of Memory <out-of-memory-conditions>` condition. 

.. include:: /includes/services-memory-capped.rst
.. include:: /includes/platform-variables.rst