Use SASL Authentication with Apache Kafka®
======================================================

Aiven offers a selection of :doc:`authentication methods for Apache Kafka® <../concepts/auth-types>`, including `SASL <https://en.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer>`_ (Simple Authentication and Security Layer).

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and choose your project. 
2. From the list of services, choose the Aiven for Apache Kafka service for which you wish to enable SASL.
3. On the **Service overview** page of the selected service, scroll down to the **Advanced configuration** section. 
4. Select **Change**.
5. Enable the setting labeled ``kafka_authentication_methods.sasl``, and then select **Save advanced configuration**.

.. image:: /images/products/kafka/enable-sasl.png
   :alt: Enable SASL authentication for Apache Kafka
   :width: 100%

The **Connection information** at the top of the **Service overview** page will now offer the ability to connect via SASL or via Client Certificate.

.. image:: /images/products/kafka/sasl-connect.png
   :alt: Choose between SASL and certificate connection details

.. note:: 
   Although these connections use a different port, the host, CA, and user credentials remain consistent.
