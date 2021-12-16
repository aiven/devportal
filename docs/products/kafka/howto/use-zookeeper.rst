Set ZooKeeper configuration
===========================

ZooKeeper is used both by Apache Kafka and by Aiven management software to coordinate work within the cluster. However, to assure the stability of the cluster the access to ZooKeeper is by default restricted.

In order to change ZooKeeper configuration properties follow these steps:

#. Log in to the Aiven web console and select your **Aiven for Apache Kafka** service.
#. On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option**.
#. Select the setting you want to change and modify the value.
#. Click **Save advanced configuration**.

The service configuration will be then updated.

.. note:: Latest versions of Apache Kafka allow ZooKeeper-less mode, however, you can continue using the advanced configuration settings as before.


