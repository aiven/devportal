Billing groups
==============

Billing groups let you to set up common billing profiles in an organization and used across multiple projects. A consolidated invoice is created for all projects assigned to a billing group.

Types of billing groups
------------------------

There are two types of billing groups:
* Organization billing groups
* Project billing groups

An organization billing group is assigned directly to an organization and can be used across all projects within that organization. These billing groups can only be used in one organization. This means that you will not be able to use that billing group for projects that are in other organizations. Aiven credits are available in an organization's billing group.

Project billing groups are assigned to one project. They can only be used for that project. By default, each project belongs to a billing group, and can only belong to a single billing group at a time.

It's best practice to create billing groups at the organization level to help keep track of them and use them across your projects in that organization. 

.. important:: Deleting a project will also remove your access to its billing group. To keep the billing group, assign it to an organization.

Benefits of billing groups
---------------------------

The key benefits of using billing groups are:

-  **Receive a single invoice for all your projects.** When you have several Aiven projects that use the same payment method, all costs for those projects are consolidated into a single invoice instead of separate invoices for each project.

-  **Group costs based on your organization need.** You can merge costs based on your organization or IT environment (development, test, production) by creating billing groups for related projects. 

-  **Minimize administrative setup of billing for multiple projects.** Instread of entering the payment information every time you create a project, you can use the same billing informatin saved in the billing group. 

-  **Create dashboards in external Business Intelligence (BI) tools to track spending.** Use the invoice API to get the line item costs and export the project cost information external BI tools.
