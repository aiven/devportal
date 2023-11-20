Optimize PostgreSQL® performance with pg_qualstats
==================================================

Discover the pg_qualstats extension and its capabilities. Check its applications, and learn how it might help you optimize your database performance. Find out how pg_qualstats works and how to use it with your Aiven for PostgreSQL® service.

About pg_qualstats
------------------

The pg_qualstats extension collects statistics on predicates in active SQL queries. The gathered statistics can be used to identify missing indexes and produce automated suggestions for creating these indexes, which might help with index optimization and reduce a manual effort on the same.

.. seealso::

   For more information on pg_qualstats, check `powa-team's pg_qualstats <https://github.com/powa-team/pg_qualstats>`_.

Why use it
----------

Statistics collected by pg_qualstats can be used for producing index creation recommendations, which might have the following benefits:

* Reducing the need to use tools or techniques for alleviating index-related performance issues
* Offloading you from continual monitoring, verifying, and identifying missing indexes manually
* Enhancing query and database performance (faster queries faster and more affordable services)

How it works
------------

The primary task of the pg_qualstats extension is to collect statistics on predicates in active PostgreSQL queries. pg_qualstats uses a distinctive method of gathering statistics on predicates in WHERE statements and JOIN clauses, as opposed to the traditional approach of statistically analyzing full queries based on the total execution time. The novel approach that pg_qualstats uses allows the identification of frequently executed predicates (``quals``), which constitute an input for identifying missing indexes and producing index creation recommendations.

.. topic:: Flow of actions

    1. You enable pg_qualstats on your service, database, or user (role).
    2. You configure pg_qualstats parameters if the default values don't match your use case.
    3. pg_qualstats starts analyzing active Aiven for PostgreSQL queries on a service, within a database, or for a user.
    4. Based on the analysis, pg_qualstats produces and stores results by populating statistics and making them accessible for your queries.
    5. You execute read-only functions and select from predefined views to retrieve insights on missing indexes or index creation suggestions.

.. seealso::

   For more information on how pg_qualstats works, check `powa-team's pg_qualstats <https://github.com/powa-team/pg_qualstats>`_.

Prerequisites
-------------

* Aiven organization, project, and service (Aiven for PostgreSQL)
* Depending on what interface you'd like to use for interacting with pg_qualstats, you might need the following:
    * Access to `Aiven Console <https://console.aiven.io/>`_
    * SQL
    * `Aiven API <https://api.aiven.io/doc/>`_
    * :doc:`Aiven CLI client </docs/tools/cli>`

Enable pg_qualstats
-------------------

You can enable the extension in `Aiven Console <https://console.aiven.io/>`_, using SQL, Aiven API, or Aiven CLI.

Enable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can enable pg_qualstats at the service level only. To enable the extension on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, navigate to **Advanced configuration** > **Configure** > **Add configuration options**.
3. Find the **pg_qualstats.enabled** parameter, set it to **true**, and select **Save configuration**.

Enable with SQL
~~~~~~~~~~~~~~~

.. note::

   SQL allows for fine-grained enablement of pg_qualstats: on a database, for a user (role), or for a database-role combination.

Enable on a database
''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER DATABASE DATABASE_NAME set pg_qualstats.enabled = 'on'

Enable for a user
'''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME SET pg_qualstats.enabled = 'on'

Enable on a DB for a user
'''''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME IN DATABASE DATABASE_NAME SET pg_qualstats.enabled = 'on'

Enable with Aiven API
~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to enable pg_qualstats on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing ``{"pg_qualstats": {"enabled": true}}`` in the ``user_config`` object.

Enable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to enable pg_qualstats for your service by running the following command:

.. code-block:: bash

   avn service update -c pg_qualstats.enabled=true SERVICE_NAME

Configure pg_qualstats
----------------------

Pg_qualstats is pre-configured with default settings but you can modify its configuration parameters in `Aiven Console <https://console.aiven.io/>`_, with SQL, using Aiven API, or Aiven CLI.

You might want to configure the following parameters:

* ``pg_qualstats.enabled`` (to enable or disable the pg_qualstats extension)
* ``pg_qualstats.track_pg_catalog`` (to enable or disable pg_qualstats on pg_catalog)
* ``pg_qualstats.sample_rate`` (to set the granularity of pg_qualstats analysis and statistics returned)
    * Allowed values: ``0`` - ``1``, where ``1`` means analysis and statistics on every single query, and ``0`` means there are no queries analysed.
    * Default value: ``1/max_connections``
* ``pg_qualstats.track_constants`` (to enable or disable pg_qualstats on constants)

.. topic:: Sample pg_qualstats configuration
   
   .. code-block:: bash

      pg_qualstats.enabled = on
      pg_qualstats.sample_rate = 0.1

.. seealso::

   For more confuguration options, check `powa-team's pg_qualstats configuration <https://github.com/powa-team/pg_qualstats>`_.

Configure in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can configure pg_qualstats at the service level only. To configure the extension on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, navigate to **Advanced configuration** > **Configure** > **Add configuration options**.
3. Find a desired pg_qualstats parameter (all prefixed with ``pg_qualstats``), set its value as needed, and select **Save configuration**.

Configure with SQL
~~~~~~~~~~~~~~~~~~

.. note::

   SQL allows for a fine-grained configuration of pg_qualstats: on a database, for a user (role), or for a database-role combination.

Configure on a database
'''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER DATABASE DATABASE_NAME SET pg_qualstats.PARAMETER_NAME = PARAMETER_VALUE

Configure for a user
''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME SET pg_qualstats.PARAMETER_NAME = PARAMETER_VALUE

Configure on a DB for a user
''''''''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME IN DATABASE DATABASE_NAME SET pg_qualstats.PARAMETER_NAME = PARAMETER_VALUE

Configure with Aiven API
~~~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to configure pg_qualstats on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing desired pg_qualstats parameters in the ``user_config`` object.

Configure with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to configure pg_qualstats on your service by running the following command:

.. code-block:: bash

   avn service update -c pg_qualstats.PARAMETER_NAME=PARAMETER_VALUE SERVICE_NAME

Use pg_qualstats
----------------

The pg_qualstats extension defines SQL functions and views that you can interact with via the standard SQL interface.

.. note::

   To use the index suggestion function, pg_qualstats needs to be enabled on a database that you want to query for statistics associated to this database.

Execute read-only functions, and select from predefined views to retrieve insights or index suggestions.

.. topic:: Example of using the index advisor to acquire recommendations on what indexes to create

   .. code-block:: bash

      SELECT v
      FROM json_array_elements(
         pg_qualstats_index_advisor(min_filter => 50)->'indexes') v
      ORDER BY v::text COLLATE "C";
                                    v
      ---------------------------------------------------------------
      "CREATE INDEX ON public.adv USING btree (id1)"
      "CREATE INDEX ON public.adv USING btree (val, id1, id2, id3)"
      "CREATE INDEX ON public.pgqs USING btree (id)"
      (3 rows)

      SELECT v
      FROM json_array_elements(
         pg_qualstats_index_advisor(min_filter => 50)->'unoptimised') v
      ORDER BY v::text COLLATE "C";
            v
      -----------------
      "adv.val ~~* ?"
      (1 row)

.. seealso::

   For more information on how to use pg_qualstats, check `powa-team's pg_qualstats usage <https://github.com/powa-team/pg_qualstats>`_.

Disable pg_qualstats
--------------------

You can disable the extension in `Aiven Console <https://console.aiven.io/>`_, using SQL, Aiven API, or Aiven CLI.

Disable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can disable pg_qualstats at the service level only, which deactivates the extension globally for the whole service: all the databases and user roles in this service. To disable the extension on a particular database or for a specific user only, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, navigate to **Advanced configuration** > **Configure** > **Add configuration options**.
3. Find the **pg_qualstats.enabled** parameter, set it to **false**, and select **Save configuration**.

Disable with SQL
~~~~~~~~~~~~~~~~

.. note::

   SQL allows for fine-grained disablement of pg_qualstats: on a database, for a user (role), or for a database-role combination.

Disable on a database
'''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER DATABASE DATABASE_NAME SET pg_qualstats.enabled = 'off'

Disable for a user
''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME SET pg_qualstats.enabled = 'off'

Disable on a DB for a user
''''''''''''''''''''''''''

1. :doc:`Connect to your Aiven for PostgreSQL service </docs/products/postgresql/howto/list-code-samples>`.

2. Run the following query:

   .. code-block:: bash

      ALTER ROLE ROLE_NAME IN DATABASE DATABASE_NAME SET pg_qualstats.enabled = 'off'

Disable with Aiven API
~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to disable pg_qualstats on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing ``{"pg_qualstats": {"enabled": false}}`` in the ``user_config`` object.

Disable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to disable pg_qualstats on your service by running the following command:

.. code-block:: bash

   avn service update -c pg_qualstats.enabled=false SERVICE_NAME

Related reading
---------------

* `pg_qualstats readme <https://github.com/powa-team/pg_qualstats>`_
* :doc:`Extensions on Aiven for PostgreSQL </docs/products/postgresql/reference/list-of-extensions>`
