Send emails from Aiven for Grafana®
===================================

Use the Aiven API or the Aiven client to configure the Simple Mail Transfer Protocol (SMTP) server settings and send the following emails from Aiven for Grafana®: invite emails, reset password emails, and alert messages.

What you need
----------------

* Aiven client installed

* Aiven for Grafana service created

* SMTP server IP or hostname

* SMTP server port

* Username for authentication (if authentication is in use - highly recommended)

* Password for authentication

* Sender email address (i.e., email address shown in "From" field)

* Sender name (optional)


Configure the SMTP server for Grafana
-------------------------------------

To configure the Aiven for Grafana service:

1. Open the Aiven client, and log in::

    avn user login <you@example.com> --token

2. configure the service using your own SMTP values::

    avn service update --project yourprojectname yourservicename \
    -c smtp_server.host=smtp.example.com \
    -c smtp_server.port=465 \
    -c smtp_server.username=emailsenderuser \
    -c smtp_server.password=emailsenderpass \
    -c smtp_server.from_address="grafana@yourcompany.com" 

3. (optionally) Review all available custom options, and configure as needed::

    avn service types -v


You have now set up your Aiven for Grafana to send emails.
