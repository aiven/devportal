Write to M3 from Telegraf
================================

M3 supports multiple methods of writing metrics to the M3 database. Two common options are the InfluxDB wire-protocol, and the Prometheus remote write protocol. It is possible to write metrics from an existing Telegraf setup to M3 using either of these protocols, so we've covered the configuration for both options here.

Variables
---------

These are the placeholders used in the examples on this page

==================      ==========================================================
Variable                Description
==================      ==========================================================
``M3_HOST``             The hostname of your M3DB
``M3_PORT``             Port where M3DB is running
``AVNADMIN_PASS``       Password for the default ``avnadmin`` user
==================      ==========================================================

Configuring Telegraf InfluxDB output plugin for M3
--------------------------------------------------

Below is an example of how to configure Telegraf to send metrics to M3 using the InfluxDB line-protocol. These lines belong in the **output plugins** section of your Telegraf configuration file::

    # Configuration for sending metrics to M3
    [[outputs.influxdb]]
      ## The full HTTP URL for your M3 instance.
      urls = ["https://M3_HOST:M3_PORT/api/v1/influxdb"]

      ## If true, no CREATE DATABASE queries will be sent.
      ## Even if sent, does not affect M3 in any way.
      skip_database_creation = true

      ## HTTP Basic Auth
      username = "avnadmin"
      password = "secretpassword"

      ## HTTP Content-Encoding for write request body, can be set to
      ## "gzip" to compress body or "identity" to apply no encoding.

      content_encoding = "gzip"

Configuring Telegraf Prometheus remote write for M3
---------------------------------------------------

Here's an example of how to configure Telegraf to send metrics to M3 using the Prometheus remote write protocol. These lines go in the output plugins section of the Telegraf configuration file::

    # Configuration for sending metrics to M3
    [outputs.http]
      ## URL is the address to send metrics to
      url = "https://M3_HOST:M3_PORT/api/v1/prom/remote/write"

      ## HTTP Basic Auth credentials
      username = "avnadmin"
      password = "secretpassword"

      ## Data format to output.
      data_format = "prometheusremotewrite"

      ## Outgoing HTTP headers
      [outputs.http.headers]
        Content-Type = "application/x-protobuf"
        Content-Encoding = "snappy"
        X-Prometheus-Remote-Write-Version = "0.1.0"
