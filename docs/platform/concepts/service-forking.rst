Service forking
================

:doc:`Fork your Aiven service </docs/platform/howto/console-fork-service>` in order to make a copy of the service. You can use it to create a development copy of your production environment, set up a snapshot to analyze an issue or test an upgrade, or create an instance in a different cloud/geographical location/under a different plan.

When you fork a service, the following items are copied into the new service:

- Configurations
- Databases
- Service users
- Connection pools

Forking a service does not cause any additional load to it, because the new fork does not communicate with the original service. The data is restored from the latest backup stored separately from the service.

.. Warning::
        The service integrations are not copied over to the forked version, and need to be re-established for each new copy.

You can fork the following Aiven services:

- PostgreSQL®
- MySQL
- Redis®*
- Apache Cassandra® (Limitation: you cannot fork to a lower amount of nodes)
- Elasticsearch
- OpenSearch®
   
  .. important:: 
        When you fork an Aiven for OpenSearch® service, any Single Sign-On (SSO) methods configured at the service level, such as SAML, must be explicitly reconfigured for the forked service. SSO configurations are linked to specific URLs and endpoints, which change during forking. Failing to reconfigure SSO methods for the forked service can lead to authentication problems and potentially disrupt user access. 

- InfluxDB®
- M3DB
- Grafana®

When forking a service with Point in Time Recovery (PITR), you can choose to fork from the latest transaction or select a specific point in the past to fork from.

------

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
