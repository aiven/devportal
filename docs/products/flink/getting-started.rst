Getting started
===============

The first step in using Aiven for Apache Flink is to create a service. You can do this in the `Aiven web console <https://console.aiven.io/>`_ or with the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

In addition to the Flink service, you also need one or more services to use as the data source and targets. To create an Aiven for Apache Kafka or Aiven for PostgreSQL service for this purpose, :doc:`follow these instructions </docs/platform/howto/create_new_service>`. Once you have created the necessary services, you can then create a Flink job to process the data stream.


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


Create an Apache Flink service with the Aiven CLI
-------------------------------------------------

1. Install and set up the Aiven CLI utility.

   See :doc:`this article </docs/tools/cli>` for instructions and more information.

2. Run the following command to create your Aiven for Apache Flink service::

       avn service create <service_name> -t flink --cloud <cloud_provider_and_region> --plan <service_plan> wait

   This creates the service and waits until the service status is *Running*.


Create a job
------------

This example uses an Aiven for Apache Kafka service as both the data source and the pipeline target. The service uses a topic named `alert` as the source, and the transformed data is inserted into another topic named `KAlert` via a Flink job.

1. Once you have created the Flink and Kafka services, create the integration between them. For details, see :doc:`this article <howto/create-integration>`.

2. Create the source and sink tables. For details, see :doc:`this article <howto/connect>`.

3. Create the job with the REST API. For details, see :doc:`this article <howto/create-job>`.
