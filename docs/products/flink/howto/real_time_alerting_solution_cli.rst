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

In addition, the instructions show you how to use a separate Python tool, `Apache Kafka Python fake data producer <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_, to create sample records for your Apache Kafka topic that provides the streamed data. The steps for using this tool include instructions for getting the necessary details and certificate files with the `Aiven web console <https://console.aiven.io>`_.


Set up Aiven services
---------------------

1. Using the Aiven CLI, run the following command to create an Aiven for Apache Kafka service named ``demo-kafka``:

   ::

      avn service create demo-kafka               \
          -t kafka                                \
          --cloud CLOUD_AND_REGION                \
          -p business-4                           \
          -c kafka.auto_create_topics_enable=true \
          -c kafka_connect=true                   \
          -c kafka_rest=true                      \
          -c schema_registry=true                 \
          --project PROJECT_NAME

#. Run the following command to create an Aiven for PostgreSQL service named ``demo-postgresql``:

   ::

      avn service create demo-postgresql          \
          -t pg                                   \
          --cloud CLOUD_AND_REGION                \
          -p business-4                           \
          --project PROJECT_NAME

#. Run the following command to create an Aiven for Apache Flink service named ``demo-flink``:

   ::

      avn service create demo-flink               \
          -t flink                                \
          --cloud CLOUD_AND_REGION                \
          -p business-4                           \
          --project PROJECT_NAME

#. Add the ``demo-kafka`` and ``demo-postgresql`` integrations to the ``demo-flink`` service.

   a. Enter the following command to add the ``demo-kafka`` service:

      ::

         avn service integration-create           \
             --project PROJECT_NAME               \
             -t flink                             \
             -s demo-kafka                        \
             -d demo-flink

   b. Enter the following command to add the ``demo-postgresql`` service:

      ::

         avn service integration-create           \
             --project PROJECT_NAME               \
             -t flink                             \
             -s demo-postgresql                   \
             -d demo-flink

   c. Enter the following command to list the integrations:

      ::

         avn service integration-list demo-flink

   d. Copy the integration IDs for the ``demo-kafka`` and ``demo-postgresql`` services. 

      You need these IDs to create tables for your Apache Flink jobs.



Set up sample data
------------------

1. Log in to the `Aiven web console <https://console.aiven.io>`_ and select the ``demo-kafka`` service.

#. On the *Overview* page, click **Download** next to *Access Key*, *Access Certificate*, and *CA Certificate*, then copy the three downloaded files to a folder on your computer.

   You need these files when running the tool that creates the sample records.

#. Copy the *Host* and *Port* values on the *Overview* page of your Kafka service.

#. Run the following Python command to create the sample records using the `Apache Kafka Python fake data producer <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_ tool:

   ::

      python3 python-fake-data-producer-for-apache-kafka/metricproducer.py \
          --cert-folder DOWNLOADED_CERTIFICATE_FOLDER \
          --host KAFKA_HOST_ADDRESS \
          --port KAFKA_PORT \
          --topic-name cpu_load_stats_real \
          --nr-messages 0 \
          --max-waiting-time 1


   Replace ``DOWNLOADED_CERTIFICATE_FOLDER`` with the folder that contains the three certificate files that you downloaded, and ``KAFKA_HOST_ADDRESS`` and ``KAFKA_PORT`` with the address and port for your Aiven for Apache Kafka service.

   .. note::
      The ``--nr-messages 0`` option creates a continuous flow of messages that never stops.

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

1. Using the Aiven CLI, run the following command to create a Kafka table named ``CPU_IN``:

   ::

      avn service flink table create demo-flink INTEGRATION_ID  \
          --table-name CPU_IN                                   \
          --kafka-topic cpu_load_stats_real                     \
          --schema-sql "TABLE_SQL"

   Replace ``INTEGRATION_ID`` with the ID for your ``demo-kafka`` service and replace ``TABLE_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 2-8
      :language: sql

#. Run the following command to create another table named ``CPU_OUT_FILTER``:

   ::

      avn service flink table create demo-flink INTEGRATION_ID  \
          --table-name CPU_OUT_FILTER                           \
          --kafka-topic cpu_load_stats_real_filter              \
          --schema-sql "TABLE_SQL"

   Replace ``TABLE_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 11-14
      :language: sql

#. Run the following command to list the tables for the ``demo-flink`` service:

   ::

      avn service flink table list demo-flink

   The output for this command shows you the table IDs, which you need in the command that you use to create Flink jobs:

   ::

     INTEGRATION_ID                        TABLE_ID                              TABLE_NAME
     ====================================  ====================================  ==========
     917bbec0-0f34-4a31-b910-c585feb95d09  305c44d9-22d5-4be8-987f-57c7642e8a89  CPU_IN
     917bbec0-0f34-4a31-b910-c585feb95d09  3d33a7c5-3716-4b21-9739-f79228f9f28f  CPU_OUT_FILTER

#. Run the following command to create a job named ``simple_filter``:

   ::

      avn service flink job create demo-flink simple_filter     \
          --table-ids TABLE_ID_1 TABLE_ID_2                     \
          --statement "JOB_SQL"

   Replace the ``TABLE_ID_`` entries with the IDs for the ``CPU_IN`` and ``CPU_OUT_FILTER`` tables, and ``JOB_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 17-24
      :language: sql


Create a pipeline with windowing
--------------------------------
   
This setup uses aggregation to determine instances of high CPU load during set intervals.

1. Using the Aiven CLI, run the following command to create a Kafka table named ``CPU_OUT_AGG``:

   ::

      avn service flink table create demo-flink INTEGRATION_ID  \
          --table-name CPU_OUT_AGG                              \
          --kafka-topic cpu_load_stats_agg                      \
          --schema-sql "TABLE_SQL"

   Replace ``INTEGRATION_ID`` with the ID for your ``demo-kafka`` service and replace ``TABLE_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 27-32
      :language: sql

#. Run the following command to list the tables for the ``demo-flink`` service and get the IDs for the ``CPU_IN`` and ``CPU_OUT_AGG`` tables:

   ::

      avn service flink table list demo-flink

#. Run the following command to create a job named ``simple_agg``:

   ::

      avn service flink job create demo-flink simple_agg        \
          --table-ids TABLE_ID_1 TABLE_ID_2                     \
          --statement "JOB_SQL"

   Replace the ``TABLE_ID_`` entries with the IDs for the ``CPU_IN`` and ``CPU_OUT_AGG`` tables, and ``JOB_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 35-49
      :language: sql


Create a Flink SQL job using PostgreSQL thresholds
--------------------------------------------------

This setup uses host-specific thresholds that are stored in PostgreSQL as a basis for determining instances of high CPU load.

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

#. Run the following command to create a PostgreSQL table named ``SOURCE_THRESHOLDS``:

   ::

      avn service flink table create demo-flink INTEGRATION_ID  \
          --table-name SOURCE_THRESHOLDS                        \
          --jdbc-table cpu_thresholds                           \
          --schema-sql "TABLE_SQL"

   Replace ``INTEGRATION_ID`` with the ID for your ``demo-postgresql`` service and replace ``TABLE_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 57-59
      :language: sql

#. Run the following command to create a Kafka table named ``CPU_OUT_FILTER_PG``:

   ::

      avn service flink table create demo-flink INTEGRATION_ID  \
          --table-name CPU_OUT_FILTER_PG                        \
          --kafka-topic cpu_load_stats_real_filter_pg           \
          --schema-sql "TABLE_SQL"

   Replace ``INTEGRATION_ID`` with the ID for your ``demo-kafka`` service and replace ``TABLE_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 62-66
      :language: sql

#. Run the following command to list the tables for the ``demo-flink`` service and get the IDs for the ``CPU_IN``, ``CPU_OUT_FILTER_PG``, and ``SOURCE_THRESHOLDS`` tables:

   ::

      avn service flink table list demo-flink

#. Run the following command to create a job named ``simple_filter_pg``:

   ::

      avn service flink job create demo-flink simple_filter_pg  \
          --table-ids TABLE_ID_1 TABLE_ID_2 TABLE_ID_3          \
          --statement "JOB_SQL"

   Replace the ``TABLE_ID_`` entries with the IDs for the ``CPU_IN``, ``CPU_OUT_FILTER_PG``, and ``SOURCE_THRESHOLDS`` tables, and ``JOB_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 69-77
      :language: sql


Create an aggregated data pipeline with Kafka and PostgreSQL
------------------------------------------------------------

This setup highlights the instances where the average CPU load over a windowed interval exceeds the threshold and stores the results in PostgreSQL.

1. In the Aiven CLI, run the following command to connect to the ``demo-postgresql`` service:
   
   ::
	  
      avn service cli demo-postgresql --project PROJECT_NAME
   
#. Enter the following command to set up the PostgreSQL table for storing the results:
   
   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 80-83
      :language: sql
   
#. Run the following command to create a PostgreSQL table named ``CPU_OUT_AGG_PG``:

   ::

      avn service flink table create demo-flink INTEGRATION_ID  \
          --table-name CPU_OUT_AGG_PG                           \
          --jdbc-table cpu_load_stats_agg_pg                    \
          --schema-sql "TABLE_SQL"

   Replace ``INTEGRATION_ID`` with the ID for your ``demo-postgresql`` service and replace ``TABLE_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 86-87
      :language: sql

#. Run the following command to list the tables for the ``demo-flink`` service and get the IDs for the ``CPU_IN``, ``CPU_OUT_AGG_PG``, and ``SOURCE_THRESHOLDS`` tables:

   ::

      avn service flink table list demo-flink

#. Run the following command to create a job named ``simple_filter_pg_agg``:

   ::

      avn service flink job create demo-flink simple_filter_pg_agg  \
          --table-ids TABLE_ID_1 TABLE_ID_2 TABLE_ID_3              \
          --statement "JOB_SQL"

   Replace the ``TABLE_ID_`` entries with the IDs for the ``CPU_IN``, ``CPU_OUT_AGG_PG``, and ``SOURCE_THRESHOLDS`` tables, and ``JOB_SQL`` with the following:

   .. literalinclude:: /code/products/flink/alerting_solution_sql.md
      :lines: 91-124
      :language: sql


