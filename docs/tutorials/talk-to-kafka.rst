Tutorial: Let's talk to Kafka. How to send and receive application data from Apache Kafka®?
==============================================================================================

.. Note::

    This tutorial doesn't assume any existing knowledge on Apache Kafka.

Learning objectives
--------------------

- How to authenticate to a Kafka broker?
- Communicate with a Kafka broker using the CLI.
- How to make your app send and receive data to/from Kafka?
- The ease of using a managed Kafka service.

Overview
--------

In this tutorial, we will learn the basics of authenticating to a Kafka broker and transferring messages to and from the broker. We'll learn how to use the built-in CLI tooling to do that as well as use some commonly used programming languages to talk to Kafka.

Here is how the setup looks like:

.. mermaid::

    graph LR;

        id1(Kafka CLI)--producing messages-->id5(Kafka Broker);
        id2(kafka-python library) --producing messages-->id5(Kafka Broker);
        id3(kafka-clients java library) --producing messages-->id5(Kafka Broker);

        id5(Kafka Broker)--consuming messages-->id1(Kafka CLI);
        id5(Kafka Broker)--consuming messages-->id2(kafka-python library);
        id5(Kafka Broker)--consuming messages-->id3(kafka-clients java library);

Under the hood, the CLI and the libraries make use of the `Producer API <https://kafka.apache.org/documentation/#producerapi>`_ and the `Consumer API <https://kafka.apache.org/documentation/#consumerapi>`_. 

.. Note::

    Although this tutorial covers two popular libraries for Python and Java, you can find one or more Kafka libraries for any modern programming language.

Prerequisites
-------------

While the entire tutorial can be completed using open-source Kafka, we're using Aiven for Apache Kafka® for ease and speed of setup. 

To get started, you'll need:

- `Java installed <https://www.java.com/en/download/help/download_options.html>`_
- `Python installed <https://www.python.org/downloads/>`_
- An `Aiven account <https://console.aiven.io/signup>`_