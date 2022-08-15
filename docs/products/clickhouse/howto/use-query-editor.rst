Use the query editor
====================

Aiven for ClickHouse® includes a web-based query editor, which you can find on the *Query Editor* tab of your service in the  `Aiven web console <https://console.aiven.io/>`_.

The requests that you run through the query editor are executed on behalf of the default user and rely on the permissions granted to this user.

Examples of queries
-------------------

Retrieve a list of current databases::

    SHOW DATABASES

Count rows::

    SELECT COUNT(*) FROM transactions.accounts

Create a new role::

    CREATE ROLE accountant

Alternatives
-------------

The query editor is convenient if you want to run queries directly from the console on behalf of the default user. However, if you want to run requests using a different user, or if you expect a large size of the response, you can use :doc:`play <use-play>`, a built-in user interface accessible through HTTPS.
