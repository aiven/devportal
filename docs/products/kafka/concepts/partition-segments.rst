Partition segments
==================

Apache Kafka® divides topics partition data into **segment** files (with ``.log`` suffix) stored on the file system. Each segment file is named using the offset of the first message (a.k.a. **base offset**) contained. For example, the segment file ``04.log`` contains the message with offset ``4`` as first entry.

The last segment in the partition is called the **active segment** and it is the only segment to which new messages are appended to.

In the example above the topic partition is divided into multiple segments, with ``06.log`` being the active one:

**01.log**

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 1
    - 1001 
    - 4 Privet Dr
  * - 2
    - 1002
    - 221B Baker Street
  * - 3
    - 1003
    - Milkman Road

**04.log**

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 4
    - 1002
    - 21 Jump St
  * - 5
    - 1001
    - Paper St

**06.log (active segment)**

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 6
    - 1001
    - Paper Road 21

When the segment file reaches a certain size or age, Apache Kafka will create a new segment file. This can be controlled by the following settings:

-  ``segment.bytes`` : creates a new segment when current segment becomes greater than this size. This setting can be set during topic creation and defaults to 1GB.

-  ``segment.ms`` : forces the segment to roll over and create a new one when the segment becomes older than this value.
