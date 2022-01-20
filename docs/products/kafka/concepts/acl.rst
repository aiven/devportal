Access control lists permission mapping
=======================================

Aiven for Apache Kafka uses access control lists (ACL) and user definitions in order to establish individual rights to produce or consume a topic. You can manage users and ACL entries in the corresponding tabs of the service page in the Aiven web console as explained in the :doc:`dedicated documentation <../howto/manage-acls>`.

ACLs are defined as: 

* a user or a wildcard mask of users
* a grant to produce and/or consume
* a topic or a wildcard mask of topics that the grant is applied to. 

By default, access is allowed for all configured users to both produce and consume on all topics.

.. Warning:: 

  By default, Aiven adds an ``Admin`` account with wildcard (``*``) permissions to every new service. When you create your own ACLs to restrict access, remove this account.

.. Note::

  When using the Aiven Terraform Provider, you can add the ``default_acl`` key to your ``resource`` and set it to ``false`` if you do not want to create the admin user with wildcard permissions.


ACL permission mapping
----------------------

You can define four types of grants for a particular topic or topic pattern:

* Admin
* Consume and Produce
* Consume
* Produce

The type of the grant dictates the actions the client is be able to perform. The following table contains a summary of the allowed action and a link to the Java APIs:

.. list-table::
  :header-rows: 1
  :align: left


  * - Action
    - Link
    - Admin
    - Consume and Produce
    - Produce
    - Consume
  * - Cluster
    -
    -
    -
    -
    -
  * - → ``CreateTopics``
    - `CreateTopics docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#createTopics(java.util.Collection)>`_
    - ✓
    - 
    -
    -
  * - Consumer Groups
    -
    -
    -
    -
    -
  * - → ``Delete``
    - `Delete docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#deleteConsumerGroups(java.util.Collection)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Describe``
    - `Describe docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeConsumerGroups(java.util.Collection)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Read``
    - `Read docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#listConsumerGroups(org.apache.kafka.clients.admin.ListConsumerGroupsOptions)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - Topics
    -
    -
    -
    -
    -
  * - → ``Read``
    - `Read docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html#poll(java.time.Duration)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Write``
    - `Write docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html#send(org.apache.kafka.clients.producer.ProducerRecord,org.apache.kafka.clients.producer.Callback)>`_
    - ✓
    - ✓
    - ✓
    -
  * - → ``Describe``
    - `Describe docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#listTransactions()>`_
    - ✓
    - ✓
    - ✓
    - ✓
  * - → ``Describe_Configs``
    - `Describe Configurations docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeTopics(java.util.Collection)>`_
    - ✓
    - ✓
    - ✓
    - ✓
  * - → ``Alter``
    - `Alter docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#alterConfigs(java.util.Map)>`_
    - ✓
    - 
    -
    -
  * - → ``AlterConfigs``
    - `AlterConfigs docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#alterConfigs(java.util.Map)>`_
    - ✓
    - 
    -
    -
  * - → ``Delete``
    - `Delete docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#deleteTopics(java.util.Collection)>`_
    - ✓
    - 
    -
    -
  * - Transactions
    -
    -
    -
    -
    -
  * - → ``Describe``
    - `Describe docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeTransactions(java.util.Collection)>`_
    - ✓
    - ✓
    - ✓
    -
  * - → ``Write``
    - `Write docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html#beginTransaction()>`_
    - ✓
    - ✓
    - ✓
    -

.. Warning:: 

    A user with the ``Admin`` permissions can create topics with any name, as the ``CreateTopics`` permissions is applied at the cluster level. 
    
    All other permissions related to a topic (``Alter``, ``Delete``) **only** apply to the topics matching the pattern that you specify.

The above mappings are subject to change and this article will be updated when that happens.

.. Note::

    By default, the number of users per service is limited to 50 in Kafka. Contact Aiven support if you need more users.