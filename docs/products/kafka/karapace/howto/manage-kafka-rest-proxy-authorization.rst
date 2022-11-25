Manage Apache Kafka® REST proxy authorization
==============================================

Apache Kafka® REST proxy authorization allows you to use the RESTful interface to connect to Kafka clusters, produce and consume messages easily, and execute administrative activities using Aiven CLI. This feature is disabled by default, and you need to :doc:`enable Apache Kafka REST proxy authorization <../howto/enable-kafka-rest-proxy-authorization>`.

When you enable Apache Kafka REST proxy authorization, Karapace sends the HTTP basic authentication credentials to Apache Kafka®. The authentication and authorization are then performed by Apache Kafka, depending on the ACL defined in Apache Kafka. To configure the ACLs for authorization, see :doc:`Kafka Access Control Lists (ACLs) </docs/products/kafka/concepts/acl>`.

.. note:: 
    If the feature is **disabled**, Apache Kafka REST proxy authorization connects to Apache Kafka® using a special **superuser** with full access to all topics.


