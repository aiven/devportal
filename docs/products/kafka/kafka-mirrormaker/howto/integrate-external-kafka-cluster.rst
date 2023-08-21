Integrate an external Apache Kafka® cluster in Aiven
====================================================

Aiven for Apache Kafka® MirrorMaker 2 enables the cross-cluster topic replication between any two Apache Kafka® clusters, which can be deployed as Aiven or external services. To enable :doc:`replication flows <setup-replication-flow>` with an external Apache Kafka cluster you need to define a service integration endpoint.

Define an external Apache Kafka® service integration endpoint via Aiven console
-------------------------------------------------------------------------------

You can define an external Apache Kafka® service integration endpoint using the Aiven console. Follow these steps:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and go to the Aiven project where you wish to integrate the external Apache Kafka cluster.

2. Select **Integration endpoints** from the left sidebar, and then **External Apache Kafka** from the list of available services.

3. Select **Add a new endpoint**.

4. Provide an **Endpoint name**, specify the **Bootstrap servers** , and configure the necessary security settings. Then, select **Create**.

4. Fill the **Endpoint name**, **Bootstrap servers** and the security settings and click **Create**.

5. The external Apache Kafka cluster is now available under the alias defined in the **Endpoint name** parameter

.. note::  Configure the ACLs for both the source and target cluster such that the MirrorMaker 2 service can describe and create topics, as well as produce and consume messages.