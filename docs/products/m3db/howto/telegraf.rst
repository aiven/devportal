How to Write to M3 from Telegraf
================================

M3 supports multiple methods of writing metrics to the M3 database. Two common options are the InfluxDB wire-protocol, and the Prometheus remote write protocol. It is possible to write metrics from an existing Telegraf setup to M3 using either of these protocols, so we've covered the configuration for both options here.

Configuring Telegraf InfluxDB output plugin for M3
--------------------------------------------------

This is how you configure Telegraf to send metrics to M3 using the InfluxDB line-protocol. This configuration needs to be part of the output plugins configuration in your Telegraf configuration file::

    # Configuration for sending metrics to M3
    [[outputs.influxdb]]
      ## The full HTTP URL for your M3 instance.
      urls = ["https://[host]:[port]/api/v1/influxdb"]

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

This is how you configure Telegraf send metrics to M3 using the Prometheus remote write protocol. This configuration needs to be part of the output plugins configration in the Telegraf configuration file::

    # Configuration for sending metrics to M3
    [outputs.http]
      ## URL is the address to send metrics to
      url = "https://[host]:[port]/api/v1/prom/remote/write"

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

