Manage Apache Kafka® REST proxy authorization
==============================================

Apache Kafka® REST proxy authorization allows you to use the RESTful interface to connect to Kafka clusters, produce and consume messages easily, and execute administrative activities using Aiven CLI. This feature is disabled by default, and you need to :doc:`enable Apache Kafka REST proxy authorization <../howto/enable-kafka-rest-proxy-authorization>`.

When you enable Apache Kafka REST proxy authorization, Karapace sends the HTTP basic authentication credentials to Apache Kafka®. The authentication and authorization are then performed by Apache Kafka, depending on the ACL defined in Apache Kafka. To configure the ACLs for authorization, see :doc:`Kafka Access Control Lists (ACLs) </docs/products/kafka/concepts/acl>`.


When Apache Kafka REST proxy authorization is enabled, a **super user** is created for the Apache Kafka REST proxy and added to the Apache Kafka ACLs. Any operation requested via the REST API uses this superuser, who has all the permissions to perform any operation without any restrictions. When Apache Kafka REST proxy authorization is disabled, the REST Proxy bypasses the Apache Kafka ACLs, so any operation via REST API call is performed without any restrictions.




