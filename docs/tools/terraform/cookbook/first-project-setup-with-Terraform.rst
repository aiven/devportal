PLACEHOLDER
===========

There are four different Terraform files - each serving a specific purpose. Let's go over each of these files.

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


Consider this code block similar to declaring a dependency; the **Aiven Terraform Provider** in this case. We mention the source of the provider and specify a certain version to be used.
Following `Aiven Terraform Provider doc <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_, ``api_token`` is the only parameter for the provider configuration.
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

This file relates to the Terraform best practices since you don't want to hardcode certain values within the main Terraform file.

3. ``var-values.tfvars`` file:

.. code:: bash

   aiven_api_token = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
   project_name = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

This is where you put the actual values for Aiven API token and Aiven console project name. This file is passed to Terraform using the ``-var-file=`` flag.

4. ``services.tf`` file: