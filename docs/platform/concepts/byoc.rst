Bring your own cloud (BYOC)
===========================

About BYOC
----------

Aiven services are usually deployed on Aiven-managed infrastructure, using Aiven-managed security protocols, and backed by Aiven-managed storage and backups. This provides the most seamless straightforward de-risked approach to deploying Aiven services. However, you might need a different configuration if your business, project, or organization has specific requirements for strict regulatory compliance, fine-grained network access control, or cloud purchase commitments in place, for instance.

This is where the bring your own cloud (BYOC) feature comes in enabling you to use your own cloud infrastructure instead of using the Aiven-managed infrastructure. With BYOC, your Aiven organization gets connected with your cloud provider account by creating custom clouds in your Aiven organization. This allows you to manage your infrastructure on the Aiven platform while keeping your data in your own cloud.

Why use BYOC
------------

There a few major reasons to utilize BYOC:

1. **Compliance**: Aiven offers managed environments for several standard compliance regulations, such as HIPAA, PCI DSS, and GDPR. However, if you have strict regulatory requirements or special compliance requirements, BYOC may be the best option for you.
2. **Network auditing**: If you require the visibility of all traffic within any VPC you operate in or need frequent auditing capabilities, BYOC is potentially a good fit. BYOC gives you the ability to audit network metadata but not the actual contents.
3. **Fine-grained network control**: BYOC requires only some specific network access (for example, service management and troubleshooting), otherwise allowing you to customize your network to meet any internal requirements or requirements of your customers.
4. **Cost optimization**: Depending on your cloud provider, with BYOC you can use cost savings plans, committed use discounts, or other strategies to save on compute and storage infrastructure costs related to Aiven services.

Who is eligible for BYOC
------------------------

The BYOC setup is a bespoke service offered on a case-by-case basis, and not all cloud providers support it yet. You need to meet a few requirements to be eligible for BYOC:

- You use one of the following public clouds: Amazon Web Services (AWS), Google Cloud Platform (GCP), or Microsoft Azure (excluding Azure Germany).
- Your total monthly spend is greater than $5,000.
- You have an active enterprise support contract.

When to use the regular Aiven deployment
----------------------------------------

BYOC deployments are not automated, and they add additional complexity to communicating to the Aiven control plane, service management, key management, and security.

In most cases, you can meet your regulatory and business requirements by utilizing a regular Aiven deployment or :doc:`Enhanced Compliance Environment </docs/platform/concepts/enhanced-compliance-env>`.

.. tip::
   
   If you would like to understand BYOC better or are unsure which deployment model is the best fit for you, contact sales@Aiven.io.

BYOC pricing and billing
------------------------

Unlike Aiven's standard all-inclusive pricing, the BYOC setup has custom pricing depending on the nature of your requirements. If you enter this arrangement, you are responsible for all cloud infrastructure and network traffic
charges.

You receive two separate monthly invoices, one from Aiven for their managed services and another from the cloud service provider for the cloud infrastructure costs. This enables you to use any cloud commit you may have and potentially leverage committed use discounts (CUDs) in certain cases.

.. note::

   For a cost estimate and analysis, contact sales@Aiven.io.

.. _byoc-deployment:

Architecture of the standard BYOC deployment
--------------------------------------------

With BYOC, you can use any standard Aiven method (for example, :doc:`CLI </docs/tools/cli>` or :doc:`Terraform </docs/tools/terraform>`) to manage your services and generally have the same user experience as with the regular Aiven deployment model.

.. image:: /images/platform/byoc-standard.png
   :alt: Overview architecture diagram with VPC set up

The standard BYOC deployment requires you to create a Virtual Private Cloud (VPC) dedicated to Aiven services within each region you want to operate in. Aiven accesses these VPCs via a static IP address and then routes traffic through a proxy for additional security. To accomplish this, Aiven utilizes a bastion host logically separated from the
Aiven services you deploy. As the user of these services (for example, Aiven for Apache Kafka®), you are able to utilize them through standard VPC peering techniques. Although the bastion host and the service nodes reside in your managed VPC, they are not accessible (for example, SSH) to anyone outside Aiven.

Depending on the service used, Aiven takes regular backups to enable forking, point in time recovery (PITR), and disaster recovery. These backups by default do not reside in your cloud. If there is a requirement to have all backups
in your own cloud, it's still possible. To accomplish this, Aiven needs an object storage and read-write permissions.

.. important::
   
   All backups are encrypted using Aiven-managed keys, and you are responsible for managing object storage configurations.

What's next
-----------

* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
