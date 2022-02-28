Creating an Apache Kafka® topic
===============================

While you can set Apache Kafka® to :doc:`automatically create a topic when the a message is produced to a topic that does not exist <create-topics-automatically>`, creating topics beforehand is generally considered a preferred practice and recommended for production environments:

* it lets you to define granular topic settings such as the number of partitions, the replication factor, the retention period and more.
* It prevents the wrong topic being generated (for instance with typos).

Create an Apache Kafka® topic via Aiven Console
-----------------------------------------------

To create a new topic via the `Aiven Console <https://console.aiven.io/>`_:

1. On the **Services** page, click on the Aiven for Apache Kafka® service where you want to crate the topic.

2. Select the **Topics** tab:

   a. In the *Add new topic* section, enter a name for your topic.

   b. In the **Advanced configuration** you can set the replication factor, number of partitions and other advanced settings. These can be modified later.

3. Click **Add Topic** on the right hand side of the console.

   The new topic will be visible immediately, but may take a few minutes before you can update its settings.



You can also use the :ref:`dedicated topic-create function <avn_cli_service_topic_create>` to create a new topic via the :doc:`Aiven CLI </docs/tools/cli>`.