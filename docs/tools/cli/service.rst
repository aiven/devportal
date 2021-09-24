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
    - ``--permission``
    - The permission type: possible values are ``read``, ``write`` or ``readwrite``
    - ``--topic``
    - The topic name pattern: accepts ``*`` and ``?`` as wildcard characters
    - ``--username``
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

Create a connection pool for a given PostgreSQL service 

``avn service connection-pool-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete a connection pool from a given service 

``avn service connection-pool-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List PGBouncer pools for a service 

``avn service connection-pool-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Update a connection pool for a given PostgreSQL service 

``avn service connector``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Service Connector commands

``avn service create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a service

``avn service credentials-reset``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Reset service credentials

``avn service current-queries``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List current service connections/queries

``avn service database-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Create a database within a given service

``avn service database-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete a database within a given service

``avn service database-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List service databases

``avn service es-acl-add``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Add rules to elastic ACL configuration

``avn service es-acl-del``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete rules from elastic ACL configuration

``avn service es-acl-disable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Disable Elasticsearch ACL configuration

``avn service es-acl-enable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Enable Elasticsearch ACL configuration

``avn service es-acl-extended-disable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Disable Elasticsearch Extended ACL 

``avn service es-acl-extended-enable``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Enable Elasticsearch Extended ACL 

``avn service es-acl-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List Elasticsearch ACL configuration

``avn service get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Show a single service

``avn service index-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Delete Elasticsearch service index

``avn service index-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List Elasticsearch service indexes

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

Service Keypair commands

``avn service list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

List services

``avn service logs``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

View project logs

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
    elasticsearch  7              unavailable  2020-08-27T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    elasticsearch  7.10           unavailable  2021-02-22T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
    elasticsearch  7.9            unavailable  2020-08-27T00:00:00Z     2021-09-23T00:00:00Z   2022-03-23T00:00:00Z    null                       null              https://help.aiven.io/en/articles/5424825
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