Using ``sstableloader`` to migrate your existing Apache Cassandra® cluster to Aiven
===================================================================================

**How to use the ``sstableloader`` utility to upload Cassandra® data files to a new Aiven service**

While it's possible to migrate a Cassandra cluster to Aiven by inserting rows using a regular Cassandra client, there is an alternative which scales better for large amounts of data. The ``sstableloader`` utility is run on the source cluster nodes and reads the raw data files for tables that you want to migrate, and uploads them efficiently to the target cluster by connecting directly to the target nodes'  internode port that is normally used only for communication between the cluster's nodes.

**Create Aiven Cassandra service in migration mode**

To be able to connect to the internode ports from outside the service nodes, the Aiven Cassandra service must be created in migration mode. This configures the service to use the external IP addresses of the service and allows connections there using an SSL client certificate.

Using `Aiven CLI client <https://github.com/aiven/aiven-client>`_, create a new Cassandra service in migration mode with:::

    avn service create -t cassandra -p <plan> -c migrate_sstableloader=true <service name>

**Migrate schema**

Because ``sstableloader`` only uploads data files to the target cluster, the schema for any uploaded tables must be created first. This can be done using the ``cqlsh`` command line client. Dump the schema for each keyspace to be migrated into a file with:::

    cqlsh <source cassandra address> -e "DESCRIBE KEYSPACE mykeyspace" > mykeyspace-schema.cql

Now before using the commands in the file to recreate the schema in the target Aiven service, the replication settings need to be adjusted first. The first non-empty line in the file is a ``CREATE KEYSPACE`` query, which defines which replication strategy to use for the keyspace and related settings.
To distribute replicas evenly across Availability Zones and to use the datacenter name your Aiven service nodes are using, change the WITH replication part of the query to use ``NetworkTopologyStrategy`` and the desired number of replicas for datacenter ``aiven``. For example:::

    CREATE KEYSPACE mykeyspace WITH replication = {'class': 'NetworkTopologyStrategy', 'aiven': '3'}  AND durable_writes = true

Note that skipping changing the replication strategy in the schema leads to inserted data not being replicated to any of the service nodes!

Please see :doc:`getting-started` for how to connect for how to connect to the target Aiven Cassandra service and recreate the schema in the target service with::: 

    SSL_CERTFILE=ca.pem cqlsh --ssl -u avnadmin -p f5v60s7ngaid02aa target-cassandra-myfirstcloudhub.aivencloud.com 24510 -f mykeyspace-schema.cql

**Retrieve client certificate and configuration for ``sstableloader``**

As mentioned earlier, connecting to the internode port requires a client certificate. One has been created for the target service since it is in migration mode. The `Aiven CLI client <https://github.com/aiven/aiven-client>`_ command below retrieves the client certificate and creates a Java keystore file ``sstableloader.keystore.p12`` suitable for ``sstableloader`` to use. It also creates a truststore file ``sstableloader.truststore.jks`` with the CA certificate of the service nodes, and creates a ``cassandra.yaml`` file for ``sstableloader`` pointing to the keystore and truststore. To retrieve the credentials into the current working directory run:::

    avn service sstableloader get-credentials <service name>

Either upload the keystore, truststore and ``cassandra.yaml`` files to each node in your source cluster, or run the command on each node. Then run the following command to print the ``sstableloader`` command to run on the nodes:::

    avn service sstableloader command <service name>

The output should be for example:::

    sstableloader -f cassandra.yaml -d target-cassandra-myfirstcloudhub.aivencloud.com -ssp 24512 -p 24510 -u avnadmin -pw f5v60s7ngaid02aa

The ``-p`` option points to the Cassandra client port which ``sstableloader`` uses to determine the addresses of cluster nodes it needs to upload data to. ``-ssp`` points to the SSL storage port, ie. the internode port number used when connecting to upload the data to nodes. The username and password are needed for authenticating to the client port, while ``cassandra.yaml`` configures ``sstableloader`` to use the client certificate retrieved earlier to authenticate with the internode port.

**Run ``sstableloader``**

Now ssh into each node of the source cluster, and run ``nodetool flush``. This forces Cassandra to write any mutations that are only in memory to disk, so that all data on the node is uploaded.

After that, run the ``sstableloader`` command printed above giving it a Cassandra table data directory as the argument:::

    sstableloader -f cassandra.yaml -d target-cassandra-myfirstcloudhub.aivencloud.com -ssp 24512 -p 24510 -u avnadmin -pw f5v60s7ngaid02aa cassandra/data/mykeyspace/mytable-3f6bcf70a6f111e98926edc04ce26602

This uploads the data files for that table from the node to the target. Note that the command must be run on every node of the source cluster, as not all rows are present on every node of the source cluster.

**Verify target service contains all data**

It's recommended to check the target service using your Cassandra client of choice to make sure all data to be migrated is there. It's possible to re-run ``sstableloader`` on the same tables again. This will simply upload any mutations in the source service's nodes' data directories to be applied in the target Cassandra service.

**Turn off migration mode**

Finally, turn off the ``sstableloader`` migration mode from the target Aiven Cassandra service with:::

    avn service update -c migrate_sstableloader=false <service name>

This closes the internode port for external access and changes the Cassandra service to use IPsec for more efficient internode communication, and enables the `Aiven service to be migrated to another cloud or network <https://help.aiven.io/en/articles/493382-can-i-migrate-my-service-to-another-cloud-or-region>`_ later. 