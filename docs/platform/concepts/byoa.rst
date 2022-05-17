Bring your own account (BYOA)
=============================

What is BYOA?
-------------
Typically, Aiven services will be deployed on Aiven managed infrastructure, using
Aiven managed security protocols, and backed by Aiven managed storage and backups.
This provides the most seamless, straight forward, and de-risked approach to deploying
Aiven services. However, there are cases where this approach is not appropriate such
as strict regulatory compliance.

To meet the needs of these cases, Aiven offers an alternative method to deploy Aiven
services – BYOA. BYOA allows customers to manage their own infrastructure, their own
security posture and keep their data in their own cloud.

Who is eligible for BYOA?
-------------------------

The BYOA setup always requires custom work, and not all cloud providers support it yet. Therefore Aiven has set two prerequisites for customers to be eligible:

- Customers must use Amazon Web Services (AWS), Google Cloud Platform (GCP) or Microsoft Azure* accounts (BYOA is not available for others)
- The customer's total monthly spend is greater than $5,000
- The customer must utilize an Enterprise Support contract

*\*Excluding Azure Germany*

Cost of BYOA
-----------------
The BYOA setup has a custom pricing structure that is calculated on case by case basis. When leveraging BYOA you will negate Aiven's feature of paying for all network traffic out of the service.

Note that with BYOA, you receive two separate monthly invoices, one from Aiven for their managed services and another from the cloud service provider for the cloud infrastructure costs. In this fashion you can utilize any cloud commit you may have and potentially leverage CUDs in certain cases.

For a cost estimate and analysis, please contact Sales@Aiven.io.

Deployment of BYOA
-----------------

With BYOA, you can use any standard Aiven method (e.g. CLI, Terraform) to manage your services and generally have the same user experience as with the regular Aiven deployment model.

BYOA Standard
*************

.. image:: /images/platform/byoa-standard.png

A standard BYOA deployment requires the customer to create a Virtual Private Cloud (VPC)
dedicated to Aiven services within each region they want to operate. Aiven will access these
VPCs via a static IP address and then route traffic through a proxy for additional security.
In order to accomplish this, Aiven will utilize a bastion host, logically separated from the
Aiven services a customer deploys. As the user of these services (e.g. Kafka), you will be
able to utilize them through standard VPC peering techniques. Although the bastion host
and the service nodes will reside in a customer managed VPC, they will not be accessible
(e.g. SSH) to anyone outside of Aiven.

Depending on the service being used, Aiven will take regular backups to enable forking,
Point inTime Recovery (PITR) and disaster recovery. These backups by default will not
reside in the customer’s cloud account. If there is a requirement to have all backups
in your own account we can do this as well. Aiven will need object storage and permissions
to read and write in order to accomplish this. Please bear in mind that all backups are
encrypted using Aiven managed keys and that the customer will be responsible for managing
object storage configurations.

BYOA with IPSec Ingress
*************

.. image:: /images/platform/byoa-ipsec-ingress.png

A slight variation on a standard BYOA deployment enables Aiven to manage a customer's
services through an IPSec tunnel. This deployment can be beneficial if management over
the public internet is infeasible or adds additional complexity.

BYOA with Direct IPSec Ingress
*************

.. image:: /images/platform/byoa-ipsec-ingress-direct.png

Again a slight variation on a standard BYOA deployment enables Aiven to manage a customer's
services through a direct IPSec tunnel. This deployment can be beneficial if there is a
desire to reduce the number of Aiven managed components.

When is BYOA a good fit?
-----------------
There are three major reasons to utilize BYOA:

1. Compliance: Aiven offers managed environments for several standard compliance regulations such as HIPAA, PCI DSS and GDPR. However, if you have strict regulatory requirements, or special compliance requirements, BYOA may be the best option for you.
2. Network auditing. If you require visibility of all traffic within any VPC you operate in or need frequent auditing capabilities, BYOA is potentially a good fit. BYOA will give you the ability to audit network metadata but not the actual contents.
3. Finer grained control over the network. BYOA requires only some specific network access (e.g. service management and troubleshooting), otherwise allowing you to customize your network to meet any internal requirements or requirements of your customers.

Why isn't BYOA a good fit?
-----------------

BYOA deployments are not automated and they add additional complexity for communicating
to the Aiven control plane, service management, key management and security.

In most cases customers can meet their regulatory and business requirements by utilizing
a standard Aiven deployment or Enhanced Compliance Environment. In fact, 99% of Aiven
customers are able to meet their requirements without BYOA. If you would like to understand
BYOA better or are still unsure which deployment model is the best fit for you, please contact our sales department.

Testing, POC, and deployments
-----------------------------

BYOA requires setup on your cloud account as well as Aiven's automation. Coordinating this process takes time so we recommend allocating sufficient time for anyone considering using the BYOA deployment model.

- Functionality Testing and Security Validation

  - Ensure the technical feasibility of the Aiven platform
  - Perform all needed technical and security audits of the proposed solution

- Deploy and Configure the BYOA Environment

  - Ensure that you have DevOps resources available to iterate and debug any networking issues
  - This can potentially be done in parallel with phase #1

- Onboarding and Migrations

  - Aiven will be available for support while teams migrate workloads onto the new platform
