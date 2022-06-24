Bring your own account (BYOA)
=============================

Aiven services are usually deployed on Aiven managed infrastructure, using
Aiven managed security protocols, and backed by Aiven managed storage and backups.
This provides the most seamless, straight forward, and de-risked approach to deploying
Aiven services. However, there are cases where this approach is not appropriate, such
as the need to achieve strict regulatory compliance.

In cases like these, Aiven offers customers the ability to instead BYOA (Bring
Your Own Account).  BYOA allows customers to manage their own infrastructure,
their own security posture and keep their data in their own cloud.

When to consider bringing your own account
------------------------------------------

There are three major reasons to utilize BYOA:

1. **Compliance**: Aiven offers managed environments for several standard compliance regulations such as HIPAA, PCI DSS and GDPR. However, if you have strict regulatory requirements, or special compliance requirements, BYOA may be the best option for you.
2. **Network auditing**: If you require visibility of all traffic within any VPC you operate in or need frequent auditing capabilities, BYOA is potentially a good fit. BYOA gives you the ability to audit network metadata but not the actual contents.
3. **Fine grained network control**: BYOA requires only some specific network access (e.g. service management and troubleshooting), otherwise allowing you to customize your network to meet any internal requirements or requirements of your customers.

Who is eligible?
----------------

The BYOA setup is a bespoke service offered on a case-by-case basis, and not
all cloud providers support it yet. Therefore customers must meet the following
requirements:

- Use a cloud that supports these features: Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure*
- Total monthly spend is greater than $5,000
- An active Enterprise Support contract

*\*Excluding Azure Germany*

When to use a standard Aiven deployment
---------------------------------------

BYOA deployments are not automated and they add additional complexity for communicating
to the Aiven control plane, service management, key management and security.

In most cases customers can meet their regulatory and business requirements by utilizing
a standard Aiven deployment or :doc:`Enhanced Compliance Environment </docs/platform/concepts/enhanced-compliance-env>`. In fact, 99% of Aiven
customers are able to meet their requirements without BYOA. If you would like to understand
BYOA better or are unsure which deployment model is the best fit for you, please contact our sales department Sales@Aiven.io.

Pricing and billing
-------------------

Unlike Aiven's standard all-inclusive pricing, the BYOA setup has custom
pricing depending on the nature of your requirements. Customers entering this
arrangement are responsible for all cloud infrastructure and network traffic
charges.

.. Note:: Customers receive two separate monthly invoices, one from Aiven for their managed services and another from the cloud service provider for the cloud infrastructure costs. This enables you to use any cloud commit you may have and potentially leverage CUDs in certain cases.

For a cost estimate and analysis, please contact Sales@Aiven.io.

Architecture of BYOA deployments
--------------------------------

With BYOA, you can use any standard Aiven method (e.g. :doc:`CLI </docs/tools/cli>`, :doc:`Terraform </docs/tools/terraform/terraform>`) to manage your services and generally have the same user experience as with the regular Aiven deployment model.

BYOA standard
'''''''''''''

.. image:: /images/platform/byoa-standard.png
   :alt: Overview architecture diagram with VPC set up

A standard BYOA deployment requires the customer to create a Virtual Private Cloud (VPC)
dedicated to Aiven services within each region they want to operate. Aiven will access these
VPCs via a static IP address and then route traffic through a proxy for additional security.
In order to accomplish this, Aiven will utilize a bastion host, logically separated from the
Aiven services a customer deploys. As the user of these services (e.g. Aiven for Apache Kafka®),
you will be able to utilize them through standard VPC peering techniques. Although the bastion
host and the service nodes will reside in a customer managed VPC, they will not be accessible
(e.g. SSH) to anyone outside of Aiven.

Depending on the service being used, Aiven will take regular backups to enable forking,
Point in Time Recovery (PITR) and disaster recovery. These backups by default will not
reside in the customer’s cloud account. If there is a requirement to have all backups
in your own account we can do this as well. Aiven will need object storage and permissions
to read and write in order to accomplish this. Please bear in mind that all backups are
encrypted using Aiven managed keys and that the customer will be responsible for managing
object storage configurations.

BYOA with IPsec ingress
'''''''''''''''''''''''

.. image:: /images/platform/byoa-ipsec-ingress.png
   :alt: Overview architecture diagram with IPsec tunnel

A slight variation on a standard BYOA deployment enables Aiven to manage a customer's
services through an IPsec tunnel. This deployment can be beneficial if management over
the public internet is infeasible or adds additional complexity.

BYOA with direct IPsec ingress
''''''''''''''''''''''''''''''

.. image:: /images/platform/byoa-ipsec-ingress-direct.png
   :alt: Overview architecture diagram with direct IPsec access

Again a slight variation on a standard BYOA deployment enables Aiven to manage a customer's
services through a direct IPsec tunnel. This deployment can be beneficial if there is a
desire to reduce the number of Aiven managed components.
