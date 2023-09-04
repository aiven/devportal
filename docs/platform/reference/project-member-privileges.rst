Project member roles
=====================

User permissions are assigned at the project level by role. Each user added to a project - individually or as part of a :doc:`group </docs/platform/howto/manage-groups>` - is assigned a role for that project.

.. important::

    Roles can only be managed by project **Admin** users on the **Members** page.

Project roles and their permissions
------------------------------------

The project roles and their permissions are:

* **Admin**: Full access to the project and its services. 
  
  * Do not have access to organization settings such as billing. 
  * Are the only users allowed to add more users to the project.
  
  .. note::
  
    Every project must have at least one admin user.

* **Operator**: Full access to all services in the project. 
  
  * Can create new services. 
  * Cannot make changes to the project members.   

* **Developer**: Allowed to manage services in this project.
  
  * Can make changes to services and databases, for example: creating databases, connecting to databases, removing Aiven for OpenSearch® indexes, creating and modifying Aiven for Apache Kafka® topics, and creating and modifying Aiven for PostgreSQL® connection pools.
  * Can create and change service database users.
  * Cannot add or change project members.
  * Cannot make changes that affect billing like powering services on or off.

* **Read-only**: Only allowed to view services.
  
  * Cannot make any changes to the project or its services.
