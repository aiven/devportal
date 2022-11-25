Apache Kafka® REST proxy authorization
======================================
The Apache Kafka® REST proxy authorization, when :doc:`enabled <../howto/enable-karapace>` on your Aiven for Apache Kafka® service, allows the delegation of user authentication and authorization to Kafka. Karapace will forward the HTTP basic authentication credentials to Apache Kafka®, and Apache Kafka then performs the authentication and authorization based on the :doc:`ACLs</docs/products/kafka/concepts/acl>`. 

Apache Kafka® REST proxy authorization is **disabled** by default on all Aiven for Apache Kafka® services.

.. seealso:: 

    * :doc:`Enable Apache Kafka® REST proxy authorization via Aiven CLI </docs/products/kafka/karapace/howto/enable-kafka-rest-proxy-authorization>`
    *  :doc:`Manage Apache Kafka® REST proxy authorization <../howto/manage-kafka-rest-proxy-authorization>` 

 