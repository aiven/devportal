Monitor and alert logs for denied ACL
=====================================

Aiven for Apache Kafka supports the definition of users and access control lists (ACL) to allow and limit producer and consumer rights at topic level. You read more about ACLs permission in the :doc:`dedicated documentation <../concepts/acl>`.

In cases of ACLs problems, an error ``io.aiven.kafka.auth.AivenAclAuthorizer`` is generated. 
The following log patterns can also be used to set up alerts checking for failed authentication and ACL evaluation.

Failed producer
---------------

A producer creates the following log in case the client has no privilege to write to a specific topic:

::

   HOSTNAME: kafka-pi-3141592-75
   SYSTEMD_UNIT: kafka.service
   MESSAGE: [2020-09-04 06:35:33,509] INFO [DENY] Auth request Write on Topic:nodejs-quickstart-kafka-topic by User test-kuser (io.aiven.kafka.auth.AivenAclAuthorizer)

Failed consumer
---------------

A consumer creates the following log in case the client has no privilege to describe a specific topic:

::

   HOSTNAME: kafka-pi-3141592-74
   SYSTEMD_UNIT: kafka.service
   MESSAGE: [2020-09-04 06:43:09,712] INFO [DENY] Auth request Describe on Topic:nodejs-quickstart-kafka-topic by User test-kuser (io.aiven.kafka.auth.AivenAclAuthorizer)

.. _valid-cert-with-invalid-key:

Valid certificate with invalid key
----------------------------------

A client creates the following log when using a valid certificate with an invalid key to perform a describe operation over a topic:

::

   HOSTNAME: kafka-pi-3141592-75
   SYSTEMD_UNIT: kafka.service
   MESSAGE: [2020-09-04 06:54:10,781] INFO [DENY] Auth request Describe on Topic:nodejs-quickstart-kafka-topic by Invalid CN=delete-user,OU=u6l6y9h1,O=kafka-pi-3141592 (io.aiven.kafka.auth.AivenAclAuthorizer)