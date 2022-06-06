Use Kpow with Aiven for Apache Kafka®
===============================================

`Kpow by Operatr.IO <https://kpow.io/start>`_ is a popular Web UI for Apache Kafka® that allows you to monitor a cluster, view topics and consumer groups, produce and consume data with integration into the Schema Registry.

Prerequisites
-------------

To connect Kpow to Aiven for Apache Kafka® you need to create a :doc:`Java keystore and truststore containing the service SSL certificates <keystore-truststore>`. 

Kpow uses a `set of Apache Kafka topics <https://docs.kpow.io/installation/minimum-acl-permissions>`_ to store the working information. You can either     :doc:`create the topics manually <create-topic>` or enable the :doc:`automatic creation of topics <create-topics-automatically>` for the Aiven for Apache Kafka service.

Furthermore, you need to collect the following information:

* ``APACHE_KAFKA_HOST``: The Aiven for Apache Kafka hostname
* ``APACHE_KAFKA_PORT``: The Aiven for Apache Kafka port
* ``KEYSTORE_FILE_NAME``: The name of the Java keystore containing the Aiven for Apache Kafka SSL certificates
* ``SSL_KEYSTORE_PASSWORD``: The password used to secure the Kava keystore
* ``SSL_KEY_PASSWORD``: The password used to secure the Kava key
* ``SSL_TRUSTSTORE_LOCATION``: The password used to secure the Kava truststore
* ``SSL_TRUSTSTORE_PASSWORD``: The password used to secure the Kava truststore
* ``SSL_STORE_FOLDER``: The absolute path of the folder containing both the truststore and keystore
* ``KPOW_LICENSE_ID``: Kpow license ID
* ``KPOW_LICENSE_CODE``: Kpow license code
* ``KPOW_LICENSEE``: Kpow licensee
* ``KPOW_LICENSE_EXPIRY_DATE``: Kpow license expiry date
* ``KPOW_LICENSE_SIGNATURE``: Kpow license signature

.. Tip::

    If you create a Kpow trial, you should receive all the ``KPOW`` related parameters in the welcome email

Retrieve Aiven for Apache Kafka® SSL certificate files
------------------------------------------------------

Aiven for Apache Kafka® by default enables TLS security.
The certificates can be manually downloaded from the service overview page in the Aiven console, or via the :ref:`dedicated Aiven CLI command <avn_service_user_creds_download>`.


Setup a Kpow configuration file
----------------------------------

Kpow supports both :doc:`SASL and SSL authentication methods<../concepts/auth-types>`. The following example shows the SSL version which requires a keystore and truststore that can be created following the :doc:`dedicated documentation <keystore-truststore>`.

Once the keystore and truststore are created, you can define a Kpow configuration file named ``kpow.env`` with the following content, replacing the ``APACHE_KAFKA_HOST``, ``APACHE_KAFKA_PORT``,  ``KPOW_LICENSE_ID``, ``KPOW_LICENSE_CODE``, ``KPOW_LICENSEE``, ``KPOW_LICENSE_EXPIRY_DATE``, ``KPOW_LICENSE_SIGNATURE``, ``KEYSTORE_FILE_NAME``, ``KEYSTORE_PASSWORD``, ``KEY_PASSWORD``, ``TRUSTSTORE_FILE_NAME`` and ``TRUSTSTORE_PASSWORD``  with the the respective values taken from the prerequisites section:

::

    BOOTSTRAP=APACHE_KAFKA_HOST:APACHE_KAFKA_PORT
    LICENSE_ID=KPOW_LICENSE_ID
    LICENSE_CODE=KPOW_LICENSE_CODE
    LICENSEE=KPOW_LICENSEE
    LICENSE_EXPIRY=KPOW_LICENSE_EXPIRY_DATE
    LICENSE_SIGNATURE=KPOW_LICENSE_SIGNATURE
    SECURITY_PROTOCOL=SSL
    SSL_KEYSTORE_LOCATION=/ssl/KEYSTORE_FILE_NAME
    SSL_KEYSTORE_PASSWORD=KEYSTORE_PASSWORD
    SSL_KEY_PASSWORD=KEY_PASSWORD
    SSL_TRUSTSTORE_LOCATION=/ssl/TRUSTSTORE_FILE_NAME
    SSL_TRUSTSTORE_PASSWORD=TRUSTSTORE_PASSWORD

.. Warning::

    Don't remove the ``/ssl/`` prefix before the keystore and truststore setting, the ``SSL_STORE_FOLDER`` local folder containing the keystore and truststore will be mapped to the ``/ssl/`` folder during the docker instance creation.

The full list of configuration parameters is available at the `dedicated Kpow page <https://docs.kpow.io/config/environment-variables>`_.

Run Kpow on Docker
---------------------

You can run Kpow in a Docker/Podman container with the following command, by replacing the ``SSL_STORE_FOLDER`` with the name of the folder containing the Java keystore and truststore:

::

    docker run -p 3000:3000 -m2G \
        -v SSL_STORE_FOLDER:/ssl \
        --env-file ./kpow.env operatr/kpow:latest

Use Kpow
-----------

Once Kpow starts, you should be able to access it at ``localhost:3000``

.. image:: /images/products/kafka/kpow.jpg
   :alt: Kpow in action

You can perform the following tasks with Kpow over an Aiven for Apache Kafka® service:

* View and search topics
* Create and delete topics
* View brokers
* Produce and consume messages
