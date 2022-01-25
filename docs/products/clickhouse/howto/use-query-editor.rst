Use query editor
================

A web-based query editor accompanies your ClickHouse service. It can be found in the in the *Query Editor* tab of your service in the  `Aiven web console <https://console.aiven.io/>`_.

The requests that are run through the query editor are executed on behalf of the default user, relying on the permissions which this user possesses.

Examples of queries
-------------------

Retrieve a list of present databases::

    SHOW DATABASES

Count rows::

    SELECT COUNT(*) FROM transactions.accounts

Create a new role::

    CREATE ROLE accountant
