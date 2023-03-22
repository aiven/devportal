Enable OpenSearch® security for Aiven for OpenSearch®
====================================================

Enabling OpenSearch Security enhances the security of your Aiven for OpenSearch service by providing essential features such as user authentication, role-based access control, data encryption both in transit and at rest, and logging of security events.

This article provides information on how to enable OpenSearch Security from the Aiven Console. 

Considerations before enabling OpenSearch Security
---------------------------------------------------

Before enabling OpenSearch Security on your Aiven for OpenSearch service, please note the following important details:

* OpenSearch Security cannot be disabled once enabled. Therefore, ensure that you thoroughly understand the security features and implications before proceeding.
* Fine-grained user access control can be managed through the OpenSearch Dashboard after enabling OpenSearch Security. Any existing user roles and permissions will be automatically transferred to the dashboard.
* To ensure the security of your OpenSearch service, managing the security features of OpenSearch is limited only to a dedicated administrator role.


Activate OpenSearch® Security
-----------------------------

Follow these steps to activate OpenSearch Security for your Aiven for OpenSearch service:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_ and access the Aiven for OpenSearch service for which you want to enable security.
2. Navigate to the **Users** tab within the service.
3. Click the **Activate** button in the OpenSearch Security banner.
4. Review the information presented on the **Enable OpenSearch Security for this service** screen and confirm by selecting the checkbox.
5. In the OpenSearch Security administrator section, enter and confirm a password for the user.

.. note:: 
   * The username for the OpenSearch Security administrator is set by default and cannot be changed.
   * In case you forget the password, it can only be reset by contacting Aiven support.
    Note that the username cannot be changed.

6. Click the **Activate** button to activate the OpenSearch Security administrator user.

After activating OpenSearch Security, you will be redirected to the Users screen, where you can verify that the security feature is enabled. You can then log in to the OpenSearch Dashboard using the Security admin user and manage user roles and permissions.
