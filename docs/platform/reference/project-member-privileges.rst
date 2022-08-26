Project member privileges
=========================

Manage user level permissions in Aiven projects

User permissions are defined at project level in Aiven. Each user invited to a project has one of the available roles in it, defined originally by the **Admin** level user who invited the user to the project.  Roles can be managed by a project **Admin** user under the **Project Members** page.

**Project roles overview**

- **Admin** role is required to invite more users to the project or to modify billing information. Admins can perform all available operations for projects and services.  Each project must always have at least one Admin user.  

- **Operator** role provides full access to services but does not allow modifying billing information or project members.  

- **Developer** role allows managing existing services (e.g. creating databases and connecting to them), but does not allow making any changes that would affect billing (for example, starting or stopping services).

- **Read-only** role allows viewing services but does not allow making any changes whatsoever to the services.

**Operations allowed for each project role**

**Developer**

- Access hosted services (PostgreSQL®, Kafka®, etc.) by using the connection parameters and service URI

- Create and modify service databases

- Create and modify service database users

- Remove Elasticsearch® indexes

- Create and modify Kafka® topics

- Create and modify PostgreSQL® connection poolers

**Operator**

- All the operations available to Developers (see above)

- Download project PDF invoices

- Create and modify services

- Start scheduled service maintenance

**Admin**

- All the operations available to Operators (see above)

- Delete the project

- Invite Aiven users to the project

- Remove users from the project

- Define the project role for users in the project

- Update project billing information



