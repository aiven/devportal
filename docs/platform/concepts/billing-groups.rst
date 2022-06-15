Billing groups
==============

Billing groups enable you to set a common billing profile for multiple
projects and generate a consolidated invoice.

Key benefits of using billing groups:

-  **Receive a single invoice for all your projects.** When you have
   several Aiven projects that use the same payment method, you can
   receive a single invoice that consolidates all costs instead of
   receiving a separate invoice for each project.

-  **Group costs based on your organization need.** You can merge costs
   based on your organization or IT environment (development, test,
   production) by creating billing groups for related projects. Each
   billing group then generates a consolidated invoice.

-  **Minimize administrative setup of billing profiles shared between
   projects.** Move projects that use the same payment card into a
   billing group and designate a single billing profile to pay their
   costs.

-  **Create dashboards in external Business Intelligence (BI) tools to
   track spending.** Use the *Invoice API* to get the line item costs in
   the invoice to export the cost information for Aiven projects to
   external BI tools.

By default, each project belongs to a billing group, and can only belong
to one billing group at a time. A billing group always generates a
single invoice. Aiven credits are available in the billing group.

.. _h_5759f235c0:

Using billing groups in the Aiven web console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  An **Account** is the entry point for creating and managing billing
   groups.

-  You can group projects under an Account into one or more billing
   groups.

-  You can set a primary billing group for an Account. All future
   projects associated with this account are then added to the primary
   billing group by default.

-  You can move projects under an Account from one billing group to
   another.

-  Aiven credits are available for all projects associated with the
   Account. You can choose to apply the credits to a specific project
   within the Account.

Navigating to billing groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To view billing groups in the Aiven web console:

#. | Click the current project and select **See all projects &
     accounts** .
   | This opens the *Projects & Accounts* view.


#. Click an account that you want to manage and then click the
   **Billing** tab.

   | Here you can create new billing groups and assign projects to your
     billing groups. For more information on creating billing groups,
     `see this article <https://help.aiven.io/en/articles/4634847>`__ .

#. Click one of the listed billing groups to see the details for that
   billing group.

   -  The **Overview** tab that opens by default shows you the projects
      assigned to this billing group, the generated invoices, and the
      applied credits. The **Projects** , **Invoices** , and **Credits**
      tabs provide more detailed information.

   -  The accumulated costs of all projects that are assigned to this
      billing group are shown in the top-right corner.

   -  The *action menu* , which is also in the top-right corner,
      includes options to rename or delete the billing group. Note that
      you can only delete a billing group that has no projects assigned
      to it.

   -  | The **Projects** tab lists the projects that are assigned to the
        billing group.
      | You can assign new projects to the billing group on this tab. If
        you have more than one billing group in the current account, you
        can also move projects between billing groups.

   -  The **Invoices** tab allows you to view and download the invoices
      generated for the billing group. The invoices include separate
      lines for the projects and services assigned to the billing group.


   -  The **Credits** tab allows you to view and assign credit codes for
      the billing group.

   -  The **Events** tab lists all the logged actions for the billing
      group.

   -  The **Billing information** tab allows you to add and update the
      payment method and billing details for generating the invoices.

.. note:: Under the Settings of your Account, you can set the **Primary Billing Group** so that new projects will be assigned by default, unless specified otherwise


For more information, see our `support page <https://help.aiven.io/>`__
or contact us at support@aiven.io .
