Manage Karapace schema registry authorization
=============================================

Karapace schema registry authorization allows you to authenticate the user, to control access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_, and to filter the content the endpoints return.

.. Tip::

    Some older Aiven for Apache Kafka® services may not have this feature enabled by default, read :doc:`how to enable schema registry authorization on older services <../howto/enable-schema-registry-authorization>`.

Karapace schema registry authorization is configured using dedicated Access Control Lists (ACLs); to learn more about defining ACLs, check the :ref:`dedicated page <karapace_schema_registry_acls>`.

To manage Karapace schema registry authorization ACL entries you can use the :doc:`Aiven CLI </docs/tools/cli/service/schema-registry-acl>`.

Here's an example of how to add an ACL entry granting a user named ``user_1`` read options (``schema_registry_read``) to the subject ``s1``, after replacing the placeholders ``PROJECT_NAME`` and ``APACHE_KAFKA_SERVICE_NAME`` with the name of the project and the Aiven for Apache Kafka® service::

    avn service schema-registry-acl-add     \
        --project PROJECT_NAME              \
        --permission schema_registry_read   \
        --resource Subject:s1               \
        --username user_1                   \
        APACHE_KAFKA_SERVICE_NAME

.. Tip::
    
    The Aiven CLI command ``service schema-registry-acl-list`` allows you to list the ACL entries already defined. ``service schema-registry-acl-delete`` allows you to delete an ACL entry.

Additionally :doc:`Aiven Aiven Terraform provider </docs/tools/terraform>` supports managing Karapace schema registry authorization ACL entries by using the resource `aiven_kafka_schema_registry_acl <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/kafka_schema_registry_acl>`_

.. code:: terraform

   resource "aiven_kafka_schema_registry_acl" "my_resource" {
     project      = aiven_kafka_topic.demo.project
     service_name = aiven_kafka_topic.demo.service_name
     resource     = "Subject:${aiven_kafka_topic.demo.topic_name}"
     username     = aiven_kafka_user.demo.username
     permission   = "schema_registry_read"
   }
