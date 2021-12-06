Authentication types
======================

It is strongly recommended to use modern encryption protocols to protect data in transit sent to and from Apache Kafka.
You can use one of the available options in **Aiven for Apache Kafka** services:

Transport Layer Security
------------------------

**Transport Layer Security (TLS)**, also known as Secure Sockets
Layer (SSL), is an established standard for securing internet traffic. This method
relies on a certificate that is provided by a Certificate
Authority (for example, `letsencrypt.org <http://letsencrypt.org>`_ ) for your domain.
With this certificate and the right technical setup, you can use
your domain to encrypt the traffic to your service.

By default Aiven enables TLS encryption for all  **Aiven for Apache Kafka** services and on your behalf
handles the application, renewal, and configuration of certificates.

There are two ways you can use TLS:

#. **TLS encryption** : your Apache Kafka client validates the certificate for
   your Apache Kafka broker.

#. **TLS authentication** : your Apache Kafka client validates the certificate
   for your Apache Kafka broker and your broker validates the certificate
   for your client.


Simple Authentication and Security Layer
----------------------------------------

**Simple Authentication and Security Layer (SASL)** acts as a layer that
allows alternative login methods for your service. For example, if you
use Active Directory for authentication, SASL supports a Kerberos login
method to provide access.

You can use SASL/PLAIN and SASL/SCRAM with **Aiven for Apache Kafka**.

SASL/PLAIN
~~~~~~~~~~

**PLAIN** relies on a combination of username
and password to log in over a TLS connection, meaning that your traffic
is encrypted. You should not use SASL/PLAIN without TLS, because in this case
anyone will be able to read your credentials when you send them.

SASL/SCRAM
~~~~~~~~~~

**SCRAM** stands for Salted Challenge Response Authentication Mechanism. It
is a mechanism that allows a client to identify itself to a server
without sending a plain-text password. A key benefit of this is that it
does not reveal the password to servers that do not already have it, for
example if a client connects to the wrong server even if that server has
a valid TLS certificate.

A brief explanation of this is that it creates a random "salt", which is
then used to create an "identity" that holds:

-  The "salt"

-  The number of iterations to use (4096 by default)

-  ``StoredKey`` (the hash of the client's key)

-  ``ServerKey``

This identity is then by default stored in Zookeeper.

Enabling different authentication methods in Aiven
--------------------------------------------------

**TLS** is enabled by default for your **Aiven for Apache Kafka** service, if you want to additionally add **SASL** follow these steps:

#. Log in to the Aiven web console and select your **Aiven for Apache Kafka** service.

#. On the *Overview* page, scroll down to *Advanced configuration* .

#. Switch on **kafka.authentication_methods.sasl** to enable SASL authentication.
