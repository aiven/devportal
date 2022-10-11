Manage Karapace schema registry authorization
=============================================

Karapace Kafka REST authorization allows you to TODO. This feature is disabled by default, and you need to :doc:`enable Karapace Kafka REST authorization <../howto/enable-kafka-rest-authorization>`.

The feature makes Kafka forward the HTTP basic authentication credentials to Kafka, essentially making Kafka to authenticate and authorize the HTTP requests sent to Kafka REST. Use :doc:`Kafka Access Control Lists (ACLs) <../../kafka/concepts/acl>` to configure the authorization.

If the feature is disabled, Kafka REST connects to Kafka using a special superuser that has full access to all topics.

Manage resources via Terraform
------------------------------
Terraform works so that a user_config entry is used to toggle the feature on and off. The Kafka ACLs are used to define the authorization rules.
