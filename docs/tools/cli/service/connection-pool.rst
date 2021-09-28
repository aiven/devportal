Command reference: ``avn service connection-pool``
==================================================

Here you’ll find the full list of commands for ``avn service connection-pool``.


Manage PgBouncer connection pools
--------------------------------------------------------

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