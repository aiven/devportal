Log integration with Loggly
===========================

Aiven supports integrating logs with a number of external monitoring
systems that support rsyslog protocol, including `Loggly <https://www.loggly.com/>`_.

To integrate your service with Loggly, a new endpoint needs to be added
into the project that contains the service you want to integrate. This
can be done using through Aiven console or command line using :doc:`Aiven
CLI </docs/tools/cli>`.

Prerequisites
-------------

Before creating the integration, you will need to generate a Loggly **customer token** . From the Loggly dashboard: 

* Navigate to **Source Setup** tab
* Select **Customer Token** tab underneath it. 
* Generate a new custom token (or use a previously generated one) and copy its value.

Define the Loggly integration endpoint
--------------------------------------

To create a Loggly integration using the `Aiven Console <https://console.aiven.io>`_: 

* Select the Project where the integration needs to be defined
* Select **Integration Endpoints** 
* Navigate to **Syslog** configuration
* Define a new endpoint with the following parameters
  
  * **Endpoint name** - the name for the endpoint (for example ``Loggly``)
  * **Server** - the Loggly hostname ``logs-01.loggly.com``
  * **Port** - the Loggly port ``514``
  * **TLS** - disabled (see below how to enable TLS with avn client)
  * **Format** - ``rfc5424``
  * **Structured Data** - ``TOKEN@NNNNN TAG="your-tag"`` replacing
    
    * ``TOKEN`` needs to be replaced with your Loggly **customer token** retrieved in the prerequisite stage
    * ``NNNNN`` is Loggly Private Enterprise Number (PEN) which is ``41058`` (check `Loggly documentation <https://www.loggly.com/docs/streaming-syslog-without-using-files/>`_ for up to date information)
    * ``your-tag`` with any arbitrary tag value wrapped in double quotes

.. Tip::

   You can automate the creation of a Loggly integration endpoint using the :ref:`Aiven CLI dedicated command <avn_service_integration_endpoint_create>`.

Enable the Loggly integration
-----------------------------

To enable the Loggly integration for a particular Aiven service:

* Open the service details in the `Aiven Console <https://console.aiven.io>`_
* Browse to the **Service Integrations** option
* Click **Manage Integrations** which will bring up a list of available integrations for your service
* Select **Rsyslog** from the provided list
* Click **Use integration** 
* Select the Loggly endpoint that you created in previous step
* Click **Enable** to enable service integration.

After enabling this service integration, it will be shown as active in the `Aiven Console <https://console.aiven.io>`_, and the logs will be now integrated with Loggly. 

.. Note::

   It may take a few moments to setup the new log, and you can track the status in your service overview.

Your logs should now be visible on Loggly **Search** tab. Enter the tag name your previously specified (e.g. ``tag:your-tag`` ) and it will populate the dashboard with the log events from the Aiven service.

.. Tip::

   You can automate the creation of the Loggly integration using the :ref:`Aiven CLI dedicated command <avn_service_integration_create>`. 