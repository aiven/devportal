Manage billing groups in the Aiven Console
==========================================

Billing groups enable you to set a common billing profile for multiple
projects and generate a consolidated invoice. To know more about the key benefits read the :doc:`related documentation <../concepts/billing-groups>`.

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

#. Click the current project and select **See all projects & accounts**.

#. Click an account that you want to manage and then click the **Billing** tab.

   .. Tip::
    This window allows you to create new billing groups and assign projects to your billing groups. For more information on creating billing groups, `see the releated article <https://help.aiven.io/en/articles/4634847>`__.

#. Click one of the listed billing groups to browse the details for that billing group.

Navigate the billing group page
'''''''''''''''''''''''''''''''

The billing group page contains multiple sections:

* the **accumulated costs** of all projects that are assigned to the billing group in the top-right corner.
* the *action menu* , available in the top-right corner, includes options to **rename or delete the billing group**. 

  .. Note::
    You can only delete a billing group that has no projects assigned to it.

* the **Overview** tab contains: 
    * the projects assigned to this billing group
    * the generated invoices
    * the applied credits
* the **Projects** tab lists the projects that are assigned to the billing group

  .. Tip::
  
    You can assign new projects to the billing group on this tab. If you have more than one billing group in the current account, you can also move projects between billing groups.

* the **Invoices** tab allows you to **view and download the invoices** generated for the billing group. The invoices include separate lines for each project and service assigned to the billing group.
* the **Credits** tab allows you to view and assign credit codes for the billing group.
* the **Events** tab lists all the logged actions for the billing group.
* the **Billing information** tab allows you to add and update the payment method and billing details for generating the invoices.

.. note:: Under the Settings of your Account, you can set the **Primary Billing Group** so that new projects will be assigned by default, unless specified otherwise


For more information, see our `support page <https://help.aiven.io/>`__
or contact us at support@aiven.io .
