Integrate Aiven for Apache Flink® with Apache Kafka® 
=====================================================
Integrating external/self-hosted Apache Kafka® with Aiven for Apache Flink® allows users to leverage the power of both technologies to build scalable and robust real-time streaming applications. 

This section provides instructions on integrating external/self-hosted Apache Kafka with Aiven for Apache Flink® using :doc:`Aiven client </docs/tools/cli>` and `Aiven Console <https://console.aiven.io/>`_. 

Prerequisites
---------------
* Aiven for Apache Flink service 
* External/self-hosted Apache Kafka service

Configure integration using CLI
---------------------------------

To configure integration using Aiven CLI, follow these steps: 

Step 1. Create a Aiven for Apache Flink service
`````````````````````````````````````````````````
Use the following command to create an Aiven for Apache Flink service: 

.. code:: 

    avn service create -t flink -p <project-name> --cloud <cloud-name> <flink-service-name>

where: 

* ``-t flink``: The type of service to create, which is Aiven for Apache Flink.
* ``-p <project-name>``: The name of the Aiven project where the service should be created.
* ``cloud <cloud-name>``: The name of the cloud provider on which the service should be created.
* ``<flink-service-name>``: The name of the new Aiven for Apache Flink service to be created. This name must be unique within the specified project.


Step 2: Setup an Apache Kafka service for the integration
`````````````````````````````````````````````````````````````````````
If you currently have a self-hosted or external Apache Kafka instance, you have the choice of either using it to integrate with the Aiven for Apache Flink service or creating a new Apache Kafka service using your preferred method.

Step 3: Download Apache Kafka certificate
```````````````````````````````````````````
Download the necessary Apache Kafka credentials certificate using your preferred method and save it in a secure yet easily accessible location on your system.

Step 4: Create an external Apache Kafka endpoint
`````````````````````````````````````````````````
To integrate external Apache Kafka with Aiven for Apache Flink, you need to create an external Apache Kafka endpoint. You can use the :ref:`avn service integration-endpoint-create <avn_service_integration_endpoint_create>` command with the required parameters. This command will create a new integration endpoint that can be used to connect to an external Apache Kafka service. 

The available security protocols for Kafka are PLAINTEXT, SSL, SASL_PLAINTEXT, and SASL_SSL. 

PLAINTEXT
''''''''''''''''

To create a PLAINTEXT protocol type endpoint, use the following command:

.. code:: 

    avn service integration-endpoint-create 
        --endpoint-name demo-ext-kafka 
        --endpoint-type external_kafka  
        --user-config-json  '{"bootstrap_servers":"servertest:123","security_protocol":"PLAINTEXT"}'

Where : 

* ``--endpoint-name``: Name of the endpoint you want to create.
* ``--endpoint-type``: The type of endpoint, which should be ``external_kafka``.
* ``--user-config-json``: The configuration for the endpoint in JSON format, which includes the following attributes:

  - ``bootstrap_servers``: List of Apache Kafka broker addresses and ports to connect to.
  - ``security_protocol``: Security protocol to use for the connection. In this example, it's set to **PLAINTEXT**.

SSL
''''
To create an SSL protocol type endpoint, use the following command:

.. code:: 

    avn service integration-endpoint-create --endpoint-name demo-ext-kafka \
    --endpoint-type external_kafka  \
    --user-config-json  '{
        "bootstrap_servers": "10.0.0.1:9092,10.0.0.2:9092,10.0.0.3:9092",
        "security_protocol": "SSL",
        "ssl_ca_cert": ssl_cert,
        "ssl_client_cert": ssl_cert,
        "ssl_client_key": ssl_key,
        "ssl_endpoint_identification_algorithm":"https",
    }'

Where: 

* ``--endpoint-name``: Name of the endpoint you want to create.
* ``--endpoint-type``: The type of endpoint, which should be ``external_kafka``.
* ``--user-config-json``:The configuration for the endpoint in JSON format, which includes the following attributes:
   - ``bootstrap_servers``: List of Apache Kafka broker addresses and ports to connect to.
   - ``security_protocol``: The type of security protocol to use for the connection, which is ``SASL`` in this case.
   - ``ssl_ca_cert``: The path to the SSL CA certificate.
   - ``ssl_client_cert``: The path to the SSL client certificate.
   - ``ssl_client_key``: The path to the SSL client key.
   - ``ssl_endpoint_identification_algorithm``: The endpoint identification algorithm to use for SSL verification. For example, ``https``. 


SASL_PLAINTEXT
''''''''''''''''
To create a SASL_PLAINTEXT protocol type endpoint, use the following command:

.. code:: 

    avn service integration-endpoint-create --endpoint-name demo-ext-kafka \
    --endpoint-type external_kafka \
    --user-config-json '{
        "bootstrap_servers": "10.0.0.1:9092,10.0.0.2:9092,10.0.0.3:9092",
        "security_protocol": "SASL_PLAINTEXT",
        "sasl_mechanism": "PLAIN",
        "sasl_plain_username": sasl_username,
        "sasl_plain_password": sasl_password
    }'

where: 

* ``--endpoint-name``: Name of the endpoint you want to create.
* ``--endpoint-type``: The type of endpoint, which should be ``external_kafka``.
* ``--user-config-json``:The configuration for the endpoint in JSON format, which includes the following attributes: 
   - ``bootstrap_servers``: List of Apache Kafka broker addresses and ports to connect to.
   - ``security_protocol``: The type of security protocol to use for the connection, which is ``SASL_PLAINTEXT`` in this case.
   - ``sasl_mechanism``: The type of SASL mechanism to use for authentication, which is **PLAIN** in this case.
   - ``sasl_plain_username``: The username for SASL authentication.
   - ``sasl_plain_password``: The password for SASL authentication.
   - ``ssl_endpoint_identification_algorithm``: The endpoint identification algorithm to use for SSL verification. For example, ``https``. 


SASL_SSL
''''''''''
To create a SASL_SSL protocol type endpoint, use the following command:

.. code:: 

    avn service integration-endpoint-create --endpoint-name demo-ext-kafka \
    --endpoint-type external_kafka \
    --user-config-json '{
        "bootstrap_servers": "10.0.0.1:9092,10.0.0.2:9092,10.0.0.3:9092",
        "security_protocol": "SASL_SSL",
        "sasl_mechanism": "PLAIN",
        "sasl_plain_username": sasl_username,
        "sasl_plain_password": sasl_password,
        "ssl_ca_cert": ssl_cert,
        "ssl_endpoint_identification_algorithm": "https"
    }'

where: 

* ``--endpoint-name``: Name of the endpoint you want to create.
* ``--endpoint-type``: The type of endpoint, which should be ``external_kafka``.
* ``--user-config-json``:The configuration for the endpoint in JSON format, which includes the following attributes: 
   - ``bootstrap_servers``: List of Apache Kafka broker addresses and ports to connect to.
   - ``security_protocol``: The type of security protocol to use for the connection, which is ``SASL_SSL`` in this case.
   - ``sasl_mechanism``: The type of SASL mechanism to use for authentication, which is **PLAIN** in this case.
   - ``sasl_plain_username``: The username for SASL authentication.
   - ``sasl_plain_password``: The password for SASL authentication.
   - ``ssl_ca_cert``: The path to the SSL CA certificate downloaded for SSL authentication.
   - ``ssl_endpoint_identification_algorithm``: The endpoint identification algorithm to use for SSL verification. For example, ``https``. 

Step 5: Integrate Aiven for Apache Flink with endpoints
`````````````````````````````````````````````````````````
To integrate Aiven for Apache Flink with the integration endpoint for external Apache Kafka, use the following command:

.. code:: 

    avn service integration-create 
        --source-endpoint-id <source-endpoint-id> 
        --dest-service <flink-service-name> 
        -t flink_external_kafka

For example, 

.. code:: 

    avn service integration-create 
        --source-endpoint-id eb870a84-b91c-4fd7-bbbc-3ede5fafb9a2 
        --dest-service flink-1 
        -t flink_kafka

where: 

* ``--source-endpoint-id``: The ID of the integration endpoint you want to use as the source. In this case, it is the ID of the external Apache Kafka integration endpoint. In this example, the ID is ``eb870a84-b91c-4fd7-bbbc-3ede5fafb9a2``.
* ``--dest-service``: The name of the Aiven for Apache Flink service you want to integrate with the external Apache Kafka endpoint. In this example, the service name is ``flink-1``.
* ``-t``: The type of integration you want to create. In this case, the ``flink_external_kafka`` integration type is used to integrate Aiven for Apache Flink with an external Apache Kafka endpoint.

Step 6: Verify integration with service
``````````````````````````````````````````
After creating the integration between Aiven for Apache Flink and external/self-hosted Apache Kafka, the next step is to verify that the integration has been created successfully and create applications that use the integration. 

To verify that the integration has been created successfully, run the following command:

.. code:: 

    avn service integration-list --project <project-name> <flink-service-name>

For example: 

.. code:: 

    avn service integration-list --project systest-project flink-1

where: 

* ``--project``: The name of the Aiven project that contains the Aiven service you want to list integrations for. In this example, the project name is ``systest-project``.
* ``flink-1``: The name of the Aiven service you want to list integrations for. In this example, the service name is ``flink-1``, which is an Aiven for Apache Flink service.

To create Aiven for Apache Flink applications, you will need the integration ID of the Aiven for Apache Flink service. Obtain the ``integration_id`` from the integration list.

Step 7: Create Aiven for Apache Flink applications
````````````````````````````````````````````````````
With the integration ID obtained from the previous step, you can now create an application that uses the integration. For information on how to create Aiven for Apache Flink applications, see :ref:`avn service flink create-application <avn service flink create-application>`. 


Configure integration using Aiven Console
--------------------------------------------

If you have an external Apache Kafka service already running, you can integrate it with Aiven for Apache Flink using the `Aiven Console <https://console.aiven.io/>`_ by following these steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and choose your project. 
2. From the **Services** page, you can either :doc:`create a new Aiven for Apache Flink </docs/platform/howto/create_new_service>` service or select an existing service.
3. Next, configure an external Apache Kafka service integration endpoint:
  
   * Navigate to the Projects screen where all the services are listed. 
   * From the left sidebar, select **Integration endpoints**. 
   * Select **External Apache Kafka** from the list, and then select **Add new endpoint**. 
   * Enter an *Endpoint name* and the *Bootstrap servers*. Then, choose a *Security protocol* from the dropdown list and select **Create**.

4. Select **Services** from the left sidebar, and access the Aiven for Apache Flink service where you plan to integrate the external Apache Kafka endpoint.
5. If you're integrating with Aiven for Apache Flink for the first time, on the **Overview** page and select **Get Started**. Alternatively, you can add a new integration in the **Data Flow** section by using the plus (+) button.
6. On the **Data Service integrations** screen, select the **Create external integration endpoint** tab. 
7. Select the checkbox next to **Apache Kafka**, and choose the external Apache Kafka endpoint from the list to integrate.
8. Select **Integrate**.

Once you have completed these steps, the integration will be ready, and you can start creating :doc:`Aiven for Apache Flink applications </docs/products/flink/howto/create-flink-applications>` that use the external Apache Kafka service as either a source or sink.
