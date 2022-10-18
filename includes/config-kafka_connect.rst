
``additional_backup_regions``
-----------------------------
*array*

**Additional Cloud Regions for Backup Replication** 



``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips``
--------------
*boolean*

**Static IP addresses** Use static public IP addresses



``kafka_connect``
-----------------
*object*

**Kafka Connect configuration values** 

``connector_client_config_override_policy``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**Client config override policy** Defines what client configurations can be overridden by the connector. Default is None

``consumer_auto_offset_reset``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**Consumer auto offset reset** What to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server. Default is earliest

``consumer_fetch_max_bytes``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum amount of data the server should return for a fetch request** Records are fetched in batches by the consumer, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that the consumer can make progress. As such, this is not a absolute maximum.

``consumer_isolation_level``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**Consumer isolation level** Transaction read isolation level. read_uncommitted is the default, but read_committed can be used if consume-exactly-once behavior is desired.

``consumer_max_partition_fetch_bytes``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum amount of data per-partition the server will return.** Records are fetched in batches by the consumer.If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch will still be returned to ensure that the consumer can make progress. 

``consumer_max_poll_interval_ms``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum delay between polls when using consumer group management** The maximum delay in milliseconds between invocations of poll() when using consumer group management (defaults to 300000).

``consumer_max_poll_records``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum number of records returned by a single poll** The maximum number of records returned in a single call to poll() (defaults to 500).

``offset_flush_interval_ms``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The interval at which to try committing offsets for tasks** The interval at which to try committing offsets for tasks (defaults to 60000).

``offset_flush_timeout_ms``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Offset flush timeout** Maximum number of milliseconds to wait for records to flush and partition offset data to be committed to offset storage before cancelling the process and restoring the offset data to be committed in a future attempt (defaults to 5000).

``producer_compression_type``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**The default compression type for producers** Specify the default compression type for producers. This configuration accepts the standard compression codecs ('gzip', 'snappy', 'lz4', 'zstd'). It additionally accepts 'none' which is the default and equivalent to no compression.

``producer_max_request_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum size of a request in bytes** This setting will limit the number of record batches the producer will send in a single request to avoid sending huge requests.

``session_timeout_ms``
~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The timeout used to detect failures when using Kafka’s group management facilities** The timeout in milliseconds used to detect failures when using Kafka’s group management facilities (defaults to 10000).



``private_access``
------------------
*object*

**Allow access to selected service ports from private networks** 

``kafka_connect``
~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to kafka_connect with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access``
----------------------
*object*

**Allow access to selected service components through Privatelink** 

``jolokia``
~~~~~~~~~~~
*boolean*

**Enable jolokia** 

``kafka_connect``
~~~~~~~~~~~~~~~~~
*boolean*

**Enable kafka_connect** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Enable prometheus** 



``public_access``
-----------------
*object*

**Allow access to selected service ports from the public Internet** 

``kafka_connect``
~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to kafka_connect from the public internet for service nodes that are in a project VPC or another type of private network** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** 



