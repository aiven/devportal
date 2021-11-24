Getting started
===============

Aiven services are managed in the Aiven `web console <https://console.aiven.io/>`__ . When you first log in to the console with your email address and password, you will see the **Services** view, which shows you all the services in the currently selected project.

.. Warning::

    Aiven for Apache Kafka Connect services can be created only on top of existing Aiven for Apache Kafka running services. 
    If your project doesn't contain any Aiven for Apache Kafka services, create one before attempting to create an Aiven for Apache Kafka Connect service.

Create a new Aiven for Apache Kafka Connect dedicated service:

1. Select the **Aiven for Apache Kafka** service for which you want to create a dedicated Aiven for Apache Kafka Connect service. 

2. Click on the **Connectors** tab and select **Create New Kafka Connect Integration**.

3. Select the **New Service** option.

4. Enter a name for your service. A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services.

5. Select the cloud provider and region that you want to run your service on.

.. note:: The pricing for the same service may vary between
    different providers and regions. The service summary on the
    right side of the console shows you the pricing for your
    selected options.

6. Select a service plan. This defines how many servers and what kind of memory, CPU, and disk resources are allocated to your service.

7. Click **Create Service** under the summary on the right side of the console. This brings you back to the **Services** view. Your new service is listed with a status indicator to show that it is being created.


While your service is being built, you can visit the **Service overview** page and
see the status change from *REBUILDING* to *RUNNING*.

Next steps
----------

* Check our `examples project <https://github.com/aiven/aiven-examples>`_ to find code samples to get your application connected.

* Try our `sample data generator project <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_ to give you some data to get started with.
