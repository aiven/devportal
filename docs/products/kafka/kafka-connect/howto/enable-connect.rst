Enable Kafka Connect on Aiven for Apache Kafka
==============================================

To enable Kafka Connect on Aiven for Apache Kafka services, those should be running on business or premium plans. 

.. Warning::

    Creating a :ref:`dedicated Aiven for Kafka Connect service <apache_kafka_connect_dedicated_cluster>`  is Aiven's suggested option. Having Kafka Connect running on the same nodes as Apache Kafka increases the load on the nodes possibly making the cluster more unstable. 
    
    For a better separation of concerns, a dedicated Aiven for Apache Kafka Connect cluster is therefore suggested.

To enable Kafka Connect on Aiven for Apache Kafka nodes

1. Click on the Aiven for Apache Kafka service where to enable Kafka Connect

2. Scroll down the **Service overview** page to the **Kafka Connect** section and turn it on.

The Kafka Connect connection information are now available at the top of the **Service overview** page in the Kafka Connect tab.
