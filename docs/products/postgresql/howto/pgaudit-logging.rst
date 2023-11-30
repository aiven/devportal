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

   For more information on the Aiven PostgreSQL® audit logging feature, check out :doc:`Aiven for PostgreSQL® audit logging </docs/products/postgresql/concepts/pg-audit-logging>`.

Prerequisites
-------------

* Pro Platform enabled for your Aiven organization
* Pro Features enabled for your Aiven project
* PostgreSQL version 11 or higher
* ``avnadmin`` superuser role
* Depending on what interface you'd like to use to interact with the feature
  * Access to `Aiven Console <https://console.aiven.io>`_
  * `Aiven API <https://www.postman.com/aiven-apis/workspace/aiven/collection/21112408-1f6306ef-982e-49f8-bdae-4d9fdadbd6cd>`_
  * Terraform
  * :doc:`Aiven CLI client </docs/tools/cli>`
  * SQL

Enable audit logging
--------------------

You can enable audit logging by setting the ``pgaudit.featureEnabled`` parameter to ``true`` in your service's advanced configuration. You can do that using `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, :doc:`Aiven CLI </docs/tools/cli>`, or SQL.

Enable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can enable audit logging at the service level only. To enable it on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io>`_, and navigate to your organization > project > Aiven for PostgreSQL service.
2. On the **Overview** page of your service, select **Service settings** from the sidebar.
3. On the **Service settings** page, navigate to the **Advanced configuration** section and select **Configure**.
4. In the **Advanced configuration** window, select **Add configuration options**, add the ``pgaudit.featureEnabled`` parameter, set it to ``true``, and select **Save configuration**.

Enable with Aiven API
~~~~~~~~~~~~~~~~~~~~~

You can use the `curl` command line tool to interact with :doc:`the Aiven API </docs/tools/api>`. Call the `ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint to update your service's configuration by passing ``{"pgaudit.featureEnabled": "true"}`` in the ``user_config`` object.

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

Enable with SQL
~~~~~~~~~~~~~~~

.. note::

   SQL allows for fine-grained enablement of audit logging: on a database, for a user (role), or for a database-role combination.

Enable on a database
''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER DATABASE DATABASE_NAME set pgaudit.featureEnabled = 'on'

Enable for a user
'''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME SET pgaudit.featureEnabled = 'on'

Enable on a DB for a user
'''''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME IN DATABASE DATABASE_NAME SET pgaudit.featureEnabled = 'on'

Enable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to interact with :doc:`the Aiven API </docs/tools/api>`. Run the :ref:`avn service update <avn-cli-service-update>` command to update your service by setting the ``pgaudit.featureEnabled`` parameter's value to ``true``.

.. code-block:: bash

   avn service update -c pgaudit.featureEnabled=true SERVICE_NAME

.. important::

   By default, audit logging does not emit any audit records. To trigger a logging operation and start receiving audit records, configure audit logging parameters as detailed in :ref:`Configure audit logging <configure-audit-logging>`.

.. _configure-audit-logging:

Configure audit logging
-----------------------

.. note::

   Configuration changes take effect only on new connections.

You can configure audit logging by setting `its parameters <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#readme>`_ using `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, :doc:`Aiven CLI </docs/tools/cli>`, SQL.

.. topic:: Audit logging parameters

   For information on all the parameters available for configuring audit logging, see `Settings <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#settings>`_.

Configure in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can enable audit logging at the service level only. To enable it on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io>`_, and navigate to your organization > project > Aiven for PostgreSQL service.
2. On the **Overview** page of your service, select **Service settings** from the sidebar.
3. On the **Service settings** page, navigate to the **Advanced configuration** section and select **Configure**.
4. In the **Advanced configuration** window, select **Add configuration options**, find a desired parameter (all prefixed with ``pgaudit.log``), set its value as needed, and select **Save configuration**.

Configure with Aiven API
~~~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to configure audit logging on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing desired audit logging parameters in the ``user_config`` object.

.. code-block:: bash

   curl --request PUT                                                                      \
      --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service/YOUR_SERVICE_NAME    \
      --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                                   \
      --header 'content-type: application/json'                                            \
      --data
         '{
            "user_config": {
              "pgaudit": {
                "PARAMETER_NAME": "PARAMETER_VALUE"
              }
            }
          }'

Configure with SQL
~~~~~~~~~~~~~~~~~~

.. note::

   SQL allows for fine-grained configuration of audit logging: on a database, for a user (role), or for a database-role combination.

Configure on a database
'''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER DATABASE DATABASE_NAME SET pgaudit.log_PARAMETER_NAME = PARAMETER_VALUE

Configure for a user
''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME SET pgaudit.log_PARAMETER_NAME = PARAMETER_VALUE

Configure on a DB for a user
''''''''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME IN DATABASE DATABASE_NAME SET pgaudit.log_PARAMETER_NAME = PARAMETER_VALUE

Configure with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to configure audit logging on your service by running the following command:

.. code-block:: bash

   avn service update -c pgaudit.PARAMETER_NAME=PARAMETER_VALUE SERVICE_NAME

Use session audit logging
-------------------------

Session audit logging allows recording detailed logs of all SQL statements and commands executed during a database session in the system's backend.

To enable the session audit logging, run the following query:

.. code-block:: bash

   set pgaudit.log = 'write, ddl';

.. seealso::

   For more details on how to set up, configure, and use session audit logging, check out `Session audit logging <https://github.com/pgaudit/pgaudit/tree/6afeae52d8e4569235bf6088e983d95ec26f13b7#session-audit-logging>`_.

Access your logs
----------------

To access audit logs from Aiven for PostgreSQL, you need to create an integration with a service that allows monitoring and analyzing logs. For that purpose, you can seamlessly integrate Aiven for PostgreSQL with an Aiven for OpenSearch® service.

Use the console
~~~~~~~~~~~~~~~

For instructions on how to integrate your service with Aiven for OpenSearch, see :ref:`Enable log integration <enable-log-integration>`.

Use Aiven CLI
~~~~~~~~~~~~~

You can also use :doc:`Aiven CLI </docs/tools/cli>` to create the service integration.

.. code-block:: bash

   avn service integration-create --project $PG_PROJECT \
     -t logs                                            \
     -s $PG_SERVICE_NAME                                \
     -d $OS_SERVICE_NAME

.. topic:: Results

   After the service integration is set up and propagated to the service configuration, the logs are available in Aiven for OpenSearch. Each log record emitted by audit logging is stored in Aiven for OpenSearch as a single message, which cannot be guaranteed for external integrations such as Remote Syslog.

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

You can disable  audit logging by setting the ``pgaudit.featureEnabled`` parameter to ``false`` in your service's advanced configuration. You can do that at any time using `Aiven Console <https://console.aiven.io>`_, `Aiven API <https://api.aiven.io/doc/>`_, :doc:`Aiven CLI </docs/tools/cli>`, or SQL.

.. important::

   Audit logging gets disabled automatically if you unsubscribe from Pro Platform or Pro Features.

Disable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can disable audit logging at the service level only. To disable it on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io>`_, and navigate to your organization > project > Aiven for PostgreSQL service.
2. On the **Overview** page of your service, select **Service settings** from the sidebar.
3. On the **Service settings** page, navigate to the **Advanced configuration** section and select **Configure**.
4. In the **Advanced configuration** window, select **Add configuration options**, add the ``pgaudit.featureEnabled`` parameter, set it to ``false``, and select **Save configuration**.

Disable with Aiven API
~~~~~~~~~~~~~~~~~~~~~~

You can use the `curl` command line tool to interact with :doc:`the Aiven API </docs/tools/api>`. Call the `ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint to update your service's configuration by passing ``{"pgaudit.featureEnabled": "false"}`` in the ``user_config`` object.

.. code-block:: bash

   curl --request PUT                                                                      \
      --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service/YOUR_SERVICE_NAME    \
      --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                                   \
      --header 'content-type: application/json'                                            \
      --data
         '{
            "user_config": {
               "pgaudit.featureEnabled": "false"
            }
         }'

Disable with SQL
~~~~~~~~~~~~~~~~

.. note::

   SQL allows you to disable audit logging on a few levels: database, user (role), or database-role combination.

Disable on a database
'''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER DATABASE DATABASE_NAME set pgaudit.featureEnabled = 'off'

Disable for a user
''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME SET pgaudit.featureEnabled = 'off'

Disable on a DB for a user
''''''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME IN DATABASE DATABASE_NAME SET pgaudit.featureEnabled = 'off'

Disable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to interact with :doc:`the Aiven API </docs/tools/api>`. Run the :ref:`avn service update <avn-cli-service-update>` command to update your service by setting the ``pgaudit.featureEnabled`` parameter's value to ``false``.

.. code-block:: bash

   avn service update -c pgaudit.featureEnabled=false SERVICE_NAME
