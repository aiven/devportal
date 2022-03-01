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

1. Select the **Aiven for Apache Kafka®** service for which you want to create a dedicated Aiven for Apache Kafka® MirrorMaker 2 service.

2. Scroll down in the service Overview page till the **Service Integration** section and click on **Manage integrations**.

3. Select **Kafka MirrorMaker 2** and click **Use integration**.

4. Select the **New service** option.

5. Enter a name for your service. A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services.

6. Select the cloud provider and region that you want to run your service on.

.. note:: The pricing for the same service may vary between
    different providers and regions. The service summary on the
    right side of the console shows you the pricing for your
    selected options.

7. Select a service plan. This defines how many servers and what kind of memory, CPU, and disk resources are allocated to your service.

8. Click **Create Service** under the summary on the right side of the console. 


You can see the service status in the **Service overview** page , wait till it changes from *REBUILDING* to *RUNNING* to be able to use its full functionality.

Next steps
----------

* Check our `examples project <https://github.com/aiven/aiven-examples>`_ to find code samples to get your application connected.

* Try our `sample data generator project <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_ to give you some data to get started with.
