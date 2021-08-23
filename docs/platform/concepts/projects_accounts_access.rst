Projects, accounts, and managing access permissions
===================================================

The Aiven platform uses accounts and projects to organize services and access to those services. This article describes those terms and how you can use them effectively based on your organization structure, deployment environments, and service security requirements.

There are two ways that you can manage access to Aiven services:

* Direct access via projects
* Indirectly via role-based access controls (RBAC)

Smaller teams usually favor direct access while larger teams favor RBAC to simplify complex access requirements for large numbers of people.

You can use accounts and teams within the Aiven platform to implement Security Assertion Markup Language single sign-on (SAML SSO) using an identity provider such as Okta, GSuite, or AzureAD. Security-conscious teams usually favor a combination of SAML and RBAC regardless of the size of team.


Projects
--------

Projects are a collection of services and user permissions. You can organize your services however you see fit. Some examples that we have seen:

* **Single project**: A project containing several services that are each named according to the relevant environment, for example ``demo_pg_project.postgres-prod`` and ``demo_pg_project.postgres-staging``.

* **Environment-based projects**: Each project represents a deployment environment, for example ``dev``, ``qa``, and ``production``. This allows you to apply uniform network security, such as the use of virtual private clouds (VPCs), to all services within the environment. This also gives you more flexibility for user permissions, such as developer access to production infrastructure.

* **Project-based**: A project that contains all the services for an internal project, with a suffix that highlights the relevant environment, for example ``customer-success-prod`` and ``business-analytics-test``.

Each project must have a unique name within the Aiven platform. The project name is combined with the service names to create the host URLs for your deployed services.


Accounts
--------

An account is a collection of projects. When you first sign up to Aiven, there are no accounts, as you can use standalone projects without every needing accounts.

If you have several different departments that are using Aiven, you can use accounts to separate access between projects and departments.

For example, you could use different accounts for different departments and their projects, or you could use accounts to separate the projects related to customer-specific systems.


Project members and roles
-------------------------

You can invite people to work with you on a project, but you may not always want to give them the same access that you have. You can specify the email addresses and permissions for members in the *Members* section of the Aiven web console, which you can find in the main menu on the left of the page.

The roles and corresponding permissions that Aiven supports are:

* **Administrator**: When you create a project, you automatically receive this access level. You can change and view billing information, remove members, and create, edit, and delete services.

* **Operator**: This role provides full access to services but does not allow you to modify billing information or project members.

* **Developer**: This allows you to manage existing services (for example, creating databases and connecting to them), but it does not allow you to make any changes that would affect billing (for example, starting or stopping services).

* **Read Only**: This allows you to view services, but does not allow you to make any changes to the services.


Teams
-----

You can also use teams within accounts to group project membership for a specific account instead of specifying them per project.

One example of this is to grant read-only access to all projects in an account for a team of external contractors. Even when you use teams, you can still apply individual memberships to projects as well.

.. important::
    When you create an account, you are automatically added to the ``Account Owners`` team. This team has administrative access to the account itself, but you must still define access levels to projects.

When you have created a team, you must manually associate projects and roles within the team.

