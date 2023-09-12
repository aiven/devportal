Trade-offs and limitations
============================

The main trade-off of tiered storage in Aiven for Apache Kafka® is the higher latency while accessing and reading data from remote storage compared to local disk storage. While adding local caching can partially solve this problem, it cannot eliminate the latency.

Limitations
-------------

* Tiered storage currently does not support compacted topics.
* If you enable tiered storage for a topic, you cannot deactivate it without losing data in the remote storage. To deactivate tiered storage, contact `Aiven support <mailto:support@aiven.io>`_. 
* Increasing the local retention threshold won't move segments already uploaded to remote storage back to local storage. This change only affects new data segments.
* If you enable tiered storage on a service, you can't migrate the service to a different region or cloud, except for moving to a virtual cloud in the same region. For migration to a different region or cloud, contact `Aiven support <mailto:support@aiven.io>`_.

