Getting started with Aiven for InfluxDB®
#######################################

Aiven services are managed from Aiven `web console <https://console.aiven.io/>`_. First login to the console with your email address and password and you will be automatically taken to the "Services" view that shows all the services of the currently selected project.

**Projects** allow organizing groups of services under different topics and each project can for example have different billing settings. An empty project is created for you automatically when you sign-up and the free credits are attached to this project. You can create new projects by clicking the project name in the left side-bar and selecting "**Create a new project**". The same menu can also be used to switch between projects.

To get started with InfluxDB®, first select the "Create a new service" button.

.. image:: /images/products/influxdb/console.png
    :width: 500px
    :alt: InfluxDB service selection in the Aiven Console

The dialog that opens allows you to specify the main service properties:

* **Service name**: A short name for the service used to distinguish it from other services. A random name is provided, but you can type in a more friendly name.
* **Service type**: Select "InfluxDB".
* **Plan**: What kind of memory/CPU/disk resources will be allocated to run your service.
* **Cloud**: Which cloud and region to run the service on. Note that the pricing of the same service may differ between cloud providers and their regions.

After making the selections, select the "Create" button and you will be taken back to the service list view and the newly created service is shown with an indicator that it is being created.

Select the service name in the list and the "Overview" information page for the service opens. This view shows the connection parameters for your service, its current status and allows making changes to the service.

The "Status" indicator will say "Rebuilding" while the service is being created for you. Once the service is up and running, the light will change to green and it will say "Running". Note that while typically services start in a couple of minutes, the performance between clouds varies and it can take longer under some circumstances.

Backups
-------

InfluxDB® backups are taken every twelve hours and are encrypted and stored securely in object storage.

.. image:: /images/products/influxdb/console-influxdb.png
    :width: 500px
    :alt: Overview InfluxDB service in the Aiven Console

InfluxDB® command-line example
-----------------------------

There are multiple ways you can try out your new InfluxDB® service, you can copy-paste the connection parameters from the overview page to use in the following examples::

    influx -host influx-23ee4d7e.demoprj.aivencloud.com -port 20188 \
        -database 'defaultdb' -username 'avnadmin' \
        -password 'krx4mpjiz498m7zc' -ssl

Programming language examples
-----------------------------
* `Python <https://github.com/aiven/aiven-examples/blob/master/influxdb/python/main.py>`_
* `Go <https://github.com/aiven/aiven-examples/blob/master/influxdb/go/influxdb_example.go>`_
