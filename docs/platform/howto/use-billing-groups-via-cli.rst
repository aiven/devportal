Manage billing groups in the Aiven Console
==========================================

.. note::
    Please ensure that you have the latest version of Aiven Client.

At the end of each calendar month, Aiven invoices you for costs accrued by Aiven services running in your project during the month. By default, we send one invoice per project, which is often just what you need. 

In some cases however, you may want to group the costs differently. It could be, for example, that you want to have separate projects for your development teams, staging environment, and production services, so that production services are billed in one invoice, and everything else in another. In situations like this, billing groups come into play.

A billing group is a group of projects that share the same billing information (credit card, billing address etc.), and their costs are consolidated into a single invoice. In short, one invoice is sent for each billing group.

By default, a dedicated billing group exists for each project. In standard cases, this is transparent to the user. As before, you are able to configure the project, including billing information, using the project APIs.

To organize your projects to groups, you have to assign them to billing groups appropriately, which requires you to be aware of our billing groups.\

Get Started
===========

Start by listing your projects and billing groups:

::

    $ avn project list

.. image:: /images/platform/billing/use-billing-groups-via-cli-image1.png
    :alt: list of projects

::

    $ avn billing-group list

.. image:: /images/platform/billing/use-billing-groups-via-cli-image2.png
    :alt: list of billing-groups

In this case, we have two projects, and can see that there's a billing group for each. We have already configured billing information (credit card etc.) for project 'test', and would like 'another-project' to appear in the same invoice, and to be charged from the same card. 

How do we do that?
==================

The solution is to assign all of you projects to a single billing group, one by one. In this case, let's use the billing group we already have for project 'test':

::

    $ avn billing-group assign-projects d30c8013-3712-45eb-ab93-371e8f47263d another-project
    $ avn billing-group get d30c8013-3712-45eb-ab93-371e8f47263d --verbose

.. image:: /images/platform/billing/use-billing-groups-via-cli-image3.png
    :alt: details of billing-group d30c8013-3712-45eb-ab93-371e8f47263d

And that's it! When the month ends, you'll only receive a single invoice, containing both of your projects. Your credit card, if you're paying with a card, will only be charged once.

Pretty names for billing groups
===============================

We can also give our billing group a nicer name if we want to, and finally delete the other billing group that's now empty.

::
    $ avn billing-group update d30c8013-3712-45eb-ab93-371e8f47263d --name "My consolidated invoice" 
    $ avn billing-group list
    $ avn billing-group delete d30c8013-3712-45eb-ab93-371e8f47263d

.. image:: /images/platform/billing/use-billing-groups-via-cli-image4.png
    :alt: details of command the three above commands

If we later decide we'd like to have separate invoices after all, we can create a new billing group and assign one of the projects to it.

Creating a new project in a pre-existing billing group
======================================================

Each project must always have billing information defined, so when creating a new project, it is assigned to a billing group. By default, a new dedicated billing group is created, with only the new project as the member.

However, it's also possible to specify another billing group that the project should created in, which saves you the trouble of assigning it to it later. If you do this, then no new billing group is created.

First, find out the ID of the billing group that should hold the new project:

::
    $ avn billing-group list BILLING_GROUP_ID BILLING_GROUP_NAME

.. image:: /images/platform/billing/use-billing-groups-via-cli-image5.png
    :alt: list of the  BILLING_GROUP_ID BILLING_GROUP_NAME and ACCOUNT_NAME

Create your project, giving the ID of your billing group:

::
    $ avn project create --billing-group-id d30c8013-3712-45eb-ab93-371e8f47263d my-new-prod-project

And when you now query the details of your billing group, your new project is a member:

::
    $ avn billing-group get d30c8013-3712-45eb-ab93-371e8f47263d --verbose 

.. image:: /images/platform/billing/use-billing-groups-via-cli-image6.png
    :alt: details of billing-group

Permissions
===========

To assign a project to a new billing group, you should have administrator level privileges for both the project, and the billing group.

You are automatically made admin of any projects or billing groups you create, and the default billing groups automatically created for any projects you create.

Discounts, credits, and commitmments
====================================

The recommended way of applying discounts and commitments is now at the billing group level. Discounts apply for all projects in the billing group, and commitment to the invoice pre-tax total.

Credits too can be assigned at the billing group level, meaning the credits are applied on the invoice total that includes costs from all projects.

API access of invoice lines
===========================

It's possible to list individual invoice lines for a given invoice. This can be useful for:

* Calculating the cost of a single service or project, in an invoice that contains several services

* Tracking credit consumption or support costs separately from service use

* Tracking amount of paid VAT separately from service or other costs

and anything else that requires details beyond the total amount of the invoice.

::
    $ avn billing-group invoice-list d30c8013-3712-45eb-ab93-371e8f47263d 

.. image:: /images/platform/billing/use-billing-groups-via-cli-image7.png
    :alt: list of invoices for billing-group d30c8013-3712-45eb-ab93-371e8f47263d 

::
    $ avn billing-group invoice-lines d30c8013-3712-45eb-ab93-371e8f47263d f3397-1

.. image:: /images/platform/billing/use-billing-groups-via-cli-image8.png
    :alt: Invoice lines of an invoice

Lines which correspond to a time interval (such as service_charge lines) have timestamp_begin and timestamp_end set. This interval is always fully within the billing month; if a service remains powered on during an interval that spans several months, the cost is split between separate lines on each month's invoice.

The interval is closed at the beginning and open at the end, which means that for e.g. interval spanning the entire November of 2020, values for timestamp_begin and timestamp_end are 2020-11-01T00:00:00Z and 2020-12-01:T:00:00:00Z.

For services and other resources billed per hour, one invoice line is created for each continuous interval during the billing month the resource is active and accruing cost. This means that if you first power a service off and then back on again, you may need to add up multiple invoice lines to get the total cost of the service.

In addition to past invoices, you can fetch invoice lines of the estimated invoice for ongoing billing month, but note that in that case, invoice contents may be incomplete. Service charge lines are created only for use up to the time the estimate was last updated, and other types of charges, such as use of credits, or special one-off charges, may be missing altogether.

Things to Remember
==================

Invoice estimates are updated periodically, so when moving projects from one billing group to another, the effect in the estimated invoice contents may not become visible until after an hour or two. The same applies to the PDF invoices downloadable in Aiven console.

Once a billing month has ended, the final invoice for that period is generated, which includes the projects that were in the billing group on the 1st day of the following month. After the month's final invoice has been generated, it's no longer possible to add or remove projects to or from that invoice.

Invoice line types
==================

These are the invoice line types that exist:

* "service_charge" : Charge for running an Aiven series during a continuous time interval.

* "extra_charge" : A one-off or monthly recurring charge of a fixed amount. the most common use for this are the support contract charges.

* "credit_consumption" : Adjustment to invoice total from using credits; note that since they reduce the invoice total, their amounts are negative.

* "commitment_fee" : Extra cost to cover the difference between minimum committed and actual spend, if there's a minimum spend agreement in place.

* "rounding" : Rounding of invoice total at the end. In practice, this is used with a small negative amount to round to zero invoices with total too small to charge (invoices with << $1.00 of total charges during a month).

* "other_event" : Something else not covered by the above categories; the line description will contain some human-readable details

* "multiplier" : The total of these lines are always zero; they exists to notify the invoice recipient that a discount multiplier has been applied on the services in the invoice.
