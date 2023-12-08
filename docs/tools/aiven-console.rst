Aiven Console overview
=======================

The `Aiven Console <https://console.aiven.io>`_ gives you access to create and manage Aiven services, update your user profile, manage settings across organizations and projects, set up billing groups, view invoices, and more. This article provides an overview of the main areas in the console:

- User profile
- Organization and organizational unit settings
- Projects and services
- Billing groups

User profile
-------------

To view your personal information, authentication settings, and organizations you belong to, click the **User information** profile icon in the top right. The user profile is also the place where you can enable :doc:`feature previews </docs/platform/howto/feature-preview>` to test upcoming features and get referral links.

Name and email
""""""""""""""

You can :doc:`update your name and other personal details </docs/platform/howto/edit-user-profile>` in your user profile. 

.. note:: You cannot edit your email address here. Instead, you can :doc:`migrate your Aiven resources to another email address </docs/platform/howto/change-your-email-address>` within specific projects.

User authentication
"""""""""""""""""""

On the **Authentication methods** tab of the **User profile**, you can manage your password and authentication settings, including:

- :doc:`Adding authentication methods </docs/platform/howto/add-authentication-method>`
- :doc:`Managing two-factor authentication </docs/platform/howto/user-2fa>`

Authentication tokens 
""""""""""""""""""""""

On the **Tokens** tab of the **User profile**, you can generate or revoke :doc:`authentication tokens </docs/platform/concepts/authentication-tokens>`.


.. _orgs-units-settings:

Organization and organizational unit settings
----------------------------------------------

The :doc:`organization or organizational unit </docs/platform/concepts/projects_accounts_access>` that you are currently working with is displayed at the top of the page. You can switch to another organization or organizational unit by clicking the name to open the drop-down menu. 

If you don't have an organization, click **Create organization** to :doc:`create your first organization</docs/tools/aiven-console/howto/create-accounts>`. 
 
.. note:: We strongly recommend creating an organization. It makes managing your projects much easier and comes with many additional features, such as groups, billing groups, and SAML authentication.

Organization and organizational unit settings are available on the **Admin** page. Here you can:

* :doc:`Manage your groups </docs/platform/howto/manage-groups>` 
* Create new projects under an organization or organizational unit
* Configure :doc:`authentication methods for an organization </docs/platform/howto/list-saml>`
* View logs of activity such as the adding or removing of users, changing authentication methods, and more
* Rename or delete an organization or organizational unit 

Projects and services
----------------------

To navigate between different projects or view all projects click the **Projects** drop-down menu. This menu shows only the projects within the organization or organizational unit that you are currently working in. Selecting a project opens the **Services** page with a list of all services in that project. Here you can view the status of the services and :doc:`create new services </docs/platform/howto/create_new_service>`.

On the **Services** page you can also access the :doc:`integration endpoints</docs/integrations>`, VPCs, project logs, list of project members, and project settings.

Billing groups
---------------

Billing groups let you use billing details across multiple projects and generate a consolidated invoice. Click **Billing** to see and :doc:`manage your billing groups</docs/platform/howto/use-billing-groups>` and :doc:`payment cards </docs/platform/howto/manage-payment-card>`.
