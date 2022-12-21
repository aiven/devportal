Aiven for ClickHouse® features overview
=======================================

Aiven for ClickHouse® is designed for developers to try out ClickHouse quickly and easily and develop analytics apps. Discover Aiven for ClickHouse's key features and attributes which let you focus on turning business data into actionable insights while Aiven takes care of managing ClickHouse.

About the core functionality
----------------------------

Aiven for ClickHouse is a fully managed distributed columnar database which is built on the open source ClickHouse solution. It is a fast highly-scalable fault-tolerant database designed for online analytical processing (OLAP) and data warehousing. Aiven for ClickHouse enables you to execute complex SQL queries on large datasets quickly and effectively to process large amounts of data in real time. On top of that, it supports built-in data integrations for Aiven for Kafka® and Aiven for PostgreSQL®.

Effortless setup
----------------

With the managed ClickHouse service, you can offload on Aiven multiple time-consuming and laborious operations on your data infrastructure: database initialization and configuration, cluster provisioning and management, or your infrastructure maintenance and monitoring are off your shoulders.

Pre-configured settings
  The managed ClickHouse service is pre-configured with a rational set of parameters and settings appropriate for the plan you have selected. You can easily launch production-ready ClickHouse clusters in minutes in a cloud of your choice.

Easy management
---------------

Scalability
  You can seamlessly :doc:`scale your ClickHouse cluster </docs/platform/howto/scale-services>` horizontally or vertically as your data and needs change using the pre-packaged plans. Aiven for ClickHouse also supports :doc:`sharding </docs/products/clickhouse/howto/use-shards-with-distributed-table>` as a horizontal cluster scaling strategy.

Resource tags
  You can assign metadata to your services in the form of tags. They help you organize, search, and filter Aiven resources. You can :doc:`tag your service <https://docs.aiven.io/docs/platform/howto/tag-resources.html>` by purpose, owner, environment, or any other criteria.

Forking
  Forking an Aiven for ClickHouse service creates a new database service containing the latest snapshot of an existing service. Forks don't stay up-to-date with the parent database, but you can write to them. It provides a risk-free way of working with your production data and schema. For example, you can use them to test upgrades, new schema migrations, or load test your app with a different plan. Learn how to :doc:`fork an Aiven service </docs/platform/howto/console-fork-service>`.

Effective maintenance
---------------------

Automatic maintenance updates
  With 99.99% SLA, Aiven makes sure that the ClickHouse software and the underlying platform stays up-to-date with the latest patches and updates with zero downtime. You can set :doc:`maintenance windows </docs/platform/concepts/maintenance-window>` for your service to make sure the changes occur during times that do not affect productivity.

Backups and disaster recovery
  Aiven for ClickHouse has automatic backups taken every 24 hours. The retention period depends on your plan tier. Check out the details on `Plan comparison <https://aiven.io/pricing?product=clickhouse&tab=plan-comparison>`_.

Intelligent observability
-------------------------

Service health monitoring
  Aiven for ClickHouse provides metrics and logs for your cluster at no additional charge. You can enable pre-integrated Aiven observability services, such as Grafana®, M3®, or OpenSearch® or push available metrics and logs to external observability tools, such as Prometheus, AWS CloudWatch, or Google Cloud Logging. For more details, see :doc:`Monitor Aiven for ClickHouse metrics </docs/products/clickhouse/howto/monitor-performance>`.

Notifications and alerts
  The service is pre-configured to alert you on, for example, your disk running out of space or CPU consumption running high when resource usage thresholds are exceeded. Email notifications are sent to admins and technical contacts of the project under which your service is created. Check :doc:`Receive technical notifications </docs/platform/howto/technical-emails>` to learn how you can sign up for such alerts.

Security and compliance
-----------------------

Single tenancy
  Your service runs on dedicated instances, thus offering true data isolation that contributes to the optimal protection and an increased security.

Network isolation
  Aiven platform supports VPC peering as a mechanism for connecting directly to your ClickHouse service via private IP, thus providing a more secure network setup. The platform also supports PrivateLink connectivity.

Regulatory compliance
  ClickHouse runs on Aiven platform that is ISO 27001:2013, SOC2, GDPR, HIPAA, and PCI/DSS compliant.

Role based Access Control (RBAC)
To learn what kind of granular access is possible in Aiven for ClickHouse, check out :ref:`RBAC with Zookeeper <zookeeper>`.

Zero lock-in
  Aiven for ClickHouse offers compatibility with open source software (OSS), which protects you from software and vendor lock-in. You can easily migrate between clouds and regions.

.. seealso::
  
  Check out more details on security and compliance in Aiven for ClickHouse in :doc:`Secure a managed ClickHouse® service </docs/products/clickhouse/howto/secure-service>`.

Devops-friendly tools
---------------------

Automation
  `Aiven Provider for Terraform <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ helps you automate the orchestration of your ClickHouse clusters.

Command-line tooling
  :doc:`Aiven CLI </docs/tools/cli>` client provides greater flexibility of use for proficient administrators allowing scripting repetitive actions with ease. 

REST APIs
  :doc:`Aiven APIs </docs/tools/api>` allow you to manage Aiven resources in a programmatic way using HTTP requests. The whole functionality available via Aiven Console is also available via APIs enabling you to build custom integrations with ClickHouse and the Aiven platform.
