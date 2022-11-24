Enable Apache Kafka® REST proxy authorization
=============================================

Aiven for Apache Kafka® services have :doc:`Apache Kafka® REST proxy authorization </docs/products/kafka/karapace/concepts/kafka-rest-authorization>` disabled by default. To enable or disable this functionality using the Aiven CLI, follow these steps:

1. To enable Apache Kafka REST proxy authorization for a service, replace the ``SERVICE_NAME`` placeholder with the name of the Aiven for Apache Kafka® service in the Aiven CLI::

    avn service update -c kafka_rest_authorization=True SERVICE_NAME

2. You can similarly disable the Apache Kafka® REST proxy authorization using::

    avn service update -c kafka_rest_authorization=False SERVICE_NAME

.. warning:: 
    Enabling Karapace schema registry authorization can disrupt access for users if the Kafka access control rules have not been configured to allow this. For more information, see :doc:`Manage Karapace Kafka REST authorization <../howto/manage-kafka-rest-authorization>`.
