Billing groups
==============

Billing groups let you to set up common billing profiles in an organization that can then be used across multiple projects. Instead of entering the payment information every time you create a project, you can use the information saved in the billing group. 

This makes it easier to manage your costs. You receive a consolidated invoice for all projects assigned to a billing group. This means you can, for instance, combine costs based on your organization or IT environment (development, test, production) by creating billing groups for each of these.

You can also track spending by exporting cost information to business intelligence tools using the `invoice API <https://api.aiven.io/doc/#tag/BillingGroup>`_.

Types of billing groups
------------------------

There are two types of billing groups:
* Organization billing groups
* Project billing groups

An organization billing group is assigned directly to an organization and can be used across all projects within that organization. This includes projects in organizational units under that organization. Organization billing groups can only be used in one organization. This means that you will not be able to use that billing group for projects that are in other organizations. Aiven credits are available in an organization's billing group.

Project billing groups are assigned to one project and can only be used for that project. 

It's best practice to create billing groups at the organization level so that they are easier to manage and so you can use them across your projects. 

.. important:: When you have a project billing group and delete the project, you will also lose access to that billing group and the its invoices. To keep the billing group, make it an organization billing group by assigning it to an organization.

