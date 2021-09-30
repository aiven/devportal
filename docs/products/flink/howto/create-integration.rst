Create Flink integrations
===================================

Apache Flink can create streaming data pipelines across services. 

Currently Aiven for Flink supports Aiven for Apache Kafka and Aiven for PostgreSQL as source and target for Flink jobs.

Create a Flink integration
--------------------------

The integration between Flink and other Aiven services can be created using :doc:`the Aiven cli</docs/tools/cli>` and the Aiven console.

Create a Flink integration via Aiven CLI
''''''''''''''''''''''''''''''''''''''''

To create a Flink integration via Aiven CLI, you can use the `avn service integration-create` command.

**Example:** Create an integration between an Aiven for Flink cluster named ``flink-demo`` and an Aiven for Kafka cluster named ``kafka-demo``.

::

  avn service integration-create    \
    --project test                  \
    -t flink                        \
    -s kafka-demo                   \
    -d flink-demo

The integration id, required for the following steps can be fetched with::

    avn service integration-list --project test flink-demo


Create a Flink integration via Aiven console
''''''''''''''''''''''''''''''''''''''''''''

To create a Aiven for Apache Flink integration via Aiven console:

1. Navigate to the Aiven for Apache Flink service page
2. If you're setting up the first integration for the selected Aiven for Apache Flink service,  click on the **Get Started** button available under the **Overview** tab.

.. image:: /images/products/flink/integrations-get-started.png
  :scale: 50 %
  :alt: Image of the Aiven for Apache Flink Overview page with focus on the Get Started Icon

3. Select the Aiven for Apache Kafka or Aiven for PostgreSQL service to integrate, and click on the **Integrate** button

.. image:: /images/products/flink/integrations-select-services.png
   :scale: 50 %
   :alt: Image of the Aiven for Apache Flink Integration page showing an Aiven for Apache Kafka and an Aiven for PostgreSQL services 

4. Additional integrations can be added using the *+* button in the **Data Flow** section

.. image:: /images/products/flink/integrations-add.png
   :scale: 50 %
   :alt: Image of the Aiven for Apache Flink Integration page showing an existing Aiven for Apache Kafka integration and the + icon to add additional integrations





