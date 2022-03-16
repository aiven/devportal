Set up your first Terraform project
===================================

This example shows the setup for a simple Terraform project and some useful commands to stand up (and destroy) your Aiven data infrastructure.

Requirements 
''''''''''''
- `Download and install Terraform <https://www.terraform.io/downloads.html>`_
- `Sign up <https://console.aiven.io/signup?utm_source=github&utm_medium=organic&utm_campaign=devportal&utm_content=repo>`_ for Aiven if you haven't already
- `Generate an authentication token <https://developer.aiven.io/docs/platform/howto/create_authentication_token.html>`_ on Aiven's console or CLI


Configure your project and services
'''''''''''''''''''''''''''''''''''

Your Terraform file(s) consists of lines for the actual infrastructure as well as required dependencies and configurations. While you can stuff these together in one file, it's ideal to keep those as separate files.
In this section, you'll learn how to structure a simple Terraform project. 

1.  BYOTF - Bring Your Own Terraform Script. 

``services.tf`` file:

.. code:: bash

   # Your actual Terraform script goes here 


2. Consider the following code block similar to declaring a dependency; the *Aiven Terraform Provider* in this case. Within the `required_providers` block, you mention the source of the provider and specify a certain version. 
The versions here are for example purpose and will change in the future. Following `Aiven Terraform Provider doc <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_, `api_token` is the only parameter for the provider configuration.

Make sure that you have either the *Administrator* or *Operator* role when creating the API token. When you create a project, you automatically receive the *Administrator* access. 
For more details, refer to the `Project members and roles page <https://developer.aiven.io/docs/platform/concepts/projects_accounts_access.html#project-members-and-roles>`_.

``provider.tf`` file:

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


3. Avoid including sensitive values in configuration files that are under source control. Rather than using sensitive information within this *variables.tf* file, you can use a ``*.tfvars`` file so that Terraform receives the values during runtime.

``variables.tf`` file:

.. code:: bash

   variable "aiven_api_token" {
      description = "Aiven console API token"
      type = string
   }

   variable "project_name" {
      description = "Aiven console project name"
      type        = string
   }


4. This is where you put the actual values for Aiven API token and Aiven console project name. This file is passed to Terraform using the ``-var-file=`` flag.

``var-values.tfvars`` file:

.. code:: bash

   aiven_api_token = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
   project_name = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"


Execution
'''''''''

Create an empty folder and add the above files to that folder. Then execute the following commands in order:

.. code:: bash

   terraform init 

This command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform Provider plugins.

.. code:: bash

   terraform plan -var-file=var-values.tfvars

This command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

.. code:: bash

   terraform apply -var-file=var-values.tfvars

If you're satisfied with ``terraform plan``, you execute ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 


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


Further reference
'''''''''''''''''

This article outlined a simple Terraform project structure. For a more complex project structure, please refer to the `Terraform Docs <https://www.terraform.io/language/modules/develop/structure>`_. 