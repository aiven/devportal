Set Apache ZooKeeper™ configuration
===================================

Apache ZooKeeper™ is a crucial component used by Apache Kafka® and Aiven management software to facilitate efficient cluster operations. By default, access to ZooKeeper is restricted to ensure cluster stability. However, it is possible to modify the ZooKeeper configuration properties as needed. 

In order to change ZooKeeper configuration properties follow these steps:

#. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your service.
#. On the **Overview** page, scroll down to the **Advanced configuration** section. 
#. Select **Change** to add configuration option. 
#. On the **Edit advanced configuration** screen, select **+ Add configuration option** to add new configurations or modify the values of existing configurations.
#. Select  **Save advanced configuration**.

The service configuration will be then updated.

.. note:: Latest versions of Apache Kafka allow ZooKeeper-less mode, however, you can continue using the advanced configuration settings as before.

-----

*Apache ZooKeeper is a trademark of the Apache Software Foundation in the United States and/or other countries*
