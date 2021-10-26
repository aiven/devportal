Supported versions on Aiven
===========================

We aim to offer current, stable versions of all the products on our platform. Aiven aims to follow the deprecation schedule set by the upstream project maintainers. Once the upstream project retires a specific version, that version no longer receives security updates or critical bug fixes. Therefore, we ensure that Aiven services are always running on supported versions of open source software so that our customers have the levels of protection their business needs.

Version numbering
-----------------

Aiven services inherit the upstream project’s software versioning scheme. Depending on the service, a major version can be either a single digit (e.g. PostgreSQL 14) or ``major.minor`` (e.g. Kafka 2.8). The exact version of the service is visible in the Aiven console once the service is up and running.

Current versions
----------------

(all dates in ``YYYY-MM-DD`` format)

.. include:: /includes/eol_table.rst

End-of-life policy for major versions
-------------------------------------

Aiven EOL policy is applicable only for services whose major versions
are controlled by the customer.

It applies to both **powered-on** and **powered-off** services running
the affected versions.

Notification of end-of-life
'''''''''''''''''''''''''''

When Aiven defines the EOL (end-of-life) date for a service major version,

-  Customers will receive an email announcement along with
   instructions on the next steps.

-  Aiven Console will also show an EOL alert for affected services.

-  Email reminders will be sent to customers on a monthly cadence (weekly when the EOL date is imminent).

When end-of-life is reached
'''''''''''''''''''''''''''

-  Affected powered-on services will be **automatically upgraded** to the
   latest available version. For example, if latest version is
   PostgreSQL 14, then upon PostgreSQL 10 EOL, it will be
   upgraded to the latest PostgreSQL 14, instead of PostgreSQL 11.

-  Affected powered-off services will **no longer be accessible** and their
   backups will be deleted.

Recommendations
---------------


We **highly recommend** customers to perform the version upgrade well before EOL so that they can test compatibility for any breaking changes, plan for unforeseen issues, and migrate to the newer version at their own schedule.

Aiven platform offers :doc:`database forking </docs/platform/howto/console-fork-service>` as an efficient tool to verify the version upgrade so that customers can safely test compatibility without committing their production services to a one-way upgrade.

