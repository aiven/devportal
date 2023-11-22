Manage users and access control in Aiven for OpenSearch®
=========================================================
Effective access control and permissions management are crucial for Aiven for OpenSearch service users. In Aiven for OpenSearch, you can manage users and permissions by creating Access Control Lists (ACLs) through the Aiven Console. 

By using the **Users** tab in the `Aiven Console <https://console.aiven.io>`_ for your Aiven for OpenSearch service, you can manage access control and permissions for your service users. You can create new users, modify their details, and assign index patterns and permissions for each user.

.. note:: 
   Alternatively, you can enable :doc:`OpenSearch Security management `/docs/products/opensearch/howto/enable-opensearch-security` for your Aiven for OpenSearch service and manage users and permissions via the OpenSearch Security dashboard.

Create user without access control
-----------------------------------
To create a service new user without any access control in Aiven Console, follow these steps:

1. In the `Aiven Console <https://console.aiven.io>`_, open the Aiven for OpenSearch service where you want to add a user.
2. Select **Users** from the left sidebar.
3. Select **Create users**, enter a username, and select **Save**.
   
By default, newly created users will be granted **full access rights**. However, to limit their access, you can enable access control and specify an Access Control List (ACL) for them, defining the relevant permissions and patterns.

Enable access control
----------------------
To enable access control for the Aiven for OpenSearch service through the `Aiven Console <https://console.aiven.io>`_, navigate to the **Users** tab and toggle the **Access Control** switch to enable it.

Create user with access control
-------------------------------
To create a service new user with access control, follow these steps:

1. In your Aiven for OpenSearch service, select **Users** from the left sidebar. 
2. Select **Create user**.
3. In the **Create service user** screen, enter a **username**.
4. Specify an **index** pattern and set the desired **permissions**.
5. Add multiple rules to the user by selecting **Add another rule**.
6. Select **Save** to finish, and view the new user in the list. 

.. note:: 
   The password for service users is automatically generated and can be reset if necessary.

After creating a new service user, the next step is for them to log in to the :doc:`OpenSearch Dashboard `/docs/products/opensearch/dashboards` using their assigned credentials. This will grant them access to the dashboard, where they can perform various actions based on their assigned permissions. 

Manage users
--------------
Aiven for OpenSearch provides several additional operations you can perform on service users, such as viewing, copying, resetting passwords, editing ACL rules, and deleting users. 

To access the additional operations, navigate to the **Users** tab within your Aiven for OpenSearch service, select the ellipsis (More options) in the respective user row, and choose the desired operation.

.. note:: 
   Deleting a service user will terminate all existing database sessions, and the user will lose access immediately.


Disable access control
-----------------------
Disabling access control for your Aiven for OpenSearch service will grant admin access to all users and override any previously defined user permissions. Therefore, it is essential to carefully consider the outcomes of disabling access control before proceeding.

To disable access control:

1. Select **Users** from the left sidebar within your Aiven for OpenSearch service, toggle the **Access Control** switch to off.
2. Confirm the decision to disable access control by clicking  **Disable** when prompted.

