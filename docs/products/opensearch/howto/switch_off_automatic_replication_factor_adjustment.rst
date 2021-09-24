Switch off automatic replication factor adjustment
==================================================

For multi-node clusters, Aiven for OpenSearch automatically increases the ``number_of_replicas`` value to 1 if it is set to 0. This is done to avoid data loss if one node is lost.

Consider switching this off if:

* you are running out of disk space, but you do not need more CPU or memory capacity, and
* you can easily regenerate all the data on the indices that are set to ``number_of_replicas = 1``, and
* you are running a multi-node cluster.

To switch off automatic increases to the ``number_of_replicas`` value, run the following command in the `Aiven command-line client <https://github.com/aiven/aiven-client>`_::

    avn service update -c disable_replication_factor_adjustment=true <your service name>

This does not lower the ``number_of_replicas`` value, but it ensures that the value is not increased automatically in the future.

.. note::
    The replication factor is still automatically lowered if it is set to a value larger than the current cluster configuration allows.

