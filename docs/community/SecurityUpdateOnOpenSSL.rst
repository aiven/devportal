Security Update on OpenSSL X.509 Email Address Buffer Overflow
(CVE-2022-3786, CVE-2022-3602)

Overview

On 25th Oct 2022, we became aware of a new potential critical OpenSSL Vulnerability, the official details were not disclosed fully till 1st Nov 2022. However, our security and operations teams have been preparing since the initial report.

On 1st Nov 2022, details revealed that there are two HIGH severity OpenSSL vulnerabilities affecting OpenSSL v3.0-3.6, CVE-2022-3786, CVE-2022-3602, which could lead to buffer overruns resulting in a denial of service (“DoS”) or remote code execution (“RCE”). According to OpenSSL.org’s statement, the buffer overrun can be triggered when X.509 certification verification contains malicious values in some certificate fields. Exploitation requires either a certificate authority (“CA”) to have signed a malicious certificate or for an application to continue certificate verification despite failure to construct a path to a trusted issuer. 

At the time of disclosure, the OpenSSL reporting team was not aware of any working exploit that could lead to remote code execution and had no evidence of the issues having been exploited prior to disclosure.

Our security, engineering, and operations teams have been investigating the potential impact on Aiven’s platform and services since additional details of the vulnerability were disclosed. At this time we do not believe that Aiven’s platform or services are affected by these vulnerabilities. 


Further Information

For more information about the vulnerability, see 
1. OpenSSL Blog Post on CVE-2022-3786 and CVE-2022-3602 on OpenSSL Blog
2. CVE-2022-3786 and CVE-2022-3602 on CVE Mitre. It could be referred to when the CVE information is public on CVE Mitre.
