Service forking
================

:doc:`Fork your Aiven service </docs/platform/howto/console-fork-service>` in order to make a copy of the service. You can use it to create a development copy of your production environment, set up a snapshot to analyze an issue or test an upgrade, or create an instance in a different cloud/geographical location/under a different plan.

When you fork a service, the following items are copied into the new service:

- Configurations
- Databases
- Service users
- Connection pools

.. Warning::
        The service integrations are not copied over to the forked version, and need to be re-established for each new copy. 

You can fork the following Aiven services:

- PostgreSQL®
- MySQL
- Redis®
- Apache Cassandra® (Limitation: you cannot fork to a lower amount of nodes)
- Elasticsearch*
- OpenSearch®
- InfluxDB®
- M3
- Grafana®

When forking a service with Point in Time Recovery (PITR), you can choose to fork from the latest transaction or select a specific point in the past to fork from. 

------

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
