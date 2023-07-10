Getting started
===============

To create an Aiven for Apache Kafka® Connect service, make sure you have existing Aiven for Apache Kafka® running services in your project. If your project doesn't have any Aiven for Apache Kafka services, you must :doc:`create one <../platform/howto/create_new_service>` before attempting to create an Aiven for Apache Kafka Connect service.

To create an Aiven for Apache Kafka® service, log in to the Aiven Console using your email address and password. Follow the steps in the :doc:Getting Started with Aiven for Apache Kafka section </docs/products/kafka/getting-started>.


.. _apache_kafka_connect_dedicated_cluster:

Create a dedicated Aiven for Apache Kafka® Connect service
-------------------------------------------------------------

To create a new Aiven for Apache Kafka Connect dedicated service:

1. Log into `Aiven Console <https://console.aiven.io>`_ and select the **Aiven for Apache Kafka** service for which you want to create a dedicated Aiven for Apache Kafka Connect service. 

2. Select **Connectors** from left sidebase and select **Integrate standalone service**.

3. Enter a name for your service. A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services.

5. Select the cloud provider and region on which you want to run your service.

.. note:: The pricing for the same service may vary between
    different providers and regions. The service summary on the
    right side of the console shows you the pricing for your
    selected options.

6. Select a service plan. This defines how many servers and what kind of memory, CPU, and disk resources are allocated to your service.

7. Select **Create and enable** under the summary in the console. 

At the top of the screen, you will notice the Apache Kafka Connect integration. Selecting the service name will take you to the **Service Overview** page to monitor the service status. Before using it, it's important to wait until the service status changes from *REBUILDING* to *RUNNING* on this page.

Next steps
----------

* Check our `examples project <https://github.com/aiven/aiven-examples>`_ to find code samples to get your application connected.

* Try our `sample data generator project <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_ to give you some data to get started with.
