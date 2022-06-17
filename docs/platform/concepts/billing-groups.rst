Billing groups
==============

Billing groups enable you to set a common billing profile for multiple
projects and generate a consolidated invoice.

Key benefits of billing groups
------------------------------

The key benefits of using billing groups are:

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

.. Note::

   By default, each project belongs to a billing group, and can only belong to a single billing group at a time. A billing group always generates a single invoice. Aiven credits are available in the billing group.

