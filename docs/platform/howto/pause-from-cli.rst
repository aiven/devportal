Pause or terminate your service
===============================

One of the nice things about cloud services is that they can be created and destroyed easily, or just paused while you aren't using them so that you aren't being charged (or using up your trial credits).

One option is to power the service off temporarily. This way you can come back and play with the cluster later without wasting your credits while the service is idle.

You can update the state of your service either through the service overview page in the `Aiven console <https://console.aiven.io>`_ or by using Aiven command line interface:

::

    avn service update demo-open-search --power-off


When you're ready to continue using the service run the command to power it on. Use ``wait`` command to easily see when the service is up and running.

::

    avn service update demo-open-search --power-on
    avn service wait demo-open-search


If you have finished exploring your OpenSearch® service, you can destroy or "terminate" the service. To terminate the service completely use the following command:

::

    avn service terminate demo-open-search

You will be prompted to re-enter the service name to confirm that you want to complete the termination.
