Connect to Apache Kafka with Conduktor
======================================

`Conduktor <https://www.conduktor.io/>`_ is a friendly user interface for Apache Kafka, and it works well with Aiven. In fact, there is built-in support for setting up the connection. You will need to add the CA certificate for each of your Aiven projects to Conduktor before you can connect, this is outlined in the steps below.

1. Visit the **Service overview** page for your Aiven for Apache Kafka service (the :doc:`../getting-started` page is a good place for more information about creating a new service if you don't have one already).

2. Download the **Access Key**, **Access Certificate** and **CA Certificate** (if you didn't have that already) into a directory on your computer.

3. Choose **New Kafka Cluster** on the main pane, and click the **Aiven** icon. This pops up a helper screen so that you can add all the information needed for Aiven in a friendly format. The fields you need to add:

   * Host and port, you can copy these from the **Service overview** page

   * The three files downloaded: access key, access certificate and CA certificate

.. image:: /images/products/kafka/conduktor-config.png
    :alt: Screenshot of the cluster configuration screen

Conduktor will create the keystore and truststore files in the folder that you specified, or you can choose an alternative location. Click the **Create** button and the helper will create the configuration for Conduktor to connect to your Aiven for Apache Kafka service.

4. Click the **Test Kafka Connectivity** button to check that everything is working as expected.

.. Tip::

   If you experience a Java SSL error when testing the connectivity, add the service CA certificate to the list of Conduktor's trusted certificates.

   * Download the **CA Certificate** file to your computer.

   * In the Conduktor application, click the settings dropdown in the bottom right hand side and choose **Network**.

   * On the **Trusted Certificates** tab, select **Import** and then supply the CA certificate file you downloaded. Save the settings.

Once connected, you can visit the `Conduktor documentation <https://docs.conduktor.io/>`_ to learn more about using this tool.
