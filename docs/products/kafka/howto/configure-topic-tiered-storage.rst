Configuring tiered storage for topics
===========================================================================

Aiven for Apache Kafka® offers flexibility in configuring tiered storage and setting retention policies. This guide will walk you through the process of configuring tiered storage for individual topics, configuring local retention policies, and configuring retention policies at the service level.

.. important:: 
    
   Aiven for Apache Kafka® tiered storage is an early availability feature, which means it has some restrictions on the functionality and service level agreement. It is intended for non-production environments, but you can test it with production-like workloads to assess the performance. To enable this feature, navigate to the :doc:`Feature preview </docs/platform/howto/feature-preview>` page within your user profile.

Prerequisite
------------
* :doc:`Tiered storage enabled for the Aiven for Apache Kafka service <docs/products/kafka/howto/enable-kafka-tiered-storage>`.

Configure tiered storage for topics
------------------------------------

1. Access `Aiven console <https://console.aiven.io/>`_, select your project, and choose your Aiven for Apache Kafka service.
2. From the left sidebar, select **Topics**.
3. Here, you have the option to either add a new topic with tiered storage configuration or modify an existing topic to use tiered storage.

For a new topic
~~~~~~~~~~~~~~~

1. From the **Topics** page, select **Add topic**.
2. Enable advanced configurations by setting the **Do you want to enable advanced configuration?** option to **Yes**.
3. In the **Topic advanced configuration** drop-down, choose ``remote_storage_enable``. This action will reveal the **Remote storage enabled** drop-down. 
4. Select **True** to activate tiered storage for the topic.
5. Additionally, you can also set the values for ``local_retention_ms`` and ``local_retention_bytes`` using the respective options from the drop-down list.

.. important:: 
    If the values for ``local_retention_bytes`` and ``local_retention_ms`` are not set, they default to -2 or take the configuration from the service level.

    When set to -2, the retention in local storage will match the total retention. In this scenario, the data segments sent to remote storage are also retained locally. The remote storage will contain older data segments than in the local storage only when the total retention is set to be greater than the local retention. 

6. Select **Add topic** to save your changes and add the topic with tiered storage.

For an existing topic
~~~~~~~~~~~~~~~~~~~~~

1. From the **Topics** page, select the topic for which you wish to enable tiered storage.
2. Use the ellipsis or open the topic and choose **Modify**.
3. In the **Modify** page, choose ``remote_storage_enable`` from the drop-down list, followed by selecting **True** from the **Remote storage enable** drop-down.
4. Additionally, you can also set the values for ``local_retention_ms`` and ``local_retention_bytes`` using the respective options from the drop-down list.

.. important:: 
    If the values for ``local_retention_bytes`` and ``local_retention_ms`` are not set, they default to -2 or take the configuration from the service level. 

    When set to -2, the retention in local storage will match the total retention. In this scenario, the data segments sent to remote storage are also retained locally. The remote storage will contain older data segments than in the local storage only when the total retention is set to be greater than the local retention. 


5. Select **Update** to save your changes and activate tiered storage.


