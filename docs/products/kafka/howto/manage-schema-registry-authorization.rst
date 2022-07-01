Manage Karapace schema registry authorization
=============================================

Schema registry authorization feature enabled in :doc:`Karapace schema registry <../howto/enable-karapace>`  allows you to both authenticate the user, and additionally grant or deny access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_ and filters the content the endpoints return.

.. Tip::

    Karapace schema registry authorization has been available in Aiven since 2022-06-30 in all Aiven for Apache Kafka® services created after that date have it enabled by default and it's not possible to disable it.

    For the services created before 2022-06-30 the feature needs to be enabled, check the :doc:`dedicated article <../howto/enable-schema-registry-authorization>` to understand how to enable the feature.

Manage Karapace schema registry ACLSs via Aiven CLI
---------------------------------------------------

Karapace schema registry authorization is configured using dedicated Access Control List (ACL), to review ACLs definitions, check the :ref:`dedicated page <karapace_schema_registry_acls>`.

To manage Karapace schema registry authorization ACL entries you can use the :doc:`Aiven CLI </docs/tools/cli>`. Here's an example how to add an ACL entry granting an user named ``user_1`` read options (``schema_registry_read``) to the subject ``s1``, after replacing the placeholders ``PROJECT_NAME`` and ``APACHE_KAFKA_SERVICE_NAME`` with the name of the project and the Aiven for Apache Kafka® service::

    avn service schema-registry-acl-add     \
        --project PROJECT_NAME              \
        --permission schema_registry_read   \
        --resource Subject:s1               \
        --username user_1                   \
        APACHE_KAFKA_SERVICE_NAME

.. Tip::
    
    The Aiven CLI command ``service schema-registry-acl-list`` allows you to list the ACL entries already defined. ``service schema-registry-acl-delete`` allows you to delete an ACL entry.