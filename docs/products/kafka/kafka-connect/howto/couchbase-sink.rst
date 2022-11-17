Create a Couchbase sink connector
==============================================

The `Couchbase <https://www.couchbase.com/>`_ sink connector pushes Apache Kafka® data to the NoSQL database.

.. note::

    You can check the full set of available parameters and configuration options in the `connector's documentation <https://github.com/couchbase/kafka-connect-couchbase>`_.

.. _connect_couchbase_sink_prereq:

Prerequisites
-------------

To setup a `Couchbase <https://www.couchbase.com/>`_ sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the sink Couchbase database upfront:

* ``COUCHBASE_SEED_NODES``: The database seed nodes
* ``COUCHBASE_USER``: The database user to connect
* ``COUCHBASE_PASSWORD``: The database password for the ``COUCHBASE_USER``
* ``COUCHBASE_BUCKET``: The bucket where to land the data
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for Apache Kafka®,  the Kafka related details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

Setup a Couchbase sink connector with Aiven Console
------------------------------------------------------------

The following example demonstrates how to setup a Couchbase sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``couchbase-sink.json``) with the following content. Creating a file is not strictly necessary but allows to have all the information in one place before copy/pasting them in the `Aiven Console <https://console.aiven.io/>`_:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.couchbase.connect.kafka.CouchbaseSourceConnector",
        "couchbase.seed.nodes": "COUCHBASE_SEED_NODES", 
        "couchbase.username": "COUCHBASE_USER",
        "couchbase.password": "COUCHBASE_PASSWORD",
        "couchbase.bucket": "COUCHBASE_BUCKET",
        "topics": "TOPIC_LIST"
    }

The configuration file contains the following entries:

* ``name``: the connector name, replace CONNECTOR_NAME with the name you want to use for the connector
* ``COUCHBASE_SEED_NODES``, ``COUCHBASE_BUCKET``, ``COUCHBASE_USER``, ``COUCHBASE_PASSWORD``: sink database parameters collected in the :ref:`prerequisite <connect_couchbase_sink_prereq>` phase.  


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Click on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select **Couchbase Sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``couchbase-sink.json`` file) into the form
6. Click on **Apply**

   .. note::

      The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tabs and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target Couchbase bucket.

.. note::

    Connectors can also be created using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.


Example: define a Couchbase sink connector
--------------------------------------------

The example creates an Couchbase sink connector with the following properties:

* connector name: ``couchbase_sink``
* Couchbase seeds: ``test.cloud.couchbase.com``
* Couchbase username: ``testuser``
* Couchbase password: ``Test123!`` 
* Couchbase bucket: ``travel-sample``
* topic to sink: ``inventory``

The connector configuration is the following:

::

    {
        "name": "couchbase_sink",
        "connector.class": "com.couchbase.connect.kafka.CouchbaseSinkConnector",
        "couchbase.seed.nodes": "test.cloud.couchbase.com",
        "couchbase.username": "testuser",
        "couchbase.password": "Test123!",
        "couchbase.bucket": "travel-sample",
        "topics": "inventory"
    }

With the above configuration stored in a ``couchbase-sink.json`` file, you can create the connector in the ``demo-kafka`` instance and you should see the data landing in an Couckbase bucket  topic named ``travel-sample``.

------

*Couchbase is a trademark of Couchbase, Inc.*
