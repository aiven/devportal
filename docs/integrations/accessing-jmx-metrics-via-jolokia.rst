Accessing JMX metrics via Jolokia
=================================

Java applications export a wealth of monitoring metrics and information
over the standard Java Management Extensions interface. Jolokia, on the
other hand, is a HTTP/REST interface for accessing this information
remotely. Jolokia is the fourth metrics integration support by Aiven
after `Aiven InfluxDB &
Grafana <https://help.aiven.io/services/integrations/getting-started-with-service-integrations>`__
,
`Datadog <https://help.aiven.io/services/integrations/getting-started-with-datadog>`__
and
`Prometheus <https://help.aiven.io/services/integrations/using-aiven-with-prometheus>`__
.

Enabling Jolokia endpoint in Aiven
----------------------------------

To enable Jolokia integration for Aiven services you first need to
create a new Jolokia endpoint configuration. This can be created from
the Service Integrations page. You only need to specify a display name
for the configuration and the system will automatically generate
username and password for authentication. In most cases, you can re-use
the same Jolokia endpoint configuration for all services within a
project.

.. image:: 2684968-accessing-jmx-metrics-via-jolokia_image1.png

Next, to finally enable Jolokia integration, you need to go to the
Service Overview page of each service you want to enable the integration
for. Click the Manage Integrations button next to Service Integrations
and then select Jolokia from the popup. After finishing the wizard the
system will configure the endpoint on all nodes of the service that
provide access to the metrics.

.. image:: 2684968-accessing-jmx-metrics-via-jolokia_image2.png

Aiven Jolokia intergration is configured to allow HTTP POST request to
read values from the service specific metrics. Bulk requests are
supported for batch collection as well. For further information on the
protocol, can refer to `Jolokia
documentation <https://jolokia.org/reference/html/protocol.html>`__ .

Please do note that many of the metrics are specific to a Kafka broker,
so you may need to query each individual node for the full picture. Node
IPs are represented by a single DNS name. In a command line you can use
``host`` command to get the list of IP addresses associated with a DNS
name:

::

   host kafka-67bd7c5-myproject.aivencloud.com
   kafka-67bd7c5-myproject.aivencloud.com has address 35.228.218.115
   kafka-67bd7c5-myproject.aivencloud.com has address 35.228.234.106
   kafka-67bd7c5-myproject.aivencloud.com has address 35.228.157.197

Here's a quick example of a cURL request. The CA certificate can be
downloaded on the Service Overview page or alternatively or with the
`Aiven command line client <https://github.com/aiven/aiven-client/>`__ :
``avn project ca-get`` . The file is identical for all endpoints and
services in the same project.

Please note to use port 6733 which is the default port Jolokia is
listening on.

::

   curl --cacert project-ca.crt \
       -X POST \
       https://jolbpko8:PWD@HOST_IP:6733/jolokia/  \
       -d \
   '{"type":"read","mbean":"kafka.server:type=ReplicaManager,name=PartitionCount"}'

Jolokia supports searching beans using ``search`` command:

::

   curl --cacert project-ca.crt \
       -X POST \
       https://jolbpko8:PWD@HOST_IP:6733/jolokia/  \
       -d \
   '{"type":"search","mbean":"kafka.server:*"}'
