Set up your first Aiven Terraform project
=========================================

This example shows the setup for a Terraform project containing a single Redis™** service, and shows off some useful commands to stand up (and destroy) your Aiven data infrastructure.

Prepare the dependencies 
''''''''''''''''''''''''
- `Download and install Terraform <https://www.terraform.io/downloads.html>`_
- `Sign up <https://console.aiven.io/signup?utm_source=github&utm_medium=organic&utm_campaign=devportal&utm_content=repo>`_ for Aiven if you haven't already
- `Generate an authentication token <https://developer.aiven.io/docs/platform/howto/create_authentication_token.html>`_

.. Tip::

    Make sure that you have either the *Administrator* or *Operator* role when creating the API token. When you create a project, you automatically receive the *Administrator* access.

    For more details, refer to the `Project members and roles page <https://developer.aiven.io/docs/platform/concepts/projects_accounts_access.html#project-members-and-roles>`_.

Configure your project and services
'''''''''''''''''''''''''''''''''''

Your Terraform files declare the structure of your infrastructure as well as required dependencies and configuration. While you can stuff these together in one file, it's ideal to keep those as separate files.
In this section, you'll learn how to structure a simple Terraform project. 

Start with an empty folder, and follow these steps to define and then create your Aiven services.

1. First we declare a dependency on the *Aiven Terraform Provider*. Within the ``required_providers`` block, you mention the source of the provider and specify a certain version (check which are the current versions and update accordingly).
Following `Aiven Terraform Provider documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_, ``api_token`` is the only parameter for the provider configuration.

Add the following to a new ``provider.tf`` file:

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


2.  The following Terraform script deploys a single-node Redis service. This is a minimal example which you can swap out with your own Terraform scripts or other advanced recipes from :doc:`the Terraform cookbook <reference/cookbook>`.

The contents of the ``redis.tf`` file should look like this:

.. code:: bash

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


3. To avoid including sensitive information in source control, the variables are defined here in the ``variables.tf`` file. You can then use a ``*.tfvars`` file with the actual values so that Terraform receives the values during runtime, and exclude it.

The ``variables.tf`` file defines both the API token, and the project name to use:

.. code:: bash

   variable "aiven_api_token" {
      description = "Aiven console API token"
      type = string
   }

   variable "project_name" {
      description = "Aiven console project name"
      type        = string
   }


The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

``var-values.tfvars`` file:

.. code:: bash

   aiven_api_token = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
   project_name = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

Edit the file and replace the ``<..>`` sections with the API token you created earlier, and the name of the Aiven project that resources should be created in.


Apply the Terraform configuration
'''''''''''''''''''''''''''''''''


The ``init`` command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform provider plugins.

.. code:: bash

   terraform init 

The ``plan`` command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

.. code:: bash

   terraform plan -var-file=var-values.tfvars

If you're satisfied with the output of ``terraform plan``, go ahead and run the ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

.. code:: bash

   terraform apply -var-file=var-values.tfvars

The output will show you if everything worked well. You can now visit the `Aiven web console <https://console.aiven.io>`_ and admire your new services.

Clean up
''''''''

If this was a test environment, be sure to delete the resources once you're done to avoid consuming unwanted bills. To be confident about the service termination, you can create a speculative destroy plan by running the following command:

.. code:: bash

   terraform plan -destroy

This will run ``terraform plan`` in destroy mode and show you the proposed destroy changes without executing them.

.. warning::

   Use the following command with caution. This will actually delete resources that might have important data.

.. code:: bash

   terraform destroy -var-file=var-values.tfvars

By destroying your services when you don't need them, for example in a testing environment, you can be confident that no unnecessary services are left running up the bills.

Further reference
'''''''''''''''''

This article outlined a simple Terraform project structure. For a more complex project structure, please refer to the `Terraform Docs <https://www.terraform.io/language/modules/develop/structure>`_. 
