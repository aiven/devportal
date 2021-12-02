Getting started
===============

The first step in using Aiven for Apache Flink is to create a service. You can do this in the `Aiven web console <https://console.aiven.io/>`_ or with the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

In addition to the Flink service, you also need one or more services to use as the data source and targets. To create an Aiven for Apache Kafka or Aiven for PostgreSQL service for this purpose, :doc:`follow these instructions </docs/platform/howto/create_new_service>`. Once you have created the necessary services, you can then create a Flink job to process the data stream.

The following video covers an example use case to give you a demonstration of Aiven for Apache Flink:

.. raw:: html

    <iframe width="712" height="400" src="https://youtube.com/embed/j1qNGLKdTJg" frameborder="0" allowfullscreen></iframe>


Create an Apache Flink service in the Aiven web console
-------------------------------------------------------


1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the *Services* page, click **Create a new service**.

3. Select the main properties for your service:

   a. Select **Flink** as the service type.

   b. Select the cloud provider and region that you want to run your service on.

      .. note:: 
	      The pricing for the same service may vary between different providers and regions. The service summary on the right side of the console shows you the pricing for your selected options.

   c. Select a service plan.

      This defines the size of the cluster and the memory, CPU, and disk resources allocated to each node.

   d. Enter a name for your service.

      A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services.


4. Click **Create Service** under the summary on the right side of the console.

   This brings you back to the **Services** view. Your new service is listed with a status indicator to show that it is being created.

5. Click the service name.

   The *Overview* page for the service opens.

   This view shows you the connection parameters for your service, its current status, and the configuration options.

   The status is *Rebuilding* while the service is being created for you. Once the service is ready, the status changes to *Running*. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions, and it may take longer in some circumstances.


Next steps
----------

* For details on using the Aiven CLI to create and manage Aiven for Apache Flink services, see the :doc:`Aiven CLI documentation </docs/tools/cli>` and the :doc:`Flink-specific command reference </docs/tools/cli/service/flink>`
* :doc:`Create integrations <howto/create-integration>` with Aiven for Apache Kafka and Aiven for PostgreSQL services
* Create source and sink data tables to map the data for :doc:`Apache Kafka <howto/connect-kafka>` or :doc:`PostgreSQL <howto/connect-pg>` services
* :doc:`Create Apache Flink jobs <howto/create-job>` to implement your data pipelines
