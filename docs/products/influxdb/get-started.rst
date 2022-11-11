Getting started with Aiven for InfluxDB®
========================================

You can easily create and manage your Aiven for InfluxDB® service from the `Aiven Console<https://console.aiven.io/>`_. 
Log in to the console with your email address and password, and you will see the Services page that shows all the services available for the selected project.


Create a new Aiven for InfluxDB® service
----------------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, click **Create service**. This opens a new page with the available service options.
3. Select **InfluxDB®** from the list of services. 
4. Select the cloud provider of your choice and select the cloud region on which you want to run your service. 
   .. note:: The pricing for the same service may vary between providers and regions. The service summary on the right side of the console shows you the pricing for your selected options.
5. Next, select the service plan. 
6. Enter a name for your service.
   .. note:: A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services. You cannot change the name of the service once it is created.  
7. The **Service Summary** on the right side provides an estimated monthly price.  
8. Click **Create service**.
   The **Overview** page for the service opens. TThis view shows your service's connection parameters, its current status, and the configuration options.
   The status is **Rebuilding** while the service is being created for you. Once the service is ready, the status changes to **Running**. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions, and it may take longer in some circumstances.

