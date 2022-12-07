Checklist
##########

* MM2 does not guarantee absolute ordering, it only guarantees key ordering
* Aiven’s MM2 service currently has a bug whereby topic replication factor and min.insync.replicas are reset
   * In order to work around this, these values can be reset after the MM2 replication flows have been created
   * This bug is expected to be fixed Q4/22
* Offsets may not be preserved upon mirroring. This will be the case if some offsets have been deleted either through data age off or compaction.
* MM2 will preserve the correlation between consumer offsets between clusters.