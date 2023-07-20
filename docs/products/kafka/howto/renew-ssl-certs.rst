Renew and Acknowledge service user SSL certificates
===================================================
In every Aiven for Apache Kafka® service, when the existing service user SSL certificate is close to expiration (approximately 3 months before the expiration date), a new certificate is automatically generated, including the renewal of the private key. 

During the renewal process, both the SSL certificate and its corresponding private key are regenerated. This approach is implemented to enhance overall security and maintain the certificate's integrity.

The project admins, operators, and tech email addresses associated with the service are notified about this certificate renewal.

The old certificate remains functional until its expiration date, allowing for a seamless transition to the new certificate.



Download the new SSL certificates
---------------------------------

The renewed SSL certificate is immediately available for download in the `Aiven Console <https://console.aiven.io/>`_, `API <https://api.aiven.io/doc/>`_, and :doc:`Aiven CLI </docs/tools/cli>` after the notification.

When accessing the `Aiven Console <https://console.aiven.io/>`_ service page for the Aiven for Apache Kafka service with expiring certificates, you'll be notified with the following message:

.. image:: /images/products/kafka/ssl-cert-renewal.png
   :alt: Apache Kafka service user SSL certificate expiring message

You can download the new certificate from the `Aiven Console <https://console.aiven.io/>`_ by: 

* Accessing the Aiven for Apache Kafka service for which you want to download the new certificate.
* Selecting **Users** from the left sidebar. 
* Selecting **Show access key** and **Show access cert** for the required user.

.. image:: /images/products/kafka/new-ssl-cert-download.png
   :alt: Apache Kafka service user SSL certificate and access key download

.. Note::

    You can download the renewed SSL certificate and key using the :ref:`dedicated Aiven CLI command <avn_service_user_creds_download>` ``avn service user-creds-download``

Acknowledge the usage of the new SSL certificate
------------------------------------------------

To stop receiving periodic notifications about certificate expiration, you need to acknowledge that the new certificate has been taken into use.

To acknowledge the new SSL certificate with the `Aiven Console <https://console.aiven.io/>`_:

* Select ``...`` next to the certificate.
* Select ``Acknowledge certificate``.

.. Note::

    You can acknowledge the renewed SSL certificate using the :ref:`dedicated Aiven CLI command <avn_service_user_creds_acknowledge>` ``avn service user-creds-acknowledge``

    The same can be achieved with the Aiven API, using the "Modify service user credentials" `endpoint <https://api.aiven.io/doc/#operation/ServiceUserCredentialsModify>`_:

    ::

        curl --request PUT \
            --url https://api.aiven.io/v1/project/<project>/service/<service>/user/<username> \
            --header 'Authorization: Bearer <bearer token>' \
            --header 'content-type: application/json' \
            --data '{"operation": "acknowledge-renewal"}'

