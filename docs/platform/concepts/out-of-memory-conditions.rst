Out of memory conditions
========================

**Many processes request more memory from the kernel then they will ever use or need.**

Because of this the kernel over allocates memory (heuristic overcommit), which allows it to satisfy multiple processes requesting more memory then is available, in the knowledge that either they will never use it, or that they will have freed it by the time any other process actually needs it.

However, if enough processes start using all their allocated memory simultaneously there may not be enough physical memory available and an ``Out Of Memory`` (``OOM``) condition occurs. 

*This situation is critical and must be resolved immediately.*


The Out of Memory Killer
------------------------

The solution that the Linux kernel employs is to invoke the ``Out of Memory Killer`` (or ``OOM Killer``), a Linux kernel process that reviews all running processes and kills one or more of them in order to free up system memory in order keep the system running.


Which process will be killed?
-----------------------------

The ``OOM Killer`` selects process to kill based on an ``oom_score``; a calculation that balances how much memory the process is using with how long the process has been running.

Processes that have been running for a long time are less likely to be killed. Subprocesses are summed with parent processes in terms of memory usage, so a process which forks a large number of subprocesses, but itself does not use a lot of memory, may still be killed.

*In most instances, the hosted data service, or a child process, will have the highest memory footprint and be a prime candidate for termination when the OOM Killer inspects the running processes.*

Aiven's cloud data platform leverages kernel namespaces (or containers) to isolate processes from each other. Isolation has several benefits, including: 

- A smaller footprint for security‑related concerns
- A smaller blast radius for failure
- Greater control of system resources

Left unchecked, the ``OOM Killer`` may opt to kill the primary service. This is undesirable as unclean termination of the primary service can lead to data loss, inconsistency, or corrupted backups. 

Further, if Aiven's management platform detects that the primary service is unavailable for **60 seconds**, the service will be marked as down and a failover will occur. 

To mitigate this scenario, namespaces are used, :doc:`some with additional memory limits <service-memory-limits>`, in combination with an ``oom_score_adjust`` on the primary process, to coax the ``OOM Killer`` into selection of less critical processes. 

This will still result in a service restart, but in a more controlled process, where the database is shut down, rather than killed; exposure to data loss is limited and recovery is faster when the service restarts, often avoiding failover.

.. warning:: Out of Memory conditions can still lead to unexpected behavior, including data unavailable or data loss conditions. 


How to avoid the OOM Killer
---------------------------

The OOM killer only runs when the system is critically low on memory, so to avoid it running you need to either reduce your memory usage or increase the available memory.

For most databases, the service memory footprint can often be reduced by:

- Reducing concurrency or implementing connection pooling
- Tuning queries to limit result sets
- Tuning indexes for query load
- Dropping unused objects from storage

In cases where the working set no longer fits into memory, consider :doc:`scaling your service <../howto/scale-services>`.




