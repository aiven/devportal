Create an Instance
=========

Aiven provides several different ways to create a PostgreSQL instance: Web-UI, `Command Line Interface <../../tools/cli.html>`_, REST APIs and Terraform Provider.

Web UI
---------------


Aiven CLI
---------------

The ``avn`` client is an ideal way to use Aiven's services in a scriptable way. You can find more resources on how to use it in the `dedicated page <../../tools/cli.html>`_.

A PostgreSQL instance can be created with:

.. code :: bash

  $ avn service create demo-pg    \
      -t pg                       \
      --cloud google-europe-west3 \
      -p business-4


The above creates a PostgreSQL database named ``demo-pg`` in the ``google-europe-west3`` region with a ``business-4`` plan. PostgreSQL service plans available in a specific region can be checked with the following command

::

  $ avn service plans -t pg         \
      --cloud google-europe-west3
