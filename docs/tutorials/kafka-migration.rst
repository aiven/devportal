Apache Kafka® migration
=======================

What you will learn
---------------------------

Follow this tutorial and you'll learn all the steps involved in an Apache Kafka® migration:

* What are the prerequisites? What should you pay attention to, before migrating?
* How to sync data with MirrorMaker 2
* How to migrate Apache Kafka topic schemas
* How to migrate Apache Kafka ACLs (Access Control Lists)
* How to migrate Apache Kafka consumer group offsets
* How to migrate Apache Kafka clients and connectors


What are you going to build
---------------------------

This tutorial is aimed at providing you all the steps to perform an Apache Kafka migration. It being between on-premises systems or from/to a managed or self-hosted Apache Kafka cluster, the tutorial provides a set of checks, actions and processes to follow to perform a complete migration. Despite the step described being generic, the tutorial will showcase an example on how to migrate to :doc:`Aiven for Apache Kafka </docs/products/kafka>`.

The data migration will be performed using :doc:`MirrorMaker 2 </docs/products/kafka/kafka-mirrormaker>`, a fully managed distributed Apache Kafka® data replication utility.


.. mermaid::

    graph LR;

        id1(Source Apache Kafka cluster)-- source alias -->id2(MirrorMaker 2);
        id2-- sink alias -->id4(Target Apache Kafka cluster);

.. Warning:: 

  MirrorMaker 2 provides an **asynchronous** replication across clusters. Therefore, to perform a successful migration avoiding data loss, you need to ensure that the replication lag is 0 before pointing the new producers and consumers to the target Kafka environment. More information in the :ref:`monitor the MirrorMaker 2 replication flow lag <tutorial_kafka_migration_replication_flow_lag>` section.


Prerequisites
-------------

The exact migration steps can vary, depending on the peculiar usage of the existing source system. This tutorial however assumes the following pre-requisites:

* **Clients compatibility**: Any clients interacting with Apache Kafka must be compatible with the version chosen as migration target.

  .. Note::

    This guide doesn't include any steps to migrate clients versions

* Available **Apache Kafka configurations**: the custom settings needed in the source system, should be available as parameters in the target system. 

  .. Note::

    You can find a list of Aiven for Apache Kafka advanced parameters in the :doc:`related documentation </docs/products/kafka/reference/advanced-params>`

* Available **Apache Kafka Connect connectors**: if you're planning to migrate a Kafka Connect cluster, review the list of :doc:`supported connectors </docs/products/kafka/kafka-connect>` or check out how to :doc:`bring your own Kafka Connect cluster </docs/products/kafka/kafka-connect/howto/bring-your-own-kafka-connect-cluster>`. 

* **Connectivity**: the source and target clusters need to be connected via MirrorMaker 2 for the data migration, therefore proper connection needs to be established. Moreover, you need to ensure all the clients reading or writing to Apache Kafka can connect to the brokers as well as any self hosted Kafka connect cluster. 

  .. Warning::

    As part of the connectivity check you also need to ensure:
        
    * That the **connection bandwidth** is enough to sync the data between environments
    * That the needed networking setups are available in the target Apache Kafka cluster, some examples on how to define custom networking setups on Aiven:
        * :doc:`Firewalls/security groups </docs/platform/concepts/cloud-security>`
        * :doc:`VPC peering </docs/platform/howto/manage-vpc-peering>`
        * :doc:`Privatelink </docs/platform/howto/use-aws-privatelinks>`


Create an Apache Kafka integration endpoint
-------------------------------------------

The first step you'll need to perform in the Apache Kafka migration is identifying the source Kafka cluster and create a connection to it. In Aiven, you can perform this action by:

* Accessing the `Aiven Console <https://console.aiven.io/>`_
* Clicking on the **Integration Endpoints**
  
  .. image:: /images/tutorials/kafka-migration/integration-endpoints.png
    :alt: The Aiven Console with the integration endpoints option highlighted

* Select **External Apache Kafka** and click on **Create New**

  .. image:: /images/tutorials/kafka-migration/external-kafka.png
    :alt: The Aiven Console with the option to create an External Apache Kafka integration highlighted

* Give the endpoint a **name** (like ``mySourceKafkaCluster``), this will later be used as reference by MirrorMaker 2. Moreover list the **bootstrap servers** and the **Security protocol** that need to be used to connect.

  .. image:: /images/tutorials/kafka-migration/external-kafka-details.png
    :alt: The list of parameters (endpoint name, bootstrap servers, security protocol) needed to define an External Apache Kafka integration

.. Warning::

    The external integration setup does **not** test the connectivity between Aiven and the source Apache Kafka cluster

Create the Aiven services
----------------------------

In this section you'll create all the services needed for the migration via the `Aiven Console <https://console.aiven.io/>`_:

* An :doc:`Aiven for Apache Kafka®</docs/products/kafka>` named ``demo-kafka`` for data streaming, this is the target Kafka cluster for the migration
* An :doc:`Aiven for Apache Kafka MirrorMaker 2</docs/products/kafka/kafka-mirrormaker>` named ``demo-mm2``, MirrorMaker 2 will be used to stream the data from the source Apache Kafka cluster to ``demo-kafka``


Create an Aiven for Apache Kafka® service
'''''''''''''''''''''''''''''''''''''''''''''

The :doc:`Aiven for Apache Kafka </docs/products/kafka>` service is acting as target cluster for the migration. You can create the service with the following steps:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

   This opens a new page with the available service options.

   .. image:: /images/platform/concepts/console_create_service.png
      :alt: Aiven Console view for creating a new service

3. Select **Apache Kafka®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `business-4` as service plan.

5. Enter ``demo-kafka`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console

Customise the Aiven for Apache Kafka service
''''''''''''''''''''''''''''''''''''''''''''

Now that your service is created, you need to customise its functionality. In the **Overview** tab of your freshly created service, you'll see a bunch of toggles and properties. Change these two:

1. **Enable REST APIs**: via **Kafka REST API (Karapace)** > **Enable**

   .. Note::

    The **Kafka REST API** allows you to manage and query Apache Kafka via REST APIs. You'll use it to inspect the data in Apache Kafka from the Aiven Console.

2. **Auto creation of topics**: via **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

   .. Note::

    The ``kafka.auto_create_topics_enable`` setting allows you to create new Apache Kafka® topics on the fly while pushing a first record. It avoids needing to create a topic in advance. To read more about the setting, check the :doc:`dedicated documentation </docs/products/kafka/howto/create-topics-automatically>`.

3. **Broker Configuration**: ensure you apply all the needed :doc:`advanced configuration </docs/products/kafka/reference/advanced-params>` to the target Apache Kafka cluster.
4. **Enable SASL** (optional): you can enable :doc:`SASL </docs/products/kafka/howto/kafka-sasl-auth>` via the dedicated configuration option
5. **VPC peering** (optional): if you need to deploy the Apache Kafka service within a VPC, you can follow the :doc:`related documentation </docs/platform/howto/migrate-services-vpc>`

Create an Aiven for Apache Kafka MirrorMaker 2 service
''''''''''''''''''''''''''''''''''''''''''''''''''''''

The :doc:`Aiven for Apache Kafka MirrorMaker 2 </docs/products/kafka/kafka-mirrormaker>` service is responsible sync the data between the source and target clusters in the migration. You can create the service with the following steps:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. Clink on the Aiven for Apache Kafka service, named ``demo-kafka`` created at the previous step.
3. On the *Overview* tab, scroll down until you locate the *Service integration* section and click on **Manage integrations**.

   .. image:: /images/tutorials/kafka-migration/service-integrations.png
      :alt: Aiven Console, *Service integration* section and **Manage integrations** button

4. Select **Apache Kafka MirrorMaker** 2.

   .. image:: /images/tutorials/kafka-migration/list-integrations.png
      :alt: Aiven Console, list of available integrations

5. In the new window popup, select the **New Service** option and click on **Continue**

6. Give the new service the ``demo-mm2`` name, select the cloud provider, region, and service plan. Then click on **Continue**

7. Define the **Cluster alias**, this is the logical name you'll use to define the target ``demo-kafka`` cluster. Therefore input ``kafka-target``

Once you follow all the steps, you should be able to see an active integration between ``demo-kafka`` and ``demo-mm2`` named ``kafka-target``

.. image:: /images/tutorials/kafka-migration/mm2-active-integration.png
    :alt: Aiven Console, active MirrorMaker 2 integration


Create a data replication using MirrorMaker 2
---------------------------------------------

The next step in the migration journey is to create a data replication from the source cluster to the Aiven for Apache Kafka service named ``demo-kafka``. To create a replication you need to:

* create an alias for the source Apache Kafka cluster (the target alias ``kafka-target`` was defined during the creation of the MirrorMaker 2 service)
* define the replication follow

Create an alias for the source Apache Kafka cluster
'''''''''''''''''''''''''''''''''''''''''''''''''''

To create a MirrorMaker 2 replication flow, you need first to create an alias to point to the source Kafka cluster (the target alias ``kafka-target`` was defined during the creation of the MirrorMaker 2 service).

To create the alias with the `Aiven Console <https://console.aiven.io/>`_ you can follow the steps below:

1. Navigate to the MirrorMaker 2 ``demo-mm2`` service page
2. Click on the **Integration** tab
3. Scroll until you reach the **External integrations** section
4. Select **Cluster for replication** within the available external integrations

   .. Warning::

    Selecting the **Cluster for replication** option from the *Aiven solutions* section will only allow you to integrate with Aiven for Apache Kafka services. Therefore, if your source Kafka cluster is not an Aiven service, you need to select the **Cluster for replication** from the **External integrations** section.
    
5. Select the endpoint name defined in a previous step (``mySourceKafkaCluster``) and click **Continue**

   .. image:: /images/tutorials/kafka-migration/external-endpoint-integration.png
    :alt: Aiven Console, MirrorMaker 2 alias definition for the external Apache Kafka endpoint integration

6. Give the source cluster an alias name, as example ``kafka-source``, and click **Enable**

Once the steps are done, you should be able to see the two aliases ``kafka-source`` and ``kafka-target`` defined as integrations in the ``demo-mm2`` service

.. image:: /images/tutorials/kafka-migration/source-target-integration-enabled.png
    :alt: Aiven Console, MirrorMaker 2 source and target integration enabled

.. Warning::

  In case of any connection problem to the source or target Apache Kafka cluster, you'll be able to see the following error message in the MirrorMaker 2 service overview page

  .. image:: /images/tutorials/kafka-migration/error-connection.png
    :alt: Aiven Console, MirrorMaker 2 service overview, error message stating that the connection to a target Kafka service is not working

Start the MirrorMaker 2 replication flow
''''''''''''''''''''''''''''''''''''''''

In the previous steps you defined MirrorMaker 2 source and target aliases. Now it's time to define the replication flow.

You first need to identify the set of topics you want to migrate to the new cluster, and create a :doc:`Java regular expression </docs/products/kafka/kafka-mirrormaker/concepts/replication-flow-topics-regex>` that includes them. As example, if you want to migrate all the topics starting with ``customer.`` your regular expression will be ``customer\..*``.

.. Tip::

  You can list both topics to be included and excluded in the allow list and stop list


You can create a MirrorMaker 2 replication flow in the `Aiven Console <https://console.aiven.io/>`__ with:

#. Navigate to the ``demo-mm2`` service page
#. Click on the **Replication Flows** tab
#. Click on **Create replication flow**
#. Fill in the replication flow details:

   * **Source cluster**: ``kafka-source`` - the alias defined for the source Kafka cluster
   * **Target cluster**: ``kafka-target`` - the alias defined for the target Aiven for Apache Kafka cluster
   * **Topics**: the :doc:`Java regular expression </docs/products/kafka/kafka-mirrormaker/concepts/replication-flow-topics-regex>` defining which topics to include. E.g. ``customer\..*`` to include all topics starting with ``customer.``
   * **Topics blacklist**: the :doc:`Java regular expression </docs/products/kafka/kafka-mirrormaker/concepts/replication-flow-topics-regex>` defining which topics to exclude. E.g. ``inventory\..*`` to exclude all topics starting with ``inventory.``
   * **Sync group offset**: to define whether to sync the topic containing the consumer group offset
   * **Sync interval in seconds**: to define the frequency of the sync
   * **Offset syncs topic location**: to provide offset translation, MirrorMaker 2 uses the ``mm2-offset-syncs`` topic, that can be located either in the source or sink cluster
   * **Replication policy class**: controls the prefix when replicating topics. ``DefaultReplicationPolicy`` sets the topic name in the target Kafka service as ``source_cluster_alias.topic_name`` (prefixing the topic name with the source cluster alias), while ``IdentityReplicationPolicy`` sets the target topic name equal to the source topic name.
   * **Emit heartbeats enabled**: allow MirrorMaker 2 to emit heartbeats to keep the connection open even in cases where no messages are replicated
   * **Enable**: to enable the data sync job

   The following represent an example of a replication flow setting

   .. image:: /images/tutorials/kafka-migration/replication-flow-details.png
    :alt: Aiven Console, replication flow details

   .. Warning::

    Before starting the replication flow, you might want to manually create the topics in the target Kafka cluster. MirrorMaker 2 replication flow will **not** recreate topics with the same configuration options. This step is specifically important if the topic needs to be :doc:`compacted </docs/products/kafka/concepts/log-compaction>` or if some settings (like partitioning) are key for the correct working of the data pipeline.

#. Click on **Create**

Once you followed all the above steps you should see the replication flow being enabled 

.. image:: /images/tutorials/kafka-migration/replication-flow-enabled.png
    :alt: Aiven Console, MirrorMaker 2 replication flow enabled

And, browsing the target ``demo-kafka`` service, you should see the topics being replicated. The following image shows the replication (using the ``DefaultReplicationPolicy``) of the ``kafka-source.customer.clicks`` and ``kafka-source.customer.purchases`` topics together with MirrorMakers 2 internal topics

.. image:: /images/tutorials/kafka-migration/replicated-topics.png
    :alt: Aiven Console, target Aiven for Apache Kafka with the replicated clicks and purchases topics

.. _tutorial_kafka_migration_replication_flow_lag:

Monitor the MirrorMaker 2 replication flow lag
''''''''''''''''''''''''''''''''''''''''''''''''

After starting the replication flow, MirrorMaker 2 will start moving data between the source and target Kafka clusters in asynchronous mode. To measure how the replication is performing you might want to check the replication lag: the delay in synchronization between the source and target Apache Kafka cluster. Once the lag metric is `0`, the two Apache Kafka clusters are in sync.

You can review how to create services integrations here. 

The metric you want to track is called ``kafka_mirrormaker_summary.replication_lag``. The image below showcases a Grafana® dashboard showing the mean MirrorMaker 2 replication lag trending to ``0``.


.. image:: /images/tutorials/kafka-migration/mirrormaker-replication-lag.png
    :alt: Grafana dashboard showing the ``kafka_mirrormaker_summary.replication_lag`` metric

Migrate topic schemas
---------------------

Apache Kafka topics schemas define the structure of the data in certain topics. They can be migrated in two different methods:

#. by replicating the schemas topic stored in Apache Kafka (usually located in the ``_schemas`` topic)
#. by extracting the schema information from the source and registering in the target environment using the appropriate APIs

The second option offers much more control over what schemas are migrated. To register the schemas in an Aiven for Apache Kafka service you can:

* Navigate in the `Aiven Console <https://console.aiven.io/>`__, service page, **Schemas** tab
* Use the `Karapace rest APIs <https://api.aiven.io/doc/#tag/Service:_Kafka/operation/ServiceSchemaRegistrySubjectVersionPost>`_
* Use :doc:`Aiven command line interface </docs/tools/cli>`


Migrate access control list
---------------------------

Apache Kafka Access Control Lists (ACLs) define how various users can interact with the topics and schemas. To migrate ACLs we recommend to extract the ACL definition from the source Apache Kafka cluster and recreate them in the target cluster. 

If the target of the migration is Aiven for Apache Kafka you can define the ACLs with:

* the `Aiven Console <https://console.aiven.io/>`__, service page, **Access Control Lists (ACL)** tab 
* the dedicated `Aiven REST API <https://api.aiven.io/doc/#tag/Service:_Kafka/operation/ServiceKafkaAclAdd>`__
* the dedicated :doc:`Aiven CLI command </docs/tools/cli/service/acl>`


Change clients settings
-----------------------

After the replication flow is running, with the schemas and ACLs are in place, you can then start point producers and consumers to the target Apache Kafka cluster. 

.. Warning::

  To avoid any Apache Kafka messages to be lost during the asynchronous migration performed with MirrorMaker 2, it is suggested to stop the producers, check that both the consumer lag in the source system and the MirrorMaker 2 replication lag is ``0`` and then point producers and consumers to the target Apache Kafka cluster. 
  
  The :ref:`migration process <tutorial_kafka_migration_migration_process>` provides a detailed series of steps to follow.

If the target of the migration is Aiven for Apache Kafka, you can find how to download the required certificates and connect as producer or consumer in the :doc:`dedicated documentation </docs/products/kafka/howto/list-code-samples>`.



.. _tutorial_kafka_migration_migration_process:

Complete migration process
--------------------------

The following diagram showcases all the steps included in an Apache Kafka migration process.

.. mermaid::

    graph TD;

        id1(Start Migration process)-->id2(Create target Apache Kafka service);
        id2-->id3(Create Apache Kafka topics in the target cluster);
        id3-->id4(Create Apache Kafka schemas in the target cluster);
        id4-->id5(Create Apache Kafka ACLs in the target cluster);
        id5-->id6(Create source Apache Kafka cluster endpoint);
        id6-->id7(Create Apache Kafka MirrorMaker 2 service);
        id7-->id8(Define MirrorMaker 2 aliases for source and target Apache Kafka clusters);
        id8-->id9(Stop Apache Kafka producers on the original Apache Kafka cluster);
        id9-->id10(Wait for consumer lag to go to 0 in the original Apache Kafka cluster);
        id10-->id11(Wait for MirrorMaker 2 replication lag to go to 0);
        id11-->id12(Stop consumers in the source Apache Kafka cluster);
        id12-->id13(Point consumers to the target Apache Kafka cluster and start them);
        id13-->id14(Point producers to the target Apache Kafka cluster and start them);
        id14-->id15(End Migration process);
