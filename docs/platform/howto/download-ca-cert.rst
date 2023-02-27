Download a CA certificate
=========================

If your service needs a CA certificate, download it through the Aiven `web console <https://console.aiven.io>`_ by accessing the overview page for the specific service, and clicking on the **Download** button on the ``CA Certificate`` line.

.. image:: /images/platform/ca-download.png
    :alt: A screenshot of the Aiven web console service page, showing where is the CA certificate download button.

Or, you can use the ``avn`` :doc:`command-line tool </docs/tools/cli>` with the following command::

  avn service user-creds-download --username <username> <service-name>

Read more: :doc:`../concepts/tls-ssl-certificates`
