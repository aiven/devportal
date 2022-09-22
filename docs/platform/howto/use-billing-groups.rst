Manage billing groups in the Aiven Console
==========================================

Billing groups enable you to set a common billing profile for multiple
projects and generate a consolidated invoice. To learn more about the key benefits of billing groups read the :doc:`related documentation <../concepts/billing-groups>`.

Billing groups and Aiven accounts
---------------------------------

An Aiven **Account** is the entry point for creating and managing billing groups. The following are options available for billing groups via the `Aiven Console <https://console.aiven.io/>`_:

- Within an Account you can create one or more billing groups, depending on the need
- You can group projects under an Account into one or more billing groups
- You can set a **primary billing group** for an Account. All future projects associated with this Account are then added to the primary billing group by default.
- You can move projects under an Account from one billing group to another.

Aiven credits are available for all projects associated with the Account. You can choose to apply the credits to a specific project within the Account.

Manage billing groups
---------------------

To view and manage billing groups in the `Aiven Console <https://console.aiven.io/>`_:

#. In the account that you want to manage, click **Billing**.

   .. tip::
    This window allows you to create new billing groups and assign projects to your billing groups. For more information on creating billing groups, `see the related article <https://help.aiven.io/en/articles/4634847-getting-started-with-billing-groups>`__.

#. Click one of the listed billing groups to browse the details for that billing group.

Billing group page overview
'''''''''''''''''''''''''''

When you select a billing group, the page that opens displays the accumulated costs of all projects that are assigned to the billing group. 

The action menu in the top right includes options to rename or delete the billing group. 

.. note:: You can only delete a billing group that has no projects assigned to it.

This page has other sections with more information:

* On the **Invoices** tab you can view and download the invoices generated for the billing group. The invoices include separate lines for each project and service assigned to the billing group.
* The **Projects** tab lists the projects that are assigned to this billing group.

  .. tip:: You can assign new projects to the billing group on this tab. If you have more than one billing group in the current account, you can also move projects between billing groups.

* On the **Credits** tab you can view and assign credit codes for the billing group.
* The **Events** tab lists all the logged actions for the billing group.
* On the **Billing information** tab you can add or update the payment method and other billing details for generating the invoices.

  .. note:: In the settings for your account, you can set the primary billing group that new projects are assigned to by default, unless specified otherwise.