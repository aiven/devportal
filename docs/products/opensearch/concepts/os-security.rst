OpenSearch Security for Aiven for OpenSearch® |beta|
=====================================================
OpenSearch Security is a powerful feature that enhances the security of your OpenSearch service. By :doc:`enabling OpenSearch Security management <../howto/enable-opensearch-security>`, you can implement fine-grained access controls, SAML authentication, and audit logging to track and analyze activities within your OpenSearch environment. 

With OpenSearch Security enabled, you can manage user access and permissions directly from the :doc:`OpenSearch Dashboard <../dashboards>`, giving you full control over your service's security.

.. warning:: 
  * Once you have enabled OpenSearch Security management, you can no longer use `Aiven Console <https://console.aiven.io/>`_, `Aiven API <https://api.aiven.io/doc/>`_, :doc:`Aiven CLI </docs/tools/cli>`, :doc:`Aiven Terraform provider </docs/tools/terraform>` or :doc:`Aiven Operator for Kubernetes® </docs/tools/kubernetes>` to manage access controls.
  * You must use the OpenSearch Security Dashboard or OpenSearch Security API for managing user authentication and access control after enabling OpenSearch Security management.
  * Once enabled, OpenSearch Security management cannot be disabled. If you need assistance disabling OpenSearch Security management, contact `Aiven support <https://aiven.io/support-services>`_.

.. note:: 
  * To implement basic and simplified access control, you can use :doc:`Aiven's Access Control Lists (ACL)<../howto/control_access_to_content>` to manage user roles and permissions.
  
OpenSearch Security use cases
--------------------------------
OpenSearch Security is a versatile and valuable feature that can meet the needs of a wide range of customers. Some common use cases for this feature include:

* **Single Sign-On integration:** 
  
  If you use an identity management software like Okta or Azure AD, you can use SAML integration to access your OpenSearch Dashboard through your identity provider. With this feature, you won't need to create and manage separate login credentials for OpenSearch, simplifying the authentication process.

* **Advanced access control:**
  
  If you need different levels of access controls for your employees, OpenSearch Security's Role-Based Access Control (RBAC) can help. With RBAC, you can set up different roles with different access levels and map them to different users. Role mapping is also available with SAML integration, making this feature ideal for enterprises.

* **Compliance and audit logging:**
  
  If OpenSearch is a critical database in your system, you may need to document a historical record of activity for compliance purposes and other business policy enforcement. OpenSearch Security includes an audit logs feature to help you meet these needs.
* **Multi-tenancy:**
  
  If you're a reseller or have many smaller departments, you may need different tenants on your OpenSearch Dashboard. OpenSearch Security provides multi-tenancy capabilities, ensuring that each tenant's data is kept separate and secure.


Key OpenSearch Security features
---------------------------------
OpenSearch Security in Aiven for OpenSearch service offers a range of features to manage the security and access control of your OpenSearch service. These include: 

* **Role-based access controls:** With OpenSearch Security, you can set up role-based access controls and advanced level security, such as document-level security, field-level security, user and role mapping, and field masking to control access to sensitive data. 

  .. note:: 
    User impersonation and cross-cluster search are not supported for the beta release. 

* **SAML integration:** Aiven for OpenSearch provides basic SAML integration. This allows you to access your OpenSearch Dashboard through the identity provider of your choice.

  .. note:: 
    Aiven for OpenSearch provides basic SAML integration for the beta release, and certain features, such as logout support and request signing, is not be included.

* **OpenSearch Dashboard multi-tenancy:** OpenSearch Security provides OpenSearch Dashboard multi-tenancy, which allows you to have different tenants on your OpenSearch Dashboard. 

* **OpenSearch audit-logs:** Aiven for OpenSearch Security includes OpenSearch Audit-logs, which allow you to document a historical record of activity for compliance purposes and other business policy enforcement.



OpenSearch Security management changes and impacts
----------------------------------------------------
Enabling OpenSearch Security management on your Aiven for OpenSearch service through the Aiven console triggers several changes:

* Users and role-based access control will be managed through the OpenSearch Security dashboard or OpenSearch Security API.

* The ``os-sec-admin`` user will initially be mapped to the pre-defined role ``service_security_admin_access``, which provides unrestricted access to the service, including the OpenSearch Security API and OpenSearch Security dashboard.

* As an ``os-sec-admin`` user, you can add or remove users from pre-defined roles, and create new roles and assignments, but some pre-defined roles cannot be changed or deleted.

* All service users defined before enabling OS Security management are included in OpenSearch's internal users, with the attribute ``provider_managed: False``. However, the users ``avnadmin`` and ``os-sec-admin``,  are still managed by the service platform and have the attribute ``provider_managed:true``. While service platform management of these users is limited to password changes, they can still be assigned to different roles as needed in the OpenSearch Security dashboard.


For information on how to enable OpenSearch Security management on Aiven Console, see :doc:`Enable OpenSearch® Security management for Aiven for OpenSearch® <../howto/enable-opensearch-security>`. 