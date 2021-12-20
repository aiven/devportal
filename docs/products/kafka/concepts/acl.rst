Access control lists permission mapping
=======================================

Aiven for Apache Kafka supports the definition of users and access control lists (ACL) to allow and limit producer and consumer rights at topic level. You can manage users and ACL entries in the corresponding tabs of the service page in the Aiven web console as explained in the :doc:`dedicated documentation <../howto/manage-acls>`.

ACLs are defined as: 

* a user or a wildcard mask of users
* the grant to produce and/or consume
* a topic or a wildcard mask of topics that the grant is applied to. 

By default, access is allowed for all configured users to both produce and consume on all topics.

.. Note:: 

    By default, Aiven adds an ``Admin`` account with wildcard (``*``) permissions to every new service. When you create your own ACLs to restrict access, remove this account.


**Important:** By default, Aiven adds an ``Admin`` account with wildcard
(*) permissions to every new service. When you create your own ACLs to
restrict access, remove this account.

**Note:** When using the Aiven Terraform Provider, you can add the
``default_acl`` key to your ``resource`` and set it to ``false`` if you
do not want to create the admin user with wildcard permissions.


ACL permission mapping
----------------------

You can define four types of grants for a particular topic or topic pattern:

* Admin
* Consume and Produce
* Consume
* Produce

The type of grant dictates the actions the client is be able to perform. The following table contains a summary of the allowed action and a link to the Java APIs:

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
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#createTopics(java.util.Collection)>`_
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
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#deleteConsumerGroups(java.util.Collection)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Describe``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeConsumerGroups(java.util.Collection)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Read``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#listConsumerGroups(org.apache.kafka.clients.admin.ListConsumerGroupsOptions)>`_
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
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html#poll(java.time.Duration)>`_
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Write``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html#send(org.apache.kafka.clients.producer.ProducerRecord,org.apache.kafka.clients.producer.Callback)>`_
    - ✓
    - ✓
    - ✓
    -
  * - → ``Describe``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#listTransactions()>`_
    - ✓
    - ✓
    - ✓
    - ✓
  * - → ``Describe_Configs``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeTopics(java.util.Collection)>`_
    - ✓
    - ✓
    - ✓
    - ✓
  * - → ``Alter``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#alterConfigs(java.util.Map)>`_
    - ✓
    - 
    -
    -
  * - → ``AlterConfigs``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#alterConfigs(java.util.Map)>`_
    - ✓
    - 
    -
    -
  * - → ``Delete``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#deleteTopics(java.util.Collection)>`_
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
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeTransactions(java.util.Collection)>`_
    - ✓
    - ✓
    - ✓
    -
  * - → ``Write``
    - `view docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html#beginTransaction()>`_
    - ✓
    - ✓
    - ✓
    -

.. Warning:: 

    A user with the ``Admin`` permission can create topics with any name, as the ``CreateTopics`` permission is applied at the cluster level. 
    
    All other permissions related to a topic (``Alter``, ``Delete``) **only** apply to the topics matching the pattern that you specify.

The above mappings are subject to change and this article will be updated when that happens.

.. Note::

    By default, the number of users per service is limited to 50 in Kafka. Contact Aiven support if you need more users.