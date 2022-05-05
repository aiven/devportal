Bring your own account (BYOA)
=============================

Bring Your Own Account (BYOA) is an optional setup feature that gives customers using Aiven services more control over their cloud service provider account. 

The BYOA setup has a custom pricing structure that is calculated case by case. 

For a cost estimate, please contact `Sales@Aiven.io <mailto:sales@aiven.io>`_.

What is BYOA?
-------------

It means that you can get your services through Aiven, but use your existing Cloud Provider account to purchase them.

With BYOA, you use the Aiven Console or CLI to manage your services and generally have the same user experience as with the regular Aiven service model. At the same time, you also receive and can apply any bonuses accruing to your existing account with the cloud provider.

Note that with BYOA, you receive two separate monthly invoices, one from Aiven for their managed services and another from the cloud service provider for the cloud infrastructure costs. 

Who is eligible for BYOA?
-------------------------

The BYOA setup always requires custom work, and not all cloud providers support it yet. Therefore Aiven has set two prerequisites for customers to be eligible:

- Customers must use Amazon Web Services (AWS), Google Cloud Platform (GCP) or Microsoft Azure* accounts (BYOA is not available for others)
- The customer's total monthly spend is over $5000

*\*Excluding Azure Germany*

Why should you use the BYOA model?
----------------------------------

Some companies have data processing limitations that require them to use virtual machines actually owned by them. In this case, the use of normal Aiven services is not possible, because VMs run under Aiven. The BYOA gets around this, because the VMs do not fall under Aiven's ownership in any way.

And as already mentioned, BYOA lets you apply any bonuses, discounts or free credits accruing to your existing account to your Aiven-managed services. 

(Apart from said discounts, cost savings are not typically achieved BYOA. In the BYOA model, you pay less for the Aiven managed service costs, but you still have to pay the cloud service provider. This means that the total costs of the BYOA setup may not be lower (and may even be higher) than Aiven’s regular offering, where Aiven handles the cloud infrastructure costs.)

Cost breakdown of the BYOA model
--------------------------------

Since the creation of each BYOA setup requires a significant amount of development work, Aiven charges a one-time fee for BYOA setup work. This fee is defined on a case by case basis.

Each month, Aiven charges a monthly BYOA fee for computing resources and Aiven services. 

Remember that in BYOA, Aiven does not invoice for the cloud service. As a BYOA customer, you pay for the cloud computing resources you are using directly through your cloud provider portal. 

All BYOA discounts are evaluated case by case. If your company fulfills the requirements specified earlier, contact `Sales@Aiven.io <mailto:sales@aiven.io>`_ for more information and cost estimations of the full setup. 

Testing, POC, and deployments
-----------------------------

BYOA requires setup on your cloud account as well as Aiven's automation. Coordinating this process takes time so we recommend allocating sufficient time for anyone considering using the BYOA deployment model.

- Functionality Testing and Security Validation

  - Ensure the technical feasibility of the Aiven platform
  - Perform all need technical and security audits of the proposed solution

- Deploy and Configure the BYOA Environment

  - Ensure that you have devops resources available to iterate and debug any networking issues
  - This can potentially be done in parallel with phase #1

- Onboarding and Migrations

  - Aiven will be available for support while teams migrate workloads onto the new platform
