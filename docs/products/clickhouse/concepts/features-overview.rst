Aiven for ClickHouse® features overview
=======================================

What is Aiven for ClickHouse® and what are its key features? Why and when to use Aiven for ClickHouse? What are its most common use cases? This article helps you discover it all and more.

About Aiven for ClickHouse
--------------------------

Aiven for ClickHouse® is a fully managed distributed columnar database which is built on the open source ClickHouse solution. It is a fast highly-scalable fault-tolerant database designed for online analytical processing and data warehousing. Aiven for ClickHouse enables you to execute complex SQL queries on large datasets quickly and effectively to process large amounts of data in real time.

Aiven for ClickHouse provides

* Fast insights at scale

  ClickHouse is built to process hundreds of millions of rows and tens of gigabytes of data per second.

* Integrated analytics data flows

  With Aiven for ClickHouse, you can build high-performance analytics pipelines, leveraging your data in other Aiven services.

* High-performance analytical queries

  ClickHouse processes typical analytical queries two to three orders of magnitude faster than traditional row-oriented systems and exceeds the speed of other columnar databases.

* Built-in data integrations

  You can integrate with other Aiven services at the click of a button. Use Aiven for Apache Kafka® as a data source. Access data in Aiven for PostgreSQL® through federated queries. Visualize results using Aiven for Grafana® or external BI tools.

* Powerful SQL extensions

  Aiven for ClickHouse offer a rich set of analytics functions, enabling fast aggregations on large datasets using familiar SQL.

ClickHouse's purpose and application
------------------------------------

ClickHouse is designed for generating detailed real-time analytical data reports using advanced SQL queries on large datasets. ClickHouse is your top pick if

* You work with enormous volumes of data (measured in terabytes) continuously written and read.
* You have tables with a huge number of columns but column values are reasonably short.
* Your data is well-structured and not yet aggregated.
* You insert data in large batches over thousands of lines. The vast majority of operations are reads with aggregations. For reads, you process large number of rows but fairly low number of columns.
* You don't need to modify data later.
* You don't need to retrieve specific rows.
* You don't need transactions.

Common use cases for ClickHouse are

* Providing real-time customer-facing analytics

  High-performance analytics views provided to your customers as part of your application and service

* Gaining deep insights internally

  Highly-scalable and performant analytics for user/ IoT device behavior: Report on aggregated data but collect and store it all so you can dig deeper into it with no risk of losing hidden insights.

* Data store for near-real-time decision engines

  When building decision engines, for example a recommendation engine or a fraud detection engine, you need a high-performance data store to host all the necessary data. This ensures that your rules and machine learning models can act with the speed required for a great user experience.

Managed ClickHouse - database as a service
------------------------------------------

With Aiven for ClickHouse, you can focus on turning your data to actionable insights, while Aiven takes care of managing your data warehouse infrastructure. As a fully managed service, Aiven for ClickHouse offers

* Effortless provisioning

  * Launch production-ready ClickHouse clusters in minutes in the cloud of your choice.
  * Seamlessly scale your clusters as your data and needs change.
  * Use the bring-your-own-account deployment model for strict control requirements

* Reliable operations

  * Self-healing platform with 99.99% SLA
  * Zero downtime during scaling, upgrading, and other management operations

* Superior observability

  * Use pre-integrated Aiven observability services for enhanced monitoring and logging with Grafana, M3, or OpenSearch®.
  * Integrate with your external observability tooling — from Datadog to Prometheus.

* Security & compliance

  * Nodes running on dedicated virtual machines (VMs)
  * End-to-end encryption
  * ISO 27001:2013, SOC2, GDPR, HIPAA and PCI/DSS compliant
  * Secure networking with VPC peering, PrivateLink, or AWS Transit Gateway

* Zero lock-in

  * Compatibility with open source software (OSS) protects you from software and vendor lock-in.
  * Easy migration between clouds and regions

* All-inclusive pricing

  * Network traffic, VPC setup, and backup storage costs covered
  * Pay as you go

* DevOps friendliness

  * Terraform provider to manage Aiven clusters
  * Aiven client for CLI access
  * REST APIs for custom integrations
