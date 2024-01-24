Troubleshoot Apache Kafka® consumer connections
#####################################################

Apache Kafka® consumers sometimes experience disconnections from a cluster node. On one hand, isolated occurrences are expected and well mitigated by the Apache Kafka® protocol, for example in case a partition leadership moved to a different node so the cluster remains available and balanced. On the other hand, repeating occurrences often raise concerns as they may impact consumer lag, and cluster performance. This article provides guidance to better identify and solve related issues.

What is observed
----------------
The client behaviour may vary depending on the library and version (remind to keep it up-to-date) in use. A typical consumer disconnection log is as follows:
``[AdminClient] Node 3 disconnected. (org.apache.kafka.clients.NetworkClient:937)``.

On the server, the GroupCoordinator undertakes some consumer-group re-balancing activity, as for example:
``Member ABC has left group my-app through explicit LeaveGroup; client reason: the consumer unsubscribed from all topics (kafka.coordinator.group.GroupCoordinator)`` or ``Timed out HeartbeatRequest``.

What it means
-------------
As they are processing messages, consumer instances may break, fail to request more local resources or to complete their current task on time. In this case, they leave their group either explicitly or by missing to send a heartbeat to the cluster.
    
As a consequence, the partition assignments of the consumer leaving the group are automatically re-affected to other consumers of the group, if they exist.

Why it occurs now (and never before)
--------------------------------------------------
* The consumer of a given topic ``A`` can get dropped because it relies on the same ``group.id`` as another consumer leaving or joining the group, even if the later consumes a totally different topic ``B``. Any rebalance triggered by any one consumer would still affect the other consumers in the group.
* Although consumer heartbeat and message processing are to be executed by 2 different client threads, the machine (on which the consumer application runs) can get overloaded and so it cannot send a heartbeat to the group coordinator after ``heartbeat.interval.ms`` (default: 3s) and before ``session.timeout.ms`` (default: 45s).
* If the consumer logic consists in expensive transformations or synchronous API calls, then your average single message processing time can dramatically increase, as in the following example scenarios:

  - The subsystem it depends on has an issue (ex. the destination server is not available).
  - The incoming message size increased.

* If the consumer lag has grown enough so that the consumer now processes ``max.poll.records`` (default: 500), then your average batch processing time and resources can dramatically increase, with the following consequences:

  - The consumer may run out-of-memory, resulting in an application crash.
  - The ``max.poll.interval.ms`` is exceeded between polls, so the consumer sends a LeaveGroup-request to the coordinator rather than sending a heartbeat.

How to solve it
---------------
* Make sure that your consumers are relying on a unique ``group.id``.
* It is generally a good idea to reduce ``max.poll.records`` or ``max.partition.fetch.bytes``, and then monitor if the situation improves.
* If it is required to stick to large batches (such as in windowing and data lake ingestion use-cases), then temporarily increasing ``session.timeout.ms`` might do the trick.
* Remind that ``session.timeout.ms`` must be in the allowable range as configured in the broker configuration by ``group.min.session.timeout.ms`` and ``group.max.session.timeout.ms``.
* It is recommended to configure ``heartbeat.interval.ms`` to be no more than a third of ``session.timeout.ms``. This ensures that even if a heartbeat or two are lost over the transient network, then the consumer is still considered alive.
* If the problem arose because of an increase in the volume of incoming messages, then we would advise to scale the consumer up/vertically or out/horizontally.

If the above didn't help you resolve your issue and you have further concerns or questions, feel free to contact `Aiven support <mailto:support@aiven.io>`_. 
