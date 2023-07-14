Cloud security
===============

Learn about Aiven's access control, encryption, network security, data privacy and operator access.


Cloud provider accounts
-------------------------

The regular Aiven services are hosted under cloud provider accounts controlled by Aiven. These accounts are managed only by Aiven operations personnel, and customers cannot directly access the Aiven cloud provider account resources.


Virtual machines
----------------

Each Aiven service consists of one or more virtual machines, which are automatically launched to the target cloud region chosen by the customer. In cloud regions that have multiple Availability Zones (or a similar mechanism), the virtual machines are distributed evenly across the zones in order to provide best possible service in cases when an entire availability zone (which can include one or more datacenters) goes unavailable.

Service-providing virtual machines (VMs) are dedicated for a single customer, i.e. there is no multi-tenancy on a VM basis, and the customer data never leaves the machine, except when uploaded to the offsite backup location.

Virtual machines are not reused and will be terminated, and wiped upon service upgrade or termination.


Data encryption
----------------

Aiven at-rest data encryption covers both active service instances as well as service backups in cloud object storage.

Service instances and the underlying VMs use full volume encryption using LUKS with a randomly generated ephemeral key per each instance and each volume. The key is never re-used and will be trashed at the destruction of the instance, so there's a natural key rotation with roll-forward upgrades. We use the LUKS2 default mode aes-xts-plain64:sha256 with a 512-bit key.

Backups are encrypted with a randomly generated key per file. These keys are in turn encrypted with RSA key-encryption key-pair and stored in the header section of each backup segment. The file encryption is performed with AES-256 in CTR mode with HMAC-SHA256 for integrity protection. The RSA key-pair is randomly generated for each service. The key lengths are 256-bit for block encryption, 512-bit for the integrity protection and 3072-bits for the RSA key.

Aiven-encrypted backup files are stored in the object storage in the same region where the service virtual machines are located. For those cloud providers that do not provide object storage services (i.e. DigitalOcean, UpCloud), the nearest region from another cloud provider that provides an object storage is used.


Networking security
-------------------

Customer access to provided services is only provided over TLS encrypted connections. There is no option for using unencrypted plaintext connections.

Communication between virtual machines within Aiven is secured with either TLS or IPsec. There are no unencrypted plaintext connections.

Virtual machine network interfaces are protected by a dynamically configured iptables-based firewall that only allows connections from specific addresses both from the internal network (other VMs in the same service) or external public network (customer client connections).  The allowed source IP addresses for establishing connections are user controlled on a per-service basis.

.. _networking-with-vpc-peering:

Networking with VPC peering
---------------------------

When using VPC peering, no public internet based access is provided to the services. Service addresses are published in public DNS, but they can only be connected to from the customer's peered VPC using private network addresses.

The services providing virtual machines are still contained under Aiven cloud provider accounts. Aiven VPCs are created per project and not shared between customers, organizations, organizational units, or projects. When services are deployed in a VPC, the DNS names resolve to their Private IP.

Some services allow both public and private access to be enabled while inside a VPC (for testing, for example) and you can find instructions for this in the :doc:`Enable public access in a VPC </docs/platform/howto/public-access-in-vpc>` article.

Connections to Aiven services are always established from your VPC to the peered Aiven VPC. So, you can use VPC firewall rules to prevent any ingress connections from the Aiven side to your network.


Operator access
------------------

Normally all the resources required for providing an Aiven service are automatically created, maintained and terminated by the Aiven infrastructure and there is no manual Aiven operator intervention required.

However, the Aiven Operations Team has the capability to securely login to the service Virtual Machines for troubleshooting purposes. These accesses are audit logged.

No customer access to the virtual machine level is provided.


Customer data privacy
----------------------

Customer data privacy is of utmost importance to Aiven, and is covered by internal security and customer privacy policies as well as strict EU regulations.  

Aiven has partnered with GitHub in scanning for service token leaks and will inform customers of tokens being made public through an email notification.  For more details, check `Improving security: Aiven and GitHub's secret scanning partnership <https://aiven.io/blog/aiven-and-github's-secret-scanning-partnership>`_.

Aiven operators never access customer data, unless explicitly requested to do so by the customer in order to troubleshoot a technical issue.

Aiven operations team has mandatory recurring training regarding the applicable policies.


Periodic security evaluation
-----------------------------

Aiven services are periodically assessed, and penetration tested for any security issues by an independent professional cyber security vendor.


Software bill of materials (SBOM)
----------------------------------

The SBOM is a list of all packages that are being used by Aiven in the services we provide. The list details packages installed in the VM operating system, as well as packages installed by the service itself.

SBOM reports are being widely adopted and may eventually be required for compliance or security assessments. We provide these reports as a file download via our :doc:`CLI </docs/tools/cli/project>`, in CSV or SPDX format.

SBOM reports are only available to customers who have an enterprise support contract and all services within the project must have the latest maintenance patches applied.


Time synchronization
--------------------

All Aiven backend and customer services are configured to use trusted NTP (Network Time Protocol) servers of the respective cloud provider where each service is deployed.
