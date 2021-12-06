Enable public access for Kafka in a VPC
========================================

To enable public access for **Aiven for Apache Kafka** service which is running within a virtual private cloud (VPC),
follow these steps:

#. Log in to the Aiven web console and select your **Aiven for Apache Kafka** service.
#. On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option** .
#. Select ``public_access.kafka`` and switch it on. For **Aiven for Apache Kafka Connect** or **Aiven for Apache Kafka Rest**, select ``public_access.kafka_connect`` or ``public_access.kafka_rest`` respectively.
#. Click **Save advanced configuration**. The *Overview* page now has an **Access Route** setting inside the *Connection information* with **Public** and **Dynamic** options.
#. Select **Public** to see the public URL for your service.

The connection details shown for the **Dynamic** option are only accessible via VPC peering, while the connection details for the **Public** option are accessible over the public internet (though the service's IP Allow List will still restrict connections).

.. note:: You can change the **public_access** settings without any downtime for your service.