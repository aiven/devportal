Aiven statement on Meltdown and Spectre vulnerabilities
=======================================================

Information regarding the Intel/AMD/ARM CPU flaw that affects Aiven services

**Document History**

2017-01-04 Created

2017-01-04, 12:20 UTC, Added link to Meltdown & Spectre information page

**Summary**

Aiven is aware of recently disclosed research regarding side-channel analysis of speculative execution on modern computer processors. This analysis has revealed several different vulnerabilities which have been named Meltdown and Spectre by the researchers and are tracked as `CVE-2017-5715 <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715>`_, `CVE-2017-5753 <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753>`_, and `CVE-2017-5754 <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754>`_. Further details on the vulnerabilities can also be found at https://meltdownattack.com/.

Aiven will perform the necessary actions to protect your data and services from these vulnerabilities. These actions are implemented as automatic or scheduled maintenance tasks, require no user intervention and result in no impact on availability of the services.

Aiven will perform the necessary actions to protect your data and services from these vulnerabilities. These actions are implemented as automatic or scheduled maintenance tasks, require no user intervention and result in no impact on availability of the services.

**Details**

Each Aiven service consists of one or more dedicated virtual machines launched to the cloud and region chosen by the customer. We thus consider these vulnerabilities on two levels: cloud infrastructure and service level.

**Cloud Infrastructure**

On infrastructure, the risk of the vulnerability is access of customer data via co-hosted virtual machines. We follow the patching efforts and guidance from the clouds providers on this front:

- Amazon Web Services reports that all infrastructure has been patched. (https://aws.amazon.com/security/security-bulletins/AWS-2018-013/)

- Google Cloud Platform states that all infrastructure has been patched. (Google Compute Engine Security Bulletin 2018-01-03)

- Azure reports that the majority of the Azure infrastructure has been patched. (https://azure.microsoft.com/en-us/blog/securing-azure-customers-from-cpu-vulnerability/). We continue to monitor and react to notifications on impacted VMs.

- UpCloud plans to roll out the necessary patches in the coming days. (UpCloud: Information regarding the Intel CPU vulnerability (Meltdown))

- DigitalOcean is conducting ongoing investigation on the issue. We continue to monitor and react to notifications on impacted VMs.

**Aiven Services**

On the service or intra-VM level, we will be rolling out maintenance updates with the relevant security patches to all services. We consider threat risk at this level lower than the infrastructure side: access to all Aiven services require user authentication.

- Aiven PostgreSQL® may be subject to the Spectre attacks resulting in privilege escalation between configured PostgreSQL database users. Custom code can be executed by authenticated PostgreSQL database users through the supported extensions.

- Aiven Redis®* may be subject to Spectre attacks as it allows execution of custom code in the form of LUA scripts for authenticated users. However, since Redis doesn't support more than one user or other access controls, the attack doesn't grant additional access.

- Aiven Elasticsearch® is not vulnerable.

- Aiven Grafana® is not vulnerable.

- Aiven InfluxDB® is not vulnerable.

- Aiven for Apache Kafka® is not vulnerable.

Regardless of this risk analysis, we will update all Aiven services in the coming days following the security best practices.

**Updates and Contact Information**

Latest updates will be added to this help article at http://help.aiven.io/incident-reports/aiven-statement-on-meltdown-and-spectre-vulnerabilities

For any further questions, please contact Aiven support.