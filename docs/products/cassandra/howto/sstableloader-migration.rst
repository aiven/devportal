Migrate your Cassandra® cluster to Aiven with sstableloader
===========================================================

While it's possible to migrate a Cassandra® cluster to Aiven by inserting rows using a regular Cassandra client, using sstableloader is an alternative which scales better for large amounts of data. Check out how to migrate your Cassandra cluster into Aiven using sstableloader.

About sstableloader
-------------------

The sstableloader utility is run on the source cluster nodes. It reads the raw data files for tables that you want to migrate and uploads them efficiently to the target cluster by connecting directly to the target nodes' internode port that is normally used only for communication between the cluster's nodes.

Create an Aiven for Apache Cassandra service in the migration mode
------------------------------------------------------------------

To be able to connect to the internode ports from outside the service nodes, the Aiven for Apache Cassandra service must be created in the migration mode. This configures the service to use the external IP addresses of the service and allows connections there using an SSL client certificate.

Using `Aiven CLI client <https://github.com/aiven/aiven-client>`__, create a new Cassandra service in the migration mode with

.. code-block:: bash

   avn service create -t cassandra -p <plan> -c migrate_sstableloader=true <service name>

Migrate the schema
------------------

1. Because sstableloader only uploads data files to the target cluster, the schema for any uploaded tables must be created first. This can be done using the ``cqlsh`` command line client.

   Dump the schema for each keyspace to be migrated into a file with

   .. code-block:: bash

      cqlsh <source cassandra address> -e "DESCRIBE KEYSPACE mykeyspace" > mykeyspace-schema.cql

2. Before using the commands in the file to recreate the schema in the target Aiven service, the replication settings need to be adjusted. The first non-empty line in the file is a ``CREATE KEYSPACE`` query, which defines which replication strategy to use for the keyspace and related settings.
   
   To distribute replicas evenly across availability zones and to use the datacenter name your Aiven service nodes are using, change the ``WITH replication`` part of the query to use ``NetworkTopologyStrategy`` and the desired number of replicas for datacenter ``aiven``. For example

   .. code-block:: bash

      CREATE KEYSPACE mykeyspace WITH replication = {'class': 'NetworkTopologyStrategy', 'aiven': '3'}  AND durable_writes = true

   .. note::
      
      Skipping changing the replication strategy in the schema leads to inserted data not being replicated to any of the service nodes.

3. :doc:`Connect to the target Aiven for Apache Cassandra service </docs/products/cassandra/howto/list-code-samples>` and recreate the schema in the target service with

.. code-block:: bash

   SSL_CERTFILE=ca.pem cqlsh --ssl -u avnadmin -p f5v60s7ngaid02aa target-cassandra-myfirstcloudhub.aivencloud.com 24510 -f mykeyspace-schema.cql

Retrieve the client certificate and configuration for sstableloader
-------------------------------------------------------------------

As mentioned earlier, connecting to the internode port requires a client
certificate. One has been created for the target service since it is in
migration mode. The `Aiven CLI
client <https://github.com/aiven/aiven-client>`__ command below
retrieves the client certificate and creates a Java keystore file
``sstableloader.keystore.p12`` suitable for sstableloader to use. It
also creates a truststore file ``sstableloader.truststore.jks`` with the
CA certificate of the service nodes, and creates a ``cassandra.yaml``
file for sstableloader pointing to the keystore and truststore. To
retrieve the credentials into the current working directory run:

.. code-block:: bash

   avn service sstableloader get-credentials <service name>

Either upload the keystore, truststore and ``cassandra.yaml`` files to
each node in your source cluster, or run the command on each node. Then
run the following command to print the sstableloader command to run on
the nodes:

.. code-block:: bash

   avn service sstableloader command <service name>

The output should be for example

.. code-block:: bash

   sstableloader -f cassandra.yaml -d target-cassandra-myfirstcloudhub.aivencloud.com -ssp 24512 -p 24510 -u avnadmin -pw f5v60s7ngaid02aa

The ``-p`` option points to the Cassandra client port which
sstableloader uses to determine the addresses of cluster nodes it needs
to upload data to. ``-ssp`` points to the SSL storage port, ie. the
internode port number used when connecting to upload the data to nodes.
The username and password are needed for authenticating to the client
port, while ``cassandra.yaml`` configures sstableloader to use the
client certificate retrieved earlier to authenticate with the internode
port.

Run sstableloader
-----------------

| Now ssh into each node of the source cluster, and run
  ``nodetool flush`` . This forces Cassandra to write any mutations that
  are only in memory to disk, so that all data on the node is uploaded.
| After that, run the sstableloader command printed above giving it a
  Cassandra table data directory as the argument:

.. code-block:: bash

   sstableloader -f cassandra.yaml -d target-cassandra-myfirstcloudhub.aivencloud.com -ssp 24512 -p 24510 -u avnadmin -pw f5v60s7ngaid02aa cassandra/data/mykeyspace/mytable-3f6bcf70a6f111e98926edc04ce26602

This uploads the data files for that table from the node to the target.
Note that the command must be run on every node of the source cluster,
as not all rows are present on every node of the source cluster.

Verify the target service contains all data
-------------------------------------------

It's recommended to check the target service using your Cassandra client
of choice to make sure all data to be migrated is there. It's possible
to re-run sstableloader on the same tables again. This will simply
upload any mutations in the source service's nodes' data directories to
be applied in the target Cassandra service.

Turn off the migration mode
---------------------------

Finally, turn off the sstableloader migration mode from the target Aiven
Cassandra service with:

.. code-block:: bash

   avn service update -c migrate_sstableloader=false <service name>

This closes the internode port for external access and changes the
Cassandra service to use IPsec for more efficient internode
communication (See :doc:`Cloud security </docs/platform/concepts/cloud-security>` for
details), and enables the :doc:`the Aiven service to be migrated to another cloud or region </docs/platform/howto/migrate-services-cloud-region>` later.
