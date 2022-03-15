Renew service users SSL certificates
====================================

In every Aiven for Apache Kafka® service, when the existing service user SSL certificate is close to expiration (approximately 3 months before the expiration date), a new certificate is automatically generated and the project admins, operators, and tech email addresses are notified.

The old certificate continues working until the expiration date and could be used in parallel with the new one to ensure a smooth transition.


Download the new SSL certificates
---------------------------------

The renewed SSL certificate is immediately available for download in the `Aiven Console <https://console.aiven.io/>`_, `API <https://api.aiven.io/doc/>`_, and :doc:`Aiven CLI </docs/tools/cli>` after the notification. Moreover, when accessing the `Aiven Console <https://console.aiven.io/>`_ service page for the Aiven for Apache Kafka service with expiring certificates, you'll be notified with the following message:

.. image:: /images/products/kafka/ssl-cert-renewal.png
   :alt: Apache Kafka service user SSL certificate expiring message

You can download the new certificate from the `Aiven Console <https://console.aiven.io/>`_ by: 

* Accessing the service details of the Aiven for Apache Kafka service for which you want to download the new certificate
* Clicking on the **Users** tab
* Clicking on **Show access key** and **Show access cert** for the required user

.. image:: /images/products/kafka/new-ssl-cert-download.png
   :alt: Apache Kafka service user SSL certificate and access key download

.. Note::

    You can download the renewed SSL certificate and key using the :ref:`dedicated Aiven CLI command <avn_service_user_creds_download>` ``avn service user-creds-download``

Acknowledge the usage of the new SSL certificate
------------------------------------------------

To stop the periodic notifications about certificate expiration, you need to acknowledge that the new certificate has been taken into use.

To acknowledge with the `Aiven Console <https://console.aiven.io/>`_:

* Click on ``...`` next to the certificate
* Click on ``Acknowledge certificate``

.. Note::

    You can acknowledge the renewed SSL certificate using the :ref:`dedicated Aiven CLI command <avn_service_user_creds_acknowledge>` ``avn service user-creds-acknowledge``

    The same can be achieved with the Aiven API, using the "Modify service user credentials" `endpoint <https://api.aiven.io/doc/#operation/ServiceUserCredentialsModify>`_:

    ::

        curl --request PUT \
            --url https://api.aiven.io/v1/project/<project>/service/<service>/user/<username> \
            --header 'Authorization: Bearer <bearer token>' \
            --header 'content-type: application/json' \
            --data '{"operation": "acknowledge-renewal"}'

