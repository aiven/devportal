Grafana® OAuth configuration and security considerations
============================================================

Grafana® version 9.5.5 introduced significant changes to the OAuth email lookup behavior to enhance security. However, some users may need to revert to the previous behavior as seen in Grafana 9.5.3. This section provides information on how to revert to the 9.5.3 behavior using the ``oauth_allow_insecure_email_lookup`` configuration option, its implications, and the associated security threats. 

Security considerations
------------------------
Before reverting to the previous behavior of Grafana version 9.5.3, it is important to consider the security risks involved.

Authentication bypass vulnerability 
`````````````````````````````````````

By enabling the ``oauth_allow_insecure_email_lookup`` configuration option, the system becomes susceptible to a critical authentication bypass vulnerability using Azure AD OAuth. This vulnerability is officially identified as CVE-2023-3128  and could potentially grant attackers access to sensitive information or unauthorized actions. For more information, refer to the following links:

* `Grafana Labs Security Advisory: CVE-2023-3128 <https://grafana.com/security/security-advisories/cve-2023-3128/>`_
* `Alternative link for CVE-2023-3128 <https://cve.report/CVE-2023-3128>`_


Configuring OAuth email lookup
------------------------------------

To revert to the OAuth email lookup behavior of Grafana version 9.5.3, you can use the ``oauth_allow_insecure_email_lookup`` configuration option.


Enable configuration
```````````````````````
To enable this configuration, include the following line in your Grafana configuration file:

.. code:: 

    [auth]
    oauth_allow_insecure_email_lookup = true

This will restore the behavior to that of Grafana version 9.5.3. However, please be aware of the potential security risks if you choose to do so.

Upgrade to Grafana 9.5.5
-----------------------------

In Grafana 9.5.5, the insecure email lookup behavior has been removed to mitigate the security threat. We recommend upgrading to this version to ensure the security of your system. 

Additional resources
---------------------

For more information on configuring authentication in Grafana, refer to the `official Grafana documentation <https://grafana.com/docs/grafana/v9.5/setup-grafana/configure-security/configure-authentication/>`_. 