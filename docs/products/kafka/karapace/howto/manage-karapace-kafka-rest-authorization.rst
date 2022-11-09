Manage Karapace schema registry authorization
=============================================

Karapace Kafka REST proxy authorization allows you to use the RESTful interface to connect to Kafka clusters, produce and consume messages easily, and execute administrative activities using Aiven CLI. This feature is disabled by default, and you need to :doc:`enable Karapace Kafka REST authorization <../howto/enable-kafka-rest-authorization>`.

The feature makes Karapace forward the HTTP basic authentication credentials to Apache Kafka® so that Apache Kafka® performs the authentication and authorization based on the ACL defined Use :doc:`Kafka Access Control Lists (ACLs) <../../kafka/concepts/acl>` to configure the authorization.

If the feature is disabled, Karapace Kafka REST API connects to Apache Kafka® using a special **superuser** with full access to all topics.

Manage resources via Terraform
------------------------------
Terraform works so that a user_config entry is used to toggle the feature on and off. The Kafka ACLs are used to define the authorization rules.
