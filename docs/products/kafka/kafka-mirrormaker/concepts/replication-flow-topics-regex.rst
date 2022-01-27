Topics included in a replication flow
=====================================

When :doc:`defining a replication flow <../howto/setup-replication-flow>` you need to define which topics in the source Apache Kafka® cluster to include or exclude from the cross-cluster replica.

The **topics** parameter dictates which topics to include in the replica and can be provided as `list of regular expressions in Java format <https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html>`_. The same is also valid for the **topics blacklist** parameter defining which topics to exclude.

Example: topic inclusion and exclusion regular expressions
----------------------------------------------------------

If you need to define a replication flow including the topic ``warehouse.operations`` and any topic starting with ``customer.``, but excluding the topic ``customer.support`` then the following regular expression can be used:

* **Topics**: ``customer\\..*`` and ``warehouse\\.operations``
* **Topics Blacklist**: ``customer\\.support``
