Enhanced compliance environments (ECE)
===========================================

As a business that collects, manages, and operates on sensitive data that is protected by privacy and
compliance rules and regulations – any vendor that assists with this collection, management and
operation is subject to these same rules and regulations. Aiven meets the needs of these
businesses by providing specialized enhanced compliance environments (ECE) that comply with many
of the most common compliance requirements.

An enhanced compliance environment will run on Aiven managed infrastructure with the additional
compliance requirement that no ECE VPC is shared and the managed account is logically separated
from the standard Aiven deployment account. This decreases the blast radius of the environment
to prevent inadvertent data sharing. Furthermore, users of an ECE **must** encrypt all data prior
to reaching an Aiven service. As part of the increased compliance of the environment, enhanced logging
is enabled for – ``stderr``, ``stout``, and ``stdin``.

Who is eligible?
----------------
Enhance compliance environments, although similar to standard environments, involve added setup
and maintenance complexity. The following are requirements to utilize an ECE:

- A BAA signed with Aiven
- Plan to operate in one or more of Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure
- Total monthly spend is greater than $5,000
- An active Enterprise Support Contract

Cost of ECE
----------------
The cost of an enhanced compliance environment, beyond the initial eligibility requirements,
is exactly the same as a standard Aiven deployment. All service costs are the same and all
egress networking charges are still covered in an ECE. Customers can still take advantage of
any applicable marketplaces and spend down their commitment accordingly.

Similarities to a standard environment
----------------
In many ways, an ECE is the same as a standard Aiven deployment. All of Aiven’s tooling
(:doc:`CLI </docs/tools/cli>`, :doc:`Terraform </docs/tools/terraform/index>`, etc.) interact with ECEs seamlessly, you will still be able to take advantage
of all of Aiven’s service integrations, and access to the environment can be achieved through
VPC peering or Privatelink (on AWS or Azure). However, there are some key differences from
standard environments as well:

- No internet access. Internet access cannot even be allow-listed as would be the case in standard private VPCs
- VPCs cannot be automatically provisioned and must be manually configured by our networking team.
- VPC peering or Privatelink connections must be manually approved on the Aiven end

With these differences in mind, Aiven requires the following to provision an Enhanced Compliance
Environment:

- A CIDR block for all region/environment combinations. For example, if you have a development, QA and production environment and operate in 3 regions in each of those, we will need 9 CIDR blocks.
The necessary peering information to enable the peer from our end. This differs between clouds:

AWS:
    * AWS account ID
    * VPC ID
GCP:
    * GCP Project ID
    * VPC Network Name
Azure:
    * Azure Tenant ID
    * Azure App ID
    * Azure VNet ID

What compliances are covered?
----------------
Although not exhaustive, Aiven is capable of supporting both the Health Insurance Portability and
Accountability Act (HIPAA) and the Payment Card Industry Data Security Standard (PCI DSS)
compliances. If you require compliance beyond these please contact our sales department so we
can better understand your specific needs. Additionally, we also offer an alternative deployment
option -- :doc:`Bring Your Own Account (BYOA) </docs/platform/concepts/byoa>`.

Migrating
----------------
Migrations to Aiven are fairly straightforward in general, but migrating to an ECE can add a
tiny bit of complexity. If the migration is for a new service there are a few standard
migration methods that will work – please contact sales at Sales@Aiven.io and a Solution Architect will be
able to help.

If you need to migrate an existing Aiven service to an ECE the standard automated migration
methods will not work out of the box. To facilitate the migration, the Aiven network
team will create a VPN tunnel between your non-compliant VPC and your ECE VPC to enable a
one-click migration. The migration will then be performed in an automated and zero-downtime
fashion. Once the migration is complete, we will remove the VPN tunnel.
