Apache Kafka® REST proxy authorization
======================================
The Apache Kafka® REST proxy authorization, when :doc:`enabled </docs/products/kafka/karapace/howto/enable-karapace>` on your Aiven for Apache Kafka® service, allows the delegation of user authentication and authorization to Apache Kafka. Karapace will forward the HTTP basic authentication credentials to Apache Kafka, and Apache Kafka then performs the authentication and authorization based on the :doc:`ACLs</docs/products/kafka/concepts/acl>`. 

Apache Kafka® REST proxy authorization is **disabled** by default on all Aiven for Apache Kafka® services.

.. seealso:: 

    * :doc:`Enable OAuth2/OIDC support for Apache Kafka® REST proxy </docs/products/kafka/karapace/howto/enable-oauth-oidc-kafka-rest-proxy>`
    *  :doc:`Manage Apache Kafka® REST proxy authorization </docs/products/kafka/karapace/howto/manage-kafka-rest-proxy-authorization>` 

 