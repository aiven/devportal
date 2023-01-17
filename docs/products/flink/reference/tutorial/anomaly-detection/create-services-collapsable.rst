Create the Aiven services collapsable
=====================================

This section of the tutorial will showcase how to create the needed Aiven services via the `Aiven Console <https://console.aiven.io/>`_. We'll create three services:

* An :doc:`Aiven for Apache Kafka®</docs/products/kafka>` named ``demo-kafka`` for data streaming
* An :doc:`Aiven for Apache Flink®</docs/products/flink>` named ``demo-flink`` for streaming data transformation
* An :doc:`Aiven for PostgreSQL®</docs/products/postgresql>` named ``demo-postgresql`` for data storage and query

.. mermaid::

    graph LR;

        id1(Kafka)-- IoT metrics stream -->id3(Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-. curated data .->id1(Kafka);

.. dropdown:: Create an Aiven for Apache Kafka service

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

.. dropdown:: Customise the Aiven for Apache Kafka service


    After creating the service, you'll be redirected to the service details page. You can now customise the service to enable the needed components in the *Overview* tab:

    1. **Kafka REST API (Karapace)** > **Enable**

    .. Note:: 
        The **Kafka REST API** enables you to manage Apache Kafka via REST APIs and also to view the data in your Apache Kafka® topics.

    2. **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

    .. Note:: 
        The ``kafka.auto_create_topics_enable`` setting allows you to create new Apache Kafka® topics as you configure your Apache Flink® data tables, so that you do not need to create the topics in advance.

.. dropdown:: Create an Aiven for PostgreSQL service


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

.. dropdown:: Create an Aiven for Apache Flink service


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

.. dropdown:: Customise the Aiven for Apache Flink service


    After creating the service, you'll be redirected to the service details page. You can now customise the service to enable the needed integrations to the Aiven for Apache Kafka and Aiven for PostgreSQL services in the *Overview* tab:

    1. Click **Get started** on the banner at the top of the *Overview* page.
    2. Select **Aiven for Apache Kafka®** and then select the ``demo-kafka`` service.
    3. Click **Integrate**.
    4. Click the **+** icon under *Data Flow*.
    5. Select **Aiven for PostgreSQL®** and then select the ``demo-postgresql`` service.
    6. Click **Integrate**.
    7. Click the **+** icon under *Data Flow*.