Set up your first Terraform project
===================================

This example shows the setup for a sample Terraform project and some useful commands to stand up (and destroy) your data infrastructure.

1. ``provider.tf`` file:

.. code:: bash

   terraform {
      required_providers {
         aiven = {
            source  = "aiven/aiven"
            version = ">= 2.6.0, < 3.0.0"
         }
      }
   }

   provider "aiven" {
      api_token = var.aiven_api_token
   }


Consider this code block similar to declaring a dependency; the *Aiven Terraform Provider* in this case. Within the *required_providers* block, you mention the source of the provider and specify a certain version. The versions here are for example purpose and will change in the future.
Following `Aiven Terraform Provider doc <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_, *api_token* is the only parameter for the provider configuration. Refer to `Create an authentication token <https://developer.aiven.io/docs/platform/howto/create_authentication_token.html>`_ page for instructions, if needed.

Make sure the owner of the API Authentication Token has admin permissions in Aiven.

2. ``variables.tf`` file:

.. code:: bash

   variable "aiven_api_token" {
      description = "Aiven console API token"
      type = string
   }

   variable "project_name" {
      description = "Aiven console project name"
      type        = string
   }

Avoid including sensitive values in configuration files that are under source control. Rather than using sensitive information within this *variables.tf* file, you can use a ``*.tfvars`` file so that Terraform receives the values during runtime.

3. ``var-values.tfvars`` file:

.. code:: bash

   aiven_api_token = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
   project_name = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

This is where you put the actual values for Aiven API token and Aiven console project name. This file is passed to Terraform using the ``-var-file=`` flag.

4. ``services.tf`` file:

.. code:: bash

   # Your actual Terraform script goes here 

Assuming that you have `Terraform installed <https://www.terraform.io/downloads>`_, create an empty folder and add the above files to that folder. Then execute the following commands in order:

.. code:: bash

   terraform init 

This command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform Provider plugins.

.. code:: bash

   terraform plan -var-file=var-values.tfvars

This command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

.. code:: bash

   terraform apply -var-file=var-values.tfvars

If you're satisfied with ``terraform plan``, you execute ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

Optional
--------

If this was a test environment, be sure to delete the resources once you're done to avoid consuming unwanted bills. 

.. warning::

   Use this command with caution. This will actually delete resources that might have important data.

.. code:: bash

   terraform destroy -var-file=var-values.tfvars
