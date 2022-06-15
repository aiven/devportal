Remote syslog integration
=========================

In addition to using Aiven Elasticsearch to store the logs from your
Aiven services, you can now integrate with an external monitoring system
that supports the rsyslog protocol.

Creating rsyslog integration
----------------------------

Add rsyslog integration endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the first step, you need to add the remote syslog you want to send
the log to into the project that contains the service you want to
integrate.

This can be configured from the Service Integrations page in the Aiven
Console.

.. image:: /images/integrations/remote-syslog-integration_image1.png

Another option is to use the `Aiven
Client <https://github.com/aiven/aiven-client>`__ .

::

   avn service integration-endpoint-create --project your-project \
       -d example-syslog -t rsyslog \
       -c server=logs.example.com -c port=514 \
       -c format=rfc5424 -c tls=true

When defining the remote syslog server the following parameters can be
applied

Required:

-  **server** -  DNS name or IPv4 address of the server

-  **port** - port to connect to

-  **format** - message format used by the server, this can be either
   ``rfc3164`` (the old BSD style message format), ``rfc5424`` (current
   syslog message format) or custom

-  **tls** - use TLS (as the messages are not filtered and may contain
   sensitive information, it is highly recommended to set this to true
   if the remote server supports it)

Conditional (required if format == custom):

-  **logline** - syslog log line template for a custom format,
   supporting limited rsyslog style templating (using
   ``%             tag            %`` ). Supported tags are: ``pri`` ,
   ``timestamp`` , ``timestamp:::date-rfc3339`` , ``HOSTNAME`` ,
   ``app-name`` , ``procid`` , ``msgid`` , ``msg`` and
   ``structured-data``

Optional:

-  **sd** - content of the structured data block of ``rfc5424`` message

-  **ca** - (PEM format) Certificate Authority to use for verifying the
   servers certificate (typically not needed unless the server's
   certificate is issued by an internal CA or it uses a self-signed
   certificate)

-  **key** - (PEM format) client key if the server requires client
   authentication

-  **cert** - (PEM format) client cert to use

Add rsyslog integration to service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can be configured in the Aiven Console by navigating to the target
service overview page and then scrolling down to the Manage Integrations
button.


.. image:: /images/integrations/remote-syslog-integration_image2.png

You should be able to select your previously configured Rsyslog service
integration by clicking Use integration in the modal window.

.. image:: /images/integrations/remote-syslog-integration_image3.png

Alternately, with the Aiven Client, first you need the id of the
endpoint previously created

::

   avn service integration-endpoint-list --project your-project
   ENDPOINT_ID                           ENDPOINT_NAME   ENDPOINT_TYPE
   ====================================  ==============  =============
   618fb764-5832-4636-ba26-0d9857222cfd  example-syslog  rsyslog

Finally you can link the service to the endpoint

::

   avn service integration-create --project your-project \
       -t rsyslog -s your-service \
       -D 618fb764-5832-4636-ba26-0d9857222cfd

Integrating with a third party syslog service
---------------------------------------------

All integrations can be configured using the Aiven Console or the Aiven
CLI though the examples are easier to copy and paste in the CLI form.

papertrail
~~~~~~~~~~

As papertrail identifies the client based on the server and port  you
only need to copy the appropriate values from the "Log Destinations"
page and use those as the values for server and port respectively. You
**do not need** the ca-bundle as papertrail's servers use certificates
signed by known CAs. You also need to set the format to ``rfc3164`` .

::

   avn service integration-endpoint-create --project your-project \
       -d papertrail -t rsyslog \
       -c server=logsN.papertrailapp.com -c port=XXXXX \
       -c format=rfc3164 -c tls=true

loggly
~~~~~~

In addition to the server and port you also need a *customer token*
which you then **need** to give as part of the ``-c sd`` parameter when
creating the endpoint.

::

   avn service integration-endpoint-create --project your-project \
       -d loggly -t rsyslog \
       -c server=logs-01.loggly.com -c port=514 \
       -c format=rfc5424 -c tls=true \
       -c sd='TOKEN@NNNNN TAG="tag-of-your-choice"'

sumo logic
~~~~~~~~~~

You need to the give the collector token as the ``-c sd`` parameter and
use the server and port of the collector.

::

   avn service integration-endpoint-create --project your-project \
       -d loggly -t rsyslog \
       -c server=syslog.collection.XX.sumologic.com \
       -c port=6514 \
       -c format=rfc5424 -c tls=true \
       -c sd='collector-token-string@NNNNN'

Datadog
~~~~~~~

For Datadog integration you need to use custom format with logline

::

   avn service integration-endpoint-create --project your-project \
       -d datadog -t rsyslog \
       -c server=intake.logs.datadoghq.com -c port=10516 \
       -c tls=true -c format=custom \
       -c logline='DATADOG_API_KEY <%pri%>1 %timestamp:::date-rfc3339% %HOSTNAME% %app-name% - - - %msg%'

NOTE: If you want to use Datadog EU environment, the service address is:

Server: ``tcp-intake.logs.datadoghq.eu``

Port: ``443``

NewRelic
~~~~~~~~

You will also need a custom logline format for NewRelic Syslog
integration. This is so you can prepend your `NewRelic Insights Insert
Key <https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/>`__
and ensure the format matches the `built-in Grok
pattern <https://docs.newrelic.com/docs/logs/ui-data/built-log-parsing-rules/#syslog-rfc5424>`__
.

::

   avn service integration-endpoint-create --project your-project \
   -d newrelic -t rsyslog \
   -c server=newrelic.syslog.nr-data.net -c port=6514 \
   -c tls=true -c format=custom \
   -c logline='NEWRELIC_INSIGHTS_INSERT_KEY <%pri%>%protocol-version% %timestamp:::date-rfc3339% %hostname% %app-name% %procid% %msgid% -  %msg%'

Coralogix
~~~~~~~~~

For coralogix integration you need to use custom format with logline

::

   avn service integration-endpoint-create --project your-project \
   -d coralogix -t rsyslog \
   -c server=syslogserver.coralogix.us -c port=5142 \
   -c tls=false -c format=custom \
   -c logline="{\"fields\": {\"private_key\":\"YOUR_CORALOGIX_KEY\",\"company_id\":\"YOUR_COMPANY_ID\",\"app_name\":\"%app-name%\",\"subsystem_name\":\"programname\"},\"message\": {\"message\":\"%msg%\",\"program_name\":\"programname\",\"pri_text\":\"%pri%\",\"hostname\":\"%HOSTNAME%\"}}"

| **NOTE: TLS needs to be set to false.**
| According to your account (If it ends in .com / .us / .in ) you will
  need to use one of the following Syslog Endpoints for server:

-  ``syslogserver.coralogix.com``

-  ``syslogserver.coralogix.us``

-  ``syslogserver.app.coralogix.in``

LogDNA
~~~~~~

For LogDNA syslog integration, you would need to use custom format with
logline. Please note that there are no backslashes around ``key`` value

::

   avn service integration-endpoint-create --project your-project -d logdna -t rsyslog -c server=syslog-a.logdna.com -c port=6514 -c tls=true -c format=custom -c logline='<%pri%>%protocol-version% %timestamp:::date-rfc3339% %hostname% %app-name% %procid% %msgid% [logdna@48950 key="YOUR_KEY_GOES_HERE"] %msg%'
