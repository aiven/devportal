Enable Karapace schema registry authorization
=============================================

.. Tip:: Most Aiven for Apache Kafka® services will have :doc:`schema registry authorization</docs/products/kafka/concepts/schema-registry-authorization>` enabled automatically, but older services may pre-date this feature. For older services, follow these steps to enable the functionality.

Replace the ``SERVICE_NAME`` placeholder with the name of the Aiven for Apache Kafka® service that should have schema registry authorization enabled::

    avn service update --enable-schema-registry-authorization SERVICE_NAME

Karapace schema registry authorization can similarly be disabled (on older services only) using::

    avn service update --disable-schema-registry-authorization SERVICE_NAME

.. Note::

    Enabling Karapace schema registry authorization can disrupt access for users if the access control rules haven't been configured to allow this.

Read the article about :doc:`managing access control</docs/products/kafka/howto/manage-schema-registry-authorization>` to configure the appropriate access for your users.
