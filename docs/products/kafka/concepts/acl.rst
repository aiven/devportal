Access control lists permission mapping
=======================================

Aiven for Apache Kafka® uses access control lists (ACL) and user definitions in order to establish individual rights to produce or consume a topic and manage topics. You can manage users and ACL entries in the corresponding tabs of the service page in the Aiven web console as explained in the :doc:`dedicated documentation <../howto/manage-acls>`.

The ACL consists of ACL entries. An ACL entry is defined as the combination of the username, the permission given to the user and the associated topic.

The username is either an Aiven username, or can have wildcards. Similarly, the the topic is an Apache Kafka® topic name as such or can have wildcards. The permission is one of ``read``, ``write``, ``readwrite`` and ``admin``.

The wildcards supported are:

* ``?`` matching a single characters
* ``*`` matching one or multiple characters

Aiven for Apache Kafka® evaluates each topic access against the ACL entries. If it finds a matching ACL entry, access is granted. If no entry matches, access is denied. Thus the order of the ACL entries is irrelevant.

Examples:

* username: ``abc``, permission: ``read``, topic: ``xyz``. User ``abc`` has read access to topic ``xyz``.
* username: ``analyst*``, permission: ``read``, topic: ``xyz``. All Aiven users with username starting ``analyst`` have read access to topic ``xyz``.
* username: ``developer*``, permission: ``read``, topic: ``test*``. All Aiven users with username starting ``developer`` have read access to topics starting with ``test``.

By default, access is allowed for all configured users to both produce and consume on all topics.

.. Warning:: 

  By default, Aiven adds an ``avnadmin`` account to every new service and adds `admin` permission for all topics to that user. When you create your own ACLs to restrict access, you probably need to remove this ACL entry.

.. Note::

  When using the Aiven Terraform Provider, you can add the ``default_acl`` key to your ``resource`` and set it to ``false`` if you do not want to create the admin user with wildcard permissions.


ACL permission mapping
----------------------

You can define four types of permission for a particular topic or topic pattern. Note each permission is called differently in the Console when creating them (e.g. Consume) and in the ACL entries list:

* Admin / `admin`
* Consume and Produce / `readwrite`
* Consume / `read`
* Produce / `write`

The type of the permission dictates the actions the client is be able to perform. The following table contains a summary of the allowed action and a link to the Java APIs:

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
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#createTopics(java.util.Collection)>`__
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
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#deleteConsumerGroups(java.util.Collection)>`__
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Describe``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeConsumerGroups(java.util.Collection)>`__
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Read``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#listConsumerGroups(org.apache.kafka.clients.admin.ListConsumerGroupsOptions)>`__
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
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html#poll(java.time.Duration)>`__
    - ✓
    - ✓
    - 
    - ✓
  * - → ``Write``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html#send(org.apache.kafka.clients.producer.ProducerRecord,org.apache.kafka.clients.producer.Callback)>`__
    - ✓
    - ✓
    - ✓
    -
  * - → ``Describe``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#listTransactions()>`__
    - ✓
    - ✓
    - ✓
    - ✓
  * - → ``Describe_Configs``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeTopics(java.util.Collection)>`__
    - ✓
    - ✓
    - ✓
    - ✓
  * - → ``Alter``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#alterConfigs(java.util.Map)>`__
    - ✓
    - 
    -
    -
  * - → ``AlterConfigs``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#alterConfigs(java.util.Map)>`__
    - ✓
    - 
    -
    -
  * - → ``Delete``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#deleteTopics(java.util.Collection)>`__
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
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/admin/Admin.html#describeTransactions(java.util.Collection)>`__
    - ✓
    - ✓
    - ✓
    -
  * - → ``Write``
    - `docs <https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/producer/KafkaProducer.html#beginTransaction()>`__
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
