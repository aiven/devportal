EOL for major versions of Aiven Services
========================================

End of Life (EOL) refers to the deadline after which affected Aiven
services are retired and will be no longer supported nor maintained.

Since August 2020, Aiven aims to follow the EOL schedule set by the
original authors and maintainers of the open source software, aka
upstream projects. Once the upstream project retires a specific version,
they do not receive security updates and critical bug fixes anymore by
the maintainers.

Continued use of outdated services means that they no longer offer our
customers the level of protection their business needs. Therefore, by
following the upstream project's EOL schedule, we ensure that Aiven
services are always running on supported versions of the open source
software.

**Version Numbering**
~~~~~~~~~~~~~~~~~~~~~

Aiven services inherit the upstream project’s software versioning
scheme. Depending on the service, a major version can be either a single
digit (e.g. PostgreSQL 12) or ``major.minor`` (e.g. Kafka 2.4). The
exact version of the service is visible in the Aiven console once the
service is up and running.

Aiven for Elasticsearch
-----------------------

Aiven for Elasticsearch major versions will reach EOL on the same date
as the upstream open source project's EOL .

.. container:: intercom-interblocks-table-container

   =========== ============= ==================
   **Version** **Aiven EOL** **Upstream EOL**
   2.x         2020-10-30    2018-02-28
   5.x         2020-10-30    2019-03-11
   6.x         2020-11-20    2020-11-20
   7.x         2022-03-23    2022-05-11 (v7.10)
   =========== ============= ==================

Aiven for PostgreSQL
--------------------

Aiven for PostgreSQL major versions will reach EOL on the same date as
the upstream open source project's EOL .

.. container:: intercom-interblocks-table-container

   +-------------+---------------+------------------+------------------+
   | **Version** | **Aiven EOL** | **Availability   | **Availability   |
   |             |               | end on Aiven     | start on Aiven   |
   |             |               | Platform**       | Platform**       |
   +-------------+---------------+------------------+------------------+
   | 9.5         | 2021-04-15    | 2021-01-26       | 2015-12-22       |
   +-------------+---------------+------------------+------------------+
   | 9.6         | 2021-11-11    | 2021-05-11       | 2016-09-29       |
   +-------------+---------------+------------------+------------------+
   | 10          | 2022-11-10    | 2022-05-10       | 2017-01-14       |
   +-------------+---------------+------------------+------------------+
   | 11          | 2023-11-09    | 2023-05-09       | 2017-03-06       |
   +-------------+---------------+------------------+------------------+
   | 12          | 2024-11-14    | 2024-05-14       | 2019-11-18       |
   +-------------+---------------+------------------+------------------+
   | 13          | 2025-11-13    | 2025-05-13       | 2021-02-15       |
   +-------------+---------------+------------------+------------------+
   | 14          | 2026-11-12    | 2026-05-12       | 2021-11-11       |
   +-------------+---------------+------------------+------------------+

.. _aiven-for-kafka:

Aiven for Apache Kafka
----------------------

Starting with v2.5, Aiven for Kafka ``major.minor`` version will reach
EOL one year after it's made available on Aiven platform.

.. container:: intercom-interblocks-table-container

   =========== ============= ========================================
   **Version** **Aiven EOL** **Availability start on Aiven Platform**
   1.0.x       2021-02-01    2017-11-01
   1.1.x       2021-02-01    2018-07-31
   2.0.x       2021-02-01    2018-07-30
   2.1.x       2021-02-01    2018-12-04
   2.2.x       2021-02-01    2019-04-19
   2.3.x       2021-08-13    2019-09-05
   2.4.x       2021-08-13    2019-10-21
   2.5.x       2021-08-13    2020-05-05
   2.6.x       2021-08-13    2020-08-13
   2.7.x       2022-01-24    2021-01-21
   2.8.x       2022-06-02    2021-04-26
   3.0         2022-11-22    2021-11-22
   3.1         2023-02-14    2022-02-14
   =========== ============= ========================================

.. _h_0f2929c770:

Aiven for Cassandra
-------------------

Starting with v4, Aiven for Cassandra ``major`` version will reach EOL
six months after it's made available on Aiven platform.

.. container:: intercom-interblocks-table-container

   +-------------+---------------+------------------+------------------+
   | **Version** | **Aiven EOL** | **Availability   | **Availability   |
   |             |               | end on Aiven     | start on Aiven   |
   |             |               | Platform**       | Platform**       |
   +-------------+---------------+------------------+------------------+
   | 3           | 2022-07-27    | 2022-04-27       | 2018-11-08       |
   +-------------+---------------+------------------+------------------+
   | 4           | N/A           | N/A              | 2021-12-09       |
   +-------------+---------------+------------------+------------------+

Aiven Service EOL Policy for major versions
-------------------------------------------

Aiven EOL policy is applicable only for services whose major versions
are controlled by the customer.

It applies to both **powered-on** and **powered-off** services running
the affected versions.

EOL notification
~~~~~~~~~~~~~~~~

When Aiven defines the EOL date for a service major version,

-  Customers will receive an EOL email announcement along with
   instructions on the next steps.

-  Aiven Console will also show an EOL alert for affected services.

-  Email reminders will be sent to customers on a monthly cadence. On
   the month of the EOL date, the cadence shifts to weekly reminders.

Upon EOL
~~~~~~~~

-  Affected powered-on services will be automatically upgraded to the
   latest available version. For example, if latest version is
   ElasticSearch 7.7, then upon Elasticsearch 5.x EOL, it will be
   upgraded to the latest ES 7.7 instead of Elasticsearch 6.x.

-  Affected powered-off services will no longer be accessible and their
   backups will be deleted.

Our Recommendation
------------------

We **highly recommend** customers to perform the version upgrade well
before EOL so that they can test compatibility for any breaking changes,
plan for unforeseen issues, and migrate to the newer version at their
own schedule.

Aiven platform offers database forking as an efficient tool to verify
the version upgrade so that customers can safely test compatibility
without committing their production services to a one-way upgrade.

**Tip:** Navigate to the service's "Overview" page and scroll down until
you see a "New database fork" button. This will allow you to make a
separate new database service that is cloned from the current one's
backups.
