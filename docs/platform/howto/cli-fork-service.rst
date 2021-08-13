Fork a service using the Aiven client (CLI)
===========================================

Fork your Aiven service in order to make a copy of the database. You can use it to create a development copy of your production environment, set up a snapshot to analyze an issue or test an upgrade, or create an instance in a different cloud/geographical location/under a different plan.


To fork a service using the CLI:

1. Open the Aiven client, and log in ``$ avn user login <you@example.com> --token``.
2. Create a new service using the ``$ avn service create`` command, and add the service_to_fork_from to the configuration arguments, as in the following example:

``avn service create forked -t pg --plan business-4 -c service_to_fork_from=forker``.

You have now copied your Aiven service.
You can now apply any integrations you may need for the copy.