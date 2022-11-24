Manage Apache Kafka® REST proxy authorization
==============================================

Apache Kafka® REST proxy authorization allows you to use the RESTful interface to connect to Kafka clusters, produce and consume messages easily, and execute administrative activities using Aiven CLI. This feature is disabled by default, and you need to :doc:`enable Apache Kafka REST proxy authorization <../howto/enable-kafka-rest-proxy-authorization>`.

Enabling Apache Kafka REST proxy authorization directs Karapace to forward the HTTP basic authentication credentials to Apache Kafka®. Apache Kafka then performs the authentication and authorization based on the ACL defined in Apache Kafka. See :doc:`Kafka Access Control Lists (ACLs) </docs/products/kafka/concepts/acl>` to configure the authorization.

.. note:: 
    If the feature is **disabled**, Apache Kafka REST proxy authorization connects to Apache Kafka® using a special **superuser** with full access to all topics.


