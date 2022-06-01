Connect to Aiven for Apache Kafka® with Python
==============================================

.. See https://docs.google.com/document/d/1PqNbBMzeED_AFeIFzfdcoR_P2bUJrNdcv4uHheeCh6I/edit
   for an explanation of the following

.. |kafka-python| replace:: ``kafka-python``
.. _`kafka-python`: https://pypi.org/project/kafka-python/

These examples show how to connect to an Aiven for Apache Kafka® service using the |kafka-python|_ library, as either a producer or consumer.

.. note:: The examples given here provide different options for the different authentication
   methods. For more information on the supported methods, see `our article on Kafka
   authentication types <https://developer.aiven.io/docs/products/kafka/concepts/auth-types>`_.

Pre-requisites
--------------

Install the Python |kafka-python|_ library:

.. code:: bash

    pip install kafka-python

Go to the *Overview* page of your Aiven for Apache Kafka service.

* If you are going to connect with SSL authentication:

  * In the *Connection information* section:

    #. If **Authentication Method** is shown, choose **Client Certificate**
    #. Next to *Access Key*, click **Download** and save the ``service.key`` file.
    #. Next to *Access Certificate*, click **Download** and save the ``service.cert`` file.
    #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file.

* If you are going to connect using SASL authentication:

  #. Follow the instructions at `Use SASL Authentication with Apache Kafka® <https://developer.aiven.io/docs/products/kafka/howto/kafka-sasl-auth.html>`_ to enable SASL.

  #. In the *Connection Information* section

     #. Select **SASL** as the **Authentication Method**
     #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file

Note that the *CA Certificate* ``ca.pem`` file has the same contents by either route.

Alternatively, you can use the `Aiven command line tool <https://developer.aiven.io/docs/tools/cli.html>`_ to download the files. See the documentation for `avn service user-creds-download <https://developer.aiven.io/docs/tools/cli/service/user.html#avn-service-user-creds-download>`_

In the examples, we just show the name of the file, but in actual use, the full path should be used.

Variables
---------

These are the placeholders you will need to replace in the code samples. The values are from the ``Connection information`` on the service overview page.

If you are using SSL (remember to choose **Client Certificate** if **Authentication Method** is shown):

=============     =============================================================
Variable          Description
=============     =============================================================
``HOST``          Host name for the connection
-------------     -------------------------------------------------------------
``SSL_PORT``      Port number to use
=============     =============================================================

If you are using SASL (**Authentication Method** should be **SASL**):

=================     =============================================================
Variable              Description
=================     =============================================================
``HOST``              Host name for the connection
-----------------     -------------------------------------------------------------
``SASL_PORT``         Port number to use
-----------------     -------------------------------------------------------------
``SASL_USERNAME``     User to connect with
-----------------     -------------------------------------------------------------
``SASL_PASSWORD``     Password for this user
=================     =============================================================

For consumers you will also need:

=================     =============================================================
Variable              Description
=================     =============================================================
``TOPIC_NAME``        The name of the topic to read from
-----------------     -------------------------------------------------------------
``START_FROM``        The value to use for the ``auto_offset_reset`` parameter,
                      which says which message to start consuming from.

                      Allowed values are:

                      * ``latest`` - consume from the end of the topic partition.
                        This is the default.
                      * ``earliest`` - consume from the beginning of the topic
                        partition
=================     =============================================================

For more information on ``auto_offset_reset``, see the Kafka documentation on
`auto.offset.reset <https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset>`_
and
`Consumer Position <https://kafka.apache.org/documentation/#design_consumerposition>`_.


Connect a producer
------------------

Using SSL authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

        from kafka import KafkaProducer

        producer = KafkaProducer(
            bootstrap_servers=f"{HOST}:{SSL_PORT}",
            security_protocol="SSL",
            ssl_cafile="ca.pem",
            ssl_certfile="service.cert",
            ssl_keyfile="service.key",
        )

Using SASL authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

         from kafka import KafkaProducer

         # Choose an appropriate SASL mechanism, for instance:
         SASL_MECHANISM = 'SCRAM-SHA-256'

         producer = KafkaProducer(
            bootstrap_servers=f"{HOST}:{SASL_PORT}",
            sasl_mechanism = SASL_MECHANISM,
            sasl_plain_username = SASL_USERNAME,
            sasl_plain_password = SASL_PASSWORD,
            security_protocol="SASL_SSL",
            ssl_cafile="ca.pem",
         )

Connect a consumer
------------------

Using SSL authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

        from kafka import KafkaConsumer

        consumer = KafkaConsumer(
            "TOPIC_NAME",
            auto_offset_reset="START_FROM",
            bootstrap_servers=f"{HOST}:{SSL_PORT}",
            client_id = CONSUMER_CLIENT_ID,
            group_id = CONSUMER_GROUP_ID,
            security_protocol="SSL",
            ssl_cafile="ca.pem",
            ssl_certfile="service.cert",
            ssl_keyfile="service.key",
        )

Using SASL authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

        from kafka import KafkaConsumer

        # Choose an appropriate SASL mechanism, for instance:
        SASL_MECHANISM = 'SCRAM-SHA-256'

        consumer = KafkaConsumer(
            "TOPIC_NAME",
            auto_offset_reset = "START_FROM",
            bootstrap_servers = f'{HOST}:{SASL_PORT}',
            client_id = CONSUMER_CLIENT_ID,
            group_id = CONSUMER_GROUP_ID,
            sasl_mechanism = SASL_MECHANISM,
            sasl_plain_username = SASL_USERNAME,
            sasl_plain_password = SASL_PASSWORD,
            security_protocol = "SASL_SSL",
            ssl_cafile = "ca.pem"
        )
