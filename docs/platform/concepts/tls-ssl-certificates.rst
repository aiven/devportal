TLS/SSL certificates
====================

All traffic to Aiven services is always protected by TLS. It ensures that third-parties can't eavesdrop or modify the data while in transit between Aiven services and the clients accessing them.

Every Aiven project has its own private Certificate Authority (CA) which is used to sign certificates that are used internally by the Aiven services to communicate between different cluster nodes and to Aiven management systems.

Some service types (listed below) uses the Aiven project's CA for external connections. To access these services, you need to download the CA certificate and configure it on your browser or client.

For other services a browser-recognized CA is used, which is normally already marked as trusted in browsers and operating systems, so downloading the CA certificate is not normally required.

Certificate requirements
------------------------

Most of our services use a browser-recognized CA certificate, but there are exceptions:

- **Aiven for PostgreSQL** requires the CA certificate to connect.

- **Aiven for Apache Kafka** requires the CA certificate, and also the client key and certificate.

For these services you can :doc:`../howto/download-ca-cert` from the service overview page.

.. note::
    Older/existing services may be using the Aiven project's CA, you can request switching to a browser-recognized certificate by opening support ticket and letting us know.

