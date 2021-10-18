Create a real-time alerting solution - Aiven console
====================================================

This tutorial shows you an example of how to combine Aiven for Apache Flink with Aiven for Apache Kafka and Aiven for PostgreSQL services to create a solution that provides real-time alerting data for CPU loads.

The article includes the steps that you need when using the `Aiven web console <https://console.aiven.io>`_ along with a few different samples of how you can set thresholds for alerts. For connecting to your PostgreSQL service, this example uses the `Aiven CLI <https://github.com/aiven/aiven-client>`_, but you can also use other tools if you prefer.

In addition, the instructions show you how to use a separate Python tool,`Apache Kafka Python fake data producer <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_, to create sample records for your Apache Kafka topic that provides the streamed data.


Set up Aiven services
---------------------

1. Follow the steps in :doc:`this article </docs/platform/howto/create_new_service>` to create these services:

   - An Aiven for Apache Kafka service with the *Business-4* service plan (this streams the CPU load)
   - An Aiven for PostgreSQL service with the *Business-4* service plan (this defines the alerting threshold values)
   - An Aiven for Apache Flink service with the *Business-4* service plan (this analyzes the data stream to find CPUs where the average load exceeds the threshold values)

#. Select the Aiven for Apache Kafka service that you created and change the following settings on the *Overview* page:

   - **Kafka REST API (Karapace)** > **Enable**
   - **Kafka Connect** > **Enable**
   - **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

#. On the *Overview page*, click **Download** next to *Access Key*, *Access Certificate*, and *CA Certificate*, then copy the three downloaded files to a folder on your computer.

   You need these files when running the tool that creates the sample records.

#. Copy the *Host* value on the *Overview* page of your Kafka service.

#. Select the Aiven for Apache Flink service that you created and add the service integrations:

   a. Click **Get started** on the banner at the top of the *Overview* page.
   b. Select **Aiven for Apache Kafka** and then select the Kafka service that you created earlier.
   c. Click **Integrate**.
   d. Click the **+** icon under *Data Flow*.
   e. Select **Aiven for PostgreSQL** and then select the PostgreSQL service that you created earlier.
   f. Click **Integrate**.


Set up sample data
------------------

Run the following Python command to create the sample records using the `Apache Kafka Python fake data producer <https://github.com/aiven/python-fake-data-producer-for-apache-kafka>`_ tool:

::

    python3 python-fake-data-producer-for-apache-kafka/metricproducer.py \
        --cert-folder $downloaded_certificate_folder \
        --host $kafka_host_address \
        --port 12693 \
        --topic-name cpu_load_stats_real \
        --nr-messages 0 \
        --max-waiting-time 1


Replace ``$downloaded_certificate_folder`` with the folder that contains the three certificate files that you downloaded, and ``$kafka_host_address`` with the address for your Aiven for Apache Kafka service.

This command pushes the following type of events to the ``cpu_load_stats_real`` topic in your Kafka service:

::
   
    {"hostname": "dopey", "cpu": "cpu4", "usage": 98.3335306302198, "occurred_at": 1633956789277}
    {"hostname": "sleepy", "cpu": "cpu2", "usage": 87.28240549074823, "occurred_at": 1633956783483}
    {"hostname": "sleepy", "cpu": "cpu1", "usage": 85.3384018012967, "occurred_at": 1633956788484}
    {"hostname": "sneezy", "cpu": "cpu1", "usage": 89.11518629380006, "occurred_at": 1633956781891}
    {"hostname": "sneezy", "cpu": "cpu2", "usage": 89.69951046388306, "occurred_at": 1633956788294}



Create Apache Flink tables and jobs
-----------------------------------

1. In the Aiven web console, select the **Jobs & Data** tab in your Aiven for Apache Flink service.

#. Create a pipeline for basic filtering.

   This setup uses a fixed threshold to filter any instances of high CPU load to a separate Kafka topic.
   
   a. Go to the **Data Tables** subtab.
   b. Select your Kafka service, enter ``CPU_IN`` as the name, select ``cpu_load_stats_real`` as the topic, and enter the following as the SQL schema, then click **Create Table**:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 2-8
         :language: sql


   c. Create another table by entering ``CPU_OUT_FILTER`` as the name, ``cpu_load_stats_real_filter`` as the topic, and the following as the SQL schema, then click **Create Table**:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 11-14
         :language: sql


   d. Go to the **Create SQL Job** subtab and enter ``simple_filter`` as the job name, select ``CPU_IN`` and ``CPU_OUT_FILTER`` as the tables, and enter the following as the SQL statement, then click **Execute job**:

      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 17
         :language: sql


#. Create a pipeline with windowing.
   
   This setup uses aggregation to determine instances of high CPU load during set intervals.
   
   a. Go to the **Data Tables** subtab.
   b. Select your Kafka service, enter ``CPU_OUT_AGG`` as the name, ``cpu_load_stats_agg`` as the topic, and the following as the SQL schema, then click **Create Table**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 20-26
         :language: sql
		 
   c. Go to the **Create SQL Job** subtab and enter ``simple_agg`` as the job name, select ``CPU_OUT_AGG`` and ``CPU_IN`` as the tables, and enter the following as the SQL statement, then click **Execute job**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 29-32
         :language: sql


#. Configure your PostgreSQL service to set the threshold values.

   This setup uses host-specific thresholds that are stored in PostgreSQL as a basis for determining instances of high CPU load.

   a. In the Aiven CLI, run the following command to connect to the PostgreSQL service that you created earlier:
   
      ::
	  
         avn service cli $postgresql_service_name --project $project_name
   
   b. Enter the following commands to set up the threshold values:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 35-36
         :language: sql
   
   c. In the Aiven web console, go to the **Jobs & Data** > **Data Tables** tab for your Flink service.
   d. Select your PostgreSQL service, enter ``SOURCE_THRESHOLDS`` as the name, select ``public.cpu_thresholds`` as the table, and enter the following as the SQL schema, then click **Create Table**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 39-41
         :language: sql

   e. Select your Kafka service, enter ``CPU_OUT_FILTER_PG`` as the name, ``cpu_load_stats_real_filter_pg`` as the topic, and the following as the SQL schema, then click **Create Table**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 44-48
         :language: sql

   f. Go to the **Create SQL Job** subtab, enter ``simple_filter_pg`` as the name, select the ``CPU_OUT_FILTER_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables, and enter the following as the SQL schema, then click **Execute job**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 51
         :language: sql
		 

#. Combine windowing with threshold values from PostgreSQL and store the results in PostgreSQL.

   This setup highlights the instances where the average CPU load over a windowed interval exceeds the threshold and stores the results in PostgreSQL.

   a. In the Aiven CLI, run the following command to connect to the PostgreSQL service that you created earlier:
   
      ::
	  
         avn service cli $postgresql_service_name --project $project_name
   
   b. Enter the following command to set up the table for storing the results:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 54
         :language: sql
   
   c. In the Aiven web console, go to the **Jobs & Data** > **Data Tables** tab for your Flink service.
   
   d. Select your PostgreSQL service, enter ``CPU_OUT_AGG_PG`` as the name, select ``cpu_load_stats_agg_pg`` as the table, and enter the following as the SQL schema, then click **Create Table**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 57-59
         :language: sql

   e. Go to the **Create SQL Job** subtab, enter ``simple_filter_pg_agg`` as the name, select the ``CPU_OUT_AGG_PG``, ``CPU_IN``, and ``SOURCE_THRESHOLDS`` tables, and enter the following as the SQL schema, then click **Execute job**:
   
      .. literalinclude:: /code/products/flink/alerting_solution_sql.md
         :lines: 62-73
         :language: sql


