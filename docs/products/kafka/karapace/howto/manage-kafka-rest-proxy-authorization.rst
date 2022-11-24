Manage Apache Kafka® REST proxy authorization
==============================================

Apache Kafka® REST proxy authorization allows you to use the RESTful interface to connect to Kafka clusters, produce and consume messages easily, and execute administrative activities using Aiven CLI. This feature is disabled by default, and you need to :doc:`enable Apache Kafka REST proxy authorization <../howto/enable-kafka-rest-proxy-authorization>`.

Enabling Apache Kafka REST proxy authorization directs Karapace to forward the HTTP basic authentication credentials to Apache Kafka®. Apache Kafka then performs the authentication and authorization based on the ACL defined in Apache Kafka. See :doc:`Kafka Access Control Lists (ACLs) </docs/products/kafka/concepts/acl>` to configure the authorization.

.. note:: 
    If the feature is **disabled**, Apache Kafka REST proxy authorization connects to Apache Kafka® using a special **superuser** with full access to all topics.

Manage resources via Terraform
------------------------------
In :doc:`Terraform </docs/tools/terraform>`, you can toggle the Apache Kafka® REST proxy authorization feature on or off by setting the value of ``kafka_rest_authorization`` entry. However, authorization rules are defined using :doc:`Apache Kafka ACLs </docs/products/kafka/concepts/acl>`. For information, see `aiven_kafka (Resource) <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/kafka#nestedblock--kafka_user_config--kafka_rest_config>`_.



