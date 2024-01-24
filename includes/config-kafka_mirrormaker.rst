
``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``service_log``
---------------
*['boolean', 'null']*

**Service logging** Store logs for the service so that they are available in the HTTP API and console.



``static_ips``
--------------
*boolean*

**Static IP addresses** Use static public IP addresses



``kafka_mirrormaker``
---------------------
*object*

**Kafka MirrorMaker configuration values** 

``refresh_topics_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Refresh topics and partitions** Whether to periodically check for new topics and partitions. Defaults to 'true'.

``refresh_topics_interval_seconds``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Frequency of topic and partitions refresh** Frequency of topic and partitions refresh in seconds. Defaults to 600 seconds (10 minutes).

``refresh_groups_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Refresh consumer groups** Whether to periodically check for new consumer groups. Defaults to 'true'.

``refresh_groups_interval_seconds``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Frequency of group refresh** Frequency of consumer group refresh in seconds. Defaults to 600 seconds (10 minutes).

``sync_group_offsets_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Sync consumer group offsets** Whether to periodically write the translated offsets of replicated consumer groups (in the source cluster) to __consumer_offsets topic in target cluster, as long as no active consumers in that group are connected to the target cluster

``sync_group_offsets_interval_seconds``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Frequency of consumer group offset sync** Frequency at which consumer group offsets are synced (default: 60, every minute)

``emit_checkpoints_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Emit consumer group offset checkpoints** Whether to emit consumer group offset checkpoints to target cluster periodically (default: true)

``emit_checkpoints_interval_seconds``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Frequency of consumer group offset checkpoints** Frequency at which consumer group offset checkpoints are emitted (default: 60, every minute)

``sync_topic_configs_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Sync remote topics** Whether to periodically configure remote topics to match their corresponding upstream topics.

``tasks_max_per_cpu``
~~~~~~~~~~~~~~~~~~~~~
*integer*

**Maximum number of MirrorMaker tasks (of each type) per service CPU** 'tasks.max' is set to this multiplied by the number of CPUs in the service.

``offset_lag_max``
~~~~~~~~~~~~~~~~~~
*integer*

**Maximum offset lag before it is resynced** How out-of-sync a remote partition can be before it is resynced.

``groups``
~~~~~~~~~~
*string*

**Comma-separated list of consumer groups to replicate** Consumer groups to replicate. Supports comma-separated group IDs and regexes.

``groups_exclude``
~~~~~~~~~~~~~~~~~~
*string*

**Comma-separated list of group IDs and regexes to exclude from replication** Exclude groups. Supports comma-separated group IDs and regexes. Excludes take precedence over includes.



