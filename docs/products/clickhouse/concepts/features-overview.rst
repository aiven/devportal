Aiven for ClickHouse® features overview
=======================================

Aiven for ClickHouse® is designed for developers to try out ClickHouse quickly and easily and develop analytics apps. Discover Aiven for ClickHouse's key features and attributes which let you focus on turning business data into actionable insights while Aiven takes care of managing ClickHouse.

About the core functionality
----------------------------

Aiven for ClickHouse is a fully managed distributed columnar database which is built on the open source ClickHouse solution. It is a fast highly-scalable fault-tolerant database designed for online analytical processing (OLAP) and data warehousing. Aiven for ClickHouse enables you to execute complex SQL queries on large datasets quickly and effectively to process large amounts of data in real time. On top of that, it supports built-in data integrations for Aiven for Kafka® and Aiven for PostgreSQL®.

Effortless setup and management
-------------------------------

With the managed ClickHouse service, you can offload on Aiven all the time-consuming and laborious operations on your data infrastructure, such as database initialization and configuration, cluster provisioning and management, or your infrastructure maintenance and monitoring.

Pre-configuration
'''''''''''''''''

The managed ClickHouse service is pre-configured with a rational set of parameters and settings appropriate for the plan you have selected. You can easily launch production-ready ClickHouse clusters in minutes in the cloud of your choice. If you desire additional control, you can tweak the settings via advanced configuration options.

Scalability
'''''''''''

You can seamlessly scale your ClickHouse cluster horizontally or vertically as your data and needs change using the pre-packaged plans. Aiven for ClickHouse also supports sharding as a horizontal cluster scaling strategy.

* Automatic maintenance updates - With 99.99% SLA, Aiven makes sure that the ClickHouse software and the underlying platform stays up-to-date with the latest patches and updates with zero downtime. You can set maintenance windows for your service to make sure the changes occur during times that do not affect productivity. Learn more about maintenance windows in :doc:`</docs/platform/concepts/maintenance-window>`

* Backups and disaster recovery - Aiven for ClickHouse has automatic backups taken every 24 hours. The retention period depends on the plan tier. View the plan comparison. https://aiven.io/pricing?product=clickhouse&tab=plan-comparison

* Forking - Forking ClickHouse creates a new database service containing the latest snapshot of an existing service.  Forks do not stay up-to-date with the parent database, though you can write to them. It provides a risk-free way of working with your production data and schema. For example, you can use them to test upgrades, new schema migrations or load test your app with a different plan. Learn how to fork an Aiven service. https://docs.aiven.io/docs/platform/howto/console-fork-service.html

* Resource tags - You can assign metadata to your services in the form of tags. They help you organize, search and filter Aiven resources. You can tag your service by purpose, owner, environment or any other criteria. Read more about tags. https://docs.aiven.io/docs/platform/howto/tag-resources.html

Observability
-------------

* Service health monitoring -  Aiven for ClickHouse provides metrics and logs for your cluster at no additional charge. You can enable pre-integrated Aiven observability services such as Grafana®, M3®, or OpenSearch® or push the available metrics and logs to external observability tools, such as Prometheus, AWS CloudWatch, and Google Cloud Logging.

* Notifications and alerts - The service is pre-configured to alert you based on resource usage triggers. Email notifications are sent to admins and technical contacts of the project under which your service is created. 

Security and compliance
-----------------------

* Single tenancy - Your service runs on dedicated instances, thus offering true data isolation that contributes to optimal protection and increased security.

* Network isolation - Aiven platform supports VPC peering as a mechanism for connecting directly to your ClickHouse service via private IP, thus providing a more secure network setup. The platform also supports PrivateLink connectivity.

* Regulatory compliance - ClickHouse runs on Aiven platform that is ISO 27001:2013, SOC2, GDPR, HIPAA and PCI/DSS compliant.

* Role based Access Control (RBAC) - see more details in :doc:`Zookeeper </docs/products/clickhouse/concepts/service-architecture>`.

* Zero lock-in

  * Compatibility with open source software (OSS) protects you from software and vendor lock-in.
  * Easy migration between clouds and regions

DevOps-friendly tools
---------------------

* Automation - AivenTerraform provider helps you automate orchestration of your ClickHouse clusters with ease.

* Command-line tooling - Aiven client provides greater flexibility of use for proficient administrators allowing scripting of repetitive actions with ease. 

* REST APIs - Aiven APIs allow you to manage Aiven resources in a programmatic way using HTTP requests. All functionality available via Aiven Console is also available via APIs enabling you to build custom integrations with ClickHouse and the Aiven platform.
