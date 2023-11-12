Enable tiered storage for Aiven for Apache Kafka®
=====================================================
Learn how to enable tiered storage capability of Aiven for Apache Kafka®. This topic provides step-by-step instructions for maximizing storage efficiency using either the `Aiven console <https://console.aiven.io/>`_ or the :doc:`Aiven CLI </docs/tools/cli>`.

.. important:: 
    
   Aiven for Apache Kafka® tiered storage is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you’re interested in trying out this feature, contact the sales team at sales@Aiven.io.

Prerequisites
--------------
* Aiven account and a project set up in the Aiven Console
* Aiven for Apache Kafka® service with Apache Kafka version 3.6. Tiered storage on Aiven for Apache Kafka is currently not available on all plans and regions. View the `plans and pricing page <https://aiven.io/pricing?product=kafka>`_ for a comprehensive list of supported plans and regions.
* Aiven CLI


Enable tiered storage via Aiven Console
------------------------------------------
Follow these steps to enable tiered storage for your service using the Aiven Console. 

1. Access the  `Aiven console <https://console.aiven.io/>`_, and select your project.
2. Create a new Aiven for Apache Kafka service or choose an existing one.  

   - If you are :doc:`creating a new service </docs/platform/howto/create_new_service>`:

     a. On the **Create Apache Kafka® service** page, scroll down to the **Tiered storage** section.
     b. To enable tiered storage, select the **Enable tiered storage** toggle.
     c. In the **Service summary**, you can view the pricing for tiered storage. 
   
   - If you are using an existing service:

     a. Go to the service's **Overview** page, scroll down to the **Tiered storage** section.
     b. To enable tiered storage, select the **Enable tiered storage** toggle.
     
   
3. Select the **Activate tiered storage** to save your settings and enable tiered storage for the service. 

Once you have enabled tiered storage and it's in use, access the :doc:`Tiered storage overview </docs/products/kafka/howto/tiered-storage-overview-page>` on the left sidebar to get an overview of the overall usage and cost details.

.. note:: 
   
   If tiered storage is not yet enabled for your service, clicking **Tiered storage** from the sidebar provides you with the option to activate tiered storage.

.. warning:: 
   If you power off a service with tiered storage active, all remote data will be permanently deleted. You will not be billed for tiered storage usage during the powered-off period.


Configuring default retention policies at service-level
`````````````````````````````````````````````````````````````````````````````

1. Access `Aiven console <https://console.aiven.io/>`_, select your project, and choose your Aiven for Apache Kafka service.
2. On the **Overview** page, navigate to **Advanced configuration** and select **Change**.
3. In the **Edit advanced configuration** view, choose **Add configuration option**.
4. To set the retention policy for Aiven for Apache Kafka tiered storage, select ``kafka.log_local_retention_ms`` for time-specific retention or ``kafka.log_local_retention_bytes`` for size-specific retention.
5. Select **Save advanced configuration** to apply your changes.

Additionally, you can configure the retention policies from the :ref:`Tiered storage overview <modify-retention-polices>` page.

Enable tiered storage via Aiven CLI 
-----------------------------------------
Follow these steps to enable tiered storage for your Aiven for Apache Kafka service using the :doc:`Aiven CLI </docs/tools/cli>`:

1. Retrieve the project information using the following command: 
   
   .. code-block:: bash

        avn project details


   If you need details for a specific project, use:

   .. code-block:: bash

        avn project details --project <your_project_name>

2. Get the name of the Aiven for the Apache Kafka service for which you want to enable tiered storage by using the following command: 

   .. code-block:: bash

       avn service list

   Make a note of the ``SERVICE_NAME`` corresponding to your Aiven for Apache Kafka service.

3. Enable tiered storage using the command below:
   
   .. code-block:: bash

        avn service update \
           --project demo-kafka-project \
           demo-kafka-service \
           -c tiered_storage.enabled=true




In this command:

* ``--project demo-kafka-project`` refers to the name of your project. In this example, it's ``demo-kafka-project``.
* ``demo-kafka-service`` denotes the Aiven for Apache Kafka® service you intend to update. 
* ``-c tiered_storage.enabled=true`` is the configuration flag that activates tiered storage for your Aiven for Apache Kafka service.









