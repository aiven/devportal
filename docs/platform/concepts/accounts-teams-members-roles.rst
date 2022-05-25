Accounts, Teams, Members and Roles

An overview of what these mean within Aiven and how you can use them to manage your services effectively
Christopher Gwilliams avatar
Written by Christopher Gwilliams
Updated over a week ago
When and Why?
There are two ways for users to gain access to Aiven managed services: (1) direct access via projects, or indirectly via role based access controls (RBAC). Smaller teams usually favor the direct access model while larger teams favor RBAC to simplify complex access requirements across many users.

Accounts and teams allow for SAML SSO with IdP like Okta, GSuite, and AzureAD. Security conscious teams usually favor SAML + RBAC regardless of team size. This article helps define those terms and how to use them effectively based on your organization structure, deployment environments, and service security requirements. 


Projects
Projects are a collection of services and user permissions. Services can be organized however you see fit. Some examples we have seen are:

Mono-Project: A project that contains a service (such as: PostgreSQL) that is then named for the environment it relates to. i.e. demo_pg_project.postgres-prod and demo_pg_project.postgres-staging


Environment Based: Each project represents a deployment environment, e.g. dev, qa, and production. That allows uniform network security to be applied to services, e.g. VPC's. This also gives flexibility to user permissions, e.g. developer access to production infrastructure.


Project Based: A project containing all services for an internal project, with a suffix that highlights the environment it relates to. i.e. customer-success-prod and business-analytics-test


Aiven requires project names to be globally unique, and as such can act as the unique identifier for your project. The project name, and service names will be used to create host url entries for deployed services.

Project Members
You can invite people to work with you on a project but you may not always want to give them the same access as you have. Members can be invited in the left hand side of the Console, where you can specify their email and the permissions they should have.

The roles Aiven supports (and their permissions) are outlined in the next section:

Member Roles
Administrator - If you create a project, you have this access level. You can change/view billing information, remove members and create/edit and delete services.

Operator - provides full access to services but does not allow modifying billing information or project members.

Developer - allows managing existing services (e.g. creating databases and connecting to them), but does not allow making any changes that would affect billing (for example, starting or stopping services).

Read Only - allows viewing services but does not allow making any changes whatsoever to the services.


Accounts
An account is a collection of projects. When you first sign up to Aiven, you will not have any accounts created. This is because projects can be standalone and your use case may never actually need Accounts. 

If you are using Aiven with a number of different departments, then Accounts can be a great way to separate access between projects and/or departments.

For example: An organization may use Accounts for different departments (and their Projects within) or it may be that an Account contains Projects all related to a system a customer is developing or running.

Teams
Teams are within Accounts and act as a way to group project memberships in an account, instead of having to specify them per project. 

An example use case for Teams is allowing external contractors read only access to all projects in an account. Of course, you can  still apply individual memberships to projects as well.

Important note: When creating an account, you will automatically be added to the Account Owners team. This Team has administrative access to the Account itself but access levels to projects must be defined yourself.

You must manually associate Projects and Roles within your Team. A GIF outlining the process is below.

