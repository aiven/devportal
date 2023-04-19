Set up OpenSearch Dashboard multi-tenancy
==========================================

Aiven for OpenSearch® provides support for multi-tenancy through OpenSearch Security Dashboard. Multi-tenancy in OpenSearch Security enables multiple users or groups to securely access the same OpenSearch cluster while maintaining their distinct permissions and data access levels. With multi-tenancy, each tenant has its own isolated space for working with indexes, visualizations, dashboards, and other OpenSearch objects, ensuring tenant-specific data and resources are protected from unauthorized access. 

Prerequisites
-------------

* Aiven for OpenSearch 
* Administrative access to both the Aiven for OpenSearch service and OpenSearch Dashboard

Configure multi-tenancy in OpenSearch Dashboard
-----------------------------------------------

This section provides information on configuring multi-tenancy in OpenSearch Dashboard, which involves enabling OpenSearch Security management, creating tenants, assigning roles, and mapping roles to users.

Step 1: Enable OpenSearch Security management
```````````````````````````````````````````````
The first step in setting up multi-tenancy in OpenSearch Dashboard is to enable OpenSearch Security management on your Aiven for OpenSearch service. Security provides authentication and authorization features that are required for multi-tenancy.  
To enable OpenSearch Security management, see docs <link pending update>. 

Step 2: Create a Tenant
`````````````````````````
After enabling OpenSearch Security management on your Aiven for OpenSearch service, the next step is to configure tenants. A tenant is a logical grouping of users and data, each with its own set of users, roles, and permissions.

OpenSearch users have access to two default tenants: Global and Private. The Global Tenant is shared by all users, and the Private Tenant is exclusively available to a single user and cannot be shared.

To create a new tenant, follow these steps: 

1. Log in to OpenSearch Dashboard with administrative access. 
2. From the left navigation menu, select **Security** and select **Tenants**. 
3. Select **Create tenant** to create a new tenant. 
4. In the **Create Tenant** screen, enter a name and description for your new tenant.
5. Select **Create** to save your new tenant.

Step 3: Assign Tenant to Roles
```````````````````````````````
After creating a tenant, you need to assign it to a role. A role is a collection of permissions for a specific tenant that can be granted to users. 
To assign a tenant to a role, follow these steps:

1. In the OpenSearch dashboard, navigate to the **Security** section in the left-hand navigation menu, then select **Roles**. 
2. Choose whether to create a new role or modify an existing one to include the tenant.
3. To create a new role: 
   
   * Select **Create role** and enter a name for your new role.
   * Select the permissions you want to grant to this role. 
   * In the **Tenant permissions** section, choose the tenant you want to assign to the role from the dropdown menu. Then, select the tenant permissions for the role, such as read and/or write permissions.
   * Select **Create** to save your new role with the assigned tenant. 

4. To modify an existing role: 
   
   * Search for the role you want to edit and select it to view its permissions screen. 
   * Select **Edit role** and add the required tenant in the **Tenant permissions** section. Additionally, select the tenant permissions for the role, such as read and/or write permissions.
   * Select **Update** to save your changes.

Step 4: Map roles to users
``````````````````````````````
Once you have assigned tenants to roles and set the necessary permissions, you need to link each user with a specific role to allow them access to the tenant and its resources. The role assigned to each user will determine their level of access and control over the tenant's data and resources.
To map roles to internal users, follow these steps:

1. In the OpenSearch dashboard, navigate to the **Security** section in the left-hand navigation menu, then select **Roles**. 
2. Search for the role you want to assign a user and select it to view its details. 
3. Select the **Mapped Users** tab and then select  **Map users**  (or **Manage mapping** if users are already mapped). 
4. In the **Users** section, choose the internal user you wish to assign to the role from the dropdown list.
5. Select **Map** to add the selected user to the mapped user list.

Step 5: Manage Tenant
```````````````````````
To manage tenants in the OpenSearch dashboard, you can follow these steps:

* **Access the tenant list**: Navigate to the Security section in the OpenSearch dashboard and select the Tenant option to view the available tenants and create new ones.
* **Switch between tenants**: Besides creating new tenants, you can switch between them by selecting the checkbox next to the desired tenant and using the **Actions** dropdown to select **Switch the selected tenant**.
* **View and create Index Patterns**: To view and create *Index Patterns*, *Saved Objects*, and manage *Advanced settings*, select **View Dashboards** or **View Visualisations** for a specific tenant.
* **Edit, delete, or duplicate tenants**: To manage existing tenants, select them from the list and use the **Actions** dropdown to edit, delete, or duplicate them according to your needs.


