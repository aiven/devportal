Enable Karapace schema registry authorization
=============================================

Most Aiven for Apache Kafka® services will automatically have :doc:`schema registry authorization </docs/products/kafka/karapace/concepts/schema-registry-authorization>` enabled. However, some older services may pre-date this feature. To enable or disable this functionality on older services, follow these steps: 

1. To enable schema registry authorization for a service, replace the ``SERVICE_NAME`` placeholder with the name of the Aiven for Apache Kafka® service in the Aiven CLI:: 

    avn service update --enable-schema-registry-authorization SERVICE_NAME

2. You can similarly disable the Karapace schema registry authorization using::

    avn service update --disable-schema-registry-authorization SERVICE_NAME

.. warning:: 
    Enabling Karapace schema registry authorization can disrupt access for users if the access control rules have not been configured to allow this. For more information, see :doc:`Manage Karapace schema registry authorization <../howto/manage-schema-registry-authorization>`.
