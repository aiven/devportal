Enable tiered storage for Aiven for Apache Kafka®
=====================================================
Learn how to enable tiered storage capability of Aiven for Apache Kafka®. This topic provides step-by-step instructions for maximizing storage efficiency using either the `Aiven console <https://console.aiven.io/>`_ or the :doc:`Aiven CLI </docs/tools/cli>`.

.. important:: 
    
   Aiven for Apache Kafka® tiered storage is an early availability feature, which means it has some restrictions on the functionality and service level agreement. It is intended for non-production environments, but you can test it with production-like workloads to assess the performance. To enable this feature, navigate to the :doc:`Feature preview </docs/platform/howto/feature-preview>` page within your user profile.

Prerequisites
--------------
* Aiven account and a project set up in the Aiven Console
* Aiven for Apache Kafka® service with Apache Kafka version 3.6
* Aiven CLI


Enable tiered storage via Aiven Console
------------------------------------------
Follow these steps to enable tiered storage for your service using the Aiven Console. 

1. Access the  `Aiven console <https://console.aiven.io/>`_, and select your project.
2. Create a new :doc:`Aiven for Apache Kafka service </docs/platform/howto/create_new_service>` or choose an existing one.  

   - If you are creating a new service:

     a. On the **Create Apache Kafka® service** page, scroll down to the **Tiered storage** section.
     b. To enable tiered storage, select the **Enable tiered storage** toggle.
   
   - If you are using an existing service:

     a. Go to the service's **Overview** page, scroll down to the **Tiered storage** section.
     b. To enable tiered storage, select the **Enable tiered storage** toggle.

3. Enter the value for **Local cache size (bytes)**. This value indicates the amount of memory reserved for storing frequently accessed data, enhancing the speed of reading data from remote storage.

4. Select the **Activate tiered storage** to save your settings and enable tiered storage for the service. 


Configuring default retention policies at service-level
`````````````````````````````````````````````````````````````````````````````

1. Access `Aiven console <https://console.aiven.io/>`_, select your project, and choose your Aiven for Apache Kafka service.
2. On the **Overview** page, navigate to **Advanced configuration** and select **Change**.
3. In the **Edit advanced configuration** view, choose **Add configuration option**.
4. To set the retention policy for Aiven for Apache Kafka tiered storage, select ``kafka.log_local_retention_ms`` for time-specific retention or ``kafka.log_local_retention_bytes`` for size-specific retention.
5. Select **Save advanced configuration** to apply your changes.


Enable tiered storage via Aiven CLI 
-----------------------------------------
Follow these steps to enable tiered storage for your Aiven for Apache Kafka service using the:doc:`Aiven CLI </docs/tools/cli>`:

1. Retrieve the project information using the following command: 
   
   .. code-block:: bash

        avn project details


   If you need details for a specific project, use:

   .. code-block:: bash

        avn project details --project <your_project_name>

2. Get the name of the Aiven for the Apache Kafka service for which you want to enable tiered storage by using the following command: 

   .. code-block:: bash

       avn service list

   Make a note of the ``SERVICE_NAME`` corresponding to your Kafka service.

3. Enable tiered storage using the command below:
   
   .. code-block:: bash

        avn service update --project demo-kafka-project demo-kafka-service -c 
        tiered_storage.enabled=true -c tiered_storage.local_cache.size=5368709120


Where: 

- ``--project demo-kafka-project``: Specifies the project name, in this example ``demo-kafka-project``.
- ``demo-kafka-service``: Refers to the Kafka service you're updating, in this example ``demo-kafka-service``.
- ``-c tiered_storage.enabled=true``: Enables tiered storage for the Kafka service.
- ``-c tiered_storage.local_cache.size=5368709120``: Sets the local cache size for tiered storage, in this example to 5 GB.






