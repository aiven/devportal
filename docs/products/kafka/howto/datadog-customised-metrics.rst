Configure Apache Kafka® metrics sent to Datadog
-----------------------------------------------

When creating a :doc:`Datadog service integration </docs/integrations/datadog/datadog-metrics>`, you can customise which metrics are sent to the Datadog endpoint using the :doc:`Aiven CLI </docs/tools/cli>`.

For each Apache Kafka® topic and partition, the following metrics are currently supported:

* ``kafka.log.log_size``
* ``kafka.log.log_start_offset``
* ``kafka.log.log_end_offset``

.. Tip::

    All the above metrics are tagged with ``topic`` and ``partition`` allowing you to monitor each topic and partition independently.

Variables
---------

These are the placeholders you will need to replace in the code samples. 

==================     ============================================================================
Variable               Description
==================     ============================================================================
``SERVICE_NAME``       Aiven for Apache Kafka® service name
------------------     ----------------------------------------------------------------------------
``INTEGRATION_ID``     ID of the integration between the Aiven for Apache Kafka service and Datadog
==================     ============================================================================

.. Tip::
    
    The ``INTEGRATION_ID`` parameter can be found by issuing::
        
        avn service integration-list SERVICE_NAME

Customise Apache Kafka® metrics sent to Datadog
-----------------------------------------------

Before customising the metrics, make sure that you have a Datadog endpoint configured and enabled in your Aiven for Apache Kafka service. For details on how to set up the Datadog integration, check the :doc:`dedicated article </docs/integrations/datadog/datadog-metrics>`.

To customise the metrics sent to Datadog, you can use the ``service integration-update`` passing the following customised parameters:

* ``kafka_custom_metrics``: defining the comma separated list of custom metrics to include (within ``kafka.log.log_size``, ``kafka.log.log_start_offset`` and ``kafka.log.log_end_offset``)
* ``include_topics``: defining the comma separated list of topics to include

.. Tip:: 

    By default all topics are included

* ``exclude_topics``: defining the comma separated list of topics to exclude
* ``include_consumer_groups``: defining the comma separated list of consumer groups to include
* ``exclude_consumer_groups``: defining the comma separated list of consumer groups to include


As example to sent the ``kafka.log.log_size`` and ``kafka.log.log_end_offset`` metrics for ``topic1`` and ``topic2`` execute the following code::

    avn service integration-update                                          \
        -c kafka_custom_metrics=kafka.log.log_size,kafka.log.log_end_offset \
        -c include_topics=topic1,topic2                                     \
        INTEGRATION_ID

Once the update is successful and metrics have been collected and pushed, you should see them in your Datadog explorer.

