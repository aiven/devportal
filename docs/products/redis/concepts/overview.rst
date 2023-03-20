Aiven for Redis®* overview
===========================

Aiven for Redis®* is a fully managed **in-memory NoSQL database**, deployable in the cloud of your choice which can help you store and access data quickly and efficiently.

Why Redis®?
-----------

Redis® is an open source, in-memory NoSQL database that serves as a fast data store, cache, or lightweight message broker. 

With Aiven, you can leverage the power of Redis to improve the performance of your applications by easily setting up high-performance data caching. Additionally, Redis can be integrated seamlessly into your observability stack for purposes such as logging and monitoring.

Redis offers a wide range of data structures, including strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams.

Features and benefits of Aiven for Redis®*
-------------------------------------------

Aiven for Redis has many features that make it easy and stress-free to use:

* **Managed service:** Aiven for Redis is fully managed, so you don't have to worry about setup, management, or updates. Aiven provides tools and integrations to help you easily use Redis in your data pipelines.

* **Fast and easy deployment:** Aiven for Redis provides production-ready Redis service within a few minutes. You can deploy Redis to the cloud of your choice from 5 public clouds and over 100 regions. Aiven uses high-performance clusters with carefully selected instance types and storage options for top-notch performance. A Bring-your-own-account (BYOA) deployment model is available for strict control requirements.

* **Integration with data infrastructure:** Aiven ensures secure network connectivity using VPC peering, PrivateLink, or TransitGateway technologies. Aiven integrates with various observability tooling, including Datadog, Prometheus, and Jolokia, or you can use Aiven's observability tools for improved monitoring and logging.

* **DevOps-friendly management and development:** Aiven for Redis is easy to manage using `Aiven Console <https://console.aiven.io/>`_, `Aiven CLI <https://github.com/aiven/aiven-client>`_, or :doc:`Terraform </docs/tools/terraform>` . Scaling, forking, and upgrading your Redis cluster is quick and easy. Aiven for Redis is compatible with open-source software, making it easy to use with your existing applications. Migrating between clouds and regions is also easy with Aiven for Redis.
  
* **Backups and disaster recovery:** Aiven for Redis offers automatic and configurable backups. Automatic backups are taken every 24 hours, and the retention period varies based on the selected service plan.

Ways to use Aiven for Redis
-----------------------------

- Redis can be used as a supplementary data store, complementing a primary database like PostgreSQL®.

- Redis is suitable for transient data, caching values for quick access, and data that can be reestablished, such as session data. While Redis is not a persistent storage solution by default, it can be configured to be persistent.


Redis resources
----------------

* `Main Redis page <https://redis.io/>`_

* `Redis documentation <https://redis.io/documentation>`_

* `Redis refcard on DZone <https://dzone.com/refcardz/getting-started-with-redis>`_
