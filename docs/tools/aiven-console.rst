Aiven Console
=============

The `Aiven Console <https://console.aiven.io>`_ gives you access to create and manage Aiven services, update your user profile, manage account settings, set up billing groups, view invoices, and more. This article provides an overview of the main areas in the Aiven Console:

- User profile
- Account settings
- Projects and services
- Billing groups


.. image:: /images/tools/console/console_services_switchaccount.png
    :alt: The Current services page of the Aiven Console. 


Manage your user profile
------------------------

To access your user information, user authentication settings, and payment options, click the **profile icon** in the upper right corner of the console.

Name and email
""""""""""""""

You can update your name on the **User Info** tab of the **User profile**. 

.. note:: You cannot edit your email address here. Instead, you can :doc:`migrate your Aiven resources to another email address </docs/platform/howto/change-your-email-address>` within specific projects.

User authentication
"""""""""""""""""""

On the **Authentication** tab of the **User profile**, you can also manage your password and authentication settings, including:

- :doc:`Enabling Aiven passwords </docs/platform/howto/enable-aiven-password>`
- :doc:`Managing two-factor authentication </docs/platform/howto/user-2fa>`
- :doc:`Generating authentication tokens </docs/platform/concepts/authentication-tokens>`

Payment cards
"""""""""""""
In the **Payment Options** section, you can :doc:`add or update credit card details </docs/platform/howto/manage-payment-card>`, assign projects to a payment method, and update the :doc:`billing contact </docs/platform/howto/change-billing-contact>`.

Manage your accounts
--------------------

The account you are currently working with is displayed at the top of the page. You can switch accounts by clicking the account name to open the drop-down menu. You can also create a new account from this menu.

If you don't have an account, click **Create account** to :doc:`create your first account </docs/tools/aiven-console/howto/create-accounts>`. 
 
.. note:: We strongly recommend creating an account. It makes managing your projects much easier and comes with many additional features, such as teams (user groups), billing groups, and SAML authentication.

Account-level settings and options are available on the **Admin** page. Here you can:

* :doc:`Manage the teams for this account</docs/tools/aiven-console/howto/create-manage-teams>`
* Create new projects for this account
* Configure :doc:`authentication methods for the account </docs/platform/howto/list-saml>`
* View **Event logs** of account activity such as the adding or removing of team members, changing authentication methods, and more
* Access the account **Settings** to rename or delete an account 


Manage your projects and services
---------------------------------

To navigate between different projects or view all projects click the **Projects** drop-down menu. Selecting a project opens the **Current services** page with a list of all services for that project. Here you see a list of all of your services and :doc:`create services </docs/platform/howto/create_new_service>`.

On the **Current services** page you can also access the :doc:`integration endpoints</docs/integrations>`, VPCs, project event logs, list of project members, and project settings.

Manage billing groups
---------------------

Billing groups let you use billing details across multiple projects and generate a consolidated invoice. Click **Billing** to see and :doc:`manage your billing groups</docs/platform/howto/use-billing-groups>`.

.. note:: You can add and update credit cards in the **User profile**. 
