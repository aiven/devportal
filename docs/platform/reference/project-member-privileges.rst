Project member privileges
=========================

User permissions are defined at project level in Aiven. Each user invited to a project has one of the available roles in it, defined originally by the **Admin** level user who invited the user to the project. 

.. Important::

    Roles can only be managed by project **Admin** users under the **Project Members** page.

Project roles
-------------

The following is the list of project roles and related priviledges:

* **Admin**: can perform all available operations for projects and services. 

  Admins are the only allowed to invite more users to the project or to modify billing information.
  
  .. Important::
  
    Each project must always have at least one Admin user.  

* **Operator**: provides full access to services but does not allow modifying billing information or project members.  

* **Developer**: allows managing existing services (e.g. creating databases and connecting to them), but does not allow making any changes that would affect billing (for example, starting or stopping services).

* **Read-only**: allows viewing services but does not allow making any changes whatsoever to the services.

Roles detailed priviledges 
--------------------------

The following is a list of priviledges enabled for each role.

Developer
~~~~~~~~~

- Access hosted services (Aiven for PostgreSQL®, Aiven for Apache Kafka®, etc.) by using the connection parameters and service URI

- Create and modify service databases

- Create and modify service database users

- Remove Aiven for OpenSearch® indexes

- Create and modify Aiven for Apache Kafka® topics

- Create and modify Aiven for PostgreSQL® connection pools

Operator
~~~~~~~~

All the operations available to Developers (see above) and:

- Download project PDF invoices

- Create and modify services

- Start scheduled service maintenance

Admin
~~~~~

All the operations available to Operators (see above) and:

- Delete the project

- Invite Aiven users to the project

- Remove users from the project

- Define the project role for users in the project

- Update project billing information