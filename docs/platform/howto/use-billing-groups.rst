Manage billing groups
=====================

View and manage billing groups in the Aiven Console
---------------------------------------------------

#. In the account that you want to manage, click **Billing**.

#. Click one of the listed billing groups to browse the details for that billing group.

Billing group page overview
"""""""""""""""""""""""""""

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

Set the account's primary billing group
---------------------------------------

When you set the **primary billing group** for an account, it is the default billing group for all future projects associated with this account unless otherwise specified. The default billing group is also used for any account-level costs or commitments.

To set the **primary billing group** for an account:

#. In the account, go to **Admin** > **Settings**.

#. In the **Primary billing group** section choose a billing group from the list. Click **Confirm**.
