Upgrade to OpenSearch with Terraform
====================================

If you manage your infrastructure with our :doc:`Terraform provider </docs/tools/terraform>` then please note that you will need to upgrade the provider to the latest release in order to have support for OpenSearch.

To perform the upgrade in place using Terraform you need to first migrate the existing Elasticsearch resource to an OpenSearch resource, and then update Terraform's state to be aware of the migration and utilize and manage the resource as an OpenSearch service.

To accomplish this, you will need to take the following steps:

1. Change the ``elasticsearch_version = 7`` to ``opensearch_version = 1``. This is the equivalent to clicking the migrate button in the console.

.. code-block::

    # Existing Elasticsearch Resource
    resource "aiven_elasticsearch" "es" {
      project = "project-name"
      cloud_name = "google-us-east4"
      plan = "business-4"
      service_name = "es"

      elasticsearch_user_config {
        elasticsearch_version = 7
      }
    }

.. code-block::

    # Modified Elasticsearch Resource
    resource "aiven_elasticsearch" "es" {
      project = "project-name"
      cloud_name = "google-us-east4"
      plan = "business-4"
      service_name = "es"

      elasticsearch_user_config {
        opensearch_version = 1
      }
    }

2. After the migration you will need to remove the Elasticsearch service from the Terraform state.

.. code-block::

    terraform state rm 'aiven_elasticsearch.es'

3. Finally, add the OpenSearch service to the Terraform state using an OpenSearch resource.

.. code-block::

    resource "aiven_opensearch" "os" {
      project = "project-name"
      cloud_name = "google-us-east4"
      plan = "business-4"
      service_name = "es"

      opensearch_user_config {
        opensearch_version = 1
      }
    }

.. code-block::

    terraform import 'aiven_opensearch.os' project-name/es