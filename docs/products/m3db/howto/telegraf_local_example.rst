Telegraf to M3 to Grafana Example
================================

Aiven M3 + Telegraf Set up
--------------------------
At a high level, here’s how to set up Telegraf to push metrics to Aiven for M3.

1. Create Aiven M3 Service.
2. Install and configure Telegraf Agent
3. Setup Aiven Grafana instance for visualization of telegraph metrics
4. Enjoy the fruits of your labor!

Create Aiven M3 Service
-----------------------
If you don’t have an existing Aiven account, please follow this link to sign up for a free 30 day trial with
$300 of credits: https://console.aiven.io/signup

Within your existing Aiven project, create a new M3 service.

1. Under Create Service, select M3.
2. Select a cloud provider
3. Select a region

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_01.png
   :alt: Screenshot creating M3 service
4. Select a service plan type. Startup-8 will be fine for this demo.

.. tip::
	Aiven never charges for networking costs. What you see for the price is what you will pay at the end of the month!


5. Enter a name for the service.
6. Click the Create Service button.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_02.png
   :alt: Screenshot creating M3 service

Navigate to the newly created M3 service via the left-side menu and the service listing, and click the **InfluxDB** tab.
You will use several values from this page including the **Service URI, user, and password** when configuring Telegraf in the next section of this blog.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_03.png
   :alt: M3 Endpoint

Install Telegraf
----------------
To simplify this example, we will install the Telegraf agent on a Macbook to collect the system metrics.
Of course, Telegraf can also be installed on `Windows and Linux <https://docs.influxdata.com/telegraf/v1.19/introduction/installation/>`_ machines.

Assuming you have homebrew installed on a Macbook, simply run the following command at the Terminal
to install Telegraf (https://formulae.brew.sh/formula/telegraf)::

    brew update && brew install telegraf

Configure Telegraf and integrate it with M3
-------------------------------------------
Use the Telegraf agent to generate a default config file for editing::

    telegraf config > telegraf.conf

Modify the **telegraf.conf** config file to change the output endpoint to that of our M3 instance.

Change the URL under the ``outputs.influxdb`` section to that of your Aiven M3 service (see above).
**NOTE:** The URL prefix should simply be ``https://`` and remove the ``username:password`` from the URI (see snippet below).

Specify the service username/password and set the database name to ``default``
(the database that is automatically created when your service is provisioned)::

		[[outputs.influxdb]]
		  urls = ["https://my-M3-service-my-project.aivencloud.com:24947/api/v1/influxdb"]
		  database = "default"
		  skip_database_creation = true
		  username = "avnadmin"
		  password = "my_service_password"

Finally, start Telegraf using the config file and begin sending system metrics to M3 by running the command below::

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

Create Aiven Grafana Service
----------------------------
In the Aiven Console, navigate to the M3 service and click the ‘Manage integrations’.
Connect your M3 instance to a new Grafana dashboard service.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_04.png
	 :alt: M3 Manage Integrations

Click the “Use Integrations” button on the Dashboard modal.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_05.png
   :alt: M3 Dashboard

In the pop-up modal, select “New Service” and click the Continue button.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_06.png
   :alt: M3 New Integration

Follow similar steps to create the service by filling in the:

1. Name
2. Cloud
3. Region
4. Service Plan (Startup-1 is OK)
5. And then click the Create and enable button.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_07.png
   :scale: 50%
   :alt: M3 create new Grafana Integration

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_08.png
   :scale: 50%
   :alt: M3 create new Grafana Integration

A new Grafana service will now be starting up and automatically connect to the M3 database to display metrics.

Click on the name of the service to navigate to the new service.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_09.png
   :alt: M3 navigate to new Grafana Integration

Once the service is running, click on the Service URI and login with the user / password from the connection information.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_10.png
   :alt: Grafana Service Login

Visualizing Metrics
-------------------
Now to what we all have been waiting for, the **Metrics**!

In the Grafana dashboard, click the **Explore** tab.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_11.png
   :scale: 30%
   :alt: Grafana Explore

Select your M3 service as the data source from the drop down menu at the top of the page.
Click the metrics browser, select `cpu_usage_user`, and then click the “Use Query” button.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_12.png
   :alt: Grafana Explore for M3

The chart displayed below represents the cpu of the Macbook.

.. image:: /images/products/m3db/telegraf-m3-example/m3_telegraph_13.png
   :alt: Grafana Metrics for M3

Tear Down
At the terminal, press Ctrl+C to stop the Telegraf agent. Then, delete your M3 and Grafana services within the Aiven Console.
