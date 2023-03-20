Collect audit logs in Aiven for PostgreSQL®
===========================================

.. important::

   Aiven for PostgreSQL® audit logging is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Learn how to enable and configure the Aiven for PostgreSQL® audit logging feature on your Aiven for PostgreSQL service. Find out how to access and visualize your logs.

About audit logging
-------------------

The audit logging feature allows you to monitor and track activities within relational database systems, which helps to achieve the following:
  
* Data security and integrity
* Detection and prevention of an unauthorized access, data breaches, and unexpected changes
* Identification of a potential fraud or misuse
* Compliance with regulations and standards required either by an industry or a government
* Accountability (by user and change tracking)
* Improved incident management and root cause analysis
* :doc:`Other </docs/products/postgresql/concepts/pg-audit-logging>`

.. seealso::

   For more information on the PostgreSQL® audit logging feature, check out :doc:`PostgreSQL® audit logging </docs/products/postgresql/concepts/pg-audit-logging>`.

Enable audit logging
--------------------

You can enable the audit logging by setting the ``pgaudit.featureEnabled`` parameter to ``true`` in your service's advanced configuration. You can do that using `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, or :doc:`Aiven CLI </docs/tools/cli>`.

Prerequisites
'''''''''''''

* Aiven for PostgreSQL Pro Plan
* PostgreSQL version 11 or higher
* ``avnadmin`` role
* :doc:`Aiven CLI </docs/tools/cli>` / ``psql``

Enable audit logs in Aiven Console
''''''''''''''''''''''''''''''''''

1. Go to `Aiven Console <https://console.aiven.io>`_ > organization > project > Aiven for PostgreSQL service > **Overview** > **Advanced configuration** > **Change** > **Add configuration option**.
2. Add the ``pgaudit.featureEnabled`` parameter and set it to ``true``.
3. Save the updated configuration.

Enable audit logs with Aiven CLI
''''''''''''''''''''''''''''''''

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to interact with :doc:`the Aiven API </docs/tools/api>`. Run the :ref:`avn service update <avn-cli-service-update>` command to update your service by setting the ``pgaudit.featureEnabled`` parameter's value to ``true``.

.. code-block:: bash

   avn service update demo-pg        \
     -c pgaudit.featureEnabled=true

Enable audit logs with Aiven API
''''''''''''''''''''''''''''''''

You can use the `curl` command line tool to interact with :doc:`the Aiven API </docs/tools/api>`. Use the `ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint to update your service's configuration by setting the ``pgaudit.featureEnabled`` parameter's value to ``true``.

.. code-block:: bash

   curl --request PUT                                                                      \
      --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service/YOUR_SERVICE_NAME    \
      --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                                   \
      --header 'content-type: application/json'                                            \
      --data
         '{
            "user_config": {
               "pgaudit.featureEnabled": "true"
            }
         }'

..
   .. note::

      Configuration changes take effect only on new connections.

   To configure the audit logging, use the ``aiven-extras`` extension and its ``set_pgaudit_parameter()`` function on the service level.

   1. Use :doc:`Aiven CLI </docs/tools/cli>` (or :doc:`psql </docs/products/postgresql/howto/connect-psql>`) to connect to your instance.

      .. code-block:: bash

         avn service cli --project $PG_PROJECT $PG_SERVICE_NAME

   2. Enable ``pgaudit`` and ``aiven-extras`` extensions.

      .. code-block:: bash

         CREATE EXTENSION pgaudit CASCADE;
         CREATE EXTENSION aiven_extras CASCADE;

   3. Use ``aiven_extras.set_pgaudit_parameter()`` to configure the audit logging.

      .. note::

         By default, the audit logging does not emit any audit records.

      To enable the logging and start getting audit records, configure relevant parameters using ``set_pgaudit_parameter`` with the parameter and the target database name.

      .. code-block:: bash

         SELECT aiven_extras.set_pgaudit_parameter('log', 'defaultdb', 'all, -misc');

Configure audit logging
-----------------------

You can configure the audit logging by setting different `audit logging parameters <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#readme>`_ to in your service's advanced configuration. You can do that using `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, or :doc:`Aiven CLI </docs/tools/cli>`.

.. topic:: Audit logging parameters

    For information on all the parameters available for configuring the audit logging, see `Settings <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#readme>`_.

Prerequisites
'''''''''''''

* Aiven for PostgreSQL Pro Plan
* PostgreSQL version 11 or higher
* ``avnadmin`` superuser role
* :doc:`Aiven CLI </docs/tools/cli>` / ``psql``

Configure audit logs in Aiven Console
'''''''''''''''''''''''''''''''''''''

1. Go to `Aiven Console <https://console.aiven.io>`_ > organization > project > Aiven for PostgreSQL service > **Overview** > **Advanced configuration** > **Change** > **Add configuration option**.
2. Add a parameter and set it as needed.
3. Save the updated configuration.

Configure audit logs with Aiven CLI
'''''''''''''''''''''''''''''''''''

Configure audit logs with Aiven API
'''''''''''''''''''''''''''''''''''

Configure the session audit logging
'''''''''''''''''''''''''''''''''''

The session audit logging allows recording detailed logs of all SQL statements and commands executed during a database session in the backend of a system.

Before enabling the session audit logging, make sure your setup meets the following prerequisites:

* Aiven for PostgreSQL Pro Plan
* Aiven for PostgreSQL version 11 or higher
* ``avnadmin`` superuser role
* SQL interface

To enable the session audit logging, run the following query:

.. code-block:: bash

   set pgaudit.log = 'write, ddl';

Access your logs
----------------

To access audit logs from Aiven for PostgreSQL, you need to create an integration with a service that allows monitoring and analyzing logs. For that purpose, you can seamlessly integrate Aiven for PostgreSQL with an Aiven for OpenSearch® service.

Use the console
'''''''''''''''

For instructions on how to integrate your service with Aiven for OpenSearch, see :ref:`Enable log integration <enable-log-integration>`.

Use Aiven CLI
'''''''''''''

You can also use :doc:`Aiven CLI </docs/tools/cli>` to create the service integration.

.. code-block:: bash

   avn service integration-create --project $PG_PROJECT \
     -t logs                                            \
     -s $PG_SERVICE_NAME                                \
     -d $OS_SERVICE_NAME

.. topic:: Results

   After the service integration is set up and propagated to the service configuration, the logs are available in Aiven for OpenSearch. Each log record emitted by the audit logging is stored in Aiven for OpenSearch as a single message, which cannot be guaranteed for external integrations such as Remote Syslog.

Visualize your logs
-------------------

Since your logs are already available in Aiven for OpenSearch, you can use :doc:`OpenSearch Dashboards </docs/products/opensearch/dashboards>` to visualize them. Check out how to access OpenSearch Dashboards in :ref:`Access OpenSearch Dashboards <access-os-dashboards>`. For instructions on how to start using OpenSearch Dashboards, see :doc:`Getting started </docs/products/opensearch/dashboards/getting-started>`.

To preview your audit logs in OpenSearch Dashboards, use the filtering tool by selecting ``AIVEN_AUDIT_FROM``, setting its value to `pg`, and applying the filter.

.. image:: /images/products/postgresql/pgaudit-logs-in-os-dashboards.png
   :alt: Audit logging logs in OpenSearch Dashboards

.. note::

   If the index pattern in OpenSearch Dashboards had been configured before you enabled the service integration, the audit-specific AIVEN_AUDIT_FROM field is not available for filtering. Refresh the fields list for the index in OpenSearch Dashboards under **Stack Management** → **Index Patterns** → Your index pattern → **Refresh field list**.

.. _disable-pgaudit:

Disable audit logging
---------------------

You can disable the audit logging on your database or service by setting the ``pgaudit.featureEnabled`` parameter to ``false`` in your service's advanced configuration. You can do that at any time using `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, or :doc:`Aiven CLI </docs/tools/cli>`.

.. note::

   The audit logging is disable automatically if you unsubscribe the service from Pro Plan.
