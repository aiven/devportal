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

The tutorial showcases how to create an Apache Kafka® source topic that provides a stream of IoT metrics data, a PostgreSQL® database that contains data on the alerting thresholds, and an Apache Flink® service that combines these two services and pushes the filtered data to a separate Apache Kafka® topic, PostgreSQL® table or OpenSearch® index.

.. mermaid::

    graph LR;

        id1(Kafka)-- IoT metrics stream -->id3(Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-. filtered data .->id4(Kafka);
        id3-. filtered/aggregated data .->id5(Kafka);
        id3-. filtered/aggregated data .->id6(OpenSearch);
        id3-. filtered data .->id7(Slack);

Prerequisites
-------------

The tutorial uses all Aiven services, therefore you'll need a valid `Aiven account <https://console.aiven.io/signup>`_. The tutorial has also three external dependencies:

* Docker, needed for the `fake data generator for Apache Kafka <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_  is the only dependency. Check out the `related installation instructions <https://docs.docker.com/engine/install/>`_.
* Slack Token: the output of a data pipeline sends out notifications to a slack channel, check out the needed steps to retrieve a `Slack authentication token <https://github.com/aiven/slack-connector-for-apache-flink>`_
* `psql <https://www.postgresql.org/docs/current/app-psql.html>`_ a terminal based tool to interact with PostgreSQL

.. button-link:: anomaly-detection/create-services
    :align: right
    :color: primary
    :outline:

Create the Aiven services
-------------------------

This section of the tutorial will showcase how to create the needed Aiven services via the `Aiven Console <https://console.aiven.io/>`_. We'll create three services:

* An :doc:`Aiven for Apache Kafka®</docs/products/kafka>` named ``demo-kafka`` for data streaming
* An :doc:`Aiven for Apache Flink®</docs/products/flink>` named ``demo-flink`` for streaming data transformation
* An :doc:`Aiven for PostgreSQL®</docs/products/postgresql>` named ``demo-postgresql`` for data storage and query

.. mermaid::

    graph LR;

        id1(Kafka)-- IoT metrics stream -->id3(Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-. curated data .->id1(Kafka);

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

   This opens a new page with the available service options.

   .. image:: /images/platform/concepts/console_create_service.png
      :alt: Aiven Console view for creating a new service

3. Select **PostgreSQL®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `hobbyist` as service plan.

5. Enter ``demo-posgresql`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console

Create an Aiven for Apache Flink service
'''''''''''''''''''''''''''''''''''''''''

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

   This opens a new page with the available service options.

   .. image:: /images/platform/concepts/console_create_service.png
      :alt: Aiven Console view for creating a new service

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
5. Select **Aiven for PostgreSQL®** and then select the ``demo-postgresql`` service.
6. Click **Integrate**.
7. Click the **+** icon under *Data Flow*.
