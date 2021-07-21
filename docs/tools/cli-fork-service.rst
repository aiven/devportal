Fork a service using the Aiven client (CLI)
===========================================

.. include:: incl-forking-intro.txt

1. Open the Aiven client, and log in::
$ avn user login <you@example.com> --token
2. Create a new service using the ``$ avn service create`` command, and add the service_to_fork_from to the config arguments, as in the following example::
``avn service create forked -t pg --plan business-4 -c service_to_fork_from=forker``

You have now copied your Aiven service.
You can now apply any integrations you may need for the copy.