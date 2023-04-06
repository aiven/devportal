Free plan
==========

The free plan is available for Aiven for PostgreSQL®, Aiven for MySQL, and Aiven for Redis®* services. You don't need a credit card to sign up and you can create one free service for each type. This means you can create one free PostgreSQL, one free MySQL, and one free Redis service.

You can run free plan services alongside a free 30-day trial without affecting your trial credits. Free plan services also continue running after the trial has expired.

Free plan features and limitations
-----------------------------------

Free plans have some limitations, but they can be run indefinitely free of charge. If you need more memory or access to features in the full platform, the free trial may be a better option. 

Free plans include:

* A single node
* 1 CPU per virtual machine
* 1GB RAM
* For PostgreSQL and MySQL: 5GB disk storage
* For Redis: ``maxmemory`` set to 50%
* Management via our web console, CLI, API, Terraform provider, or Kubernetes® operator
* Monitoring for metrics and logs
* Backups
* Integrations between different Aiven services including free, paid, and trial services
* AWS hosting in a limited number of regions:
    * EMEA: aws-eu-north-1, aws-eu-west-1, aws-eu-west-2, aws-eu-west-3
    * Americas: aws-us-east-1, aws-us-east-2, aws-us-west-2, aws-ca-central-1
    * APAC: aws-ap-south-1

There are some limitations of the free plan services:

* No VPC peering
* No external service integrations
* No forking
* For PostgreSQL and MySQL: no connection pooling
* Support only through the `Aiven Community Forum <https://aiven.io/community/forum/>`_
* Only a limited number of AWS regions, no other cloud providers
* Only one service per service type per user and :doc:`organization </docs/platform/concepts/projects_accounts_access>`
* Not covered under Aiven's 99.99% SLA

Free plans do not have any time limitations. However, Aiven reserves the right to shut down services if we believe they violate the `acceptable use policy <https://aiven.io/terms>`_ or are unused for some time.

Upgrading and downgrading
--------------------------

You can upgrade your free plan to a paid plan at any time. 

To upgrade, you need to add a payment method or start a full platform trial. After adding a payment method, selecting upgrade lets you choose a new plan size, cloud, and region. 

.. important::

    If you upgrade your free plan service to a paid plan using a free trial, your service will be terminated if you run out of trial credits and have not entered a payment method.

You can also downgrade a trial or paid plan to the free plan as long as the data you have in that trial or paid service fits into the smaller instance size. 
