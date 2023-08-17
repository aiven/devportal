Enable JIT in PostgreSQL®
=========================

PostgreSQL® 11 introduces a new component in the execution engine, a `Just-in-Time (JIT) expression compiler <https://www.postgresql.org/docs/current/jit-reason.html>`_.

By default, the JIT feature is disabled for PostgreSQL 11 and enabled for all the subsequent PostgreSQL versions that Aiven supports. You can change JIT settings in Aiven for PostgreSQL on the global level or just for a specific database.

Enable JIT on the global level
------------------------------

You can enable JIT for the complete Aiven for PostgreSQL service both via `Aiven Console <https://console.aiven.io/>`_ and :doc:`Aiven CLI </docs/tools/cli>`. 

To enable JIT in the `Aiven console <https://console.aiven.io/>`_, take the following steps:

#. Log in to the `Aiven web console <https://console.aiven.io/>`_.
#. From the **Services** page, select the the Aiven for PostgreSQL service where you want to enable JIT.
#. In your service's **Overview** page, scroll down to the **Advanced configuration** settings, and select **Change**.
#. In the **Edit advanced configuration** window, select **Add configuration option**.
#. Select parameter ``pg.jit``, and switch the toggle to ``on``.
#. Select **Save advanced configuration**.

To enable JIT via :doc:`Aiven CLI </docs/tools/cli>`, you can use the :ref:`service update command <avn-cli-service-update>`:

::

    avn service update -c pg.jit=true PG_SERVICE_NAME

Enable JIT for a specific database
----------------------------------

You might not want to use JIT for most simple queries since it would increase the cost. JIT can also be enabled for a single database:

1. Connect to the database where you want to enable JIT. E.g. with ``psql`` and the service URI available in the Aiven for PostgreSQL service overview console page

::

    psql PG_CONNECTION_URI

2. Alter the database (in the example ``mytestdb``) and enable JIT

::

    alter database mytestdb set jit=on;

.. Note::

    The above setting enables JIT by default for a logical database. The default is only applied to new client sessions.

Enable JIT for a specific user
------------------------------

JIT can be enabled also for a specific user:

1. Connect to the database where you want to enable JIT using, for example, ``psql`` and the service URI available in `Aiven Console <https://console.aiven.io/>`_ > the **Overview** page of your Aiven for PostgreSQL service.

::

    psql PG_CONNECTION_URI

2. Alter the role (in the example: ``mytestrole``), and enable JIT.

::

    alter role mytestrole set jit=on;

.. Note::

    The above setting enables JIT by default for a logical database. The default is only applied to new client sessions.

3. Start a new session with the role, and check that JIT is running.

::

    show jit;

The result should be:

::

     jit 
    -----
     on
    (1 row)

4. Run a simple query to test JIT is applied properly.

::

    defaultdb=> explain analyze select sum(row) from table;
                                                                QUERY PLAN                                                     
            
    ------------------------------------------------------------------------------------------------------------------------------
    -----------
    Finalize Aggregate  (cost=10633.55..10633.56 rows=1 width=8) (actual time=299.417..299.418 rows=1 loops=1)
    ->  Gather  (cost=10633.33..10633.54 rows=2 width=8) (actual time=299.111..307.748 rows=3 loops=1)
            Workers Planned: 2
            Workers Launched: 2
            ->  Partial Aggregate  (cost=9633.33..9633.34 rows=1 width=8) (actual time=178.676..178.676 rows=1 loops=3)
                ->  Parallel Seq Scan on bigone  (cost=0.00..8591.67 rows=416667 width=4) (actual time=0.022..89.465 rows=33333
    3 loops=3)
    Planning Time: 0.087 ms
    JIT:
    Functions: 12
    Options: Inlining false, Optimization false, Expressions true, Deforming true
    Timing: Generation 1.878 ms, Inlining 0.000 ms, Optimization 4.438 ms, Emission 44.926 ms, Total 51.243 ms
    Execution Time: 308.777 ms
    (12 rows)

In the above example, a separate JIT section is shown after the planning time. 

.. Tip::

    The last row of the ``explain analyze`` command output above shows the execution time, which could be useful for a benchmark comparison.
