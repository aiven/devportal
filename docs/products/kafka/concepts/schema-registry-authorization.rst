Schema registry authorization
=============================

Schema registry authorization feature enabled in :doc:`Karapace schema registry <../howto/enable-karapace>`  allows you to both authenticate the user, and additionally grant or deny access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_ and filters the content the endpoints return.

.. Tip::

  Karapace schema registry authorization has been available in Aiven since 2022-06-30 in all Aiven for Apache Kafka® services created after that date have it enabled by default and it's not possible to disable it.

  For the services created before 2022-06-30 the feature needs to be enabled, check the :doc:`dedicated article <../howto/enable-schema-registry-authorization>` to understand how to enable the feature.

.. _karapace_schema_registry_acls:

Karapace schema registry ACLs
-----------------------------

Karapace schema registry authorization is configured using dedicated Access Control List (ACL). 

Karapace schema registry ACL definition
'''''''''''''''''''''''''''''''''''''''

A Karapace schema registry authorization ACL consists of zero or more entries that each specify a **username**, an **operation** and a **resource**.

* The **username** is the name of a service user in the Aiven for Apache Kafka service.
* The **operations** are: 
  
  * ``schema_registry_read`` (later: ``read``)
  * ``schema_registry_write`` (later: ``write``). ``write`` implies ``read``.

* The **resource** is can be in the following formats: 

  * ``Config:``: the entry controls the access to global compatibility configurations. As of Karapace allows only to retrieve and change the default schema compatibility mode via the global ``Config:`` resource, check the `project README for more information <https://github.com/aiven/karapace/blob/main/README.rst>`_.

    .. Note::

      The global compatibility APIs require ``Config:`` resource access with ``Read`` permission when getting the configuration and ``Write`` permission when setting it.

  * ``Subject:subject_name``: the entry controls the access to subjects in Schema Registry
    

.. Tip::

  The ``name`` specified in the ACL entry resource and username can use wildcards:
      
  * ``*`` matching any characters
  * ``?`` matching a single character

The algorithm to determine if a request has the necessary permissions is the following:

* Iterate over ACL entries in the order
* Check if the current requesting user matches the ACL entry and the resource in the ACL entry matches the accessed resource
* If it matches, use that ACL entry. Check whether the operation in the ACL entry matches the accessed operation, based on that grant or deny access
* If no ACL entry is found, deny access, with HTTP response having status code 401

Endpoints and required ACLs
---------------------------

Karapace schema registry offers a series of endpoints to:

* Get/set the global configurations: ``/config``
* Get/set schema subjects and associated details: ``/subject``

In order to access properly the endpoints you need to have the following ACLs:

* The endpoints involving subjects that are read-like, i.e. don't modify anything, require ``schema_registry_read`` operation for the subject in the request. The endpoints that return subject-related data filter the output so that only the entries the username has access to are returned. 
* The endpoints that mutate a subject-related entity correspondingly require ``schema_registry_write`` operation.

The following are some Examples

.. list-table:: Examples
  :widths: 25 25 25 25
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
    - ``Subject: s1``
    - Read access for ``user_1`` to the subject ``s1``. When filtering results in list endpoints, only return the results related to subjects ``s1``.
  * - ``user_1``
    - ``schema_registry_write``
    - ``Subject: s1``
    - Write access for ``user_1`` to the subject ``s1``. Write implies read access, see the above row.
  * - ``user_readonly*``
    - ``schema_registry_read``
    - ``Subject: s*``
    - Read access for users with prefix ``user_readonly`` to the subjects with prefix ``s``. When filtering results, only return entities for subjects with prefix ``s``.
  * - ``user_write*``
    - ``schema_registry_write``
    - ``Subject: s*``
    - Write (add, delete etc) access for users with prefix ``user_write`` to the subjects with prefix ``s``. Write implies read access, see the above row.


.. Warning::
  Currently there's no `Aiven Console <https://console.aiven.io/>`_ support for Karapace schema registry authentication management. Enabling it, and managing the ACL entries can only be done using Aiven Client. Console support will be added later.

Note the user `Aiven Console <https://console.aiven.io/>`_, Aiven Client and Aiven REST API use when working with Schema Registry is a special superuser with write access to everything in Schema Registry. This means e.g. that in `Aiven Console <https://console.aiven.io/>`_, all schemas can be seen, all schemas can be modified etc in the Schemas tab of a Kafka service. This user and the ACL entries for it are not visible in Console, but Aiven platform adds them automatically.
