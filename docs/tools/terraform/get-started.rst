Get started with Aiven Provider for Terraform
==============================================

This example shows you how to use the Aiven Provider to set up your Aiven data infrastructure by creating a :doc:`project </docs/platform/concepts/projects_accounts_access>` with a single Aiven for Redis®* service. 

.. caution::

  Recreating stateful services with Terraform may delete the service and all its data before creating it again. Some properties, like project and resource name, cannot be changed and it will trigger a resource replacement. Check the Terraform plan to find out whether a service will be deleted or replaced.

  It's recommended to set the ``termination_protection`` property to true on all production services. This prevents Terraform from removing the service. However, logical databases, topics, or other configurations may still be removed with this setting enabled.


Prerequisities  
'''''''''''''''
- `Sign up for Aiven <https://console.aiven.io/signup?utm_source=github&utm_medium=organic&utm_campaign=devportal&utm_content=repo>`_ 
- `Download and install Terraform <https://www.terraform.io/downloads>`_
- `Create an authentication token <https://docs.aiven.io/docs/platform/howto/create_authentication_token.html>`_

Configure your project and services
'''''''''''''''''''''''''''''''''''

In this section, you'll learn how to structure a simple Terraform project. Terraform files declare the structure of the infrastructure, the dependencies, and configuration. These can be grouped together in one file, but it's ideal to put them in separate files.

In an empty folder and follow these steps to define your Aiven project and Redis®* service: 

1. Create a new Terraform file, ``provider.tf``. This will be used to declare a dependency on the Aiven Provider for Terraform.

2. In the ``required_providers`` block, add the source of the provider and specify the version. In the provider configuration block, ``api_token`` is the only parameter.

.. tip::
  View the latest version on the `Aiven Provider page <https://registry.terraform.io/providers/aiven/aiven/latest>`_.

Add the following code to the ``provider.tf`` file:

.. code:: terraform

  terraform {
    required_providers {
      aiven = {
        source  = "aiven/aiven"
        version = ">=4.0.0, < 5.0.0"
      }
    }
  }
  
  provider "aiven" {
    api_token = var.aiven_api_token
  }
  
.. tip::
  Set the environment variable ``AIVEN_TOKEN`` for the ``api_token`` property so that you you don't need to pass the ``-var-file`` flag when executing Terraform commands.

3. Create a file named ``redis.tf`` to define the configuration of an Aiven for Redis®* service.

4. Add the following block for a single-node Redis service to the ``redis.tf`` file:

.. code:: terraform

    # A single-node Redis service
    
    resource "aiven_redis" "single-node-aiven-redis" {
      project                 = var.project_name
      cloud_name              = "google-northamerica-northeast1"
      plan                    = "startup-4"
      service_name            = "gcp-single-node-redis1"
      maintenance_window_dow  = "monday"
      maintenance_window_time = "10:00:00"
    
      redis_user_config {
        redis_maxmemory_policy = "allkeys-random"
    
        public_access {
          redis = true
        }
      }
    }
    
    
5. Create a new file named ``variables.tf``. This is used to avoid including sensitive information in source control. 

It defines both the API token and the project name:

.. code:: terraform

   variable "aiven_api_token" {
     description = "Aiven console API token"
     type        = string
   }
   
   variable "project_name" {
     description = "Aiven console project name"
     type        = string
   }
   
   
6. Create a file named ``var-values.tfvars`` to hold the actual values of the sensitive information. The values are passed to Terraform using the ``-var-file=`` flag.

Add your API token and project name to the ``var-values.tfvars`` file:

.. code:: terraform

   aiven_api_token = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
   project_name    = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"
   

Apply the Terraform configuration
'''''''''''''''''''''''''''''''''

1. The ``init`` command performs several different initialization steps to prepare the current working directory for use with Terraform. 

Run this command to automatically find, download, and install the necessary Aiven Provider plugins:

.. code:: bash

   terraform init 

2. The ``plan`` command creates an execution plan and shows you the resources that will be created or modified. It does not actually create any resources. 

Run this command to preview the changes:

.. code:: bash

   terraform plan -var-file=var-values.tfvars

3. The ``terraform apply`` command creates or modifies the infrastructure resources. 

Run the following command to create the Redis service:

.. code:: bash

   terraform apply -var-file=var-values.tfvars

The output will be similar to the following:

.. code:: bash
  
  Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

You can also see the service in the `Aiven Console <https://console.aiven.io>`_.

Clean up
''''''''

1. Create a destroy plan to preview the changes by running the following command:

.. code:: bash

   terraform plan -var-file=var-values.tfvars -destroy

This runs ``terraform plan`` in destroy mode and shows you the proposed changes without making them.

2. To delete the resources and all their data, run the following command: 

.. code:: bash

   terraform destroy -var-file=var-values.tfvars


Further reference
'''''''''''''''''

This article outlined a simple Terraform project structure. For a more complex project structure, refer to the `Terraform Docs <https://www.terraform.io/language/modules/develop/structure>`_. 
