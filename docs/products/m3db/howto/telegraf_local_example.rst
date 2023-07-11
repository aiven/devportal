Telegraf to M3 to Grafana® Example
==================================

Aiven for M3 + Telegraf set up
------------------------------
At a high level, here is how to set up Telegraf to push metrics to Aiven for M3.

1. Log into `Aiven Console <https://console.aiven.io>`_ and :doc: `create an Aiven for M3 Service </docs/platform/howto/create_new_service>`.
2. Install and configure Telegraf Agent.
3. Setup Aiven for Grafana® instance for visualization of telegraph metrics.


Create Aiven for M3 service
---------------------------

If you don't have an existing Aiven account, you can sign up for a free 30-day trial with $300 credits using the `Aiven Console <https://console.aiven.io>`_ link. 

Within your existing Aiven project, create a new M3 service.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new Aiven for M3DB® service.
   
Open the newly created M3 service and select the **InfluxDB®** tab in the **Connection information** section. 
You will use several values from this page including the **Service URI, user, and password**. You will need these values when configuring Telegraf in the next section.

Install Telegraf
----------------
To simplify this example, we will install the Telegraf agent on a MacBook to collect the system metrics.
Of course, Telegraf can also be installed on `Windows and Linux <https://docs.influxdata.com/telegraf/v1.19/introduction/installation/>`_ machines.

Assuming you have Homebrew installed on a MacBook, simply run the following command at the Terminal
to install Telegraf (https://formulae.brew.sh/formula/telegraf)::

    brew update && brew install telegraf

Configure Telegraf and integrate it with M3
-------------------------------------------
Use the Telegraf agent to generate a default configuration file for editing::

    telegraf config > telegraf.conf

Modify the ``telegraf.conf`` configuration file to change the output endpoint to that of our M3 instance.

Change the URL under the ``outputs.influxdb`` section to that of your Aiven for M3 service (see above).
**NOTE:** The URL prefix should simply be ``https://`` and remove the ``username:password`` from the URI (see snippet below).

Specify the service username/password and set the database name to ``default``
(the database that is automatically created when your service is provisioned)::

		[[outputs.influxdb]]
		  urls = ["https://my-M3-service-my-project.aivencloud.com:24947/api/v1/influxdb"]
		  database = "default"
		  skip_database_creation = true
		  username = "avnadmin"
		  password = "my_service_password"

Finally, start Telegraf using the configuration file and begin sending system metrics to M3 by running the command below::

		telegraf -config telegraf.conf

Wait 10 seconds or so (the default collection interval) to see if there are any error messages displayed in the terminal::

		MacBook-Pro tmp % telegraf -config telegraf.conf
		2021-10-08T01:21:15Z I! Starting Telegraf 1.20.1
		2021-10-08T01:21:15Z I! Loaded inputs: cpu disk diskio kernel mem processes swap system
		2021-10-08T01:21:15Z I! Loaded aggregators:
		2021-10-08T01:21:15Z I! Loaded processors:
		2021-10-08T01:21:15Z I! Loaded outputs: influxdb
		2021-10-08T01:21:15Z I! Tags enabled: host=MacBook-Pro
		2021-10-08T01:21:15Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"MacBook-Pro", Flush Interval:10s

Create Aiven for Grafana service
--------------------------------

1. In the `Aiven Console <https://console.aiven.io>`_ , and access the M3DB service. 
2. In the **Service integrations** section, select **Manage integrations**.
3. On the **Integrations** page, select **Grafana Metrics Dashboard** to establish a connection between your M3 instance and a new Grafana dashboard service.
4. In the pop-up modal, select **New service** and select **Continue**.
5. Fill out the required details and follow similar steps to create the service. This will initiate the startup process for your Aiven for Grafana service, which will automatically connect to the M3 database to display metrics.
6. On the **Integrations** page on your M3DB service, you will find a link to the Grafana dashboard. Select the link to view the new Grafana service. 
7. Once service is running, select the Service URI and login with the user / password from the connection information.


Visualizing metrics
-------------------
Now to what we all have been waiting for, the **Metrics**!

In the Grafana dashboard, click the **Explore** tab.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_11.png
   :scale: 30%
   :alt: Grafana Explore

Select your M3 service as the data source from the drop down menu at the top of the page.
Click the metrics browser, select ``cpu_usage_user``, and then click the “Use Query” button.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_12.png
   :alt: Grafana Explore for M3

The chart displayed below represents the CPU of the MacBook.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_13.png
   :alt: Grafana Metrics for M3

Tear Down
At the terminal, press ``Ctrl+C`` to stop the Telegraf agent. Then, delete your M3 and Grafana services within the Aiven Console.
