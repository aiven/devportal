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


Set up Aiven services
---------------------

1. Follow the steps in :doc:`this article </docs/platform/howto/create_new_service>` to create these services:

   - An Aiven for Apache Kafka service with the *Business-4* service plan, named ``demo-kafka`` (this streams the CPU load)
   - An Aiven for PostgreSQL service with the *Business-4* service plan, named ``demo-postgresql`` (this defines the alerting threshold values)
   - An Aiven for Apache Flink service with the *Business-4* service plan, named ``demo-flink`` (this analyzes the data stream to find CPUs where the average load exceeds the threshold values)

#. Select the ``demo-kafka`` service and change the following settings on the *Overview* page:

   - **Kafka REST API (Karapace)** > **Enable**
   - **Kafka Connect** > **Enable**
   - **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

#. Select the ``demo-flink`` service and add the service integrations:

   a. Click **Get started** on the banner at the top of the *Overview* page.
   b. Select **Aiven for Apache Kafka** and then select the ``demo-kafka`` service.
   c. Click **Integrate**.
   d. Click the **+** icon under *Data Flow*.
   e. Select **Aiven for PostgreSQL** and then select the ``demo-postgresql`` service.
   f. Click **Integrate**.


Set up sample data
------------------

Before you start, clone the `Dockerized fake data producer for Aiven for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ Git repository to your computer.

1. Follow :doc:`these instructions </docs/platform/howto/create_authentication_token>` to create an authentication token for your Aiven account.

#. Go to the data producer tool directory and copy the ``conf/env.conf.sample`` file to ``conf/env.conf``.

#. Edit the ``conf/env.conf`` file and update the parameters:

   ::

      PROJECT_NAME="AIVEN_PROJECT_NAME"
      SERVICE_NAME="demo-kafka"
      TOPIC="cpu_load_stats_real"
      PARTITIONS=2
      REPLICATION=2
      NR_MESSAGES=200
      MAX_TIME=0
      SUBJECT="metrics"
      USERNAME="AIVEN_ACCOUNT_EMAIL"
      TOKEN="AUTHENTICATION_TOKEN"

   Replace ``AIVEN_PROJECT_NAME`` and ``AIVEN_ACCOUNT_EMAIL`` with the details for your Aiven account, and replace ``AUTHENTICATION_TOKEN`` with the token that you created.

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


1. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink service.

#. Go to the **Data Tables** subtab.

#. Create the source Kafka table:

   a. Select your Kafka service.
   b. Select **Apache Kafka SQL Connector** as the connector type.
   c. Select **Empty key** as the key.
   d. Select **JSON** as the value data format.
   e. Enter ``CPU_IN`` as the name
   f. Select ``cpu_load_stats_real`` as the topic.
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 2-8
         :language: sql

   h. Click **Create Table**.

#. Create the sink Kafka table:

   a. Select your Kafka service.
   b. Select **Apache Kafka SQL Connector** as the connector type.
   c. Select **Empty key** as the key.
   d. Select **JSON** as the value data format.
   e. Enter ``CPU_OUT_FILTER`` as the name
   f. Select ``cpu_load_stats_real_filter`` as the topic.
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 11-14
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_filter`` as the job name, select ``CPU_IN`` and ``CPU_OUT_FILTER`` as the tables, and enter the following as the SQL statement, then click **Execute job**:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 17-24
      :language: sql


Create a pipeline with windowing
--------------------------------
   
This setup uses :doc:`windows </docs/products/flink/concepts/windows>` to determine instances of high CPU load during set intervals based on :doc:`event time </docs/products/flink/concepts/event_processing_time>`.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
        id3-- 30-second average CPU -->id4(Kafka sink);


1. Go to the **Data Tables** subtab.

#. Create the sink Kafka table:

   a. Select your Kafka service.
   b. Select **Apache Kafka SQL Connector** as the connector type.
   c. Select **Empty key** as the key.
   d. Select **JSON** as the value data format.
   e. Enter ``CPU_OUT_AGG`` as the name
   f. Select ``cpu_load_stats_agg`` as the topic.
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 27-32
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_agg`` as the job name, select ``CPU_OUT_AGG`` and ``CPU_IN`` as the tables, and enter the following as the SQL statement, then click **Execute job**:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 35-49
      :language: sql


Create a Flink SQL job using PostgreSQL thresholds
--------------------------------------------------

This setup uses host-specific thresholds that are stored in PostgreSQL as a basis for determining instances of high CPU load.

.. mermaid::

    graph LR;

        id1(Kafka source)-- metrics stream -->id3(Flink job);
		id2(PosgreSQL source)-- host-specific thresholds -->id3;
        id3-- host with high CPU -->id4(Kafka sink);


1. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:
   
   ::
	  
      avn service cli demo-postgresql --project PROJECT_NAME
   
#. Enter the following commands to set up the PostgreSQL table containing the threshold values:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 52-53
      :language: sql

#. Enter the following command to check that the threshold values are created:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 54
      :language: sql

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
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 57-59
      :language: sql

#. Create the sink Kafka table:

   a. Select your Kafka service.
   b. Select **Apache Kafka SQL Connector** as the connector type.
   c. Select **Empty key** as the key.
   d. Select **JSON** as the value data format.
   e. Enter ``CPU_OUT_FILTER_PG`` as the name
   f. Select ``cpu_load_stats_real_filter_pg`` as the topic.
   g. Enter the following as the SQL schema:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 62-66
         :language: sql

   h. Click **Create Table**.

#. Go to the **Create SQL Job** subtab

#. Enter ``simple_filter_pg`` as the name, select the ``CPU_OUT_FILTER_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables, and enter the following as the SQL schema, then click **Execute job**:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 69-77
      :language: sql


Create an aggregated data pipeline with Kafka and PostgreSQL
------------------------------------------------------------

This setup highlights the instances where the average CPU load over a :doc:`windowed interval </docs/products/flink/concepts/windows>` exceeds the threshold and stores the results in PostgreSQL.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
		id2(PosgreSQL source)-- host-specific thresholds -->id3;
        id3-- high 30-second average CPU -->id4(PostgreSQL sink);


1. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:
   
   ::
	  
      avn service cli demo-postgresql --project PROJECT_NAME
   
#. Enter the following command to set up the PostgreSQL table for storing the results:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 80-83
      :language: sql
   
#. In the Aiven web console, go to the **Jobs & Data** > **Data Tables** tab for your Flink service.
   
#. Select your PostgreSQL service, enter ``CPU_OUT_AGG_PG`` as the name, select ``cpu_load_stats_agg_pg`` as the table, and enter the following as the SQL schema, then click **Create Table**:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 86-88
      :language: sql

#. Go to the **Create SQL Job** subtab.

#. Enter ``simple_filter_pg_agg`` as the name, select the ``CPU_OUT_AGG_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables, and enter the following as the SQL schema, then click **Execute job**:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 91-124
      :language: sql


