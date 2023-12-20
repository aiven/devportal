Streaming anomaly detection with Apache Flink®, Apache Kafka® and PostgreSQL®
==============================================================================================

What you will learn
---------------------------

Follow this tutorial and you'll learn how to build a streaming anomaly detection system. In particular, we'll cover the following:

* How to create a fake streaming dataset.
* How to create and use Apache Kafka for data streaming.
* How to create and use PostgreSQL® to store threshold data.
* How to create and use Apache Flink® to define streaming data pipelines.
* How to push the outcome of the anomaly detection system as a Slack notification.


What are you going to build
---------------------------

Anomaly detection is a way to find unusual or unexpected things in data. It is immensely helpful in a variety of fields, such as fraud detection, network security, quality control and others. By following this tutorial you will build your own streaming anomaly detection system.

For example: a payment processor might set up anomaly detection against an e-commerce store if it notices that the store - which sells its items in Indian Rupees and is only configured to sell to the Indian market - is suddenly receiving a high volume of orders from Spain. This behavior could indicate fraud. Another example is that of a domain hosting service implementing a CAPTCHA against an IP address it deems is interacting with one of its domains in rapid succession.

While it's often easier to validate anomalies in data once they due to be stored in the database, it's more useful to check in-stream and address unwanted activity before it affects our dataset.

We can check for anomalies in data by creating filtering pipelines using Apache Fiink®. Apache Flink is a flexible, open source tool for in-stream and batch processing of data. It lets us run SQL-like queries against a stream of data and perform actions based on the results of those queries.

In this tutorial you'll use a fake Internet of Things (IoT) sensor that generates data on a CPU usage for various devices as our continuous flow of data. Once the data is flowing, you'll then create a basic filtering pipeline to separate the usage values surpassing a fixed threshold (80%).

This example mimics a scenario where you might want to separate and generate alerts for anomalies in single events. For instance, a sensor having a CPU utilization of 99% might create a heating problem and therefore you might want to notify the team in charge of the inventory to schedule the replacement.

.. mermaid::

    graph LR;

        id1(IoT device)-- sensor reading -->id2(usage > 80%?);
        id2-- yes -->id3(notification);

However, receiving a notification on every sensor reading that surpasses a fixed threshold can be overwhelming and create false positives for short usage spikes. Therefore you'll create a second, more advanced, pipeline to average the sensor readings values over 30 seconds windows and then compare the results with various thresholds, defined for every IoT device, and stored in a reference table.

Reading the average CPU value in 30 second windows will improve your initial implementation and help avoid false positive notifications for single spikes, but still let you flag components that are at potential risk of overheating. The threshold lookup enables a more precise definition of alert ranges depending on the device type.

.. mermaid::

    graph LR;

        id1(IoT device)-- sensor reading -->id2(average 30 seconds);
        id2-- average reading -->id4(over threshold?);
        id4-- yes --> id5(notification);
        id3(threshold table)-- thresholds --> id4;



The tutorial includes:

* Apache Flink for data transformation.
* Apache Kafka for data streaming.
* PostgreSQL® for data storage/query.
* Slack as notification system.

In this tutorial we'll be using Aiven services, specifically `Aiven for Apache Flink® <https://aiven.io/flink>`_, `Aiven for Apache Kafka® <https://aiven.io/kafka>`_, and `Aiven for PostgreSQL® <https://aiven.io/postgresql>`_. All of these are open source tools widely available. We encourage you to `sign up for a free trial <https://console.aiven.io>`_ to follow along as it will reduce any issues you might have with networking and getting services to communicate with each other to nearly zero.

Architecture overview
---------------------

To build near real-time anomaly detection system, you'll build a streaming data pipeline that will be able to process the IoT sensor readings as soon as they are generated. The pipeline relies on two sources: the first source is an Apache Kafka topic that contains the fake stream of IoT metrics data and the second is a table in PostgreSQL® database containing alerting thresholds, defined for each IoT device. Then an Apache Flink® service combines the data, applies some transformation SQL to find the anomalies, and pushes the result to a separate Apache Kafka® topic or a Slack channel for team notification.


.. mermaid::

    graph TD;

        id1(Apache Kafka)-- IoT metrics stream -->id3(Apache Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-- filtered/aggregated data -->id1;
        id3-- filtered data -->id7(Slack);

Prerequisites
-------------

The tutorial uses Aiven services, therefore you'll need a valid `Aiven account <https://console.aiven.io/signup>`_. On top of the Aiven account, you will also need the following three items:

* **Docker**, needed for the `fake data generator for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_. Check out the `related installation instructions <https://docs.docker.com/engine/install/>`_.
* **Slack App and Token**: the data pipeline output is a notifications to a Slack channel, check out the needed steps to `set up a Slack app and retrieve the Slack authentication token <https://github.com/aiven/slack-connector-for-apache-flink>`_.
* `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ a terminal based tool to interact with PostgreSQL where the threshold data will be stored.

Create the Aiven services
----------------------------

In this section you'll create all the services needed to define the anomaly detection system via the `Aiven Console <https://console.aiven.io/>`_:

* An :doc:`Aiven for Apache Kafka®</docs/products/kafka>` named ``demo-kafka`` for data streaming, this is where the stream of IoT sensor readings will land.
* An :doc:`Aiven for Apache Flink®</docs/products/flink>` named ``demo-flink`` for streaming data transformation, to define the anomaly detection queries.
* An :doc:`Aiven for PostgreSQL®</docs/products/postgresql>` named ``demo-postgresql`` for alerting thresholds storage and query.


Create an Aiven for Apache Kafka® service
'''''''''''''''''''''''''''''''''''''''''''''

The :doc:`Aiven for Apache Kafka </docs/products/kafka>` service is responsible for receiving the inbound stream of IoT sensor readings. Create the service with the following steps:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create service**.

   This opens a new page with the available service options.

   .. image:: /images/platform/concepts/console_create_service.png
      :alt: Aiven Console view for creating a new service

3. Select **Apache Kafka®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `business-4` as service plan. The `business-4` plan allows you to define the service integrations needed to define Apache Flink streaming transformations over the Apache Kafka topic.

5. Enter ``demo-kafka`` as name for your service.

6. Click **Create service** under the summary on the right side of the console

Customise the Aiven for Apache Kafka service
''''''''''''''''''''''''''''''''''''''''''''

Now that your service is created, you need to customise its functionality. In the **Overview** tab of your freshly created service, you'll see a bunch of toggles and properties. Change these two:

1. Enable the Apache Kafka REST APIs to manage and query via the Aiven Console.

   Navigate to **Kafka REST API (Karapace)** > **Enable**.


2. Enable the :doc:`automatic creation of Apache Kafka topics </docs/products/kafka/howto/create-topics-automatically>` to create new Apache Kafka® topics on the fly while pushing a first record.

   Navigate to **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**.


Create an Aiven for PostgreSQL® service
'''''''''''''''''''''''''''''''''''''''''

The :doc:`PostgreSQL </docs/products/postgresql>` database is where you'll store the threshold data for each IoT device. These thresholds represent the alerting range of each IoT device, e.g. a device might trigger an alert when the usage is over `90%`, for other devices, the threshold should be `60%`.

You can create the Aiven for PostgreSQL database with the following steps:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create service**.

3. Select **PostgreSQL®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `Startup-4` as service plan. The `Startup-4` plan allows you to define the service integrations needed to define Apache Flink streaming transformations over the data in the PostgreSQL® table.

5. Enter ``demo-postgresql`` as name for your service.

6. Click **Create service** under the summary on the right side of the console


Create an Aiven for Apache Flink service
'''''''''''''''''''''''''''''''''''''''''

The :doc:`Apache Flink </docs/products/flink>` service is where you'll define the streaming data pipelines to calculate and detect the anomalies.

You can create the Aiven for Apache Flink service with the following steps:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

3. Select **Apache Flink®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `business-4` as service plan. The `business-4` is the minimal plan available for Aiven for Apache Flink, enough to define all the data transformations in this tutorial.

5. Enter ``demo-flink`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console.



Integrate Aiven for Apache Flink service with sources and sinks
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

After creating the service, you'll be redirected to the service details page. Apache Flink doesn't work in isolation, it needs data sources and sinks. Therefore you'll need to define the integrations between Apache Flink service and:

* Aiven for Apache Kafka®, which contains the stream of IoT sensor readings.
* Aiven for PostgreSQL®, which contains the alerting thresholds.

You can define the service integrations, in the Aiven for Apache Flink® **Overview** tab, with the following steps:

1. Click **Get started** on the banner at the top of the **Overview** page.

   .. image:: /images/tutorials/anomaly-detection/flink-console-integration.png
      :alt: Aiven for Apache Flink Overview tab, showing the **Get started** button

2. Select **Aiven for Apache Kafka®** and then select the ``demo-kafka`` service.
3. Click **Integrate**.
4. Click the **+** icon under *Data Flow*.
5. Check the **Aiven for PostgreSQL** checkbox in the ``Aiven Data Services`` section.
6. Select **Aiven for PostgreSQL®** and then select the ``demo-postgresql`` service.
7. Click **Integrate**.

Once the above steps are completed, your **Data Flow** section should be similar to the below:

.. image:: /images/tutorials/anomaly-detection/flink-integrations-done.png
      :alt: Aiven for Apache Flink Overview tab, showing the Integrations to Aiven for Apache Kafka and Aiven for PostgreSQL


Set up the IoT metrics streaming dataset
----------------------------------------

Now that the plumbing of all the components is sorted, it's time for you to create a continuous stream of fake IoT data that will land in an Aiven for Apache Kafka topic. There are various ways to generate fake data, for the tutorial you'll use the `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ allowing you to generate a continuous flow of data with a minimal setup.

Create an Aiven authentication token
''''''''''''''''''''''''''''''''''''

The `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ requires an Aiven authentication token to fetch all the Apache Kafka connection parameters.

You can create an authentication token with the following steps:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. Click the user icon in the top-right corner of the page.
3. Click **Tokens** tab.
4. Click the **Generate token** button.
5. Enter a description (optional) and a time limit (optional) for the token. Leave the *Max age hours* field empty if you do not want the token to expire.

   .. image:: /images/tutorials/anomaly-detection/generate-token.png
      :alt: Aiven Console showing the authentication tokens

6. Click **Generate token**.
7. Click the **Copy** icon or select and copy the access token.

   .. note::
       You cannot get the token later after you close this view.

8. Store the token safely and treat this just like a password.
9. Click **Close**.

Start the fake IoT data generator
''''''''''''''''''''''''''''''''''''

It's time to start streaming the fake IoT data that you'll later process with with Apache Flink:

.. Note::
    You can also use other existing data, although the examples in this tutorial are based on the IoT sample data.

1. Clone the `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ repository to your computer:
   
   .. code::
   
      git clone https://github.com/aiven/fake-data-producer-for-apache-kafka-docker.git

#. Navigate in the to the ``fake-data-producer-for-apache-kafka-docker`` directory and copy the ``conf/env.conf.sample`` file to ``conf/env.conf``.

#. Edit the ``conf/env.conf`` file and update the following parameters:

   * ``PROJECT_NAME`` to the Aiven project name where your services have been created.
   * ``SERVICE_NAME`` to the Aiven for Apache Kafka service name ``demo-kafka``.
   * ``TOPIC`` to ``cpu_load_stats_real``.
   * ``NR_MESSAGES`` to  ``0``.

     .. note::
        The ``NR_MESSAGES`` option defines the number of messages that the tool creates when you run it. Setting this parameter to ``0`` creates a continuous flow of messages that never stops.

   * ``USERNAME`` to the username used to login in the Aiven console.
   * ``TOKEN`` to the Aiven token generated at the previous step of this tutorial.

   .. Note::

    See the `Dockerized fake data producer for Aiven for Apache Kafka® instructions <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker#readme>`_ for details on the parameters.

#. Run the following command to build the Docker image:

   .. code::

        docker build -t fake-data-producer-for-apache-kafka-docker .

#. Run the following command to run the Docker image:

   .. code::

        docker run fake-data-producer-for-apache-kafka-docker

   You should now see the above command pushing IoT sensor reading events to the ``cpu_load_stats_real`` topic in your Apache Kafka® service:

   .. code::

      {"hostname": "dopey", "cpu": "cpu4", "usage": 98.3335306302198, "occurred_at": 1633956789277}
      {"hostname": "sleepy", "cpu": "cpu2", "usage": 87.28240549074823, "occurred_at": 1633956783483}
      {"hostname": "sleepy", "cpu": "cpu1", "usage": 85.3384018012967, "occurred_at": 1633956788484}
      {"hostname": "sneezy", "cpu": "cpu1", "usage": 89.11518629380006, "occurred_at": 1633956781891}
      {"hostname": "sneezy", "cpu": "cpu2", "usage": 89.69951046388306, "occurred_at": 1633956788294}

Check the data in Apache Kafka
''''''''''''''''''''''''''''''

To check if your fake data producer is running, head to Apache Kafka in the Aiven console and look for the ``cpu_load_stats_real`` topic:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. Click on the Aiven for Apache Kafka service name ``demo-kafka``.
3. Click on the **Topics** from the left sidebar.
4. On the ``cpu_load_stats_real`` line, select the ``...`` symbol and then click on **Topic messages**.

   .. image:: /images/tutorials/anomaly-detection/view-kafka-topic-messages.png
      :alt: Aiven for Apache Kafka Topic tab, showing the ``cpu_load_stats_real`` topic being created and the location of the ``...`` icon

5. Click on the **Fetch Messages** button.
6. Toggle the **Decode from base64** option.
7. You should see the messages being pushed to the Apache Kafka topic:

   .. image:: /images/tutorials/anomaly-detection/kafka-messages-detail.png
      :alt: detail of the messages in the ``cpu_load_stats_real`` topic including both key and value in JSON format

8. Click again on the **Fetch Messages** button to refresh the visualization with new messages.

Create a basic anomaly detection pipeline with filtering
--------------------------------------------------------

The first anomaly detection pipeline that you'll create showcases a basic anomaly detection system: you want to flag any sensor reading exceeding a fixed ``80%`` threshold since it could represent a heating anomaly. You'll read the IoT sensor readings from the ``cpu_load_stats_real`` in Apache Kafka, build a filtering pipeline in Apache Flink, and push the readings above the ``80%`` threshold back to Apache Kafka, but to a separate ``cpu_load_stats_real_filter`` topic.

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_load_stats_real)-- IoT metrics stream -->id2(Flink application: filtering);
        id2-- is CPU high? -->id3(Kafka topic: cpu_load_stats_real_filter);

The steps to create the filtering pipeline are the following:

#. Create a new Aiven for Apache Flink application.
#. Define a source table to read the metrics data from your Apache Kafka® topic.
#. Define a sink table to send the processed messages to a separate Apache Kafka® topic.
#. Define a SQL transformation definition to process the data.
#. Create an application deployment to execute the pipeline.

If you feel brave, you can go ahead and try try yourself in the `Aiven Console <https://console.aiven.io/>`_. Otherwise you can follow the steps below:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for Apache Flink service named ``demo-flink`` and go to the **Applications** from the left sidebar.
2. Click **Create new application** to create your Flink application.

   .. image:: /images/tutorials/anomaly-detection/create-application.png
      :alt: The Apache Flink **Application** tab with the **Create Application** button

3. Name the new application ``filtering`` and click **Create application**.

   .. image:: /images/tutorials/anomaly-detection/filtering-application-name.png
      :alt: The Apache Flink **Application** named ``filtering``

4. Create the first version of the application by clicking on **Create first version** button.

5. In the **Add source tables** tab, create the source table (named ``CPU_IN``), pointing to the Apache Kafka® topic ``cpu_load_stats_real`` where the IoT sensor readings are stored by:

   * Select ``Aiven for Apache Kafka - demo-kafka`` as *Integrated service*.
   * Paste the following SQL:

     .. literalinclude:: /code/products/flink/basic_cpu-in_table.md
        :language: sql

   Once created, the source table tab should look like the following:

   .. image:: /images/tutorials/anomaly-detection/CPU_IN_source.png
      :alt: Source table tab with ``CPU_IN`` table defined

   Before saving the source table definition, you can check if it matches the data in the topic by clicking on the triangle next to **Run**. You should see the populated data.

   .. image:: /images/tutorials/anomaly-detection/cpu_in_table_preview.png
      :alt: The Apache Flink source definition with SQL preview of the data



6. Navigate to the **Add sink table** tab.
7. Create the sink table (named ``CPU_OUT_FILTER``), pointing to a new Apache Kafka® topic named ``cpu_load_stats_real_filter`` where the readings exceeding the ``80%`` threshold will land, by:

   * Clicking on the **Add your first sink table**.
   * Selecting ``Aiven for Apache Kafka - demo-kafka`` as *Integrated service*.
   * Pasting the following SQL:

     .. literalinclude:: /code/products/flink/basic_cpu-out-filter_table.md
         :language: sql

   Once created, the sink table tab should look like the following:

   .. image:: /images/tutorials/anomaly-detection/CPU_OUT_target.png
      :alt: Sink table tab with ``CPU_OUT`` table defined


8. Navigate to the **Create statement** tab.
9. Enter the following as the transformation SQL statement, taking data from the ``CPU_IN`` table and pushing the samples over the ``80%`` threshold to ``CPU_OUT_FILTER``:

   .. literalinclude:: /code/products/flink/basic_job.md
      :language: sql

   If you're curious, you can preview the output of the transformation by clicking on the triangle next to the **Run** section, the *Create statement* window should be similar to the following image.

   .. image:: /images/tutorials/anomaly-detection/filtering-preview.png
      :alt: The Apache Flink data transformation with SQL preview of the data

10. Click **Save and deploy later**.
11. Click **Create deployment**.
12. Accept the default deployment parameters and click on **Deploy without a savepoint**.

    .. image:: /images/tutorials/anomaly-detection/filtering-application-deployment.png
        :alt: Detail of the new deployment screen showing the default version, savepoint and parallelism parameters

13. The new application deployment status will show **Initializing** and then **Running: version 1**.

Once the application is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_real_filter`` topic of your ``demo-kafka`` Apache Kafka service.

.. image:: /images/tutorials/anomaly-detection/filtering-topic-preview.png
      :alt: The Apache Flink data transformation with SQL preview of the data


.. Important::

    Congratulations! You created your first streaming anomaly detection pipeline!

    The data is now available in the Apache Kafka topic named ``cpu_load_stats_real_filter``, from there you could either write your own :doc:`Apache Kafka consumer </docs/products/kafka/howto/list-code-samples>` to read the high sensor records or use :doc:`Kafka Connect </docs/products/kafka/kafka-connect>` to sink the data to a wide range of technologies.


Evolve the anomaly detection pipeline with windowing and threshold lookup
---------------------------------------------------------------------------------

In most production environments, you wouldn't want to send an alert on every measurement above the threshold. Sometimes CPUs spike momentarily, for example, and come back down in usage milliseconds later. What's really useful to you in production is if a CPU spike is sustained over a certain period of time.

If a CPU usage spike happens continuously for a 30 seconds interval, there might be a problem. In this step, you'll aggregate the CPU load over a configured time using :doc:`windows </docs/products/flink/concepts/windows>` and the :doc:`event time </docs/products/flink/concepts/event-processing-time>`. By averaging the CPU values over a time window you can filter out short term spikes in usage, and flag only anomaly scenarios where the usage is consistently above a pre-defined threshold for a long period of time.

To add a bit of complexity, and mimic a real scenario, we'll also move away from a fixed ``80%`` threshold, and compare the average utilization figures with the different thresholds, set in a reference table (stored in PostgreSQL), for the various IoT devices based on their ``hostname``. Every IoT device is different, and various devices usually have different alerting ranges. The reference table provides an example of variable, device dependent, thresholds.

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_load_stats_real)-- IoT metrics stream -->id3(Flink application: cpu_aggregation);
        id3-- 30-second average CPU -->id4(Kafka topic: cpu_agg_stats);
        id4-- aggregated data -->id5(Flink application: cpu_agg);
        id6(Postgresql table: thresholds)-- threshold -->id5(Flink application: cpu_agg_comparison);
        id5-- over threshold -->id7(Slack notification);

Create the windowing pipeline
'''''''''''''''''''''''''''''

In this step, you'll create a pipeline to average the CPU metrics figures in 30 seconds windows. Averaging the metric over a time window allows to avoid notification for temporary spikes.

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_load_stats_real)-- IoT metrics stream -->id3(Flink application: cpu_aggregation);
        id3-- 30-second average CPU -->id4(Kafka topic: cpu_agg_stats);

.. Note::

    In this section, you will be able to reuse ``CPU_IN`` source table definition created previously. Importing a working table definition, rather than re-defining it, is a good practice to avoid mistakes.

To complete the section, you will perform the following steps:

* Create a new Aiven for Apache Flink application.
* Import the previously created ``CPU_IN`` source table to read the metrics data from your Apache Kafka® topic.
* Define a sink table to send the processed messages to a separate Apache Kafka® topic.
* Define a SQL transformation definition to process the data.
* Create an application deployment to execute the pipeline.

You can go ahead an try yourself to define the windowing pipeline. If, on the other side, you prefer a step by step approach, follow the instructions below:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for Apache Flink service and go to the **Applications** tab.
2. Click on **Create new application** and name it ``cpu_agg``.
3. Click on **Create first version**.
4. To import the source ``CPU_IN`` table from the previously created ``filtering`` application:

   1. Click on **Import existing source table**
   2. Select ``filtering`` as application, ``Version 1`` as version, ``CPU_IN`` as table and click **Next**
   3. Click on **Add table**

5. Navigate to the **Add sink tables** tab.
6. Create the sink table (named ``CPU_OUT_AGG``) pointing to a new Apache Kafka® topic named ``cpu_agg_stats``, where the 30 second aggregated data will land, by:

   * Clicking on the **Add your first sink table**.
   * Selecting ``Aiven for Apache Kafka - demo-kafka`` as *Integrated service*.
   * Pasting the following SQL:

     .. literalinclude:: /code/products/flink/windowed_cpu-out-agg_table.md
        :language: sql

   * Click **Add table**.

7. Navigate to the **Create statement** tab.
8. Enter the following as the transformation SQL statement, taking data from the ``CPU_IN`` table, aggregating the data over a 30 seconds window, and pushing the output to ``CPU_OUT_AGG``:

   .. literalinclude:: /code/products/flink/windowed_job.md
      :language: sql

9. Click **Save and deploy later**.
10. Click **Create deployment**.
11. Accept the default deployment parameters and click on **Deploy without a savepoint**.

12. The new application deployment status will show **Initializing** and then **Running: version 1**.

When the application  is running, you should start to see messages containing the 30 seconds CPU average in the ``cpu_agg_stats`` topic of your ``demo-kafka`` service.

Create a threshold table in PostgreSQL
''''''''''''''''''''''''''''''''''''''

You will use a PostgreSQL table to store the various IoT thresholds based on the ``hostname``. The table will later be used by a Flink application to compare the average CPU usage with the thresholds and send the notifications to a Slack channel.

You can create the thresholds table in the ``demo-postgresql`` service with the following steps:

.. Note::

    The below instructions assume ``psql`` is installed in your local machine.

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for PostgreSQL service ``demo-postgresql``.
2. In the **Overview** tab locate the **Service URI** parameter and copy the value.
3. Connect via ``psql`` to ``demo postgresql`` with the following terminal command, replacing the ``<SERVICE_URI>`` placeholder with the **Service URI** string copied in the step above:
   
   .. code::
   
      psql "<SERVICE_URI>"

4. Create the ``cpu_thresholds`` table and populate the values with the following code:

   .. literalinclude:: /code/products/flink/pgthresholds_cpu-thresholds_table.md
        :language: sql

5. Enter the following command to check that the threshold values are correctly populated:

   .. code::

      SELECT * FROM cpu_thresholds;

   The output shows you the content of the table:

   .. code::

      hostname | allowed_top
      ---------+------------
      doc      |     20
      grumpy   |     30
      sleepy   |     40
      bashful  |     60
      happy    |     70
      sneezy   |     80
      dopey    |     90

Create the notification pipeline comparing average CPU data with the thresholds
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

At this point, you should have both a stream of the 30 seconds average CPU metrics coming from Apache Kafka, and a set of "per-device" thresholds stored in the PostgreSQL database. This section showcases how you can compare the usage with the thresholds and send a slack notification identifying anomaly situations of when the usage is exceeding the thresholds.

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_agg_stats);
        id1-- aggregated CPU data -->id2(Flink application: cpu_agg);
        id3(Postgresql table: thresholds)-- threshold -->id2(Flink application: cpu_agg_comparison);
        id2-- over threshold -->id4(Slack notification);

You can complete the section with the following steps:

* Create a new Aiven for Apache Flink application.
* Create a source table to read the aggregated metrics data from your Apache Kafka® topic.
* Define a sink table to send the processed messages to a separate Slack channel.
* Define a SQL transformation definition to process the data.
* Create an application deployment to execute the pipeline.

To create the notification data pipeline, you can go ahead an try yourself or follow the steps below:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for Apache Flink service and go to the **Applications** tab.
2. Click on **Create new application** and name it ``cpu_notification``.
3. Click on **Create first version**.
4. To create a source table ``CPU_IN_AGG`` pointing to the Apache Kafka topic ``cpu_agg_stats``:

   * Click on **Add your first source table**.
   * Select ``Aiven for Apache Kafka - demo-kafka`` as *Integrated service*.
   * Paste the following SQL:

     .. literalinclude:: /code/products/flink/windowed_cpu-in-agg_table.md
        :language: sql

   * Click **Add table**.

5. To create a source table ``CPU_THRESHOLDS`` pointing to the PostgreSQL table ``cpu_thresholds``:

   * Click on **Add new table**.
   * Select ``Aiven for PostgreSQL - demo-postgresql`` as *Integrated service*.
   * Paste the following SQL:

     .. literalinclude:: /code/products/flink/pgthresholds_source-thresholds_table.md
         :language: sql

   * Click **Add table**.

6. Navigate to the **Add sink tables** tab.
7. To create a sink table ``SLACK_SINK`` pointing to a Slack channel for notifications:

   * Click on **Add your first sink table**.
   * Select **No integrated service** as **Integrated service**.
   * Paste the following SQL, replacing the ``<SLACK_TOKEN>`` placeholder with the Slack authentication token:

     .. literalinclude:: /code/products/flink/slack_sink.md
         :language: sql

8. Navigate to the **Create statement** tab.
9. Enter the following as the transformation SQL statement, taking data from the ``CPU_IN_AGG`` table, comparing it with the threshold values from ``CPU_THRESHOLDS`` and pushing the samples over the threshold to ``SLACK_SINK``:

   .. literalinclude:: /code/products/flink/slack_notification.md
      :language: sql

   .. Note::

        The ``<CHANNEL_ID>`` placeholder needs to be replaced by the Slack channel ID parameter.

10. Click **Save and deploy later**.
11. Click **Create deployment**.
12. Accept the default deployment parameters and click on **Deploy without a savepoint**.

13. The new application deployment status will show **Initializing** and then **Running: version 1**.

When the application  is running, you should start to see notifications about the IoT devices having CPU usage going over the defined thresholds in the Slack channel.

.. image:: /images/tutorials/anomaly-detection/slack-notifications.png
      :alt: A list of Slack notifications driven by the anomaly detection data pipeline

.. Important::

    Congratulations! You created an advanced streaming data pipeline including windowing, joining data coming from different technologies and a Slack notification system
