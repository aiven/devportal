Create a real-time alerting solution - Aiven console
====================================================

This tutorial shows you an example of how to combine Aiven for Apache Flink® with Aiven for Apache Kafka®, Aiven for PostgreSQL® and Aiven for OpenSearch® services to create a solution that provides real-time alerting data for CPU loads. 

Architecture overview
---------------------

This example involves creating an Apache Kafka® source topic that provides a stream of metrics data, a PostgreSQL® database that contains data on the alerting thresholds, and an Apache Flink® service that combines these two services and pushes the filtered data to a separate Apache Kafka® topic, PostgreSQL® table or OpenSearch® index.

.. mermaid::

    graph LR;

        id1(Kafka)-- metrics stream -->id3(Flink);
        id2(PostgreSQL)-- threshold data -->id3;
        id3-. filtered data .->id4(Kafka);
        id3-. filtered/aggregated data .->id5(PostgreSQL);
        id3-. filtered data .->id6(OpenSearch);

This article includes the steps that you need when using the `Aiven web console <https://console.aiven.io>`_ along with a few different samples of how you can set thresholds for alerts. For connecting to your PostgreSQL® service, this example uses the `Aiven CLI <https://github.com/aiven/aiven-client>`_ calling `psql <https://www.postgresql.org/docs/current/app-psql.html>`_, but you can also use other tools if you prefer.

In addition, the instructions show you how to use a separate Python-based tool, `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_, to create sample records for your Apache Kafka® topic that provides the streamed data.


Requirements
------------

* An Aiven account
* `Aiven CLI <https://github.com/aiven/aiven-client>`_ and `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ to connect to PostgreSQL® services
* `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ and `Docker <https://www.docker.com/>`_ to generate sample data (optional)


Set up Aiven services
---------------------


1. Follow the steps in :doc:`this article </docs/platform/howto/create_new_service>` to create these services:

   - An Aiven for Apache Kafka® service with the *Business-4* service plan, named ``demo-kafka`` 
     This service provides the CPU load input streams
   - An Aiven for PostgreSQL® service with the *Business-4* service plan, named ``demo-postgresql``
     This service contains the CPU alerting threshold values, and is also used as a data sink
   - An Aiven for OpenSearch® service with the *Business-4* service plan, named ``demo-opensearch`` 
     This service is going to contain filtered CPU data streams for further analysis and visualization
   - An Aiven for Apache Flink® service with the *Business-4* service plan, named ``demo-flink``
     This service defines the data transformation and aggregation pipelines


#. Select the ``demo-kafka`` service and change the following settings on the *Overview* page:

   - **Kafka REST API (Karapace)** > **Enable**

     .. Note:: 
      
      The **Kafka REST API** enables you to manage Apache Kafka via REST APIs and also to view the data in your Apache Kafka® topics.

   - **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**
     
     .. Note:: 
     
      The ``kafka.auto_create_topics_enable`` setting allows you to create new Apache Kafka® topics as you configure your Apache Flink® data tables, so that you do not need to create the topics in advance.

#. Select the ``demo-flink`` service and add the **service integrations**:

   a. Click **Get started** on the banner at the top of the *Overview* page.
   b. Select **Aiven for Apache Kafka®** and then select the ``demo-kafka`` service.
   c. Click **Integrate**.
   d. Click the **+** icon under *Data Flow*.
   e. Select **Aiven for PostgreSQL®** and then select the ``demo-postgresql`` service.
   f. Click **Integrate**.
   g. Click the **+** icon under *Data Flow*.
   h. Select **Aiven for OpenSearch** and then select the ``demo-opensearch`` service.
   i. Click **Integrate**.


Set up sample data
------------------

These steps show you how to create sample records to provide streamed data that is processed by the data pipelines presented in this tutorial. You can also use other existing data, although many of the examples in this tutorial are based on the use of this sample data.

Before you start, clone the `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ Git repository to your computer.

1. Follow :doc:`these instructions </docs/platform/howto/create_authentication_token>` to create an authentication token for your Aiven account.

   This is required to allow the tool to connect to a service in your Aiven account.

#. Go to the data producer tool directory and copy the ``conf/env.conf.sample`` file to ``conf/env.conf``.

#. Edit the ``conf/env.conf`` file and update the parameters with your Aiven account information and the authentication token that you created.

   Set ``TOPIC`` to be ``cpu_load_stats_real``, and set ``NR_MESSAGES`` to be ``0``.

   .. note::
      The ``NR_MESSAGES`` option defines the number of messages that the tool creates when you run it. Setting this parameter to ``0`` creates a continuous flow of messages that never stops.

      See the `instructions for the tool <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker#readme>`_ for details on the parameters.

#. Run the following command to build the Docker image:

   ::

      docker build -t fake-data-producer-for-apache-kafka-docker .

#. Run the following command to run the Docker image:

   ::

      docker run fake-data-producer-for-apache-kafka-docker

   This command pushes the following type of events to the ``cpu_load_stats_real`` topic in your Apache Kafka® service:

   ::

      {"hostname": "dopey", "cpu": "cpu4", "usage": 98.3335306302198, "occurred_at": 1633956789277}
      {"hostname": "sleepy", "cpu": "cpu2", "usage": 87.28240549074823, "occurred_at": 1633956783483}
      {"hostname": "sleepy", "cpu": "cpu1", "usage": 85.3384018012967, "occurred_at": 1633956788484}
      {"hostname": "sneezy", "cpu": "cpu1", "usage": 89.11518629380006, "occurred_at": 1633956781891}
      {"hostname": "sneezy", "cpu": "cpu2", "usage": 89.69951046388306, "occurred_at": 1633956788294}


Create a pipeline for basic filtering
-------------------------------------

The first example filters any instances of high CPU load based on a fixed threshold and pushes the high values into a separate Apache Kafka® topic.

.. mermaid::

    graph LR;

        id1(Kafka source)-- metrics stream -->id2(Flink job);
        id2-- high CPU -->id3(Kafka sink);

You need to configure:

`` A source table to read the metrics data from your Apache Kafka® topic
* A sink table to send the processed messages to a separate Apache Kafka® topic
* A Flink job to process the data

To create the filtering data pipeline you can follow the steps below:

1. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink® service.

#. Go to the **Data Tables** subtab.

#. Create the source Apache Kafka® table:

   a. Select your Apache Kafka® service.
   b. Select ``cpu_load_stats_real`` as the topic.
   c. Select **kafka** as the connector type.
   d. Select **key not used** as the key.
   e. Select **json** as the value data format.
   f. Enter ``CPU_IN`` as the name
   g. Enter the following as the ``CPU_IN`` SQL schema

      .. literalinclude:: /code/products/flink/basic_cpu-in_table.md
         :language: sql

   h. Click **Create Table**.

#. Create the sink Apache Kafka® table:

   a. Select your Apache Kafka® service.
   b. Enter ``cpu_load_stats_real_filter`` as the topic.
   c. Select **kafka** as the connector type.
   d. Select **key not used** as the key.
   e. Select **json** as the value data format.
   f. Enter ``CPU_OUT_FILTER`` as the name
   g. Enter the following as the ``CPU_OUT_FILTER`` SQL schema:

      .. literalinclude:: /code/products/flink/basic_cpu-out-filter_table.md
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_filter`` as the job name, select ``CPU_IN`` and ``CPU_OUT_FILTER`` as the tables.

#. Enter the following as the filtering SQL statement:

   .. literalinclude:: /code/products/flink/basic_job.md
      :language: sql

#. click **Execute job**

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_real_filter`` topic of your ``demo-kafka`` service.

Create a pipeline with windowing
--------------------------------
   
The second example aggregates the CPU load over a configured time using :doc:`windows </docs/products/flink/concepts/windows>` and :doc:`event time </docs/products/flink/concepts/event-processing-time>`.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
        id3-- 30-second average CPU -->id4(Kafka sink);

The example  reuses the ``CPU_IN`` Apache Kafka® source table previously created. In addition, you need to configure:

* A new sink table to send the processed messages to a separate Apache Kafka® topic
* A new Flink job to process the data

To create the data pipeline you can follow the steps below:

1. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink® service.

#. Go to the **Data Tables** subtab.

#. Create the sink Apache Kafka® table:

   a. Select your Apache Kafka® service.
   b. Enter ``cpu_load_stats_agg`` as the topic.
   c. Select **kafka** as the connector type.
   d. Select **key not used** as the key.
   e. Select **json** as the value data format.
   f. Enter ``CPU_OUT_AGG`` as the name
   g. Enter the following as the ``CPU_OUT_AGG`` SQL schema:

      .. literalinclude:: /code/products/flink/windowed_cpu-out-agg_table.md
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_agg`` as the job name, select ``CPU_OUT_AGG`` and ``CPU_IN`` as the tables.

#. Enter the following as the filtering SQL statement:

   .. literalinclude:: /code/products/flink/windowed_job.md
      :language: sql

#. Click **Execute job**.

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_agg`` topic of your ``demo-kafka`` service.

.. _flink_sample_pg_thresholds:

Create a Flink SQL job using PostgreSQL® thresholds
---------------------------------------------------

The third example defines host-specific thresholds in a PostgreSQL®  table. The thresholds table is joined with the inbound stream of CPU measurements by hostname to filter instances of CPU load going over the defined thresholds.

.. mermaid::

    graph LR;

        id1(Kafka source)-- metrics stream -->id3(Flink job);
		  id2(PosgreSQL source)-- host-specific thresholds -->id3;
        id3-- host with high CPU -->id4(Kafka sink);

This uses the same ``CPU_IN`` Apache Kafka® source table that you created earlier. In addition, you need to define:

* A sink table to send the processed messages to a separate Apache Kafka® topic
* A source table to get the PostgreSQL® threshold data
* A Flink job to process the data.

To create the data pipeline you can follow the steps below:

.. note::
   For creating and configuring the tables in your PostgreSQL® service, these steps use the Aiven CLI to call ``psql``. You can instead use other tools to complete these steps if you prefer.

1. If you haven't yet logged in to the Aiven CLI, then use the authentication token generated earlier to do so:

   ::

     avn user login YOUR_EMAIL_ADDRESS --token

   The command will prompt for the authentication token.

#. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:

   ::

      avn service cli demo-postgresql --project PROJECT_NAME

#. Enter the following commands to set up the PostgreSQL® table containing the threshold values:

   .. literalinclude:: /code/products/flink/pgthresholds_cpu-thresholds_table.md
      :language: sql

#. Enter the following command to check that the threshold values are created:

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

#. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink® service.

#. Go to the **Data Tables** subtab.

#. Create the Flink table pointing to the PostgreSQL® table

   a. Select your PostgreSQL® service
   b. Enter ``public.cpu_thresholds`` as the table
   c. Enter ``SOURCE_THRESHOLDS`` as the name
   d. Enter the following as the ``SOURCE_THRESHOLDS`` SQL schema:

      .. literalinclude:: /code/products/flink/pgthresholds_source-thresholds_table.md
         :language: sql

   e. click **Create Table**

#. Create the Flink sink table pointing to the Apache Kafka® topic:

   a. Select your Apache Kafka® service.
   b. Enter ``cpu_load_stats_real_filter_pg`` as the topic.
   c. Select **kafka** as the connector type.
   d. Select **key not used** as the key.
   e. Select **json** as the value data format.
   f. Enter ``CPU_OUT_FILTER_PG`` as the name
   g. Enter the following as the ``CPU_OUT_FILTER_PG`` SQL schema:

      .. literalinclude:: /code/products/flink/pgthresholds_cpu-out-filter-pg_table.md
         :language: sql

   h. Click **Create Table**.

#. Create the Flink data pipeline joining the stream of CPU measurement with the host specific thresholds to filter high CPU samples
   
   a. Go to the **Create SQL Job** subtab
   b. Enter ``simple_filter_pg`` as the name
   c. Select the ``CPU_OUT_FILTER_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables
   d. Enter the following SQL statement to join the tables and filter:

   .. literalinclude:: /code/products/flink/pgthresholds_job.md
         :language: sql
   
   e. Click **Execute job**.

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see messages indicating CPU loads that exceed the PostgreSQL®-defined thresholds in the ``cpu_load_stats_real_filter_pg`` topic of your ``demo-kafka`` service.


Create an aggregated data pipeline with Apache Kafka® and PostgreSQL®
---------------------------------------------------------------------

The fourth example highlights the instances where the average CPU load over a :doc:`windowed interval </docs/products/flink/concepts/windows>` exceeds the threshold and stores the results in PostgreSQL®.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
		  id2(PosgreSQL source)-- host-specific thresholds -->id3;
        id3-- high 30-second average CPU -->id4(PostgreSQL sink);

This uses the same ``CPU_IN`` Kafka source table and ``SOURCE_THRESHOLDS`` PostgreSQL® source table that you created earlier. In addition, you need to define:

* A new sink table to store the processed data in PostgreSQL®
* A new Flink job to process the data

To create the data pipeline you can follow the steps below:

.. note::
   For creating and configuring the tables in your PostgreSQL® service, these steps use the Aiven CLI to call ``psql``. You can instead use other tools to complete these steps if you prefer.

1. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:
   
   ::
	  
      avn service cli demo-postgresql --project PROJECT_NAME
   
#. Enter the following command to set up the PostgreSQL® table for storing the results:
   
   .. literalinclude:: /code/products/flink/combined_cpu-load-stats-agg-pg_table.md
      :language: sql
   
#. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink® service.

#. Go to the **Data Tables** subtab.

#. Create a Flink table to sink data to the PostgreSQL® service

   a. Select your PostgreSQL® service
   b. Enter ``cpu_load_stats_agg_pg`` as the table
   c. Enter ``CPU_OUT_AGG_PG`` as the name
   d. Enter the following as the ``CPU_OUT_AGG_PG`` SQL schema:

      .. literalinclude:: /code/products/flink/combined_cpu-out-agg-pg_table.md
         :language: sql

   e. Click **Create Table**

#. Create the Flink data pipeline calculating the CPU average over the time window and checking the value against the thresholds

   a. Go to the **Create SQL Job** subtab
   b. Enter ``simple_filter_pg_agg`` as the name
   c. Select the ``CPU_OUT_AGG_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables
   d. Enter the following SQL to join the tables, calculate the average over a window and filter the high CPU average values:
   
      .. literalinclude:: /code/products/flink/combined_job.md
         :language: sql

   d. Click **Execute job**

      The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

      When the job is running, you should start to see entries indicating hosts with high CPU loads in the ``cpu_load_stats_agg_pg`` table of your ``demo-postgresql`` database.

Replicate the filter stream of data to OpenSearch® for further analysis and data visualization
-----------------------------------------------------------------------------------------------

The last example takes the list of filtered high CPU samples contained in the ``CPU_OUT_FILTER_PG`` Flink table and, after filtering for only the ``happy`` and ``sleepy`` hostnames, pushes the result to an Aiven for OpenSearch® index for further analysis and data visualization.

.. mermaid::

    graph LR;

        id4(Kafka source)-- host with high CPU -->id5(Current Flink job);
        id5-- host with high CPU -->id6(OpenSearch sink);

This uses the ``CPU_OUT_FILTER_PG`` Flink table defined during the :ref:`third example <flink_sample_pg_thresholds>` containing the list of CPU samples above the host-specific threshold defined in PostgreSQL®. In addition, you need to define:

* A new sink table to store the filtered data in OpenSearch®
* A new Flink job to process the data

To create the data pipeline you can follow the steps below:

1. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink® service.

#. Go to the **Data Tables** subtab.

#. Create a Flink table to sink data to the OpenSearch® service

   a. Select your OpenSearch® service
   b. Enter ``cpu_high_load`` as the index
   c. Enter ``CPU_OUT_OS`` as the name
   d. Enter the following as the ``CPU_OUT_OS`` SQL schema:

      .. literalinclude:: /code/products/flink/opensearch_out_table.md
         :language: sql

      .. Note::

         We can reuse a similar definition to the ``CPU_OUT_FILTER_PG`` Flink table since they share the same columns.
         The only difference is the ``time_ltz`` column which is now ``STRING``, as we need to translate the Flink ``TIMESTAMP`` to the timestamp format accepted by OpenSearch®.

   e. Click **Create Table**

#. Create the Flink data pipeline calculating the CPU average over the time window and checking the value against the thresholds

   a. Go to the **Create SQL Job** subtab
   b. Enter ``data_filtering_replication`` as the name
   c. Select the ``CPU_OUT_FILTER_PG`` and ``CPU_OUT_OS`` tables
   d. Enter the following SQL to select from the source table, filter ``happy`` and ``sleepy`` hostnames and push the data to ``CPU_OUT_OS``:
   
      .. literalinclude:: /code/products/flink/filter_job_os.md
         :language: sql
         
      The above SQL converts the ``local_ltz`` field to a string in the format ``yyyy/MM/dd hh:mm:ss`` which is recognised by OpenSearch as timestamp.
   
   e. Click **Execute job**

      The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

      When the job is running, you should start to see entries indicating samples of the ``sleepy`` and ``happy`` hostnames with high CPU loads in the ``cpu_high_load`` table of your ``demo-opensearch`` OpenSearch service. You can use OpenSearch Dashboard to discover more about the datapoints and build advanced visualizations.
