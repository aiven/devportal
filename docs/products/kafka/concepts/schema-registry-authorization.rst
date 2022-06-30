Schema Registry Authorization
=============================

With Schema Registry authorization feature enabled Schema Registry not only authenticates the user, but additionally grants or denies access to individual Schema Registry REST API endpoints and filters the content the endpoints return.

Enabling
--------

Schema Registry authorization has been available in Aiven since 2022-06-30 and Aiven for Kafka® services created after that date have it enabled and it's not possible to disable it.

For the services created before that the feature needs to be enabled using Aiven Client ``avn service update --enable-schema-registry-authorization``. It can be disabled using ``--disable-schema-registry-authorization``. Note enabling it can lead to access rights issues if the ACL hasn't been configured properly.

Usage
-----

Schema Registry authorization is configured using Schema Registry Access Control List (ACL). The ACL consists of zero or more entries that each specify a username, an operation and a resource.

The username is the name of a service user in the Kafka service.

The operations are ``schema_registry_read`` (later: read) and ``schema_registry_write`` (later: write). ``write`` implies ``read``.

The resource is of format ``Subject:subject_name`` or ``Config:``. In the first case, the entry controls access to subjects in Schema Registry, in the latter to the global compatibility config.

The ``subject_name`` in the resource and username in the ACL entry can have wildcards:
 * ``*`` matching any characters
 * ``?`` matching a single character

The global compatibility APIs require ``Config:`` resource access with ``Read`` permission when getting the config and ``Write`` permission when setting it.

The endpoints involving subjects that are read-like, i.e. don't modify anything, require ``schema_registry_read`` operation for the subject in the request. The endpoints that return subject-related data filter the output so that only the entries the username has access to are returned. The endpoints that mutate a subject-related entity correspondingly require ``schema_registry_read`` operation.

If access to an endpoint is denied because of ACL, the HTTP response will have status code 401.

.. list-table:: Examples
   :widths: 25 25 25 25
   :header-rows: 1

   * - username
     - operation
     - resource
     - explanation
   * - user_1
     - schema_registry_read
     - Config:
     - Read access for user_1 to the global compatibility config
   * - user_1
     - schema_registry_read
     - Subject: s1
     - Read access for user_1 to the subject s1. When filtering results in list endpoints, only return the results related to subjects s1.
   * - user_1
     - schema_registry_write
     - Subject: s1
     - Write access for user_1 to the subject s1
   * - user_readonly*
     - schema_registry_read
     - Subject: s*
     - Read access for users with prefix user_readonly to the subjects with prefix s. When filtering results, only return entities for subjects with prefix s.
   * - user_write*
     - schema_registry_write
     - Subject: s*
     - Write (add, delete etc) access for users with prefix user_write to the subjects with prefix s. Implies read access, see the above row.


Aiven Client can be used to add the ACL entries. Here's an example how to add the ACL entry of the first row in the above table:

``avn service schema-registry-acl-add --project your_project --permission schema_registry_read --resource Subject:t1 --username user_1 kafka_service``

There is additionally the command ``service schema-registry-acl-list`` to list the ACL entries and ``service schema-registry-acl-delete`` to delete an ACL entry.

Note the user Aiven Console, Aiven Client and Aiven REST API use when working with Schema Registry is a special superuser that has write access to everything in Schema Registry. This means e.g. that in Console, all schemas can be seen, all schemas can be modified etc in the Schemas tab of a Kafka service. This user and the ACL entries for it are not visible in Console, but Aiven platform adds them automatically.


Limitations
-----------

Currently there's no Console support for the feature. Enabling it, and managing the ACL entries can only be done using Aiven Client. Console support will be added later.


