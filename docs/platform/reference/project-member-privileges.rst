Project member roles
=====================

User permissions are assigned at the project level by role. Each user added to a project - individually or as part of a :doc:`group </docs/platform/howto/manage-groups>` - becomes a project member and is assigned a role for that project.

You can grant different levels of access to project members using roles:


* **Admin**: Full access to the project and its services. 
  
  * This role is automatically granted to users who create a project. 
  * Does not have access to organization settings such as billing. 
  * Can add and remove project members.

  .. note::
  
    Every project must have at least one admin user.

* **Operator**: Full access to all services in the project. 
  
  * Can create new services. 
  * Cannot make changes to the project members.   

* **Developer**: Allowed to manage services in this project.
  
  * Can make changes to services and databases, for example: creating databases, connecting to databases, removing Aiven for OpenSearch® indexes, creating and modifying Aiven for Apache Kafka® topics, and creating and modifying Aiven for PostgreSQL® connection pools.
  * Can create and change service database users.
  * Cannot make changes to the project members.
  * Cannot make changes that affect billing (such as powering services on or off).

* **Read-only**: Only allowed to view services.
  
  * Cannot make any changes to the project or its services.


.. list-table::
   :header-rows: 1

   * - Role
     - View services
     - Create services
     - Manage services
     - Connect
     - Power services on/off
     - Edit members and roles
   * - Administrator
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
   * - Operator
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - 
   * - Developer
     - ✅
     - ✅
     - ✅
     - ✅
     - 
     - 
   * - Read Only
     - ✅
     - 
     - 
     - 
     - 
     - 
