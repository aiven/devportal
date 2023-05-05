Access control in Aiven for OpenSearch®
=============================================================

Access control is a crucial security measure that allows you to control who can access your data and resources. By setting up access control rules, you can restrict access to sensitive data and prevent unauthorized changes or deletions.

Aiven for OpenSearch® provides the following ways to manage user accounts and access control in OpenSearch®. 

Method 1: Enable access control on the Aiven Console
---------------------------------------------------------------
When you enable :doc:`Access control <../howto/control_access_to_content>` in the Aiven Console for your Aiven for OpenSearch® service, you can create service users and set their permissions. The Aiven Console has an easy-to-use interface that helps you manage who can access your data. Aiven for OpenSearch supports index-level access control lists (ACLs) to control permissions and API-level rules to restrict access to specific data sets.

With access control enabled, you can customize the access control lists for each user by setting up individual "pattern/permission" rules. The "pattern" parameter specifies the indices to which the permission applies and uses glob-style matching, where * matches any number of characters (including none) and ? matches any single character.

For more information about access control, patterns and permissions, see :doc:`Understanding access control in Aiven for OpenSearch® <../concepts/users-access-controls>`. 

Method 2: Enable OpenSearch® Security management |beta|
--------------------------------------------------------
Another way to manage user accounts, access control, roles, and permissions for your Aiven for OpenSearch® service is by :doc:`enabling OpenSearch® Security management <../howto/enable-opensearch-security>`. This method lets you use the OpenSearch Dashboard and OpenSearch API to manage all aspects of your service's security. 

You can use advanced features such as fine-grained access control with OpenSearch Security. This allows you to specify the exact actions that each user can take within your OpenSearch service. OpenSearch Security also supports SAML integrations, which provide single sign-on (SSO) authentication and authorization for your OpenSearch Service.

For more information, see :doc:`OpenSearch Security for Aiven for OpenSearch® <../concepts/os-security>`. 
