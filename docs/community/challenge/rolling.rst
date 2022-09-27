Rolling - Aiven challenge with Apache Kafka® and Apache Flink®
==============================================================

Welcome to Aiven's "Rolling" challenge, an easy way for you to explore Aiven for Apache Kafka® and Aiven for Apache Flink®. 

With the launch of Aiven for Apache Flink® we added the a new way to manipulate your Apache Kafka® streaming data via SQL statements, providing the best combination of tools for real-time data transformation.

For this challenge, we'll be using `Aiven fake data generator on Docker <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ to generate a series of symbols, the challenge consist of understanding the overall meaning of the symbols by transforming the original series of data with Apache Flink.

Let's dive right in.

Instructions
------------

The goal is to make sense of the incoming stream of data.

1. Create an Aiven free trial account: `sign up for free <https://console.aiven.io/signup/email?credit_code=AivenChallengeCURRENTNA22&trial_challenge=the_rolling_challenge>`_.

2. Create an :doc:`Aiven for Apache Kafka® service </docs/products/kafka/getting-started>`

3. Create an :doc:`Aiven for Apache Flink® service </docs/products/flink/getting-started>`

4. Create an :doc:`integration between the Aiven for Apache Kafka® and Apache Flink® services </docs/products/flink/howto/create-integration>`

5. Create a new :doc:`Aiven authentication token </docs/platform/howto/create_authentication_token>`

6. Clone the `Aiven fake data generator on Docker <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ with::

    git clone https://github.com/aiven/fake-data-producer-for-apache-kafka-docker

7. Copy the file ``conf/env.conf.sample`` to ``conf/env.conf`` and edit the following parameters

   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   | Parameter Name | Parameter Value                                                                                                              |
   +================+==============================================================================================================================+
   |PROJECT_NAME    | Name of the Aiven Project where the Aiven for Apache Kafka service is running                                                |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |SERVICE_NAME    | Name of the Aiven for Apache Kafka service running                                                                           |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |TOPIC           | Name of the Topic to write messages in. ``rolling`` for the challenge                                                        |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |PARTITIONS      | 5                                                                                                                            |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |REPLICATION     | 2                                                                                                                            |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |NR_MESSAGES     | 0                                                                                                                            |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |MAX_TIME        | 0                                                                                                                            |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |SUBJECT         | ``rolling``                                                                                                                  |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |USERNAME        | Your Aiven account username                                                                                                  |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |TOKEN           | Your Aiven account token                                                                                                     |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |PRIVATELINK     | ``NO``                                                                                                                       |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+
   |SECURITY        | ``SSL``                                                                                                                      |
   +----------------+------------------------------------------------------------------------------------------------------------------------------+

8. Build the Docker image

   ::
    
    docker build -t fake-data-producer-for-apache-kafka-docker .

9. Run the Docker image

   ::
    
    docker run fake-data-producer-for-apache-kafka-docker

10. Check the fake messages being produced by Docker

11. In the `Aiven Console <https://console.aiven.io/>`_, navigate to the Aiven for Apache Flink service page

12. Play with the Aiven for Apache Flink **Jobs & Data** tab and try to make sense of the data. 

    .. Tip:: 
    
        The source table can be mapped in Aiven for Apache Flink with the following SQL, using the ``rolling`` topic as source::

            
            ts BIGINT,
            val string,
            ts_ltz AS TO_TIMESTAMP_LTZ(ts, 3),
            WATERMARK FOR ts_ltz AS ts_ltz - INTERVAL '10' SECOND

13. If you find the solution, email us at hacks@Aiven.io and come to the booth C10 to collect your prize

Tips
----

Some tips that could help solving the challenge:

* ``kcat`` is a tool to explore data in Apache Kafka topics, check the :doc:`dedicate documentation </docs/products/kafka/howto/kcat>` to understand how to use it with Aiven for Apache Kafka
* ``jq`` is a helpful tool to parse JSON payloads, read `the instructions <https://stedolan.github.io/jq/>`_ on how to install and check the following useful flags:
    * ``-r`` retrieves the raw output
    * ``-j`` doesn't create a new line for every message
    * ``-c`` shows data in compact view

* If you're stuck with visualizing ``kcat`` consumer data with ``jq``, check the `-u` flag `as per dedicated example <https://ftisiot.net/posts/jq-kcat-consumer/>`_


