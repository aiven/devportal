Connect Aiven for Apache Kafka® with Klaw
=========================================

`Klaw <https://www.klaw-project.io/>`_ is an open-source, web-based data governance toolkit for managing Apache Kafka® Topics, ACLs, Schemas,  and Connectors. Klaw provides a self-service user interface where teams of Apache Kafka service users can request changes to the Apache Kafka configuration without the intervention of administrators. 

This article provides you with the steps to connect Aiven for Apache Kafka® service with Klaw. 

Prerequisites
-------------
To connect Aiven for Apache Kafka® and Klaw, you need to have the following setup: 

* A running Aiven for Apache Kafka® service. See :doc:`Getting started with Aiven for Apache Kafka </docs/products/kafka/getting-started>` for more information. 
* A running Klaw cluster. See `Run Klaw from the source <https://www.klaw-project.io/docs/run-source>`_ for more information.
* Configured :doc:`Java keystore and truststore containing the service SSL certificates </docs/products/kafka/howto/keystore-truststore>`. 

Connect Aiven for Apache Kafka® to Klaw
---------------------------------------

Follow the below steps to configure and connect Aiven for Apache Kafka® with Klaw: 

1. Log in to the **Klaw web interface**. 
2. Click **Environments**, and then click **Clusters**. 
3. On the **Clusters** page, click **Add Cluster** to add an Aiven for Apache Kafka® cluster. 
4. Enter the following details:
   
   -  **Cluster Type:** Select Kafka from the drop-down list
   -  **Cluster Name:** Provide a name for the cluster
   -  **Protocol:** Select the protocol for your cluster
   
   .. note:: 
      Based on the protocol selected, you need to :ref:`configure Klaw application.properties file<klaw-application-properties-configs>` to enable connection between Aiven for Apache Kafka® and Klaw clusters. 

   -  **Kafka Flavor:** Select Aiven for Apache Kafka® as the flavor
   -  **Project Name:** Select the project name defined in the Aiven Console
   -  **Bootstrap server:** Enter the Service URI for your Apache Kafka service. You can find the service URI in the **Connection information** page of your service in Aiven Console 
   -  **Service Name:** Enter the name of the service as defined in the `Aiven Console <https://console.aiven.io/>`_ for your Apache Kafka service
5. Click **Save**.
6. Next, add the cluster to the preferred environment. Select **Environments**, and then select **Environments** from the drop-down menu. 
7. Click **Add Environment** and enter the details to add Kafka environment: 
   
   -  **Environment Name:** Select environment from the drop-down list
   
      .. note::  
         To learn more, see `Clusters and environments <https://www.klaw-project.io/docs/clusters-environments>`__ in Klaw documentation.  

   -  **Select Cluster:** Select the cluster you added from the drop-down list. The bootstrap servers and protocol details are automatically populated 
   -  **Default Partitions:** Enter the number of partitions based on your requirements. The default value is set to 2
   -  **Maximum Partitions:** Enter the maximum number of partitions. The default value is set to 2
   -  **Default Replication factor:** Enter the required replication factor. The default value is set to 1
   -  **Max Replication factor:** Enter the required max replication factor. The default value is set to 1
   -  **Topic prefix (optional):** Enter a topic prefix
   -  **Tenant:** The value is set to default Tenant
   
      .. note:: Klaw is multi-tenant by default. Each tenant manages topics with their own teams in isolation. Every tenant has its own set of Apache Kafka® environments, and users of one tenant cannot view/access topics, or ACLS from other tenants. It provides isolation avoiding any security breach. For this topic, I have used the default tenant configuration. For more information, see `Klaw documentation <https://www.klaw-project.io/docs/get-started-kafka#configure-the-cluster-to-sync>`__. 

8. Click **Save**. 

If the connection based on the cluster and environment configurations are **successful**, the connection status displays a **blue thumbs-up icon** on the Environments page in the Klaw web interface.  If it is **unsuccessful**, a **red thumbs-down icon** is displayed. 

For unsuccessful connections, check the authentication protocol configurations. See the :ref:`Configure Klaw application.properties file<klaw-application-properties-configs>` section for further details. After completing these configurations, check the connection status on the Environments page by clicking the thumbs-down icon to see if the setup was successful.

.. _klaw-application-properties-configs:

Configure Klaw application.properties file
-----------------------------------------------
`Klaw <https://www.klaw-project.io/>`_ uses the ``application.properties`` file to configure any application-related properties, such as secret key and authentication protocol configurations. Connecting Aiven for Apache Kafka® with Klaw requires you to perform the following additional configurations in the ``application.properties`` file.

Secret key configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Set the value of ``klaw.clusterapi.access.base64.secret`` with a secret key in the form of a Base64 encoded string in the ``application.properties`` file located in the following paths: 

* ``klaw/cluter-api/src/main/resources``
* ``klaw/core/src/main/resources``

Configure authentication protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can connect Aiven for Apache Kafka® using either of the following authentication protocols: 

* ``PLAINTEXT``
* ``SSL``, ``SASL PLAIN``, ``SASL SSL`` 
* ``SASL SSL (GSSAPI / Kerberos)``, ``SASL_SSL (SCRAM SHA 256/512)``

.. Note:: If you are using ``PLAINTEXT``, you do not need to perform any additional configuration. 


Connect using SSL protocol
""""""""""""""""""""""""""""""""
To use SSL as the authentication protocol to connect the Apache Kafka® cluster to Klaw, you need to perform the following steps: 

Retrieve SSL certificate files
''''''''''''''''''''''''''''''
You need to retrieve the Aiven for Apache Kafka SSL certificate files. Aiven for Apache Kafka® by default enables TLS security. Download the certificates from the service overview page in the Aiven console or via the :ref:`dedicated page <avn_service_user_kafka_java_creds>`.

Considering you have already configured the :doc:`Java SSL keystore and truststore files </docs/products/kafka/howto/keystore-truststore>`, move the keystore named ``client.keystore.p12`` and truststore named ``client.truststore.jks`` into a directory that can be easily accessed and configured with Klaw. 

Configure SSL properties 
'''''''''''''''''''''''''
After retrieving the SSL certificate files and configuring the SSL keystore and truststore files, you need to configure these SSL values in the ``application.properties`` file.

1. Get the **Cluster ID** by clicking the copy icon on the **Clusters** page in the **Klaw web interface**.  
2. Next, open the ``application.properties`` file located in the ``klaw/cluster-api/src/main/resources`` directory. 
3. Configure the SSL properties to connect to Apache Kafka® clusters by editing the following lines:

   ::

      klawssl.kafkassl.keystore.location=client.keystore.p12
      klawssl.kafkassl.keystore.pwd=klaw1234
      klawssl.kafkassl.key.pwd=klaw1234
      klawssl.kafkassl.truststore.location=client.truststore.jks
      klawssl.kafkassl.truststore.pwd=klaw1234
      klawssl.kafkassl.keystore.type=pkcs12
      klawssl.kafkassl.truststore.type=JKS

   * For the lines starting with ``klawssl``, replace ``klawssl`` with the Klaw Cluster ID.
   * Replace ``client.keystore.p12`` with the path for the keystore and ``klaw1234`` with the password configured for the keystore file. 
   * Replace ``client.truststore.jks`` with the path for the truststore and ``klaw1234`` with the password configured for the truststore file. 
   * Save the ``application.properties`` file.

   The following is an example of an ``application.properties`` file configured with Klaw Cluster ID, keystore, and truststore paths and passwords. 

   ::

      demo_cluster.kafkassl.keystore.location=/Users/demo.user/Documents/Klaw/demo-certs/client.keystore.p12
      demo_cluster.kafkassl.keystore.pwd=Aiventest123!
      demo_cluster.kafkassl.key.pwd=Aiventest123!
      demo_cluster.kafkassl.truststore.location=/Users/demo.user/Documents/Klaw/demo-certs/client.truststore.jks
      demo_cluster.kafkassl.truststore.pwd=Aiventest123!
      demo_cluster.kafkassl.keystore.type=pkcs12
      demo_cluster.kafkassl.truststore.type=JKS

   .. note:: To add multiple SSL configurations, copy and paste the above lines by prefixing them with the required cluster identification and relevant certificates.

Connect using SASL protocols
""""""""""""""""""""""""""""""""""
To use protocols, such as ``SASL_PLAIN``, ``SASL_SSL/PLAIN``, and ``SASL_SSL/GSSAPI``, in the ``application.properties`` file, look for the lines starting with ``acc1.kafkasasl.jaasconfig.<>``, uncomment the line and enter the required values. Save the ``application.properties`` file. 

.. seealso:: 
   * For more information about Klaw, see `Klaw documentation <https://www.klaw-project.io/docs>`__. 
   * Additionally, checkout the `Klaw GitHub project repository <https://github.com/aiven/klaw>`_. 
