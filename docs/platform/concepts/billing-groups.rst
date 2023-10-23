Billing groups overview
========================

Billing groups let you set up common billing profiles in an organization that can then be used for any projects within that organization. This includes projects in organizational units within that organization. So, instead of entering the payment information every time you create a project, you can use the information saved in the billing group. 

This also makes it easier to manage your costs. You receive a consolidated invoice for all projects assigned to a billing group. This means you can, for instance, combine costs based on your organization or IT environment (development, test, production) by creating billing groups for each of these.

Organization billing groups can only be used in one organization. You cannot use a billing group for projects that are in other organizations. Aiven credits are also assigned to a billing group and are automatically used to cover charges of any project assigned to that billing group.

To access billing groups, you must be a super admin or account owner.

You can also track spending by exporting cost information to business intelligence tools using the `invoice API <https://api.aiven.io/doc/#tag/BillingGroup>`_.