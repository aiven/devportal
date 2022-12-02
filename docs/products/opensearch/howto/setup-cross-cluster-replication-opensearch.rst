Setup cross cluster replication for Aiven for OpenSearch® (beta)
================================================================

.. note:: 
    - Cross cluster replication feature for Aiven for OpenSearch is a beta release. 
    - Cross cluster replication is not available for Hobbyist and Startup plans.

Follow these steps to set up :doc:`cross cluster replication <../concepts/cross-cluster-replication-opensearch>` for your Aiven for OpenSearch service: 

1. From the **Services** page in the `Aiven Console <https://console.aiven.io/>`_, select the Aiven for OpenSearch service for which you want to set up cross cluster replication. 
2. In the service's **Overview** tab, scroll down to the **Cross cluster replications** section and click **Create follower**.
3. In the **Create OpenSearch follow cluster** page, 

   * Enter a name for the follower cluster 
   * Select the desired cloud provider
   * Select the desired cloud region
   * Select the service plan
      .. note:: 
        The follower cluster service needs to have the same plan as the leader service. 
    
   * Add additional disk storage based on your business requirements
4. Click **Create**.

The follower cluster service will be in a `Rebuilding` state, and, once complete, the follower cluster will be ready to pull all data and indexes from the leader service. 

.. note:: 
   To learn about the current limitations with cross cluster replications for Aiven for OpenSearch, see the :ref:`Limiations <ccr-limitatons>` section. 

View follower cluster services
-------------------------------

You can view all the follower cluster services configured for your OpenSearch service either from the **Service integration** section on the service **Overview** page or in the **Integrations** tab. 
Additionally, the OpenSearch services display **Leader** and **Follower** tags below the service name to help identify leader cluster and follower cluster services. 

Setup cross-cluster replication via API 
---------------------------------------

You can set up the cross cluster replication for Aiven for OpenSearch service using the service integration endpoint and setting the ``integration-type`` to ``opensearch_cross_cluster_replication``.
For more information, see `Create a new service integration <https://api.aiven.io/doc/#tag/Service_Integrations>`_. 

Setup cross-cluster replication via Terraform provider 
------------------------------------------------------
You can set up the cross cluster replication for Aiven for OpenSearch service via the :doc:`Aiven Terraform provider </docs/tools/terraform>`. Set the ``integration-type`` to ``opensearch_cross_cluster_replication`` in the `Service Integration resource <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/service_integration>`_. 


