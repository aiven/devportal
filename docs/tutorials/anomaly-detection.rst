Tutorial: streaming anomaly detection with Apache Flink®, Apache Kafka® and PostgreSQL®
==============================================================================================

.. Note::

    This tutorial doesn't assume any existing Apache Kafka®, PostgreSQL® or Apache Flink® knowledge

Before we start
---------------

In this tutorial we will build a streaming anomaly detection system based on IoT type sensor readings. Even if the sample dataset and the data pipeline examples might seem basic, they offer a wide coverage on the integration and transformation options available with Apache Flink that can be applied to other, more complex, scenarios. 

The tutorial includes:

* Apache Flink for data transformation
* Apache Kafka for data streaming
* PostgreSQL® for data storage/query
* Slack as notification system

.. Tip::

    All the tools listed above are fully open source, and can therefore be installed and used locally. We're going to use the comparable Aiven services to avoid any network and integration complexities. 

Architecture overview
---------------------

The tutorial showcases how to create an Apache Kafka® source topic that provides a stream of IoT metrics data, a PostgreSQL® database that contains data on the alerting thresholds, and an Apache Flink® service that combines these two services and pushes the filtered data to a separate Apache Kafka® topic, PostgreSQL® table or a Slack channel.

.. mermaid::

    graph LR;

        id1(Kafka)-- IoT metrics stream -->id3(Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-. filtered data .->id4(Kafka);
        id3-. filtered/aggregated data .->id5(Kafka);
        id3-. filtered data .->id7(Slack);

Prerequisites
-------------

The tutorial uses all Aiven services, therefore you'll need a valid `Aiven account <https://console.aiven.io/signup>`_. The tutorial has also three external dependencies:

* **Docker**, needed for the `fake data generator for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_  is the only dependency. Check out the `related installation instructions <https://docs.docker.com/engine/install/>`_.
* **Slack Token**: the output of a data pipeline sends out notifications to a slack channel, check out the needed steps to retrieve a `Slack authentication token <https://github.com/aiven/slack-connector-for-apache-flink>`_
* `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ a terminal based tool to interact with PostgreSQL

Create the Aiven services
-------------------------

This section of the tutorial will showcase how to create the needed Aiven services via the `Aiven Console <https://console.aiven.io/>`_. We'll create three services:

* An :doc:`Aiven for Apache Kafka®</docs/products/kafka>` named ``demo-kafka`` for data streaming
* An :doc:`Aiven for Apache Flink®</docs/products/flink>` named ``demo-flink`` for streaming data transformation
* An :doc:`Aiven for PostgreSQL®</docs/products/postgresql>` named ``demo-postgresql`` for data storage and query


Create an Aiven for Apache Kafka® service
'''''''''''''''''''''''''''''''''''''''''

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

   This opens a new page with the available service options.

   .. image:: /images/platform/concepts/console_create_service.png
      :alt: Aiven Console view for creating a new service

3. Select **Apache Kafka®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `business-4` as service plan.

5. Enter ``demo-kafka`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console

Customise the Aiven for Apache Kafka service
''''''''''''''''''''''''''''''''''''''''''''

After creating the service, you'll be redirected to the service details page. You can now customise the service to enable the needed components in the *Overview* tab:

1. **Kafka REST API (Karapace)** > **Enable**

   .. Note:: 
    The **Kafka REST API** enables you to manage Apache Kafka via REST APIs and also to view the data in your Apache Kafka® topics.

2. **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

   .. Note:: 
    The ``kafka.auto_create_topics_enable`` setting allows you to create new Apache Kafka® topics as you configure your Apache Flink® data tables, so that you do not need to create the topics in advance.

Create an Aiven for PostgreSQL® service
'''''''''''''''''''''''''''''''''''''''''

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

3. Select **PostgreSQL®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `hobbyist` as service plan.

5. Enter ``demo-posgresql`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console


Create an Aiven for Apache Flink service
'''''''''''''''''''''''''''''''''''''''''

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

3. Select **Apache Flink®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `business-4` as service plan.

5. Enter ``demo-flink`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console

Customise the Aiven for Apache Flink service
''''''''''''''''''''''''''''''''''''''''''''

After creating the service, you'll be redirected to the service details page. You can now customise the service to enable the needed integrations to the Aiven for Apache Kafka and Aiven for PostgreSQL services in the *Overview* tab:

1. Click **Get started** on the banner at the top of the *Overview* page.
2. Select **Aiven for Apache Kafka®** and then select the ``demo-kafka`` service.
3. Click **Integrate**.
4. Click the **+** icon under *Data Flow*.
5. Check the **Aiven for PostgreSQL** checkbox in the `Aiven Data Services` section.
6. Select **Aiven for PostgreSQL®** and then select the ``demo-postgresql`` service.
7. Click **Integrate**.

Set up the IoT metrics streaming dataset
----------------------------------------

This section enables you to create a stream of fake IoT data against an Aiven for Apache Kafka topic.

Create an Aiven authentication token
''''''''''''''''''''''''''''''''''''

The Aiven authentication token is needed to generate fake streaming IoT metric data against to an Aiven for Apache Kafka topic. To create an authentication token:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. Click the user icon in the top-right corner of the page.
3. Click **Authentication** tab and scroll down to *Authentication tokens*.
4. Click the **Generate token** button.
5. Enter a description (optional) and a time limit (optional) for the token. Leave the *Max age hours* field empty if you do not want the token to expire.
6. Click **Generate token**.
7. Click the **Copy** icon or select and copy the access token.

   .. note::
       You cannot get the token later after you close this view.

8. Store the token safely and treat this just like a password.
9. Click **Close**.

Start the fake IoT data generator
''''''''''''''''''''''''''''''''''''

In this step you will create a streaming dataset producer to Apache Kafka. The dataset will contain random IoT metrics that will later be processed with Apache Flink. 

.. Note:: 
    You can also use other existing data, although many of the examples in this article are based on this sample data.

1. Clone the `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ Git repository to your computer::

    git clone https://github.com/aiven/fake-data-producer-for-apache-kafka-docker.git

#. Navigate in the to the data ``fake-data-producer-for-apache-kafka-docker`` directory and copy the ``conf/env.conf.sample`` file to ``conf/env.conf``.

#. Edit the ``conf/env.conf`` file and update the following parameters:

   * ``PROJECT_NAME`` to the Aiven project name where your services have been created
   * ``SERVICE_NAME`` to the Aiven for Apache Kafka service name ``demo-kafka``
   * ``TOPIC`` to ``cpu_load_stats_real``
   * ``NR_MESSAGES`` to  ``0``

     .. note::
        The ``NR_MESSAGES`` option defines the number of messages that the tool creates when you run it. Setting this parameter to ``0`` creates a continuous flow of messages that never stops.

   * ``USERNAME`` to the username used to login in the Aiven console
   * ``TOKEN`` to the Aiven token generated at the previous step of this tutorial

   .. Note::
    
    See the `Dockerized fake data producer for Aiven for Apache Kafka® instructions <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker#readme>`_ for details on the parameters.

#. Run the following command to build the Docker image:

   ::

        docker build -t fake-data-producer-for-apache-kafka-docker .

#. Run the following command to run the Docker image:

   ::

        docker run fake-data-producer-for-apache-kafka-docker

   The above command pushes IoT sensor reading events to the ``cpu_load_stats_real`` topic in your Apache Kafka® service:

   ::

      {"hostname": "dopey", "cpu": "cpu4", "usage": 98.3335306302198, "occurred_at": 1633956789277}
      {"hostname": "sleepy", "cpu": "cpu2", "usage": 87.28240549074823, "occurred_at": 1633956783483}
      {"hostname": "sleepy", "cpu": "cpu1", "usage": 85.3384018012967, "occurred_at": 1633956788484}
      {"hostname": "sneezy", "cpu": "cpu1", "usage": 89.11518629380006, "occurred_at": 1633956781891}
      {"hostname": "sneezy", "cpu": "cpu2", "usage": 89.69951046388306, "occurred_at": 1633956788294}

Check the data in Apache Kafka
''''''''''''''''''''''''''''''

You can check the data flowing in the Aiven for Apache Kafka by:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. Click on the Aiven for Apache Kafka service name ``demo-kafka``.
3. Click on the **Topics** tab.
4. On the ``cpu_load_stats_real`` line, select the ``...`` symbol and then click on **Topic messages**.

   .. image:: /images/tutorials/anomaly-detection/view-kafka-topic-messages.png
      :alt: Aiven for Apache Kafka Topic tab, showing the ``cpu_load_stats_real`` topic being created and the location of the ``...`` icon

5. Click on **Fetch Messages** button
6. Toggle the **Decode from base64** option
7. You should see the messages being pushed to the Apache Kafka topic

   .. image:: /images/tutorials/anomaly-detection/kafka-messages-detail.png
      :alt: detail of the messages in the ``cpu_load_stats_real`` topic including both key and value in JSON format

8. Click again on the **Fetch Messages** button to refresh the visualization with new messages

Create an anomaly detection pipeline with filtering
---------------------------------------------------

The first anomaly detection pipeline is based on filtering any instances of high CPU load based on a fixed threshold. The messages above the threshold are pushed to a separate Apache Kafka® topic.

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_load_stats_real)-- IoT metrics stream -->id2(Flink application: filtering);
        id2-- high CPU -->id3(Kafka topic: cpu_load_stats_real_filter);

You need to:

* Create a new Aiven for Apache Flink application
* Define a source table to read the metrics data from your Apache Kafka® topic
* Define a sink table to send the processed messages to a separate Apache Kafka® topic
* Define a SQL transformation definition to process the data
* Create an application deployment to execute the pipeline

To create the filtering data pipeline you can follow the steps below:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for Apache Flink service named ``demo-flink`` and go to the **Applications** tab.
2. Click **Create new application** to create your Flink application.
3. Name the new application ``filtering`` and click **Create application**
4. In the **Add source tables** tab, create the source table (named ``CPU_IN``) pointing to the Apache Kafka® topic by clicking on **Create first version** and:
   
   * Select ``Aiven for Apache Kafka - demo-kafka`` as `Integrated service`
   * Paste the following SQL:

     .. literalinclude:: /code/products/flink/basic_cpu-in_table.md
        :language: sql

   .. Note::
        You can check that the columns are properly defined and aligned with the data in the Kafka topic using the interactive query capability. You need to click on the **Run** icon below the SQL definition box.



5. Navigate to the **Add sink table** tab
6. Create the sink table (named ``CPU_OUT_FILTER``) pointing to a new Apache Kafka® topic named ``cpu_load_stats_real_filter`` by:

   * Clicking on the **Add your first sink table**
   * Selecting ``Aiven for Apache Kafka - demo-kafka`` as `Integrated service`
   * Pasting the following SQL:

     .. literalinclude:: /code/products/flink/basic_cpu-out-filter_table.md
         :language: sql


7. Navigate to the **Create statement** tab.
8. Enter the following as the transformation SQL statement, taking data from the ``CPU_IN`` table and pushing the samples over the threshold to ``CPU_OUT_FILTER``:

   .. literalinclude:: /code/products/flink/basic_job.md
      :language: sql

9. Click **Save and deploy later**
10. Click **Create deployment**. 
11. Accept the default deployment parameters and click on **Deploy without a savepoint**

    .. image:: /images/tutorials/anomaly-detection/filtering-application-deployment.png
        :alt: Detail of the new deployment screen showing the default version, savepoint and parallelism parameters

12. The new application deployment status will show **Initializing** and then **Running: version 1**.

When the application  is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_real_filter`` topic of your ``demo-kafka`` service.


Create an anomaly detection pipeline with windowing and threshold lookup
------------------------------------------------------------------------

Sending an alert on every IoT measurement above a threshold might cause too much noise, you don't want to receive a notification every time your computer's CPU goes above 90%, but, if that happens continuously for a 10 minute interval there might be a problem. In the second example, you'll aggregate the CPU load over a configured time using :doc:`windows </docs/products/flink/concepts/windows>` and the :doc:`event time </docs/products/flink/concepts/event-processing-time>`. 

The averaged CPU value will then be checked across a reference table (stored in PostgreSQL) defining different thresholds for the various IoT devices based on their ``hostname``.

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_load_stats_real)-- IoT metrics stream -->id3(Flink application: cpu_aggregation);
        id3-- 30-second average CPU -->id4(Kafka topic: cpu_agg_stats);
        id4-- aggregated data -->id5(Flink application: cpu_agg);
        id6(Postgresql table: thresholds)-- threshold -->id5(Flink application: cpu_agg_comparison);
        id5-- over threshold -->id7(Slack notification);

Create the windowing pipeline
'''''''''''''''''''''''''''''

In this step, you'll create a pipeline to average the CPU metrics figures in 30 second windows. 

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_load_stats_real)-- IoT metrics stream -->id3(Flink application: cpu_aggregation);
        id3-- 30-second average CPU -->id4(Kafka topic: cpu_agg_stats);

The steps below allows you to import the ``CPU_IN`` source table previously created. To complete the example, you need to:

* Create a new Aiven for Apache Flink application
* Import the previously created ``CPU_IN`` source table to read the metrics data from your Apache Kafka® topic
* Define a sink table to send the processed messages to a separate Apache Kafka® topic
* Define a SQL transformation definition to process the data
* Create an application deployment to execute the pipeline

To create the windowing data pipeline you can follow the steps below:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for Apache Flink service and go to the **Applications** tab.
2. Click on **Create new application** and name it ``cpu_agg``
3. Click on **Create first version**
4. To import the ``CPU_IN`` table from the previously created ``filtering`` application
    * Click on **Import existing source table**
    * Select ``filtering`` as application, ``Version 1`` as version, ``CPU_IN`` as table and click **Next**
    * Click on **Add table**

5. Navigate to the **Add sink tables** tab. 
6. Create the sink table (named ``CPU_OUT_AGG``) pointing to a new Apache Kafka® topic named ``cpu_agg_stats`` by:

   * Clicking on the **Add your first sink table**
   * Selecting ``Aiven for Apache Kafka - demo-kafka`` as `Integrated service`
   * Pasting the following SQL:

     .. literalinclude:: /code/products/flink/windowed_cpu-out-agg_table.md
        :language: sql

   * Click **Add table**.

7. Navigate to the **Create statement** tab
8. Enter the following as the transformation SQL statement, taking data from the ``CPU_IN`` table and pushing the samples over the threshold to ``CPU_OUT_AGG``:

   .. literalinclude:: /code/products/flink/windowed_job.md
      :language: sql

9. Click **Save and deploy later**
10. Click **Create deployment**
11. Accept the default deployment parameters and click on **Deploy without a savepoint**

12. The new application deployment status will show **Initializing** and then **Running: version 1**.

When the application  is running, you should start to see messages containing the 30 seconds CPU average in the ``cpu_agg_stats`` topic of your ``demo-kafka`` service.

Create a threshold table in PostgreSQL
''''''''''''''''''''''''''''''''''''''

In this step, you will create a table in Aiven for PostgreSQL containing the alerting thresholds for each IoT device based on the `hostname`. The table will later be used by a Flink application to compare the average CPU usage with the thresholds and send the notifications to a Slack channel. 

.. Note::

    The below instructions assume ``psql`` is installed in your local machine.

To create a thresholds table in the ``demo-postgresql`` service:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for PostgreSQL service ``demo-postgresql``
2. In the **Overview** tab locate the **Service URI** parameter and copy the value
3. Connect via ``psql`` to ``demo postgresql`` with the following terminal command, replacing the ``<SERVICE_URI>`` placeholder with the **Service URI** string copied in the step above::

        psql <SERVICE_URI>

4. Create the ``cpu_thresholds`` table and populate the values with the following code:

   .. literalinclude:: /code/products/flink/pgthresholds_cpu-thresholds_table.md
        :language: sql

5. Enter the following command to check that the threshold values are correctly populated:

   ::

      SELECT * FROM cpu_thresholds;

   The output shows you the content of the table:

   ::

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

In this step, you'll create a pipeline to compare the 30 seconds average CPU metrics with the thresholds coming from the PostgreSQL database and send a slack notification when the thresholds are exceeded. 

.. mermaid::

    graph TD;

        id1(Kafka topic: cpu_agg_stats);
        id1-- aggregated CPU data -->id2(Flink application: cpu_agg);
        id3(Postgresql table: thresholds)-- threshold -->id2(Flink application: cpu_agg_comparison);
        id2-- over threshold -->id4(Slack notification);

To complete the example, you need to:

* Create a new Aiven for Apache Flink application
* Create a source table to read the aggregated metrics data from your Apache Kafka® topic
* Define a sink table to send the processed messages to a separate Slack channel
* Define a SQL transformation definition to process the data
* Create an application deployment to execute the pipeline

To create the notification data pipeline you can follow the steps below:

1. In the `Aiven Console <https://console.aiven.io/>`_, open the Aiven for Apache Flink service and go to the **Applications** tab.
2. Click on **Create new application** and name it ``cpu_notification``
3. Click on **Create first version**
4. To create a source table ``CPU_IN_AGG`` pointing to the Apache Kafka topic ``cpu_agg_stats``:

   * Click on **Add your first source table**
   * Select ``Aiven for Apache Kafka - demo-kafka`` as `Integrated service`
   * Paste the following SQL:

     .. literalinclude:: /code/products/flink/windowed_cpu-in-agg_table.md
        :language: sql

   *. Click **Add table**.

5. To create a source table ``CPU_THRESHOLDS`` pointing to the PostgreSQL table ``cpu_thresholds``:

   * Click on **Add new table**
   * Select ``Aiven for PostgreSQL - demo-postgresql`` as `Integrated service`
   * Paste the following SQL:
     
     .. literalinclude:: /code/products/flink/pgthresholds_source-thresholds_table.md
         :language: sql

   *. Click **Add table**.

6. Navigate to the **Add sink tables** tab
7. To create a sink table ``SLACK_SINK`` pointing to a Slack channel for notifications:

   * Click on **Add your first sink table**
   * Select **No integrated service** as **Integrated service**
   * Paste the following SQL, replacing the ``<SLACK_TOKEN>`` placeholder with the Slack authentication token:

     .. literalinclude:: /code/products/flink/slack_sink.md
         :language: sql

8. Navigate to the **Create statement** tab
9. Enter the following as the transformation SQL statement, taking data from the ``CPU_IN_AGG`` table, comparing it with the threshold values from ``CPU_THRESHOLDS`` and pushing the samples over the threshold to ``SLACK_SINK``:

   .. literalinclude:: /code/products/flink/slack_notification.md
      :language: sql

   .. Note::

        The ``<CHANNEL_ID>`` placeholder needs to be replaced by the Slack channel ID parameter.

10. Click **Save and deploy later**
11. Click **Create deployment**
12. Accept the default deployment parameters and click on **Deploy without a savepoint**

13. The new application deployment status will show **Initializing** and then **Running: version 1**.

When the application  is running, you should start to see messages containing the 30 seconds CPU average in the ``cpu_agg_stats`` topic of your ``demo-kafka`` service.