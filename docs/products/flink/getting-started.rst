Getting started
===============

The first steps in using Aiven for Apache Flink are to create a service and a Flink job. You can do this in the Aiven web console or with the Aiven CLI.

In addition to the Flink service, you also need a service that you can use as a data source. This article outlines an example of using an Apache Kafka service as the data source.


Create an Apache Flink service in the Aiven web console
-------------------------------------------------------


1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the *Services* page, click **Create a new service**.

   This opens a new page with the available service options.


3. Select the main properties for your service:

   a. Select **Flink** as the service type.

   b. Select the cloud provider and region that you want to run your service on.

      .. note:: 
	      The pricing for the same service may vary between different providers and regions. The service summary on the right side of the console shows you the pricing for your selected options.

   c. Select a service plan.

      This defines the number of servers and what kind of memory, CPU, and disk resources are allocated to your service.

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

2. Run the following command to create your Apache Flink service::

       avn service create <service_name> -t flink --plan <service_plan> wait

   This creates the service and waits until the service status is *Running*.


Create a job
------------

This example uses an Aiven for Apache Kafka service with a topic named `alert` as the source for the Flink job.

1. Create the integration between Flink and Kafka. For details, see :doc:`this article <howto/connect>`.

2. Create the source and sink tables. For details, see :doc:`this article <howto/connect-kafka>`.

3. Create the job with the REST API. For details, see :doc:`this article <howto/create-job>`.
