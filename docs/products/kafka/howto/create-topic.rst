Creating an Apache Kafka® topic
===============================

While you can set Apache Kafka® to :doc:`automatically create a topic when the a message is produced to a topic that does not exist <create-topics-automatically>`, creating topics beforehand is generally considered a preferred practice and recommended for production environments since:

* Allows you to define granular topic settings like the number of partitions, replication factor, retention etc.
* Avoids wrong topic generation in case of typos

If you're using Aiven for Apache Kafka you can create topics via the `Aiven console <https://console.aiven.io>`_ or the :doc:`Aiven CLI </docs/tools/cli>`.

Create a new Apache Kafka topic using the Aiven console
--------------------------------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, click on the service name.

3. Select the **Topics** tab:

   a. Enter a name for your topic.

   b. Select **Advanced configuration** to set the replication factor, number of partitions and other advanced settings. These can be modified later.

4. Click **Add Topic** on the right hand side of the console.

   The new topic will be visible immediately, but may take a few minutes before you can update its settings.


Create an Apache Kafka topic using the Aiven client (CLI)
----------------------------------------------------------

Use the :ref:`dedicated topic-create function <avn_cli_service_topic_create>` to create a new topic via the :doc:`Aiven CLI </docs/tools/cli>`.

Example: Create a new topic via Aiven CLI
'''''''''''''''''''''''''''''''''''''''''

Create a new topic named ``students`` on the Aiven for Apache Kafka instance ``demo-kafka`` with the following settings:

* ``replication_factor``: 3
* ``partitions``: 2
* ``retention``: 4 hours

Execute following command:

::
   
   avn service topic-create demo-kafka students   \
      --partitions 2                               \
      --replication 3                              \
      --retention 4

.. Note::

   After executing the command the required changes are applied immediately. However some operation, like partition balancing after a overall partition number change, can take some time (depending on the data volume) to take full effect.

