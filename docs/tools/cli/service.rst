Command reference: ``avn service``
==================================

Here you’ll find the full list of commands for ``avn service``.


Manage service details
-------------------------

Commands for managing Aiven services via ``avn`` commands. 


``avn service acl-add``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Adds an Aiven for Apache Kafka ACL entry.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--permission``
    - The permission type: possible values are ``read``, ``write`` or ``readwrite``
  * - ``--topic``
    - The topic name pattern: accepts ``*`` and ``?`` as wildcard characters
  * - ``--username``
    - The username pattern: accepts ``*`` and ``?`` as wildcard characters

**Example:** Add an ACLs for users with username ending with ``userA`` to ``readwrite`` on topics having name starting with ``topic2020`` in the service``kafka-doc``.

::

  avn service acl-add kafka-doc --username *userA --permission readwrite --topic topic2020*



``avn service acl-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes an Aiven for Apache Kafka ACL entry.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``acl_id``
    - The id of the ACL to delete


**Example:** Delete the ACLs with id ``acl3604f96c74a`` on the Aiven for Apache Kafka instance named ``kafka-doc``.

::

  avn service acl-delete kafka-doc acl3604f96c74a

``avn service acl-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists Aiven for Apache Kafka ACL entries.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List the ACLs defined for a service named ``kafka-doc``.

::

  avn service acl-list kafka-doc


An example of ``account service acl-list`` output:

.. code:: text

    ID              USERNAME  TOPIC      PERMISSION
    ==============  ========  =========  ==========
    default         *         *          admin
    acl3604f96c74a  Jon       orders     readwrite
    acl3604fa706cb  Frida     invoices*  write

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

``avn service connection-pool-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--pool-name``
    - The name of the connection pool
  * - ``--dbname``
    - The name of the database
  * - ``--username``
    - The database username to use for the connection pool
  * - ``--pool-size``
    - Size of the connection pool in number of connections
  * - ``--pool-mode``
    - The :ref:`pool mode <pooling-modes>`. Possible values are ``transaction``, ``session`` and ``statement``

**Example:** In the service ``pg-doc`` Create a new connection pool named ``cp-analytics-it`` for the database ``it-analytics`` with:

* username ``avnadmin``
* pool-size of ``10`` connections 
* ``transaction`` pool-mode

::

  avn service connection-pool-create pg-doc \
    --pool-name cp-analytics-it             \
    --dbname analytics-it                   \
    --username avnadmin                     \
    --pool-size 10                          \
    --pool-mode transaction

``avn service connection-pool-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes a :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--pool-name``
    - The name of the connection pool

**Example:** Delete the connection pool named ``cp-analytics-it`` in the service ``pg-doc``.

::

  avn service connection-pool-delete pg-doc --pool-name cp-analytics-it


``avn service connection-pool-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists the :doc:`PgBouncer connection pools </docs/products/postgresql/concepts/pg-connection-pooling>` available in a given PostgreSQL service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service

**Example:** List the PgBouncer connection pools for the service ``pg-doc``.

::

  avn service connection-pool-list pg-doc 


An example of ``account service connection-pool-list`` output:

.. code:: text

  POOL_NAME        DATABASE   USERNAME  POOL_MODE    POOL_SIZE
  ===============  =========  ========  ===========  =========
  cp-analytics-it  defaultdb  avnadmin  transaction  10


``avn service connection-pool-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Updates a :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--pool-name``
    - The name of the connection pool
  * - ``--dbname``
    - The name of the database
  * - ``--username``
    - The database username to use for the connection pool
  * - ``--pool-size``
    - Size of the connection pool in number of connections
  * - ``--pool-mode``
    - The :ref:`pool mode <pooling-modes>`. Possible values are ``transaction``, ``session`` and ``statement``

**Example:** Update the connection pool named ``cp-analytics-it`` in the service ``pg-doc`` and set the ``--pool-size`` parameter to ``20``.

::
  
  avn service connection-pool-update pg-doc \
    --pool-name cp-analytics-it             \
    --pool-size 20


``avn service connector``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Set of commands for managing Aiven for Apache Kafka Connect connectors. :doc:`See detailed command information <service/connector>` for more information

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

Resets the service credentials.


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

``avn service database-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a database within an Aiven for PostgreSQL, Aiven for MySQL or Aiven for InfluxDB service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--dbname``
    - The name of the database

**Example:** Create a new database named ``analytics-it`` within the service named ``pg-demo``.

::
  
  avn service database-create pg-demo --dbname analytics-it

``avn service database-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Removes a specific database within an Aiven for PostgreSQL, Aiven for MySQL or Aiven for InfluxDB service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--dbname``
    - The name of the database

**Example:** Delete the database named ``analytics-it`` within the service named ``pg-demo``

::

    avn service database-delete pg-demo --dbname analytics-it  

``avn service database-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists the service databases available in an Aiven for PostgreSQL, Aiven for MySQL or Aiven for InfluxDB service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List the service databases within the service named ``pg-demo``

::

    avn service database-list pg-demo

``avn service es-acl-add``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Add rules to opensearch ACL configuration

``avn service es-acl-del``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete rules from opensearch ACL configuration

``avn service es-acl-disable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Disable Opensearch ACL configuration

``avn service es-acl-enable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Enable Opensearch ACL configuration

``avn service es-acl-extended-disable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Disable Opensearch Extended ACL 

``avn service es-acl-extended-enable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Enable Opensearch Extended ACL 

``avn service es-acl-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List Opensearch ACL configuration

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


``avn service index-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete Opensearch service index

``avn service index-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List Opensearch service indexes

``avn service integration-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service integration

``avn service integration-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete a service integration

``avn service integration-endpoint-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service integration endpoint 

``avn service integration-endpoint-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete a service integration endpoint 

``avn service integration-endpoint-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service integration endpoints 

``avn service integration-endpoint-types-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List all available integration endpoint types for given project 

``avn service integration-endpoint-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Update a service integration endpoint 

``avn service integration-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service integrations

``avn service integration-types-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List all available integration types for given project 

``avn service integration-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Update a service integration

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

Service Sstableloader commands

``avn service task-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service task

``avn service task-get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service task

``avn service terminate``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Terminate service

``avn service topic-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a Kafka topic

``avn service topic-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete a Kafka topic

``avn service topic-get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Get Kafka service topic

``avn service topic-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List Kafka service topics

``avn service topic-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Update a Kafka topic


.. _avn-cli-service-type:

``avn service types``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service types

``avn service update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Update service settings

``avn service user-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create service user

``avn service user-creds-download``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Download service user certificate/key/CA certificate 

``avn service user-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete a service user

``avn service user-get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Get details for a single user

``avn service user-kafka-java-creds``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Download user certificate/key/CA certificate and create a Java keystore/truststore/properties from them 

``avn service user-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists the users defined for the selected service, and the related type (``primary`` or ``normal``).

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List the users defined for a service named ``pg-doc``.

::

  avn service user-list pg-doc


An example of ``account service user-list`` output:

.. code:: text

    USERNAME   TYPE
    =========  =======
    analytics  normal
    avnadmin   primary

``avn service user-password-reset``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Resets or changes the service user password.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--username``
    - The username to change the password for
  * - ``--new-password``
    - The new password for the user

**Example:** Change the password for the ``avnadmin`` user of the service named ``pg-doc`` to ``VerySecurePwd123``.

::

  avn service user-password-reset pg-doc --username avnadmin --new-password VerySecurePwd123


``avn service user-set-access-control``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Set Redis service user access control 

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
    Opensearch  7              unavailable  2020-08-27T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    Opensearch  7.10           unavailable  2021-02-22T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    Opensearch  7.9            unavailable  2020-08-27T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
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