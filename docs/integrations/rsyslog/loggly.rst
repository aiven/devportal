Log integration with Loggly
===========================

Aiven supports integrating logs with a number of external monitoring
systems that support rsyslog protocol, including Loggly.

To integrate your service with Loggly, a new endpoint needs to be added
into the project that contains the service you want to integrate. This
can be done using through Aiven console or command line using `Aiven
Client <https://github.com/aiven/aiven-client>`__ .

.. note:: 
  Before adding an endpoint, you will need to generate a **customer
  token** . From the Loggly dashboard, navigate to **Source Setup** tab
  and then select **Customer Token** tab underneath it. Generate a new
  custom token (or use a previously generated one) and copy its value.

Integrate with Loggly using the Aiven Console
---------------------------------------------

Navigate to https://console.aiven.io, select your Project and select **Service Integrations** on the left hand side and navigate to **Syslog** configuration.

When defining a new endpoint, the following parameters can be applied

-  **name** - Create a name for this endpoint (e.g. Loggly)

-  **server** - set to `logs-01.loggly.com`

-  **port** - 514

-  **tls** - disable (please see below how to enable TLS with avn
   client)

-  **format** - set to `rfc5424``

-  **structured data** - TOKEN@NNNNN TAG="your-tag" 

.. note:: 
  `TOKEN` needs to be replaced with your Loggly **customer token** and `NNNNN`` is Loggly Private Enterprise Number (PEN) which is **41058** (check `Loggly documentation <https://www.loggly.com/docs/streaming-syslog-without-using-files/>`__ for up to date information). **TAG** can be any arbitrary value wrapped in double quotes.

Next, open your service in Aiven console and under **Service Integrations** option, click **Manage Integrations** which will bring up a list of available integrations for your service. Select **Rsyslog** from the provided list and click **Use integration** .

Finally, select the endpoint that you created in previous step and click **Enable** to enable service integration.

After enabling this service integration, you can see that it has been
activated in the Aiven console and the logs will be now integrated
with Loggly. It may take a few moments to setup the new log, and you
can track the status in your service overview.

Your logs should now be visible on Loggly **Search** tab. Enter the tag name your previously specified (e.g. *tag:your-tag* ) and it will populate the dashboard with the log events from your service.

Integrate with Loggly using the Aiven client
--------------------------------------------

From the Aiven client, enter the following command, replacing values as
specified below. In addition to the server and port you also need a
*customer token* which you then **need** to give as part of the sd
parameter when creating the endpoint.

.. code-block:: bash

   avn service integration-endpoint-create --project your-project \
      -d loggly -t rsyslog \
      -c server=logs-01.loggly.com -c port=6514 \
      -c format=rfc5424 -c tls=true \
      -c sd='TOKEN@NNNNN TAG="tag-of-your-choice"'
      -c ca='loggly-tls-cert'

| 
| When defining new endpoint, the following parameters can be applied

-  **name** - Create a name for this endpoint (e.g. Loggly)

-  **server** - set to `logs-01.loggly.com``

-  **port** - 6514 for TLS enabled or 514 for TLS disabled

-  **tls** - set to true (recommended) or false

-  **format** - set to rfc5424

-  **sd** - TOKEN@NNNNN TAG="tag-of-your-choice" 

.. note:: 
  `TOKEN` needs to be replaced with your Loggly **customer token** and `NNNNN`` is Loggly Private Enterprise Number (PEN) which is **41058** (check `Loggly documentation <https://www.loggly.com/docs/streaming-syslog-without-using-files/>`__ for up to date information). **TAG** can be any arbitrary value wrapped in double quotes.

Optional:

-  **ca** - when TLS enabled, enter the contents of Loggly TLS
   certificate available
   `here <https://www.loggly.com/docs/upgrade-tls-certificate/>`__ .

Add rsyslog integration to service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First you need the ID of the endpoint previously created

.. code-block:: bash

   avn service integration-endpoint-list --project your-project
   ENDPOINT_ID                           ENDPOINT_NAME   ENDPOINT_TYPE
   ====================================  ==============  =============
   618fb764-5832-4636-ba26-0d9857222cfd  example-syslog  rsyslog

Using the **ENDPOINT_ID** from above and you can now link the service to
the endpoint

.. code-block:: bash

   avn service integration-create --project your-project \
       -t rsyslog -s your-service \
       -D 618fb764-5832-4636-ba26-0d9857222cfd

After enabling  thisservice integration, you can see that it has been
activated in the Aiven console and the logs will be now integrated
with Loggly. It may take a few moments to setup the new log, and you
can track the status in your service overview.
 
Your logs should now be visible on Loggly **Search** tab. Enter the
tag name your previously specified (e.g. *tag:your-tag* ) and it will
populate the dashboard with the log events from your service.

If you have any questions about our integrations, please feel free to reach
out to `Support <mailto:support@aiven.io>`__ and let us know.
