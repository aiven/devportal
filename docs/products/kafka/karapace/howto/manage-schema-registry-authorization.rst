Manage Karapace schema registry authorization
=============================================

Karapace schema registry authorization allows you to authenticate the user, to control access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_, and to filter the content the endpoints return.

.. tip:: 
  Some older Aiven for Apache Kafka® services may not have this feature enabled by default, and you need to :doc:`enable Karapace schema registry authorization <../howto/enable-schema-registry-authorization>`.

Karapace schema registry authorization is configured using :doc:`Access Control Lists (ACLs) <../concepts/schema-registry-authorization>`. You can manage the Karapace schema registry authorization ACL entries using the :doc:`Aiven CLI </docs/tools/cli/service/schema-registry-acl>`. 

Using the Aiven CLI commands, you can 

* Add ACL
* Delete ACL
* View ACL list

For more information on the ACL commands, the required parameters and examples, see :doc:`avn service schema-registry-acl </docs/tools/cli/service/schema-registry-acl>`.

Manage Resources via Terraform
------------------------------
Additionally, the :doc:`Aiven Aiven Terraform provider </docs/tools/terraform>` supports managing Karapace schema registry authorization ACL entries with the aiven_kafka_schema_registry_acl resource. For more information, see the `resource documentation  <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/kafka_schema_registry_acl>`_.

An example of recource configuration via Terraform is as shown below: 

.. code:: terraform

   resource "aiven_kafka_schema_registry_acl" "my_resource" {
     project      = aiven_kafka_topic.demo.project
     service_name = aiven_kafka_topic.demo.service_name
     resource     = "Subject:${aiven_kafka_topic.demo.topic_name}"
     username     = aiven_kafka_user.demo.username
     permission   = "schema_registry_read"
   }
