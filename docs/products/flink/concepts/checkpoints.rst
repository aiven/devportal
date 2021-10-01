Checkpoints
===========

To achieve resilience and fault tolerance, Apache Flink uses *checkpoints* with stateful functions. These checkpoints allow Flink to recover the state and position within the stream and provide failure-free execution for applications.

Essentially, a checkpoint creates a snapshot of the data stream and stores it. The snapshots then provide a mechanism to recover from unexpected job failures. Compared to traditional database systems, checkpoints are closer to recovery logs than to backups.

.. mermaid::

    graph TD;

        id5[/Older records in data stream/]-->id4[[Checkpoint barrier n-1]];
		id4 --- id3[(Checkpoint operator state)];
		id3 --- id2[[Checkpoint barrier n]];
		id2-->id1[/Newer records in data stream/];
        id3-->id6[(State backend)];


For more information, see the `Apache Flink documentation on checkpoints <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/ops/state/checkpoints/>`_.


