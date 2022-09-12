
Karapace schema registry authorization
======================================
The schema registry authorization feature when enabled in :doc:`Karapace schema registry <../howto/enable-karapace>` allows you to authenticate the user, and control read or write access to the individual resources available in the Schema Registry. 
Authorization in Karapace is achieved by using :doc:`Access Control Lists (ACLs) <../concepts/acl-definition>`. ACLs provide a way to achieve fine-grained access control for the resources in Karapace.

.. Note::

  Karapace schema registry authorization is enabled on all Aiven for Apache Kafka® services. The exception is older services created before mid-2022, where the feature needs to be :doc:`enabled <../howto/enable-karapace>`.

Common use cases
----------------
Some of the common use cases for Karapace schema registry authorization include: 

* **Schemas as API contract among teams:** Allow teams to leverage schemas as API contracts with other teams by providing read-only access to schemas in Schema Registry.
* **Kafka as a communication broker with third parties:** Allow conditional read-only access to schemas by third parties to establish Kafka topics as communication channels.
* **Schema registration automated with CI/CD:** Achieve automation of schema registration using Continuous Integration(CI) tools in such a way that add, update and delete operations on schemas is limited to the CI Tools. At the same time, the different applications are allowed read-only access to the schemas as needed.
* **Segregated consumers of Schema Registry and REST Proxy:** Limits the attack surface by segregating and limiting access to only what is required for the consumers of the Schema Registry and REST Proxy.

