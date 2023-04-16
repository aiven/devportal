Aiven for Apache Flink® quickstart guide 
===============================================

The first step in using Aiven for Apache Flink® is to create a service. You can do this in the `Aiven web console <https://console.aiven.io/>`_ or with the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

This quickstart section provides you with the information you need to get started with Aiven for Apache Flink and build data pipelines to stream to analyze your data. Learn how to set up and configure Aiven for Flink, connect to your desired data sources, and start processing and analyzing your data in real-time.


Create an Aiven for Apache Flink® service 
------------------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new Aiven for Apache Flink service.

   Once the service is ready, the status changes to *Running*. Depending on your selected cloud provider and region, this generally takes a couple of minutes.

Create data service integration
--------------------------------
Aiven for Apache Flink® allows you to build data pipelines that stream across different services. It currently supports integration with Aiven for Apache Kafka®, Aiven for PostgreSQL®, and Aiven for OpenSearch® as sources and targets for Flink applications.

To create your first data service integration: 

1. Open your Aiven for Apache Flink. 
2. In the **Overview** tab, click the **Get Started** button.
3. Choose the service you wish to integrate: Aiven for Apache Kafka®, Aiven for PostgreSQL®, or Aiven for OpenSearch®.
4. Click the **Integrate** button to complete the integration process.

For detailed steps, see :doc:`Create Apache Flink® data service integrations <howto/create-integration>`. 

Create Aiven for Apache Flink® application
-------------------------------------------

An :doc:`Aiven for Apache Flink® application<concepts/flink-applications>` is an abstraction layer on top of Apache Flink SQL that includes all the elements related to a Flink job to help build your data processing pipeline. 

Applications are the starting point for running an Apache Flink job within the Aiven managed service and contains the definition of source and sink tables, data processing logic, deployment parameters, and other necessary metadata.

For information on creating Flink applications and integrating data services, see :doc:`Create an Aiven for Apache Flink® application <howto/create-flink-applications>` and :doc:`Create Apache Flink® data service integrations<howto/create-integration>` sections.


Next steps
----------

* Create source and sink data tables to map the data for :doc:`Apache Kafka® <howto/connect-kafka>`,  :doc:`PostgreSQL® <howto/connect-pg>` or :doc:`OpenSearch® <howto/connect-opensearch>` services
* For details on using the Aiven CLI to create and manage Aiven for Apache Flink® services, see the :doc:`Aiven CLI documentation </docs/tools/cli>` and the :doc:`Flink-specific command reference </docs/tools/cli/service/flink>`

