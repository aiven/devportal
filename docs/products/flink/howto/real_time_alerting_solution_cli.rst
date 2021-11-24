Create a real-time alerting solution - Aiven CLI
================================================

This Aiven CLI tutorial shows you an example of how to combine Aiven for Apache Flink with Aiven for Apache Kafka and Aiven for PostgreSQL services to create a solution that provides real-time alerting data for CPU loads.

Architecture overview
---------------------

This example involves creating an Apache Kafka source topic that provides a stream of metrics data, a PostgreSQL database that contains data on the alerting thresholds, and an Apache Flink service that combines these two services and pushes the filtered data to a separate Apache Kafka topic or PostgreSQL table.

.. mermaid::

    graph LR;

        id1(Kafka)-- metrics stream -->id3(Flink);
        id2(PostgreSQL)-- threshold data -->id3;
        id3-. filtered data .->id4(Kafka);
        id3-. filtered data .->id5(PostgreSQL);

The article includes the steps that you need when using the `Aiven CLI <https://github.com/aiven/aiven-client>`_ along with a few different samples of how you can set thresholds for alerts. For connecting to your PostgreSQL service, this example uses the Aiven CLI calling `psql <https://www.postgresql.org/docs/current/app-psql.html>`_, but you can also use other tools if you prefer.

In addition, the instructions show you how to use a separate Python-based tool, `Dockerized fake data producer for Aiven for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_, to create sample records for your Apache Kafka topic that provides the streamed data.


Set up Aiven services
---------------------

.. note::
   The commands given in this example use ``business-4`` service plans, but you can use any other service plan instead if you prefer.

1. Using the Aiven CLI, run the following command to create an Aiven for Apache Kafka service named ``demo-kafka``:

   ::

      avn service create demo-kafka               \
          --service-type kafka                    \
          --cloud CLOUD_AND_REGION                \
          --plan business-4                       \
          -c kafka.auto_create_topics_enable=true \
          -c kafka_rest=true                      \
          -c schema_registry=true                 \
          --project PROJECT_NAME

#. Run the following command to create an Aiven for PostgreSQL service named ``demo-postgresql``:

   ::

      avn service create demo-postgresql          \
          --service-type pg                       \
          --cloud CLOUD_AND_REGION                \
          --plan business-4                       \
          --project PROJECT_NAME

#. Run the following command to create an Aiven for Apache Flink service named ``demo-flink``:

   ::

      avn service create demo-flink               \
          --service-type flink                    \
          --cloud CLOUD_AND_REGION                \
          --plan business-4                       \
          --project PROJECT_NAME

#. Add the ``demo-kafka`` and ``demo-postgresql`` integrations to the ``demo-flink`` service.

   a. Enter the following command to add the ``demo-kafka`` service integration:

      ::

         avn service integration-create           \
             --project PROJECT_NAME               \
             --service-type flink                 \
             -s demo-kafka                        \
             -d demo-flink

   b. Enter the following command to add the ``demo-postgresql`` service integration:

      ::

         avn service integration-create           \
             --project PROJECT_NAME               \
             --service-type flink                 \
             -s demo-postgresql                   \
             -d demo-flink

   c. Enter the following command to list the integrations:

      ::

         avn service integration-list demo-flink

      The output should show you that both ``demo-kafka`` and ``demo-postgresql`` integrations are enabled as well as the corresponding ``integration_id`` values that you need later when creating data tables.



Set up sample data
------------------

These steps show you how to create sample records to provide streamed data that is processed by the data pipelines presented in this tutorial. You can also use other existing data, although many of the examples in this tutorial are based on the use of this sample data.

Before you start, clone the `Dockerized fake data producer for Aiven for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ Git repository to your computer.

1. Follow `these instructions <https://developer.aiven.io/docs/tools/cli/user/user-access-token.html#manage-access-tokens>`_ to create an authentication token for your Aiven account.

   This is required to allow the tool to connect to a service in your Aiven account.

#. Go to the data producer tool directory and copy the ``conf/env.conf.sample`` file to ``conf/env.conf``.

#. Edit the ``conf/env.conf`` file and update the parameters.

   Replace ``AIVEN_PROJECT_NAME`` and ``AIVEN_ACCOUNT_EMAIL`` with the details for your Aiven account, and replace ``AUTHENTICATION_TOKEN`` with the token that you created.

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


1. Using the Aiven CLI, create a Kafka table named ``CPU_IN``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``KAFKA_INTEGRATION_ID``
       - The ID for your ``demo-kafka`` service integration.
     * - ``TABLE_SQL``
       - .. literalinclude:: /code/products/flink/basic_cpu-in_table.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink table create demo-flink KAFKA_INTEGRATION_ID \
          --table-name CPU_IN                                        \
          --kafka-topic cpu_load_stats_real                          \
          --schema-sql "TABLE_SQL"

#. Create an output table named ``CPU_OUT_FILTER``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``TABLE_SQL``
       - .. literalinclude:: /code/products/flink/basic_cpu-out-filter_table.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink table create demo-flink KAFKA_INTEGRATION_ID \
          --table-name CPU_OUT_FILTER                                \
          --kafka-topic cpu_load_stats_real_filter                   \
          --schema-sql "TABLE_SQL"

#. Run the following command to list the tables for the ``demo-flink`` service:

   ::

      avn service flink table list demo-flink

   The output for this command shows you the table IDs, which you need in the command that you use to create Flink jobs:

   ::

     INTEGRATION_ID                        TABLE_ID                              TABLE_NAME
     ====================================  ====================================  ==========
     917bbec0-0f34-4a31-b910-c585feb95d09  305c44d9-22d5-4be8-987f-57c7642e8a89  CPU_IN
     917bbec0-0f34-4a31-b910-c585feb95d09  3d33a7c5-3716-4b21-9739-f79228f9f28f  CPU_OUT_FILTER

#. Create a data pipeline job named ``simple_filter``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``CPU_IN_ID``
       - The table ID for your ``CPU_IN`` table.
     * - ``CPU_OUT_FILTER_ID``
       - The table ID for your ``CPU_OUT_FILTER`` table.
     * - ``JOB_SQL``
       - .. literalinclude:: /code/products/flink/basic_job.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink job create demo-flink simple_filter     \
          --table-ids CPU_IN_ID CPU_OUT_FILTER_ID               \
          --statement "JOB_SQL"

   The new job is added and starts automatically once a task slot is available.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_real_filter`` topic of your ``demo-kafka`` service.


Create a pipeline with windowing
--------------------------------
   
This setup uses :doc:`windows </docs/products/flink/concepts/windows>` to determine instances of high CPU load during set intervals based on :doc:`event time </docs/products/flink/concepts/event_processing_time>`.

.. mermaid::

    graph LR;

        id1(Kafka source)-- timestamped metrics -->id3(Flink job);
        id3-- 30-second average CPU -->id4(Kafka sink);


1. Using the Aiven CLI, create a Kafka table named ``CPU_OUT_AGG``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``KAFKA_INTEGRATION_ID``
       - The ID for your ``demo-kafka`` service integration.
     * - ``TABLE_SQL``
       - .. literalinclude:: /code/products/flink/windowed_cpu-out-agg_table.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink table create demo-flink KAFKA_INTEGRATION_ID  \
          --table-name CPU_OUT_AGG                                    \
          --kafka-topic cpu_load_stats_agg                            \
          --schema-sql "TABLE_SQL"

#. Run the following command to list the tables for the ``demo-flink`` service and get the IDs for the ``CPU_IN`` and ``CPU_OUT_AGG`` tables:

   ::

      avn service flink table list demo-flink

#. Create a data pipeline job named ``simple_agg``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``CPU_IN_ID``
       - The table ID for your ``CPU_IN`` table.
     * - ``CPU_OUT_AGG_ID``
       - The table ID for your ``CPU_OUT_AGG`` table.
     * - ``JOB_SQL``
       - .. literalinclude:: /code/products/flink/windowed_job.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink job create demo-flink simple_agg        \
          --table-ids CPU_IN_ID CPU_OUT_AGG_ID                  \
          --statement "JOB_SQL"

   The new job is added and starts automatically once a task slot is available.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_agg`` topic of your ``demo-kafka`` service.


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
   
   .. literalinclude:: /code/products/flink/pgthresholds_cpu-thresholds_table.md
      :language: sql

#. Enter the following command to check that the threshold values are created:

   ::

      SELECT * FROM CPU_THRESHOLDS;

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

#. Create a PostgreSQL table named ``SOURCE_THRESHOLDS``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``POSTGRESQL_INTEGRATION_ID``
       - The ID for your ``demo-postgresql`` service integration.
     * - ``TABLE_SQL``
       - .. literalinclude:: /code/products/flink/pgthresholds_source-thresholds_table.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink table create demo-flink POSTGRESQL_INTEGRATION_ID  \
          --table-name SOURCE_THRESHOLDS                                   \
          --jdbc-table cpu_thresholds                                      \
          --schema-sql "TABLE_SQL"

#. Create a Kafka table named ``CPU_OUT_FILTER_PG``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``KAFKA_INTEGRATION_ID``
       - The ID for your ``demo-kafka`` service integration.
     * - ``TABLE_SQL``
       - .. literalinclude:: /code/products/flink/pgthresholds_cpu-out-filter-pg_table.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink table create demo-flink KAFKA_INTEGRATION_ID  \
          --table-name CPU_OUT_FILTER_PG                              \
          --kafka-topic cpu_load_stats_real_filter_pg                 \
          --schema-sql "TABLE_SQL"

#. Run the following command to list the tables for the ``demo-flink`` service and get the IDs for the ``CPU_IN``, ``CPU_OUT_FILTER_PG``, and ``SOURCE_THRESHOLDS`` tables:

   ::

      avn service flink table list demo-flink

#. Create a data pipeline job named ``simple_filter_pg``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``CPU_IN_ID``
       - The table ID for your ``CPU_IN`` table.
     * - ``CPU_OUT_FILTER_PG_ID``
       - The table ID for your ``CPU_OUT_FILTER_PG`` table.
     * - ``SOURCE_THRESHOLDS_ID``
       - The table ID for your ``SOURCE_THRESHOLDS`` table.
     * - ``JOB_SQL``
       - .. literalinclude:: /code/products/flink/pgthresholds_job.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink job create demo-flink simple_filter_pg            \
          --table-ids CPU_IN_ID CPU_OUT_FILTER_PG_ID SOURCE_THRESHOLDS_ID \
          --statement "JOB_SQL"

   The new job is added and starts automatically once a task slot is available.

   When the job is running, you should start to see messages indicating hosts with high CPU loads in the ``cpu_load_stats_real_filter_pg`` topic of your ``demo-kafka`` service.


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
   
   .. literalinclude:: /code/products/flink/combined_cpu-load-stats-agg-pg_table.md
      :language: sql
   
#. Create a PostgreSQL table named ``CPU_OUT_AGG_PG``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``POSTGRESQL_INTEGRATION_ID``
       - The ID for your ``demo-postgresql`` service integration.
     * - ``TABLE_SQL``
       - .. literalinclude:: /code/products/flink/combined_cpu-out-agg-pg_table.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink table create demo-flink POSTGRESQL_INTEGRATION_ID  \
          --table-name CPU_OUT_AGG_PG                                      \
          --jdbc-table cpu_load_stats_agg_pg                               \
          --schema-sql "TABLE_SQL"

#. Run the following command to list the tables for the ``demo-flink`` service and get the IDs for the ``CPU_IN``, ``CPU_OUT_AGG_PG``, and ``SOURCE_THRESHOLDS`` tables:

   ::

      avn service flink table list demo-flink

#. Create a data pipeline job named ``simple_filter_pg_agg``.

   .. list-table::
     :header-rows: 1
     :align: left

     * - Variable
       - Value
     * - ``CPU_IN_ID``
       - The table ID for your ``CPU_IN`` table.
     * - ``CPU_OUT_AGG_PG_ID``
       - The table ID for your ``CPU_OUT_AGG_PG`` table.
     * - ``SOURCE_THRESHOLDS_ID``
       - The table ID for your ``SOURCE_THRESHOLDS`` table.
     * - ``JOB_SQL``
       - .. literalinclude:: /code/products/flink/combined_job.md
            :language: sql

   Run the following command, replacing the variables listed in the above table with the corresponding values:

   ::

      avn service flink job create demo-flink simple_filter_pg_agg     \
          --table-ids CPU_IN_ID CPU_OUT_AGG_PG_ID SOURCE_THRESHOLDS_ID \
          --statement "JOB_SQL"

   The new job is added and starts automatically once a task slot is available.

   When the job is running, you should start to see entries indicating hosts with high CPU loads in the ``cpu_load_stats_agg_pg`` table of your ``demo-postgresql`` database.

