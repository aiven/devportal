
ACLs definition
================
An ACL for Karapace schema registry authorization consists of zero or more entries that specify a **username**, an **operation**, and a **resource**. 

* **Username** is the name of a service user in the Aiven for Apache Kafka® service.
* **Operations** are:
  
  * ``schema_registry_read``
  * ``schema_registry_write`` (always includes ``schema_registry_read``)

*  A **resource** can be in the following formats:
  
   * ``Config:``: the entry controls access to global compatibility configurations. Karapace only allows a user to retrieve and change the default schema compatibility mode via the global ``Config:`` resource. For more information, see the project `README <https://github.com/aiven/karapace/blob/main/README.rst>`_.

    .. Note::

      The global compatibility APIs require ``Config:`` resource access with ``schema_registry_read`` permission when getting the configuration and ``schema_registry_write`` permission when setting it.    
  
   * ``Subject:subject_name``: the entry controls access to subjects in the schema registry.

.. Tip::

  The ``name`` specified in the ACL entry resource and username can use wildcards:
      
  * ``*`` matching any characters
  * ``?`` matching a single character

When a user requests access to a resource, the schema registry checks to see if any entry in the ACL matches the requesting user and the requested resource, to decide whether to grant or deny read/write access to the requested resource. The order of entries in the ACL does not affect the access control decision.

The schema registry responds with HTTP status code 401 Unauthorized message if no ACL entries grant access.

.. Note:: 
  Enabling or disabling Karapace schema registry authorization, and managing the ACLs, is done using the Aiven CLI (requires version 2.16 or later). For more information, see :doc:`Enable Karapace schema registry authorization <../howto/enable-schema-registry-authorization>`. 
 

Securing endpoints with ACL
---------------------------

To correctly set up access control for the different endpoints, you need to have the following in the ACL:

* Endpoints that provide read-only operations require ``schema_registry_read`` permission in the ACL for the specific subject.  In the case of endpoints that return data related to multiple subjects, the response is filtered to include data against only those subjects the user has been granted read permission. 
* Endpoints that provide write operations require the schema_registry_write permission in the ACL for the specific subject.  

The following table provides you with examples: 

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
    - Provides ``user_1`` he permission to read everything in the resource configuration. 
  * - ``user_1``
    - ``schema_registry_read``
    - ``Subject:s1``
    - Provides ``user_1`` the permission to read only data related to subject ``s1``. In case of list endpoints, data related to all other subjects is filtered out.
  * - ``user_1``
    - ``schema_registry_write``
    - ``Subject:s1``
    - Provides ``user_1`` the permission to write (add, modify, delete) data associated with subject ``s1``. Having write permission also means that the user also has the corresponding read permission. 
  * - ``user_readonly*``
    - ``schema_registry_read``
    - ``Subject:s*``
    - Provides read access for all users with prefix ``user_readonly``, to all the subjects with prefix ``s``. The response is filtered to only contain results for all subjects with prefix ``s``. 
  * - ``user_write*``
    - ``schema_registry_write``
    - ``Subject:s*``
    - Provides the user with write (add, modify, delete) access for users with prefix ``user_write``, to the subjects with prefix ``s``. Having write permission also means that the user also has the corresponding read permission.

The user that manages the ACLs is a superuser with write access to everything in the schema registry. In the Aiven Console, the superuser can view and modify all schemas in the Schema tab of a Kafka service. The superuser and its ACL entries are not visible in the Console but are added automatically by the Aiven platform. 

The schema registry authorization feature enabled in :doc:`Karapace schema registry <../getting-started>` allows you to both authenticate the user, and additionally grant or deny access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_ and filter the content the endpoints return.

