Get Started with Aiven for OpenSearch®
======================================

To start using Aiven for OpenSearch®, the first step is to create a service. You can do this on the `Aiven Console <https://console.aiven.io/>`_ or with the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

This quickstart section provides the steps to create an Aiven for OpenSearch® service. 


Create an Aiven for OpenSearch® service
-----------------------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new Aiven for OpenSearch service.

Once the service is ready, the status changes to *Running*. Depending on your selected cloud provider and region, this generally takes a couple of minutes.

.. _access-os-dashboards:

Access OpenSearch Dashboards 
---------------------------------
When you create an Aiven for OpenSearch service, you will automatically get access to OpenSearch Dashboards. This enables you to quickly and easily visualize data from your OpenSearch service with minimal effort.

To access OpenSearch Dashboards, follow these steps:

1. On the **Overview** page of your Aiven for OpenSearch service, click **OpenSearch Dashboards**.
2. Copy or click on the Service URI to open OpenSearch Dashboards in your browser.
3. Enter the username and password from the connection information screen when prompted.
4. Click **Sign In** to view the OpenSearch Dashboards.

After logging in, you can explore and interact with your data, as well as add sample data and utilize OpenSearch API features.

For more information, see :doc:`OpenSearch Dashboards </docs/products/opensearch/dashboards>` section. 

Connect to OpenSearch
----------------------

To start working with your data in OpenSearch, you need to first connect to your service. A good starting point is to learn how to :doc:`connect with cURL <howto/opensearch-with-curl>`. You can find the necessary connection details in the service overview.

If you're new to OpenSearch and looking for inspiration, recommend checking out our :doc:`sample dataset <howto/sample-dataset>`, which provides a great starting point for exploring the capabilities of the platform.
