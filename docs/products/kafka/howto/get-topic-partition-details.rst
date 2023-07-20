Get partition details of an Apache Kafka® topic
===============================================

Use one of three available approaches to retrieve partition details of an Apache Kafka® topic.

With Aiven console
------------------

In the Aiven Console follow these steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka service.
2. Select **Topics** from the left sidebar. 
3. Select a specific topic in the **Topics** screen or click on the ellipsis (More options).
4. On the **Topics info** screen, select **Partitions** to view detailed information about the partitions.


With Aiven API
--------------

Retrieve topic details with an API call using `the endpoint to get Kafka topic info <https://api.aiven.io/doc/#operation/ServiceKafkaTopicGet>`_.

Learn more about API usage in the :doc:`Aiven API overview </docs/tools/api>`.

With Aiven CLI
--------------

Retrieve topic details by using Aiven CLI commands. Find the full list of commands for ``avn service topic`` in :doc:`the CLI reference </docs/tools/cli/service/topic>`.

For example, this bash script, with a help of ``jq`` utility, lists topics and their details for a specified Apache Kafka service:

.. code:: bash

   #!/bin/bash
   proj=${1:-YOUR-AIVEN-PROJECT-NAME}
   serv="${2:-YOUR-KAFKA-SERVICE-NAME}"
   cloud=$(avn service get --project $proj $serv --json | jq -r '.cloud_name')
   topics=$(avn service topic-list --project $proj $serv --json | jq -r '.[] | .topic_name')

   echo "Cloud: $cloud Service: $serv"
   for topic in $topics
   do
      echo "Topic: $topic"
      avn service topic-get --project $proj $serv $topic
   done
