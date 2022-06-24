Upgrade to OpenSearch® with Terraform
=====================================

If you manage your infrastructure with our :doc:`Terraform provider </docs/tools/terraform/terraform>` then please note that you will need to upgrade the provider to 2.4.0 or later in order to have support for OpenSearch®.

To upgrade an existing Elasticsearch service to OpenSearch using Terraform:

* Migrate the existing Elasticsearch resource to an OpenSearch resource.

* Update Terraform's state to be aware of and manage the resource as an OpenSearch service.

Use the following steps to complete the upgrade safely:

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

    # Modified Elasticsearch Resource, upgrades to OpenSearch v1
    resource "aiven_elasticsearch" "es" {
      project = "project-name"
      cloud_name = "google-us-east4"
      plan = "business-4"
      service_name = "es"

      elasticsearch_user_config {
        opensearch_version = 1
      }
    }

Once you have updated your configuration, check that the change looks correct::

    terraform plan

Apply the upgrade::

    terraform apply

Your service will now upgrade to OpenSearch, and if you view it in the web console, it will show as an OpenSearch service.

2. After the migration you will need to remove the Elasticsearch service from the Terraform state.

.. code-block::

    terraform state rm 'aiven_elasticsearch.<service-name>'

3. Update the resource configuration to be an OpenSearch resource type, the example shown above would then look like this:

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

Bring the Terraform state back in sync with your OpenSearch service by importing the service.

.. code-block::

    terraform import 'aiven_opensearch.os' <project-name>/<service-name>

Your Elasticsearch service has been upgraded to OpenSearch with Terraform, and the resource configuration updated to use a resource type of OpenSearch.

------

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
