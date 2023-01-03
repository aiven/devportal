Organizations, projects, and managing access permissions
=========================================================

The Aiven platform uses organizations, organizational units, and projects to organize services and access to those services. Learn how you can use these effectively to accommodate your organization's structure.

Organizations and organizational units
---------------------------------------

Organizations and organizational units are collections of projects. When you sign up to Aiven, an organization is created for you.

You can use these to create a hierarchical structure that fits your needs. Organizational units (or org units) can be nested within an organization, adding another level to group your projects. This gives you greater flexibility to organize your setup to meet your specific use cases. For example, you can easily split production and testing workloads into different org units that are in the same organization. 

Grouping your projects in organizations and org units lets you centrally manage settings like:

* Authentication methods - Only available on the organization level

* ACLs - Can be set on all levels (organization, organizational unit, and project)

  * Plan enablement ACLs are inherited, meaning all projects within an organization or organizational unit will have the same service plan.

* Teams - Specific to a single organization or organizational unit and cannot be shared between them

* Support contracts - Specific to a single organization or organizational unit and cannot be shared between them

* Billing groups - Specific to a single organization or organizational unit and cannot be shared between them

Projects
--------

Projects are collections of services and user permissions. Each project must have a unique name within an organization. You can group your services however you see fit. These are some examples of how customers organize their services:

* Single project: One project containing services that are distinguished by their names. For example, services are named based on the type of environment: ``demo_pg_project.postgres-prod`` and ``demo_pg_project.postgres-staging``.

* Environment-based projects: Each project represents a deployment environment, for example: ``dev``, ``qa``, and ``production``. This allows you to apply uniform network security, such as the use of virtual private clouds (VPCs), to all services within each environment. This also gives you more granular user permissions, such as developer access to production infrastructure.

* Project-based: Each project contains all the services for an internal project, with naming that highlights the relevant environment; for example: ``customer-success-prod`` and ``business-analytics-test``.

Service access management
--------------------------

There are two ways that you can manage access to Aiven services:

* Direct access via projects
* Indirectly via role-based access controls (RBAC)

Smaller teams usually favor direct access, while larger teams favor RBAC to simplify complex access requirements.

.. mermaid::

    graph LR;

        User-- Direct access --> Project;
        User-- RBAC --> Team;
        Organization-->Team & B["Org unit"];
        B["Org unit"]-->Team;
        Team-->Project;
        Project-->Service;

Aiven organizations help you organize and manage your projects and services. Within organizations you can have organizational units. The services you create are collected in projects, and each project can be in an organization or an organizational unit. 

You can use organizations and teams within the Aiven platform to implement :doc:`SAML single sign-on (SSO) </docs/platform/howto/list-saml>`` using an identity provider such as Okta, GSuite, or AzureAD. For greater security, you may want to use a combination of SAML and RBAC regardless of the size of team.


Project members and roles
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can invite people to work with you on a project, but you may not always want to give them the same access that you have. You can define different levels of access for each projects member using roles:

* **Administrator**: Can change and view billing information, remove members, and create, edit, and delete services. When you create a project, you automatically receive this access level. 

* **Operator**: Full access to services, but can't modify billing information or project members.

* **Developer**: Can manage existing services (for example, creating databases and connecting to them), but can't make any changes that would affect billing (for example, starting or stopping services).

* **Read Only**: Can view services, but can't make any changes to them.


.. list-table::
   :header-rows: 1

   * - Role
     - View status
     - Connect
     - Deploy
     - Billing/editing access
   * - Administrator
     - |tick|
     - |tick|
     - |tick|
     - |tick|
   * - Operator
     - |tick|
     - |tick|
     - |tick|
     - 
   * - Developer
     - |tick|
     - |tick|
     - 
     - 
   * - Read Only
     - |tick|
     - 
     - 
     - 
.. Note::
    The Read-Only role cannot view or copy service account passwords, but the Administrator, Operator and Developer roles have full access to manage service accounts.

Teams
~~~~~

You can also use teams within organizations or org unitsto control access to projects for a group of users instead of specifying them per project. When you create a team, you choose which projects to associate it to and define the roles.

One example of this is to grant read-only access to all projects in an organization or org unit for a team of external contractors. You can use a mix of team and individual access rights for projects.

.. important::
    When you create an organization, you are automatically added to a default team that has administrative access to the organization. You can still define additional access levels to the organization’s projects.

Best practices for organizations
---------------------------------

**Small organizations**
Smaller organizations that have a limited number of projects, we recommend consolidating these within one organization. 

**Medium and large organizations**
For more complex cases, it's helpful to take advantage of the organizational units. Org units let you collect together related projects by, for example, your internal departments or other categories like testing, staging, and production environments. 

**Enterprise organizations**
For enterprise organizations, it's best to use organizations to group organizational units. By keeping all of your projects in organizational units you can define teams, support contracts, and billing groups for each org unit.
