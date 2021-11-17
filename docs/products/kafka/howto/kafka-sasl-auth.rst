Use SASL Authentication with Apache Kafka
=========================================

Aiven offers a choice of `authentication methods for Apache Kafka <https://help.aiven.io/en/articles/4331547>`_, including `SASL <https://en.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer>`_ (Simple Authentication and Security Layer).

1. Scroll down the **Service overview** page to the **Advanced configuration** section.

2. Turn on the setting labelled ``kafka_authentication_methods.sasl``, and click **Save advanced configuration**.

.. image:: /images/products/kafka/enable-sasl.png
   :alt: Enable SASL authentication for Apache Kafka

The connection information at the top of the **Service overview** page will now offer the ability to connect via SASL or via client certificate.

.. image:: /images/products/kafka/sasl-connect.png
   :alt: Choose between SASL and certificate connection details

These connections are on a different port, but the host, CA and user credentials stay the same.
