Causes of "connector list not currently available"
==================================================

Sometimes, when accessing the `Aiven Console <https://console.aiven.io/>`_ and trying to view the list of connectors in your Aiven for Apache Kafka® Connect cluster you can encounter the message ``connector list not currently available``. 

.. Note::

    The same error message is shown in Terraform (for example, when using ``terraform plan``) because it uses the same backend API.
 
There can be a number of reasons why you are seeing the above message:

* The dedicated Apache Kafka Connect cluster was just created. The list will load after the cluster is fully online with all the nodes in running state
* The Apache Kafka Connect API on a Kafka cluster was just enabled. It should take a few seconds for the Apache Kafka Connect services to be operational
* The Apache Kafka Connect cluster is in the process of setting up/reconfiguring a connector. This message should clear after a few seconds
* The Apache Kafka Connect cluster is running out of memory. You will likely keep seeing this message unless you upgrade to a larger plan
* One or more nodes on the Apache Kafka Connect cluster crashed. The API that fetches the connector list calls the Apache Kafka Connect cluster by it's hostname and that maps to one of the 3 workers randomly. If you see this message appear intermittently, this is likely the reason. The crashed node should recover automatically, but if it doesn't, please `contact our support <https://help.aiven.io/en/articles/868101-aiven-support-details>`_ for further help


If you are in doubt whether or not any of the following reasons above is the issue  that you are experiencing, you can `contact our support channel <https://help.aiven.io/en/articles/868101-aiven-support-details>`_ and we will be able to help you further.
