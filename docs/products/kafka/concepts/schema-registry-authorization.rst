Schema registry authorization
=============================

The schema registry authorization feature enabled in :doc:`Karapace schema registry <../howto/enable-karapace>`  allows you to both authenticate the user, and additionally grant or deny access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_ and filters the content the endpoints return.

.. Tip::

  Karapace schema registry authorization is enabled on all Aiven for Apache Kafka® services. The exception is older services created before mid-2022, where the feature needs to be enabled. Check the :doc:`dedicated article <../howto/enable-schema-registry-authorization>` to learn how to enable the feature.

.. _karapace_schema_registry_acls:

Karapace schema registry ACLs
-----------------------------

Karapace schema registry authorization is configured using dedicated Access Control Lists (ACLs). 

Karapace schema registry ACL definition
'''''''''''''''''''''''''''''''''''''''

A Karapace schema registry authorization ACL consists of zero or more entries that each specify a **username**, an **operation** and a **resource**.

* The **username** is the name of a service user in the Aiven for Apache Kafka®G service.
* The **operations** are: 
  
  * ``schema_registry_read``
  * ``schema_registry_write`` (always includes ``schema_registry_read``)

* The **resource** can be in the following formats:

  * ``Config:``: the entry controls access to global compatibility configurations. Karapace only allows a user to retrieve and change the default schema compatibility mode via the global ``Config:`` resource, check the `project README <https://github.com/aiven/karapace/blob/main/README.rst>`_ for more information.

    .. Note::

      The global compatibility APIs require ``Config:`` resource access with ``schema_registry_read`` permission when getting the configuration and ``schema_registry_write`` permission when setting it.

  * ``Subject:subject_name``: the entry controls access to subjects in the schema registry.
    

.. Tip::

  The ``name`` specified in the ACL entry resource and username can use wildcards:
      
  * ``*`` matching any characters
  * ``?`` matching a single character

The schema registry will determine if there are necessary permissions to serve the request by checking if any of the ACL entries match the requesting user, the accessed resource, and grant the requested access.  The order of the ACL entries does not matter.  If none of the ACL entries grant access, the schema registry responds with HTTP status code 401 Unauthorized.

Endpoints and required ACLs
---------------------------

In order to properly access the endpoints you need to have the following ACLs:

* The endpoints involving subjects that are read-like, i.e. don't modify anything, require ``schema_registry_read`` operation for the subject in the request. The endpoints that return subject-related data filter the output so that only the entries the username has access to are returned. 
* The endpoints that mutate a subject-related entity correspondingly require ``schema_registry_write`` operation.

The following are some examples

.. list-table::
  :widths: 15 25 15 45
  :header-rows: 1

  * - username
    - operation
    - resource
    - explanation
  * - ``user_1``
    - ``schema_registry_read``
    - ``Config:``
    - Read access for ``user_1`` to the global compatibility configuration
  * - ``user_1``
    - ``schema_registry_read``
    - ``Subject:s1``
    - Read access for ``user_1`` to the subject ``s1``. When filtering results in list endpoints, only return the results related to subjects ``s1``.
  * - ``user_1``
    - ``schema_registry_write``
    - ``Subject:s1``
    - Write access for ``user_1`` to the subject ``s1``. Write implies read access, see the above row.
  * - ``user_readonly*``
    - ``schema_registry_read``
    - ``Subject:s*``
    - Read access for users with prefix ``user_readonly`` to the subjects with prefix ``s``. When filtering results, only return entities for subjects with prefix ``s``.
  * - ``user_write*``
    - ``schema_registry_write``
    - ``Subject:s*``
    - Write (add, delete etc) access for users with prefix ``user_write`` to the subjects with prefix ``s``. Write implies read access, see the above row.


.. Warning::
  Enabling Karapace schema registry authentication management, and managing the ACL entries, is done using the :doc:`Aiven CLI </docs/tools/cli/service/schema-registry-acl>` (requires version 2.16 or later).

Note the user that manages the ACLs is a special superuser with write access to everything in the schema registry. This means that in `Aiven Console <https://console.aiven.io/>`_, all schemas can be seen, all schemas can be modified etc in the Schemas tab of a Kafka service. This user and the ACL entries for it are not visible in Console, but the Aiven platform adds them automatically.

Read more: :doc:`/docs/products/kafka/howto/manage-schema-registry-authorization`.


