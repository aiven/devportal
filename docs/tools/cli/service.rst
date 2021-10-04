Command reference: ``avn service``
==================================

Here you’ll find the full list of commands for ``avn service``.


Manage service details
-------------------------

Commands for managing Aiven services via ``avn`` commands. 


``avn service acl``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages the Aiven for Apache Kafka ACL entries. 

More information on ``acl-add``, ``acl-delete`` and ``acl-list`` can be found in :doc:`the dedicated page <service/acl>`.

``avn service ca``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves the project CA that the selected service belongs to.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--target-filepath``
    - The file path used to store the CA certificate locally

**Example:** Retrieve the CA certificate for the project where the service named ``kafka-doc`` belongs and store it under ``/tmp/ca.pem``.

::

  avn service ca get kafka-doc --target-filepath /tmp/ca.pem


``avn service cli``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Opens an interactive shell to the given service. Supported only for Aiven for InfluxDB and Aiven for PostgreSQL services.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** Open a new ``psql`` shell connecting to an Aiven for PostgreSQL service named ``pg-doc``.

::

  avn service cli pg-doc

``avn service connection-pool``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages the :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL service.

More information on ``connection-pool-add``, ``connection-pool-delete``, ``connection-pool-list`` and ``connection-pool-update`` can be found in :doc:`the dedicated page <service/connection-pool>`.

``avn service connector``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Set of commands for managing Aiven for Apache Kafka Connect connectors. 

More information on ``connector available``, ``connector create``, ``connector delete``, ``connector list``, ``connector pause``, ``connector restart``, ``connector restart-task``, ``connector resume``, ``connector schema``, ``connector status`` and ``connector update`` can be found in the :doc:`dedicated page <service/connector>`.

``avn service create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--service-type``
    - The type of service; check :ref:`avn-cli-service-type` for more information
  * - ``--plan``
    - Aiven subscription plan name; check :ref:`avn-cloud-list` for more information
  * - ``--cloud``
    - The cloud region name; check :ref:`avn-cloud-list` for more information
  * - ``--no-fail-if-exists``
    - The create command will not fail if a service with the same name already exists
  * - ``--project-vpc-id``
    - Id of the project VPC where to include the created service. The project VPC's cloud must match the service's cloud
  * - ``--no-project-vpc``
    - Stops the service to be included in the project VPC even if one is available in the selected cloud
  * - ``--enable-termination-protection``
    - Enables termination protection for the service
  * - ``-c KEY=VALUE``
    - Additional configuration settings; check :ref:`avn-cli-service-type` for more information

**Example:** Create a new Aiven for Kafka service named ``kafka-demo`` in the region ``google-europe-west3`` with the plan ``business-4`` and enable Kafka Connect.

::
  
  avn service create kafka-demo             \
    --service-type kafka                    \
    --cloud google-europe-west3             \
    --plan business-4                       \
    -c kafka_connect=true                   

``avn service credentials-reset``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Resets the service credentials. More information on user password change is provided in the :doc:`dedicated page <service/user>`.


.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** Reset the credentials of a service named ``kafka-demo``.

::
  
  avn service credentials-reset kafka-demo


``avn service current-queries``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List current service connections/queries for an Aiven for PostgreSQL, Aiven for MySQL or Aiven for Redis service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List the queries running for a service named ``pg-demo``.

::
  
  avn service current-queries pg-demo

``avn service database``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages databases within an Aiven for PostgreSQL, Aiven for MySQL or Aiven for InfluxDB service.

More information on ``database-add``, ``database-delete`` and ``database-list`` can be found in :doc:`the dedicated page <service/database>`.


``avn service es-acl``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages rules to opensearch ACL and extended ACL configuration.

More information on ``es-acl-add``, ``es-acl-del``, ``es-acl-disable``, ``es-acl-enable``, ``es-acl-extended-disable``, ``es-acl-extended-enable`` and ``es-acl-extended-list``  can be found in :doc:`the dedicated page <service/es-acl>`.

``avn service flink``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages Aiven for Apache Flink tables and jobs.

More info on LIST_HERE can be found in :doc:`the dedicated page <service/flink>`.

``avn service get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves a single service details.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--format``
    - Format of the output string

**Example:** Retrieve the ``pg-demo`` service details in the ``'{service_name} {service_uri}'`` format.

::

    avn service get pg-demo --format '{service_name} {service_uri}'

**Example:** Retrieve the ``pg-demo`` full service details in JSON format.

::

    avn service get pg-demo --json


``avn service index``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages Opensearch service indexes.

More information on ``index-delete`` and  ``index-list`` can be found in :doc:`the dedicated page <service/index>`.

``avn service integration``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages Aiven internal and external services integrations.

More information on ``integration-delete``, ``integration-endpoint-create``, ``integration-endpoint-delete``, ``integration-endpoint-list``, ``integration-endpoint-types-list``, ``integration-endpoint-update``, ``integration-list``, ``integration-types-list`` and ``integration-update`` can be found in :doc:`the dedicated page <service/integration>`.

``avn service keypair``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Service keypair commands

``avn service list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists services within an Aiven project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** Retrieve all the services running in the currently selected project.

::

    avn service list

An example of ``account service list`` output:

.. code:: tex

  SERVICE_NAME        SERVICE_TYPE  STATE    CLOUD_NAME           PLAN         CREATE_TIME           UPDATE_TIME
  ==================  ============  =======  ===================  ===========  ====================  ====================
  cassandra-28962a5b  cassandra     RUNNING  google-europe-west3  business-16  2021-09-27T10:18:19Z  2021-09-27T10:25:58Z
  os-24a6d6db         opensearch    RUNNING  google-europe-west3  business-4   2021-09-27T10:18:04Z  2021-09-27T10:23:31Z
  influx-103c3f07     influxdb      RUNNING  google-europe-west3  startup-4    2021-09-27T10:18:13Z  2021-09-27T10:22:05Z
  kafka-2134          kafka         RUNNING  google-europe-west3  business-4   2021-09-27T08:48:35Z  2021-09-27T11:20:55Z
  mysql-12f7628c      mysql         RUNNING  google-europe-west3  business-4   2021-09-27T10:18:09Z  2021-09-27T10:23:02Z
  pg-123456           pg            RUNNING  google-europe-west3  business-4   2021-09-27T07:41:04Z  2021-09-27T10:56:19Z

**Example:** Retrieve all the services with name ``demo-pg`` running in the project named ``mytestproject``.

::

    avn service list demo-pg --project mytestproject


``avn service logs``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves the selected service logs.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** Retrieve the logs for the service named ``pg-demo``.

::

    avn service logs pg-demo

``avn service m3``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Service M3 commands

``avn service maintenance-start``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Start service maintenance updates

``avn service metrics``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Get service metrics

``avn service migration-status``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Get migration status

``avn service plans``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service plans

``avn service privatelink``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Service Privatelink commands

``avn service queries``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service query statistics

``avn service queries-reset``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Reset service query statistics

``avn service schema``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Service Schema commands

``avn service sstableloader``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Service ``sstableloader`` commands

``avn service task-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service task

``avn service task-get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service task

``avn service terminate``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Terminate service

``avn service topic``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages Aiven for Apache Kafka topics.

More information on ``topic-create``, ``topic-delete``, ``topic-list`` and  ``topic-update`` can be found in :doc:`the dedicated page <service/topic>`.


.. _avn-cli-service-type:

``avn service types``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service types

``avn service update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Update service settings

``avn service user``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Manages Aiven users and credentials.

More information on ``user-create``, ``user-creds-download``, ``user-delete``, ``user-get``, ``user-kafka-java-creds``, ``user-list``, ``user-password-reset`` and  ``user-set-access-control`` can be found in :doc:`the dedicated page <service/user>`.


``avn service versions``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

For each service, lists the versions available together with:

* ``STATE``: if the version is ``available`` or ``unavailable``
* ``AVAILABILITY_START_TIME`` and ``AVAILABILITY_END_TIME``: Period in which the specific version is available
* ``AIVEN_END_OF_LIFE_TIME``: Aiven deprecation date for the specific version
* ``UPSTREAM_END_OF_LIFE_TIME``: Upstream deprecation date for the specific version 
* ``TERMINATION_TIME``: Termination time of the active instances
* ``END_OF_LIFE_HELP_ARTICLE_URL``: URL to "End of Life" documentation

**Example:** List all service versions.

::

  avn service versions

An example of ``account service versions`` output:

.. code:: text

    SERVICE_TYPE   MAJOR_VERSION  STATE        AVAILABILITY_START_TIME  AVAILABILITY_END_TIME  AIVEN_END_OF_LIFE_TIME  UPSTREAM_END_OF_LIFE_TIME  TERMINATION_TIME  END_OF_LIFE_HELP_ARTICLE_URL
    =============  =============  ===========  =======================  =====================  ======================  =========================  ================  ====================================================================================================
    cassandra      3.11           available    2018-11-08T00:00:00Z     null                   null                    null                       null              null
    Opensearch     7              unavailable  2020-08-27T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    Opensearch     7.10           unavailable  2021-02-22T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    Opensearch     7.9            unavailable  2020-08-27T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    kafka          2.3            unavailable  2019-09-05T00:00:00Z     2021-08-13T00:00:00Z   2021-08-13T00:00:00Z    null                       null              https://help.aiven.io/en/articles/4472730-eol-instructions-for-aiven-for-kafka
    kafka          2.4            unavailable  2019-10-21T00:00:00Z     2021-08-13T00:00:00Z   2021-08-13T00:00:00Z    null                       null              https://help.aiven.io/en/articles/4472730-eol-instructions-for-aiven-for-kafka
    ...
    pg             12             available    2019-11-18T00:00:00Z     2024-05-14T00:00:00Z   2024-11-14T00:00:00Z    2024-11-14T00:00:00Z       null              https://help.aiven.io/en/articles/2461799-how-to-perform-a-postgresql-in-place-major-version-upgrade
    pg             13             available    2021-02-15T00:00:00Z     2025-05-13T00:00:00Z   2025-11-13T00:00:00Z    2025-11-13T00:00:00Z       null              https://help.aiven.io/en/articles/2461799-how-to-perform-a-postgresql-in-place-major-version-upgrade
    pg             9.6            unavailable  2016-09-29T00:00:00Z     2021-05-11T00:00:00Z   2021-11-11T00:00:00Z    2021-11-11T00:00:00Z       null              https://help.aiven.io/en/articles/2461799-how-to-perform-a-postgresql-in-place-major-version-upgrade

``avn service wait``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Waits for the service to reach the ``RUNNING`` state

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** Wait for the service named ``pg-doc`` to reach the ``RUNNING`` state.

::

  avn service wait pg-doc