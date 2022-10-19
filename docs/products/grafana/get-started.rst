Get started with Aiven for Grafana®
===================================

Get up and running with Aiven for Grafana®. This article shows you how to set up a Grafana service in Aiven, connect to it, view your default dashboards.


.. Add Step 1: Check the basics
 


Step 1: Create a new Aiven service
-----------------------------------

You can add services for Grafana in the Aiven web console.


.. image:: /images/products/grafana/get-started-grafana.gif
   :width: 500px
   :alt: Grafana in action


To create a new Aiven for Grafana service:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the *Services* page, click **Create a new service**.

   This opens a new page with the available service options.

3. Select the main properties for your service:

   a. Select the service type.

      If there are several versions available, select the version that you want to use. By default, the latest available version is selected.

   b. Select the cloud provider and region that you want to run your service on.

      .. Note::
          The pricing for the same service may vary between different providers and regions. The service summary on the right side of the console shows you the pricing for your selected options.
          
   c. Select a service plan.

      This defines the number of servers and what kind of memory, CPU, and disk resources are allocated to your service.

   d. Enter a name for your service.

      A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services.


4. Click **Create Service** under the summary on the right side of the console.

   This brings you back to the **Services** view. Your new service is listed with a status indicator to show that it is being created.

5. Click the service name.

   The *Overview* page for the service opens. This view shows you the connection parameters for your service, its current status, and the configuration options.

   The status is *REBUILDING* while the service is being created for you. Once the service is ready, the status changes to *RUNNING*. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions, and it may take longer in some circumstances.



Step 2: Log in to Grafana
--------------------------

You can log in easily to your Aiven for Grafana service from the console. See :doc:`how to log in <howto/log-in>`.

.. Add the following (Step 4: Display default dashboards in Aiven for Grafana)
