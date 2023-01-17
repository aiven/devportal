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

    All the Apache Flink data transformations defined in the tutorial, are fully compatible with the open-source Apache Flink. We're going to use Aiven for Apache Flink to avoid any network and integration complexities. 

The tutorial is divided into several sections:

* :doc:`Create the Aiven services <anomaly-detection/create-aiven-services>` provides the steps to create the needed Aiven for Apache Kafka and Aiven for Apache Flink
* :doc:`Create the Aiven token and start the fake IoT data generator <>` starts a continous flow of data towards an Aiven for Apache Kafka topic
* :doc:`Create a filtering data pipeline <>` showcases an Apache Flink SQL to filter the dataset
* :doc:`Create an aggregation data pipeline <>` provides an example of time bounded aggregation
* :doc:`Create a Slack notification data pipeline <>` showcases how to send notifications using the Slack integration

Architecture overview
---------------------

The tutorial showcases how to create an Apache Kafka® source topic that provides a stream of IoT metrics data, a PostgreSQL® database that contains data on the alerting thresholds, and an Apache Flink® service that combines these two services and pushes the filtered data to a separate Apache Kafka® topic, PostgreSQL® table or OpenSearch® index.

.. mermaid::

    graph LR;

        id1(Kafka)-- IoT metrics stream -->id3(Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-. filtered data .->id4(Kafka);
        id3-. filtered/aggregated data .->id5(Kafka);
        id3-. filtered data .->id6(Slack);

Prerequisites
-------------

The tutorial uses all Aiven services, therefore you'll need a valid `Aiven account <https://console.aiven.io/signup>`_. The tutorial has also three external dependencies:

* Docker, needed for the `fake data generator for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_  is the only dependancy. Check out the `related installation instructions <https://docs.docker.com/engine/install/>`_.
* Slack Token: the output of a data pipeline sends out notifications to a slack channel, check out the needed steps to retrieve a `Slack authentication token <https://github.com/aiven/slack-connector-for-apache-flink#set-up-slack-application>`_
* `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ a terminal based tool to interact with PostgreSQL

.. button-link:: anomaly-detection/create-services.html
    :align: right
    :color: primary
    :outline:

    Start the tutorial
