Get partition details of an Apache Kafka® topic
===============================================

Use one of three available approaches to retrieve partition details of an Apache Kafka® topic.

With Aiven console
------------------

In the Aiven Console follow these steps:

1. Log in to the Aiven web console and select your Apache Kafka service.
2. On the **Topics** tab click the three dots next to the topic you wish to inspect.
3. In the appeared menu click on the **Info** entry, it will open a modal window with topic details.
4. Navigate to the **Partitions** tab.

With Aiven API
--------------

Retrieve topic details with an API call using `the endpoint to get Kafka topic info <https://api.aiven.io/doc/#operation/ServiceKafkaTopicGet>`_.

Learn more about API usage in the :doc:`Aiven API overview </docs/tools/api/index>`.

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
