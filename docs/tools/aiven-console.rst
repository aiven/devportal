Aiven Console overview
=======================

The `Aiven Console <https://console.aiven.io>`_ gives you access to create and manage Aiven services, update your user profile, manage settings across projects, set up billing groups, view invoices, and more. This article provides an overview of the main areas in the Aiven Console:

- User profile
- Organization and organizational unit settings
- Projects and services
- Billing groups


.. image:: /images/tools/console/console_services_switchaccount.png
    :alt: The Current services page of the Aiven Console. 


User profile
-------------

To access your user information, user authentication settings, and payment options, click the **profile icon** in the upper right corner of the console.

Name and email
""""""""""""""

You can update your name on the **User Info** tab of the **User profile**. 

.. note:: You cannot edit your email address here. Instead, you can :doc:`migrate your Aiven resources to another email address </docs/platform/howto/change-your-email-address>` within specific projects.

User authentication
"""""""""""""""""""

On the **Authentication** tab of the **User profile**, you can also manage your password and authentication settings, including:

- :doc:`Adding authentication methods </docs/platform/howto/add-authentication-method>`
- :doc:`Managing two-factor authentication </docs/platform/howto/user-2fa>`
- :doc:`Generating authentication tokens </docs/platform/concepts/authentication-tokens>`

Payment cards
"""""""""""""
In the **Payment Options** section, you can :doc:`add or update credit card details </docs/platform/howto/manage-payment-card>`, assign projects to a payment method, and update the :doc:`billing contact </docs/platform/howto/change-billing-contact>`.

Organization and organizational unit settings
----------------------------------------------

The organization or organizational unit that you are currently working with is displayed at the top of the page. You can switch to another organization or organizational unit by clicking the name to open the drop-down menu. You can also create a new organization from this menu.

If you don't have an organization, click **Create organization** to :doc:`create your first organization</docs/tools/aiven-console/howto/create-accounts>`. 
 
.. note:: We strongly recommend creating an organization. It makes managing your projects much easier and comes with many additional features, such as teams (user groups), billing groups, and SAML authentication.

Organization and organizational unit settings are available on the **Admin** page. Here you can:

* :doc:`Manage the teams</docs/tools/aiven-console/howto/create-manage-teams>` 
* Create new projects under an organization or organizational unit
* Configure :doc:`authentication methods for an organization </docs/platform/howto/list-saml>`
* View **Event logs** of activity such as the adding or removing of team members, changing authentication methods, and more
* Access the **Settings** to rename or delete an organization or organizational unit 


Projects and services
----------------------

To navigate between different projects or view all projects click the **Projects** drop-down menu. Selecting a project opens the **Current services** page with a list of all services for that project. Here you see a list of all of your services and :doc:`create services </docs/platform/howto/create_new_service>`.

On the **Current services** page you can also access the :doc:`integration endpoints</docs/integrations>`, VPCs, project event logs, list of project members, and project settings.

Billing groups
---------------

Billing groups let you use billing details across multiple projects and generate a consolidated invoice. Click **Billing** to see and :doc:`manage your billing groups</docs/platform/howto/use-billing-groups>`.

.. note:: You can add and update credit cards in the **User profile**. 
