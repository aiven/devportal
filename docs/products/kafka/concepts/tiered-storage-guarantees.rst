Guarantees
============
With Aiven for Apache Kafka®'s tiered storage, there are two primary types of data retention guarantees: *total retention* and *local retention*.

**Total retention**: Tiered storage ensures that your data will be available up to the limit defined by the total retention threshold, regardless of whether it is stored locally or remotely. This means that your data will not be deleted until the total retention threshold, whether on local or remote storage, is reached.

**Local retention**: Log segments are only removed from local storage after successfully being uploaded to remote storage, even if the data exceeds the local retention threshold.


Example
--------

Let's say you have a topic with a total retention threshold of 1000 bytes and a local retention threshold of 200 GB. This means that:

* All data for the topic will be retained, regardless of whether it is stored locally or remotely, as long as the total size of the data does not exceed 1000 GB.
* If the total size of the data exceeds 200 GB, Kafka will move older segments to the remote storage and delete them from the local disk. No data will be deleted from local storage until it has been safely transferred to remote storage.
* If the total size of the data exceeds 1000 GB, Apache Kafka will begin deleting the oldest data from remote storage.
