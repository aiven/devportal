Aiven for PostgreSQL® audit logging
===================================

.. important::

   Aiven for PostgreSQL® audit logging is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Discover the Aiven for PostgreSQL® audit logging feature and its capabilities. Learn why use it and how it works.

.. seealso::

   For information on how to enable the audit logging on your Aiven for PostgreSQL service and how to access and visualize your logs, check out :doc:`Collect audit logs in Aiven for PostgreSQL® </docs/products/postgresql/howto/pgaudit-logging>`.

About audit logging
-------------------

The audit logging feature allows you to monitor and track activities within rellational database systems, which helps you cope with unauthorized access, data breaches, or fraudulent activities ensuring data integrity and security. Using audit logs enables you to maintain compliance with regulations and standards set by a government or an industry. The audit logging is also a tool for investigating and resolving data discrepancies, troubleshooting system errors, and optimizing database performance. For more applications of the audit logging feature, check out :ref:`Why use the audit logging <why-use-pgaudit>`.

.. _why-use-pgaudit:

Why use audit logging
---------------------

There are multiple reasons why you may want to use the audit logging. Note the following benefits of using this feature:

Data Security
* Monitor user activities to identify unusual or suspicious behavior
* Detect unauthorized access attempts to critical data or systems
* Identify intrusion attempts or unauthorized activities within the organization's IT environment

Compliance
* Use audit logs as a regulatory compliance evidence to demonstrate that the organization meets industry or state regulations during audits
* Track access to sensitive data to comply with data privacy regulations

Accountability
* Have specific actions attributed to individual users to hold them accountable for their activities within the system
* Track changes to databases and systems to hold users accountable for alterations or configurations

Operational security
* Monitor and analyze audit logs to proactively identify and resolve security incidents
* Analyze audit logs to detect and respond to potential security threats

Incident management and root cause analysis
* Investigate an incident with audit logs as a detailed trail of events leading up to the incidents
* Analyze the root cause of an incident with audit logs providing data on actions and events that may have led to the incident

System performance optimization
* Monitor and analyze system performance to identify bottlenecks.
* Analyzing audit logs to assess resource utilization patterns and optimize the system configuration

Data recovery and disaster planning
* Use audit logs for data restoration in case of data loss or system failure
* Analyze audit logs to improve system resilience and disaster planning strategies by identify potential points of failure

Change management and version control
* Use audit logs to keep a record of changes made to databases, software, and configurations, ensuring a proper version control

Use cases
---------

Typically, capabilities of the audit logging feature are most appreciated by organizations or enterprises that value data security, integrity, and compliance. The audit logging has a wide range of applications in various industries:

Finance and banking
  Ensuring compliance with regulatory requirements, tracking financial transactions, and detecting fraudulent activities
Healthcare
  Maintaining the confidentiality and integrity of patient records as well as complying with privacy regulations
Government and public sector
  Tracking changes in critical systems, secure sensitive data, and meet legal and regulatory requirements
Information technology (IT) and software companies
  Monitoring access to the systems, tracking software changes, and identifying potential security breaches
Retail and e-commerce
  Tracking customer data, transactions, and inventory management to ensure data integrity and prevent unauthorized access
Manufacturing
  Tracking changes to production processes, monitoring equipment performance, and maintaining data integrity for quality control
Education
  Protecting sensitive student data, tracking changes to academic records, and monitoring system access for security purposes

How it works
------------

Before you start
''''''''''''''''

You can enable, configure, and use the audit logging feature on the service level or the database level with Aiven for PostgreSQL 11+ Pro Plan as an ``avnadmin`` superuser.

Enable with predefined settings
'''''''''''''''''''''''''''''''

To use the audit logging on your service (database) for collecting logs in Aiven for PostgreSQL, you need to :doc:`enable and configure this feature </docs/products/postgresql/howto/pgaudit-logging>` in `Aiven Console <https://console.aiven.io>`_, via `Aiven API <https://api.aiven.io/doc/>`_, or with :doc:`Aiven CLI </docs/tools/cli>`.

Configure for your use case
'''''''''''''''''''''''''''

When enabled on your service, the audit logging can be configured so that it addresses your specific needs. There are a few `audit logging parameters <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#readme>`_ that you might want to configure for that purpose:

``pgaudit.targetDatabases``
  Names of databases where the audit logging is to be enabled
``pgaudit.log`` (default: none)
  Classes of statements to be logged by the session audit logging
``pgaudit.log_catalog`` (default: on)	
  Whether the session audit logging should be enabled for a statement with all relations in pg_catalog
``pgaudit.log_client``
  Whether log messages should be visible to a client process, such as ``psql``
``pgaudit.log_level``
  Log level that should be used for log entries
``pgaudit.log_parameter`` (default: off)
  Whether audit logs should include the parameters passed with the statement
``pgaudit.log_parameter_max_size`` 
  Maximum size (in bytes) of a parameter's value that can be logged
``pgaudit.log_relation`` (default: off)
  Whether a separate log entry for each relation (for example, TABLE or VIEW) referenced in a SELECT or DML statement should be created
``pgaudit.log_rows``
  Whether the audit logging should include the rows retrieved or affected by a statement (with the rows field located after the parameter field)
``pgaudit.log_statement`` (default: on)
  Whether the audit logging should include the statement text and parameters
``pgaudit.log_statement_once`` (default: off)
  Whether the audit logging should include the statement text and parameters in the first log entry for a statement/ sub-statement combination (as opposed to including them in all the entries)
``pgaudit.role``
  Master role to use for an object audit logging

.. topic:: Full list of audit logging parameters

    For information on all the parameters available for configuring the audit logging, see `Settings <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#readme>`_.

Collect and visualize logs
''''''''''''''''''''''''''

You can access the collected logs by :ref:`integrating with a service monitoring and analyzing logs, for example, Aiven for OpenSearch® <enable-log-integration>`. Finally, to visuaize your logs, you can use :doc:`OpenSearch Dashboards </docs/products/opensearch/dashboards>`.

Disable if no longer neeeded
''''''''''''''''''''''''''''

To disable the audit logging on your service (database), you can use `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, or :doc:`Aiven CLI </docs/tools/cli>` for :ref:`modifying your service's advanced configuration <disable-pgaudit>`. 

Limitations
-----------

To be able to activate, configure, and use the audit logging, you need the following:

* Pro Platform enabled for your Aiven organization
* Pro Features enabled for your Aiven project
* PostgreSQL version 11 or higher
* ``avnadmin`` superuser role

What's next
-----------

:doc:`Set up the audit logging on your Aiven for PostgreSQL service </docs/products/postgresql/howto/pgaudit-logging>` and start collecting audit logs.
