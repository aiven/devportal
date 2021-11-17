``avn service topic``
==================================================

Here you’ll find the full list of commands for ``avn service topic``.


Manage Aiven for Apache Kafka topics
--------------------------------------------------------

``avn service topic-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new Kafka topic on the specified Aiven for Apache Kafka service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``topic``
    - The name of the topic
  * - ``partitions``
    - The number of topic partitions
  * - ``--replication``
    - The topic replication factor
  * - ``--min-insync-replicas``
    - The minimum required nodes In Sync Replicas (ISR) for the topic/partition (default: 1)
  * - ``--retention``
    - The retention period in hours (default: unlimited)
  * - ``--retention-bytes``
    - The retention limit in bytes (default: unlimited)
  * - ``--cleanup-policy``
    - The topic cleanup policy; can be either ``delete`` or ``compact``.
  * - ``-tag KEY[=VALUE]``
    - Topic tagging

**Example:** Create a new topic named ``invoices`` with ``3`` partitions and ``2`` as replication factor in the ``demo-kafka`` service. Furthermore tag the topic with ``BU=FINANCE`` tag.

::

  avn service topic-create demo-kafka invoices  \
    --partitions 3                              \
    --replication 2                             \
    --tag BU=FINANCE

``avn service topic-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes a Kafka topic on the specified Aiven for Apache Kafka service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``topic``
    - The name of the topic

**Example:** Delete the topic named ``invoices`` in the ``demo-kafka`` service.

::

    avn service topic-delete demo-kafka invoices

``avn service topic-get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves Kafka topic on the specified Aiven for Apache Kafka service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``topic``
    - The name of the topic

**Example:** Retrieve the information about a topic named ``invoices`` in the ``demo-kafka`` service.

::

    avn service topic-get demo-kafka invoices

An example of ``avn service topic-get`` output:

.. code:: text

    PARTITION  ISR  SIZE  EARLIEST_OFFSET  LATEST_OFFSET  GROUPS
    =========  ===  ====  ===============  =============  ======
    0          2    0     0                0              0
    1          2    null  0                0              0
    2          2    0     0                0              0

    (No consumer groups)

``avn service topic-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists Kafka topics on the specified Aiven for Apache Kafka service together with the following information:

* partitions
* replication
* min in-sync replicas
* retention bytes
* retention hours
* cleanup policy
* tags

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** Retrieve list of topics available in the ``demo-kafka`` service.

::

    avn service topic-list demo-kafka

An example of ``avn service topic-get`` output:

.. code:: text

    TOPIC_NAME  PARTITIONS  REPLICATION  MIN_INSYNC_REPLICAS  RETENTION_BYTES  RETENTION_HOURS  CLEANUP_POLICY  TAGS
    ==========  ==========  ===========  ===================  ===============  ===============  ==============  ==========
    bills       3           2            1                    -1               unlimited        delete
    invoices    3           2            1                    -1               168              delete          BU=FINANCE
    orders      2           3            1                    -1               unlimited        delete


``avn service topic-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Updates a Kafka topic on the specified Aiven for Apache Kafka service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``topic``
    - The name of the topic
  * - ``partitions``
    - The number of topic partitions
  * - ``--replication``
    - The topic replication factor
  * - ``--min-insync-replicas``
    - The minimum required nodes In Sync Replicas (ISR) for the topic/partition (default: 1)
  * - ``--retention``
    - The retention period in hours (default: unlimited)
  * - ``--retention-bytes``
    - The retention limit in bytes (default: unlimited)
  * - ``--cleanup-policy``
    - The topic cleanup policy; can be either ``delete`` or ``compact``.
  * - ``-tag KEY[=VALUE]``
    - Topic tagging
  * - ``--untag KEY``
    - Topic tag to remove

**Example:** Update the topic named ``invoices`` in the ``demo-kafka`` service. Set ``4`` partitions and ``3`` as replication factor. Furthermore remove the ``BU`` tag and add a new ``CC=FINANCE_DE`` tag.

::

  avn service topic-update demo-kafka invoices  \
    --partitions 4                              \
    --replication 3                             \
    --tag CC=FINANCE_DE                         \
    --untag BU