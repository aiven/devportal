Create a real-time alerting solution - Aiven console
====================================================

This tutorial shows you an example of how to combine Aiven for Apache Flink with Aiven for Apache Kafka and Aiven for PostgreSQL services to create a solution that provides real-time alerting data for CPU loads.

Architecture overview
---------------------

This example involves creating an Apache Kafka source topic that provides a stream of metrics data, a PostgreSQL database that contains data on the alerting thresholds, and an Apache Flink service that combines these two services and pushes the filtered data to a separate Apache Kafka topic or PostgreSQL table.

.. mermaid::

    graph LR;

        id1(Kafka)-- metrics stream -->id3(Flink);
        id2(PostgreSQL)-- threshold data -->id3;
        id3-. filtered data .->id4(Kafka);
        id3-. filtered data .->id5(PostgreSQL);

The article includes the steps that you need when using the `Aiven web console <https://console.aiven.io>`_ along with a few different samples of how you can set thresholds for alerts. For connecting to your PostgreSQL service, this example uses the `Aiven CLI <https://github.com/aiven/aiven-client>`_ calling `psql <https://www.postgresql.org/docs/current/app-psql.html>`_, but you can also use other tools if you prefer.

In addition, the instructions show you how to use a separate Python-based tool, `Dockerized fake data producer for Aiven for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_, to create sample records for your Apache Kafka topic that provides the streamed data.


Requirements
------------

* An Aiven account
* `Aiven CLI <https://github.com/aiven/aiven-client>`_ and `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ to connect to PostgreSQL services
* `Dockerized fake data producer for Aiven for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ and `Docker <https://www.docker.com/>`_ to generate sample data (optional)


Set up Aiven services
---------------------

1. Follow the steps in :doc:`this article </docs/platform/howto/create_new_service>` to create these services:

   - An Aiven for Apache Kafka service with the *Business-4* service plan, named ``demo-kafka`` (this streams the CPU load)
   - An Aiven for PostgreSQL service with the *Business-4* service plan, named ``demo-postgresql`` (this defines the alerting threshold values)
   - An Aiven for Apache Flink service with the *Business-4* service plan, named ``demo-flink`` (this analyzes the data stream to find CPUs where the average load exceeds the threshold values)

#. Select the ``demo-kafka`` service and change the following settings on the *Overview* page:

   - **Kafka REST API (Karapace)** > **Enable**

     This setting allows you to integrate your Aiven for Apache Kafka service with Aiven for Apache Flink, and you can also use the API to view the data in your Apache Kafka topics.

   - **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

     This setting allows you to create new Apache Kafka topics as you configure your Apache Flink data tables, so that you do not need to create the topics in advance.

#. Select the ``demo-flink`` service and add the service integrations:

   a. Click **Get started** on the banner at the top of the *Overview* page.
   b. Select **Aiven for Apache Kafka** and then select the ``demo-kafka`` service.
   c. Click **Integrate**.
   d. Click the **+** icon under *Data Flow*.
   e. Select **Aiven for PostgreSQL** and then select the ``demo-postgresql`` service.
   f. Click **Integrate**.


Set up sample data
------------------

These steps show you how to create sample records to provide streamed data that is processed by the data pipelines presented in this tutorial. You can also use other existing data, although many of the examples in this tutorial are based on the use of this sample data.

Before you start, clone the `Dockerized fake data producer for Aiven for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ Git repository to your computer.

1. Follow :doc:`these instructions </docs/platform/howto/create_authentication_token>` to create an authentication token for your Aiven account.

   This is required to allow the tool to connect to a service in your Aiven account.

#. Go to the data producer tool directory and copy the ``conf/env.conf.sample`` file to ``conf/env.conf``.

#. Edit the ``conf/env.conf`` file and update the parameters with your Aiven account information and the authentication token that you created.

   See the `instructions for the tool <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker#readme>`_ for details on the parameters.

   .. note::
      The ``NR_MESSAGES`` option defines the number of messages that the tool creates when you run it. Setting this parameter to ``0`` creates a continuous flow of messages that never stops.

#. Run the following command to build the Docker image:

   ::

      docker build -t fake-data-producer-for-apache-kafka-docker .

#. Run the following command to run the Docker image:

   ::

      docker run fake-data-producer-for-apache-kafka-docker

   This command pushes the following type of events to the ``cpu_load_stats_real`` topic in your Kafka service:

   ::
   
      {"hostname": "dopey", "cpu": "cpu4", "usage": 98.3335306302198, "occurred_at": 1633956789277}
      {"hostname": "sleepy", "cpu": "cpu2", "usage": 87.28240549074823, "occurred_at": 1633956783483}
      {"hostname": "sleepy", "cpu": "cpu1", "usage": 85.3384018012967, "occurred_at": 1633956788484}
      {"hostname": "sneezy", "cpu": "cpu1", "usage": 89.11518629380006, "occurred_at": 1633956781891}
      {"hostname": "sneezy", "cpu": "cpu2", "usage": 89.69951046388306, "occurred_at": 1633956788294}


Create a pipeline for basic filtering
-------------------------------------

This setup uses a fixed threshold to filter any instances of high CPU load to a separate Kafka topic.

.. mermaid::

    graph LR;

        id1(Kafka source)-- metrics stream -->id2(Flink job);
        id2-- high CPU -->id3(Kafka sink);

For this setup, you need to configure a source table to read the metrics data from your Kafka topic, a sink table to send the processed messages to a separate Kafka topic, and a Flink job to process the data.

1. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink service.

#. Go to the **Data Tables** subtab.

#. Create the source Kafka table:

   a. Select your Kafka service.
   b. Select ``cpu_load_stats_real`` as the topic.
   c. Select **Apache Kafka SQL Connector** as the connector type.
   d. Select **Key not used** as the key.
   e. Select **JSON** as the value data format.
   f. Enter ``CPU_IN`` as the name
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/basic_cpu-in_table.md
         :language: sql

   h. Click **Create Table**.

#. Create the sink Kafka table:

   a. Select your Kafka service.
   b. Enter ``cpu_load_stats_real_filter`` as the topic.
   c. Select **Apache Kafka SQL Connector** as the connector type.
   d. Select **Key not used** as the key.
   e. Select **JSON** as the value data format.
   f. Enter ``CPU_OUT_FILTER`` as the name
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/basic_cpu-out-filter_table.md
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_filter`` as the job name, select ``CPU_IN`` and ``CPU_OUT_FILTER`` as the tables, and enter the following as the SQL statement, then click **Execute job**:

   .. literalinclude:: /code/products/flink/basic_job.md
      :language: sql

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_real_filter`` topic of your ``demo-kafka`` service.

Create a pipeline with windowing
--------------------------------
   
This setup measures CPU load over a configured time using :doc:`windows </docs/products/flink/concepts/windows>` and :doc:`event time </docs/products/flink/concepts/event-processing-time>`.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
        id3-- 30-second average CPU -->id4(Kafka sink);

This uses the same ``CPU_IN`` Kafka source table that you created in the previous section. In addition, you need a new sink table to send the processed messages to a separate Kafka topic and a new Flink job to process the data.

1. Go to the **Data Tables** subtab.

#. Create the sink Kafka table:

   a. Select your Kafka service.
   b. Enter ``cpu_load_stats_agg`` as the topic.
   c. Select **Apache Kafka SQL Connector** as the connector type.
   d. Select **Key not used** as the key.
   e. Select **JSON** as the value data format.
   f. Enter ``CPU_OUT_AGG`` as the name
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/windowed_cpu-out-agg_table.md
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_agg`` as the job name, select ``CPU_OUT_AGG`` and ``CPU_IN`` as the tables, and enter the following as the SQL statement, then click **Execute job**:
   
   .. literalinclude:: /code/products/flink/windowed_job.md
      :language: sql

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_agg`` topic of your ``demo-kafka`` service.


Create a Flink SQL job using PostgreSQL thresholds
--------------------------------------------------

This setup uses host-specific thresholds that are stored in PostgreSQL as a basis for determining instances of high CPU load.

.. mermaid::

    graph LR;

        id1(Kafka source)-- metrics stream -->id3(Flink job);
		id2(PosgreSQL source)-- host-specific thresholds -->id3;
        id3-- host with high CPU -->id4(Kafka sink);

This uses the same ``CPU_IN`` Kafka source table that you created earlier. In addition, you need a new sink table to send the processed messages to a separate Kafka topic, a source table to get the PostgreSQL threshold data, and a new Flink job to process the data.

.. note::
   For creating and configuring the tables in your PostgreSQL service, these steps use the Aiven CLI to call ``psql``. You can instead use other tools to complete these steps if you prefer.

1. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:
   
   ::
	  
      avn service cli demo-postgresql --project PROJECT_NAME
   
#. Enter the following commands to set up the PostgreSQL table containing the threshold values:
   
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

#. In the Aiven web console, go to the **Jobs & Data** > **Data Tables** tab for your Flink service.

#. Select your PostgreSQL service, enter ``SOURCE_THRESHOLDS`` as the name, select ``public.cpu_thresholds`` as the table, and enter the following as the SQL schema, then click **Create Table**:
   
   .. literalinclude:: /code/products/flink/pgthresholds_source-thresholds_table.md
      :language: sql

#. Create the sink Kafka table:

   a. Select your Kafka service.
   b. Select ``cpu_load_stats_real_filter_pg`` as the topic.
   c. Select **Apache Kafka SQL Connector** as the connector type.
   d. Select **Key not used** as the key.
   e. Select **JSON** as the value data format.
   f. Enter ``CPU_OUT_FILTER_PG`` as the name
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/pgthresholds_cpu-out-filter-pg_table.md
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab

#. Enter ``simple_filter_pg`` as the name, select the ``CPU_OUT_FILTER_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables, and enter the following as the SQL schema, then click **Execute job**:
   
   .. literalinclude:: /code/products/flink/pgthresholds_job.md
      :language: sql

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see messages indicating CPU loads that exceed the PostgreSQL-defined thresholds in the ``cpu_load_stats_real_filter_pg`` topic of your ``demo-kafka`` service.


Create an aggregated data pipeline with Kafka and PostgreSQL
------------------------------------------------------------

This setup highlights the instances where the average CPU load over a :doc:`windowed interval </docs/products/flink/concepts/windows>` exceeds the threshold and stores the results in PostgreSQL.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
		id2(PosgreSQL source)-- host-specific thresholds -->id3;
        id3-- high 30-second average CPU -->id4(PostgreSQL sink);

This uses the same ``CPU_IN`` Kafka source table and ``SOURCE_THRESHOLDS`` PostgreSQL source table that you created earlier. In addition, you need a new sink table to store the processed data in PostgreSQL and a new Flink job to process the data.

.. note::
   For creating and configuring the tables in your PostgreSQL service, these steps use the Aiven CLI to call ``psql``. You can instead use other tools to complete these steps if you prefer.

1. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:
   
   ::
	  
      avn service cli demo-postgresql --project PROJECT_NAME
   
#. Enter the following command to set up the PostgreSQL table for storing the results:
   
   .. literalinclude:: /code/products/flink/combined_cpu-load-stats-agg-pg_table.md
      :language: sql
   
#. In the Aiven web console, go to the **Jobs & Data** > **Data Tables** tab for your Flink service.
   
#. Select your PostgreSQL service, enter ``CPU_OUT_AGG_PG`` as the name, select ``cpu_load_stats_agg_pg`` as the table, and enter the following as the SQL schema, then click **Create Table**:
   
   .. literalinclude:: /code/products/flink/combined_cpu-out-agg-pg_table.md
      :language: sql

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_filter_pg_agg`` as the name, select the ``CPU_OUT_AGG_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables, and enter the following as the SQL schema, then click **Execute job**:
   
   .. literalinclude:: /code/products/flink/combined_job.md
      :language: sql

   The new job is added to the list on the **Jobs** subtab and starts automatically once a task slot is available. The status changes to *RUNNING* once the job starts.

   When the job is running, you should start to see entries indicating hosts with high CPU loads in the ``cpu_load_stats_agg_pg`` table of your ``demo-postgresql`` database.
