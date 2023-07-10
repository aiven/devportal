Getting started
===============

Aiven services are managed in the Aiven `web console <https://console.aiven.io/>`__ . When you first log into the console with your email address and password, you will see the **Services** view, which shows you all the services in the currently selected project.

.. Warning::

    Aiven for Apache Kafka® MirrorMaker 2 services can be created only alongside at least one existing Aiven for Apache Kafka running service.
    If your project doesn't contain any Aiven for Apache Kafka services, create one before attempting to create an Aiven for Apache Kafka MirrorMaker 2 service.

.. _apache_kafka_mirrormaker_dedicated_cluster:

Creating a dedicated Aiven for Apache Kafka® MirrorMaker 2 service
------------------------------------------------------------------

Create a new Aiven for Apache Kafka MirrorMaker 2 dedicated service:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_ and select the **Aiven for Apache Kafka®** service for which you want to create a dedicated Aiven for Apache Kafka® MirrorMaker 2 service.

2. Scroll down to the **Service Integration** section on the service Overview page and select **Manage integrations**.

3. In the **Integrations** screen, select **Apache Kafka MirrorMaker 2**. 

4. Select the **New service** option.

5. Provide a name for your service. By default, a random name is generated, but you can enter a more identifiable name to distinguish it from other services.

6. Select the cloud provider aand region where you want to deploy the service.

.. note:: 
    Pricing may vary across providers and regions.

7. Select a service plan. This defines how many servers and what kind of memory, CPU, and disk resources are allocated to your service.

8. Specify a **Cluster alias**. This alias is a name assigned to an Apache Kafka cluster within MirrorMaker. It helps identify and differentiate the source and target clusters used for replication. Ensure careful selection, as the cluster alias cannot be modified once the integration is created.

9.  Select **Create and enable** under the summary on the right side of the console. 

Accessing the integration link at the top of the screen will take you to the Service Overview page for the newly created Apache Kafka integration. Monitor the service status on the **Service overview** page, and wait until it transitions from REBUILDING to RUNNING to use its full functionality.


Next steps
----------

* Check our `examples project <https://github.com/aiven/aiven-examples>`_ to find code samples to get your application connected.

* Try our `sample data generator project <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_ to give you some data to get started with.
