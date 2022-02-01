Fake sample dataset
===================

Learning streaming is way more fun with data, so to get you started on your Apache Kafka® journey we help you creating fake streaming data to a topic.

.. Note::

    The following example is based on `Docker <https://www.docker.com/>`_ images, which require `Docker <https://www.docker.com/>`_ or `Podman <https://podman.io/>`_ to be executed.

The following example assumes you have an Aiven for Apache Kafka® service running. You can create one following the :doc:`dedicated istructions <../getting-started>`.


Fake data generator on Docker
-----------------------------

To learn data streaming, you need a continuous flow of data and for that you can use the `Dockerized fake data producer for Aiven for Apache Kafka® <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_. To take the generator into use:

1. Clone the repository:

::

    git clone https://github.com/aiven/fake-data-producer-for-apache-kafka-docker

2. Copy the file ``conf/env.conf.sample`` to ``conf/env.conf``

3. Create a new access token via the `Aiven console <https://console.aiven.io/>`_ or the following command in the :doc:`Aiven CLI </docs/tools/cli/account>`, changing the ``max-age-seconds`` appropriately for the duration of your test:

::

    avn user access-token create                            \
    --description "Token used by Fake data generator"       \
    --max-age-seconds 3600                                  \
    --json | jq -r '.[].full_token'

.. Tip::

    The above command uses `jq <https://stedolan.github.io/jq/>`_ to parse the result of the Aiven CLI command. If you don't have jq installed, you can remove the ``| jq -r '.[].full_token'`` section from the above command and parse the JSON result manually to extract the access token.

4. Edit the ``conf/env.conf`` file filling the following placeholders:

* ``my_project_name``: the name of your Aiven project
* ``my_kafka_service_name``: the name of your Aiven for Apache Kafka instance
* ``my_topic_name``: the name of the target topic, can be any name
* ``my_aiven_email``: the email address used as username to log in Aiven services
* ``my_aiven_token``: the access token generated during the previous step

5. Build the Docker image with:

::

    docker build -t fake-data-producer-for-apache-kafka-docker .

.. Tip::

    Every time you change any parameters in the ``conf/env.conf`` file, you need to rebuild the Docker image to take them into use.

6. Start the streaming data flow with:

::

    docker run fake-data-producer-for-apache-kafka-docker

7. Once the Docker image is running, check in the target Aiven for Apache Kafka® service that the topic is populated. This can be done with the `Aiven console <https://console.aiven.io/>`_ or using tools like :doc:`kcat <kcat>`.
