Jolokia

Access JMX metrics via Jolokia
===============================

<<<<<<< HEAD
`Jolokia <https://jolokia.org/>`_ is one of the external metrics integration supported on the Aiven platform besides :doc:`Datadog metrics </docs/integrations/datadog/datadog-metrics>` and :doc:`Prometheus metrics </docs/platform/howto/integrations/prometheus-metrics>`.
=======
`Jolokia <https://jolokia.org/>`_ is one of the external metrics integration supported on the Aiven platform besides :doc:`Datadog metrics </docs/integrations/datadog/datadog-metrics>` and :doc:`Prometheus metrics </docs/platform/howto/integrations/prometheus-metrics-limit.html>`.
>>>>>>> b9dfaae5 (Added note with reference to source github repository)

.. note:: 

    Only Aiven for Apache Kafka® has support for Jolokia integration. 

Jolokia endpoint
----------------

To enable Jolokia integration for Aiven services you first need to
create a new Jolokia endpoint configuration. This can be created from
the Service Integrations page. You only need to specify a display name
for the configuration and the system will automatically generate
username and password for authentication. In most cases, you can re-use
the same Jolokia endpoint configuration for all services within a
project.

   .. image:: /images/integrations/jolokia-service-integration-image-1.png
      :alt: Jolokia service integration endpoint
   .. image:: /images/integrations/jolokia-service-integration-image-2.png
      :alt: Jolokia integration endpoint details

.. note::
    You can :ref:`create a new service endpoint using the Aiven CLI <avn_service_integration_endpoint_create>` as well.

Next, to enable Jolokia integration, you need to go to the
Service Overview page of each service you want to enable the integration
for. Click the **Set up integration** button under *Service integrations*
and then click **Use integration** under Jolokia from the popup. After finishing the wizard the
system will configure the endpoint on all nodes of the service that provide access to the metrics.

Aiven Jolokia integration is configured to allow HTTP POST request to
read values from the service specific metrics. Bulk requests are
supported for batch collection as well. For further information on the
protocol, can refer to `Jolokia
documentation <https://jolokia.org/reference/html/protocol.html>`__ .

Please do note that many of the metrics are specific to a Kafka® broker,
so you may need to query each individual node for the full picture. Node
IP is represented by a single DNS name. In a command line you can use
``host`` command (Unix systems) or ``nslookup`` command (Windows systems) 
to get the list of IP addresses associated with a DNS name:

.. code-block:: shell

   host kafka-67bd7c5-myproject.aivencloud.com
   kafka-67bd7c5-myproject.aivencloud.com has address 35.228.218.115
   kafka-67bd7c5-myproject.aivencloud.com has address 35.228.234.106
   kafka-67bd7c5-myproject.aivencloud.com has address 35.228.157.197

<<<<<<< HEAD
Here's a quick example of a cURL request. :doc:`Download the CA certificate </docs/platform/howto/download-ca-cert>` first before executing the cURL request.
=======
Here's a quick example of a cURL request. :doc:`Download the CA certificate </docs/platform/howto/download-ca-cert>` first before executing the cURL request. 
>>>>>>> b9dfaae5 (Added note with reference to source github repository)
The file is identical for all endpoints and services in the same project.

Please note to use port 6733 which is the default port Jolokia is
listening on. ``joljkr2l:PWD`` are the values of the username/password from the Jolokia endpoint setup step. 
You can find this endpoint details from the **Service Integrations --> Jolokia** page.

.. code-block:: shell

   curl --cacert ca.pem \
       -X POST \
       https://joljkr2l:PWD@HOST_IP:6733/jolokia/  \
       -d \
   '{"type":"read","mbean":"kafka.server:type=ReplicaManager,name=PartitionCount"}'

Jolokia supports searching beans using ``search`` command:

.. code-block:: shell

   curl --cacert ca.pem \
       -X POST \
       https://joljkr2l:PWD@HOST_IP:6733/jolokia/  \
       -d \
   '{"type":"search","mbean":"kafka.server:*"}'


