Create a Google Cloud Storage sink connector
============================================

The Apache Kafka Connect® Google Cloud Storage (GCS) sink connector by Aiven enables you to move data from an Aiven for Apache Kafka® cluster to a Google Cloud Storage bucket for long term storage. The full connector documentation is available in the dedicated `GitHub repository <https://github.com/aiven/aiven-kafka-connect-gcs>`_.



Prerequisites
-------------

To setup the Google Cloud Storage sink connector by Aiven, you need an Aiven for Apache Kafka® service :doc:`with Apache Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to follow the steps :doc:`to prepare the GCP account and GCS sink <gcs-sink-prereq>` and collect the following information about the target GCS bucket upfront:

* ``GCS_NAME``: The name of the GCS bucket
* ``GCS_CREDENTIALS``: The Google service account JSON service key :ref:`created during the prerequisit phase <gcs-sink-connector-google-account>`

.. Warning::

    The GCS sink connector accepts the ``GCS_CREDENTIALS`` JSON service key as string, therefore all  ``"`` symbols within it must be escaped ``\"``.

    The ``GCS_CREDENTIALS`` parameter should be in the format ``{\"type\": \"service_account\",\"project_id\": \"XXXXXX\", ...}``


Setup an GCS sink connector with Aiven Console
----------------------------------------------

The following example demonstrates how to setup an Apache Kafka Connect® GCS sink connector using the `Aiven Console <https://console.aiven.io/>`_.

Define an Apache Kafka Connect® configuration file
''''''''''''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``gcs_sink.json``) with the following content:

::

    {
        "name": "my-gcs-connector",
        "connector.class": "io.aiven.kafka.connect.gcs.GcsSinkConnector",
        "tasks.max": "1",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "topics": "TOPIC_NAME",
        "gcs.credentials.json": "GCS_CREDENTIALS",
        "gcs.bucket.name": "GCS_NAME",
        "file.name.prefix": "my-custom-prefix/",
        "file.compression.type": "gzip",
        "format.output.type": "jsonl",
        "format.output.fields": "value,offset"
    }

The configuration file contains the following entries:

* ``name``: The connector name
* ``topics``: The list of Apache Kafka® topics to sink to the GCS bucket
* ``key.converter`` and ``value.converter``: Data converters, depending on the topic data format. Check the `GitHub repository documentation <https://github.com/aiven/gcs-connector-for-apache-kafka>`_ for more information
* ``gcs.credentials.json``: The Google service account JSON service key as JSON string
* ``gcs.bucket.name``: The name of the GCS bucket
* ``file.name.prefix``: The file name prefix
* ``file.compression.type``: The type of compression to use when creating the file
* ``format.output.type``: The format used to store the message values
* ``format.output.fields``: The message fields to be included in the target file

.. Tip::

    You can define GCS sink connector naming and data formats by setting the :doc:`dedicated parameters <../reference/gcs-sink-formats>`.


Check out the `GitHub repository parameters documentation <https://github.com/aiven/gcs-connector-for-apache-kafka>`_ for the full list of configuration options.


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Google Cloud Storage sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``gcs_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target GCS bucket

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.


Example: define a GCS sink connector
------------------------------------

The example creates an GCS sink connector with the following properties:

* connector name: ``my_gcs_sink``
* source topics: ``test``
* target GCS bucket name: ``my-test-bucket``
* target Google service key: ``{\"type\": \"service_account\",   \"project_id\": \XXXXXXXXX\", ..}``
* name prefix: ``my-custom-prefix/``
* data compression: ``gzip``
* message data format: ``jsonl``
* fields to include in the message: ``value, offset``
* number of messages per file: 1

The connector configuration is the following:

::

    {
        "name": "my_gcs_sink",
        "connector.class": "io.aiven.kafka.connect.gcs.GcsSinkConnector",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "topics": "test",
        "gcs.credentials.json": "{\"type\": \"service_account\",   \"project_id\": \XXXXXXXXX\", ..}",
        "gcs.bucket.name": "my-test-bucket",
        "file.name.prefix": "my-custom-prefix/",
        "file.compression.type": "gzip",
        "file.max.records": "1",
        "format.output.type": "jsonl",
        "format.output.fields": "value,offset"
    }
