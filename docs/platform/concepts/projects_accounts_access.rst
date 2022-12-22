Organizations, projects, and managing access permissions
=========================================================

The Aiven platform uses organizations, organizational units, and projects to organize services and access to those services.This article describes how you can use these effectively to accommodate your organization’s structure.

Organizations and organizational units
---------------------------------------

Organizations and organizational units are collections of projects. When you sign up to Aiven, an organization is created for you.

You can use these to create a hierarchical structure that fits your needs. Organizational units (or org units) can be added to an organization. They can also be used to group projects. This gives you greater flexibility to organize your setup to meet your specific use cases. For example, you can easily split production and testing workloads into different org units that are in the same organization. 

Having these centralized entities lets you manage settings like:

* Authentication methods - Only available on the organization level

* ACLs - Can be set on all levels (organization, organizational unit, and project)

  * Plan enablement ACsL are inherited, meaning all projects within an organization or organizational unit will have the same service plan.

* Teams - Specific to a single organization or organizational unit and cannot be shared between them

* Support contracts - Specific to a single organization or organizational unit and cannot be shared between them

* Billing groups - Specific to a single organization or organizational unit and cannot be shared between them

Projects
--------

Projects are a collection of services and user permissions. You can group your services however you see fit. Each project must have a unique name within an organization. Some examples that we have seen:

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

You can invite people to work with you on a project, but you may not always want to give them the same access that you have. You can specify the email addresses and permissions for members in the *Members* section of the Aiven web console, which you can find in the main menu on the left of the page.

The roles and corresponding permissions that Aiven supports are:

* **Administrator**: When you create a project, you automatically receive this access level. You can change and view billing information, remove members, and create, edit, and delete services.

* **Operator**: This role provides full access to services but does not allow you to modify billing information or project members.

* **Developer**: This allows you to manage existing services (for example, creating databases and connecting to them), but it does not allow you to make any changes that would affect billing (for example, starting or stopping services).

* **Read Only**: This allows you to view services, but does not allow you to make any changes to the services.


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
    Read-Only role cannot view or copy service account passwords.  Administrator, Operator and Developer can fully manage service accounts.

Teams
~~~~~

You can also use teams within accounts to group project membership for a specific account instead of specifying them per project.

One example of this is to grant read-only access to all projects in an account for a team of external contractors. Even when you use teams, you can still apply individual memberships to projects as well.

.. important::
    When you create an account, you are automatically added to the ``Account Owners`` team. This team has administrative access to the account itself, but you must still define access levels to projects.

When you have created a team, you must manually associate projects and roles within the team.

Best practices for organizations
---------------------------------