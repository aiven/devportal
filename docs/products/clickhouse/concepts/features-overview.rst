Aiven for ClickHouse® features overview
=======================================

What is Aiven for ClickHouse® and what are its key features? Why and when to use Aiven for ClickHouse? What are its most common use cases? This article helps you discover it all and more.

About Aiven for ClickHouse
--------------------------

Aiven for ClickHouse® is a fully managed distributed columnar database which is built on the open source ClickHouse datastore. It is a fast highly-scalable fault-tolerant solution designed for online analytical processing and data warehousing. Aiven for ClickHouse enables you to execute complex SQL queries on large datasets quickly and effectively to process large amounts of data in real time.

Aiven for ClickHouse provides the following:

* Faster insights at scale

  ClickHouse is built to process hundreds of millions of rows and tens of gigabytes of data per second, so you can keep up with the ever increasing speed of your business

* Integrated analytics dataflows

  Build high performance analytics pipelines with Aiven for ClickHouse, easily leveraging your data in other Aiven services

* High performance analytical queries

  ClickHouse processes typical analytical queries two to three orders 
  of magnitude faster than traditional row-oriented systems. 
  Exceeds the speed of other columnar databases

* Built-in data integrations

  Integrate with other Aiven services at the click of a button. Use Aiven for Apache Kafka® as a data source. Access data in Aiven for PostgreSQL® through federated queries. Visualize results using Aiven for Grafana® or external BI tools

* Powerful SQL extensions

  Rich set of analytics functions available, enabling extremely fast aggregations on large datasets using familiar SQL

ClickHouse's purpose and application
------------------------------------

ClickHouse is designed for generation of detailed real-time analytical data reports using advanced SQL queries on large data-sets. ClickHouse is your top pick if

* You work with enormous volumes of data (measured in terabytes) continuously written and read;
* You have tables with the massive number of columns (ClickHouse loves large numbers of columns!), but column values are reasonably short;
* Your data is well-structured and not yet aggregated;
* You insert data in large batches over thousands of lines, a million is a good number;
the vast majority of operations are reads with aggregations;
for reads, you process large number of rows, but fairly low number of columns;
* You don't need to modify data later;
* You don't need to retrieve specific rows;
* You don't need transactions.

Common use cases for ClickHouse are

* Providing real-time customer facing analytics

  High-performance analytics views provided to your customers  as part of your application and service - your customers need to know what is the status  NOW, and don't want to have to wait for their analytics views

* Gaining deep insights internally

  Highly scalable and performant analytics for user/ IoT device behavior. Report on aggregated data, but collect and store everything so you can dig deeper into it and  don't risk losing  hidden insights

* Data store for near-real time decision engines

  When building decision engines - e.g. recommendation engine, fraud detection engine - you need a high-performance data store to host all the necessary data. This ensures that your rules and machine learning models can act with the speed required for a great user experience.

Managed ClickHouse - database as a service
------------------------------------------

With Aiven for ClickHouse, you can focus on turning your data to actionable insights, while Aiven takes care of managing your data warehouse infrastructure. As a fully managed service, Aiven for ClickHouse offers the following:

* Effortless provisioning

  * Launch production ready ClickHouse clusters in minutes, in the cloud of your choice
  * Seamlessly scale your clusters as your data and need changes
  * Bring-your-own-account deployment model available for strict control requirements

* Reliable operations

  * Self-healing platform with 99.99% SLA
  * Zero downtime during scaling, upgrading and other management operations

* Superior observability

  * Use pre-integrated Aiven observability services for enhanced monitoring and logging with Grafana, M3, OpenSearch
  * Integrate with your favorite external observability tooling — from Datadog to Prometheus, Jolokia, and more

* Security & compliance

  * Nodes run on dedicated VMs
  * End-to-end encryption
  * ISO 27001:2013, SOC2, GDPR, HIPAA and PCI/DSS compliant
  * Secure networking with VPC peering, PrivateLink or Transit GW

* Zero lock-in

  * Guaranteed compatibility with open source software protects you from software and vendor lock-in 
  * Migrate easily between clouds and regions

* All-inclusive pricing

  * Including network traffic, VPC setup and backup storage costs
  * Pay as you go

* Devops friendliness

  * Terraform Provider to manage Aiven clusters
  * Aiven Client for CLI access
  * REST APIs for custom integrations
