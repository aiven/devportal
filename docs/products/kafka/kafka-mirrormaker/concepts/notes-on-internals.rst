Notes on internals
#############

Offset sync versus Checkpoints
--------------

The offset sync records are used internally to create the checkpoint records. Hence, the checkpoint messages contains everything that's needed for offset
translation.

``Discussion <https://lists.apache.org/thread/5ogswjbrf875dcg32h43dnzrqkksxpwj>``

Checkpoints capture the consumers state and are replicated. 

The structure:
``1. topic=primary.topic1
  2. partition=4
  3. group=consumer.group-2
  4. upstreamOffset=100
  5. offset=102``

OffsetSyncs are needed for checkpoints. They are just offset mapping between clusters. The structure:

``1. topic=primary.topic1
  2. partition=4
  3. upstreamOffset=100
  4. offset=102``

They are emitted when topics are out of sync.
See `Ryanne Dolan talk <https://www.confluent.io/kafka-summit-lon19/disaster-recovery-with-mirrormaker-2-0/>` for details.