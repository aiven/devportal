Enable OpenSearch® Security management for Aiven for OpenSearch® |beta|
========================================================================

:doc:`OpenSearch Security <../concepts/os-security>` provides a range of security features, including fine-grained access controls, SAML authentication, and audit logging to monitor activity within your OpenSearch service. By enabling this, you can easily manage user permissions, roles, and other security aspects through the OpenSearch Dashboard.

This article provides information on how to enable OpenSearch Security from the Aiven Console. 

Considerations before enabling OpenSearch Security management
-------------------------------------------------------------

Before enabling OpenSearch Security management on your Aiven for OpenSearch service, please note the following important details:

* OpenSearch Security management cannot be disabled once enabled. Therefore, ensure that you thoroughly understand the security features and implications before proceeding. If you need assistance disabling OpenSearch Security management, contact `Aiven support <https://aiven.io/support-services>`_.
* Fine-grained user access control can be managed through the OpenSearch Dashboard after enabling OpenSearch Security management for the service.  
* Any existing user roles and permissions will be automatically transferred to the OpenSearch Dashboard.
* To ensure the security of your OpenSearch service, managing the security features of OpenSearch is limited only to a dedicated administrator role.
* Once you have enabled OpenSearch Security management, you can no longer use `Aiven Console <https://console.aiven.io/>`_, `Aiven API <https://api.aiven.io/doc/>`_, :doc:`Aiven CLI </docs/tools/cli>`, :doc:`Aiven Terraform provider </docs/tools/terraform>` or :doc:`Aiven Operator for Kubernetes® </docs/tools/kubernetes>` to manage access controls.


Enable OpenSearch® Security management
--------------------------------------

Follow these steps to activate OpenSearch Security management for your Aiven for OpenSearch service:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_ and access the Aiven for OpenSearch service for which you want to enable security.
2. Navigate to the **Users** tab within the service.
3. Select **Enable** in the OpenSearch Security management banner.
4. Review the information presented on the **Enable OpenSearch Security for this service** screen and confirm by selecting the checkbox.
5. In the OpenSearch Security administrator section, enter and confirm a password for the user.

   .. note:: 
     * The username for the OpenSearch Security administrator is set by default and cannot be changed.
     * In case you forget the password, it can only be reset by contacting Aiven support.

6. Select **Enable** to activate the OpenSearch Security administrator user.

After activating OpenSearch Security, you will be redirected to the **Users** screen, where you can verify that the security feature is enabled. 

Next, log in to the :doc:`OpenSearch Dashboard <../dashboards>` using your security admin credentials to access OpenSearch Security, where you can manage user permissions and other security settings.