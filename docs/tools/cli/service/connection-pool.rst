``avn service connection-pool``
==================================================

Here you’ll find the full list of commands for ``avn service connection-pool``.


Manage PgBouncer connection pools
--------------------------------------------------------

``avn service connection-pool-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL® service.

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

**Example:** In the service ``demo-pg`` Create a new connection pool named ``cp-analytics-it`` for the database ``it-analytics`` with:

* username ``avnadmin``
* pool-size of ``10`` connections 
* ``transaction`` pool-mode

::

  avn service connection-pool-create demo-pg \
    --pool-name cp-analytics-it             \
    --dbname analytics-it                   \
    --username avnadmin                     \
    --pool-size 10                          \
    --pool-mode transaction

``avn service connection-pool-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes a :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--pool-name``
    - The name of the connection pool

**Example:** In the service ``demo-pg`` delete a connection pool named ``cp-analytics-it``.

::

  avn service connection-pool-delete demo-pg \
    --pool-name cp-analytics-it             

``avn service connection-pool-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists the :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List the connection pools available in the service ``demo-pg``.

::

  avn service connection-pool-list demo-pg

An example of ``avn service connection-pool-list`` output:

.. code:: text

    POOL_NAME        DATABASE      USERNAME  POOL_MODE    POOL_SIZE
    ===============  ============  ========  ===========  =========
    cp-analytics-it  analytics-it  avnadmin  transaction  10
    cp-sales         sales-it      test-usr  session      20

``avn service connection-pool-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Updates a :doc:`PgBouncer connection pool </docs/products/postgresql/concepts/pg-connection-pooling>` for a given PostgreSQL® service.

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

**Example:** In the service ``demo-pg`` update the connection pool named ``cp-analytics-it`` for the database ``it-analytics`` with:

* username ``avnadmin``
* pool-size of ``20`` connections 
* ``session`` pool-mode

::

  avn service connection-pool-update demo-pg \
    --pool-name cp-analytics-it             \
    --dbname analytics-it                   \
    --username avnadmin                     \
    --pool-size 20                          \
    --pool-mode session
