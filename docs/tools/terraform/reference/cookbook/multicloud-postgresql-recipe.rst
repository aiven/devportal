Deploy PostgreSQL® services to multiple clouds and regions
==========================================================

There are many reasons why businesses need to distribute their databases geographically. One of the primary reason is data residency/regulation which mandates user data to stay within certain regions. 
This example shows how to set up three highly-available PostgreSQL databases in three regions and across different cloud providers for data regulation and compliance. In addition, these databases must be configured in a way that they are protected against database deletion.
`Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ can help create multiple services programmatically. 

The following image shows that the Aiven Terraform Provider calls the Aiven API under the hood to create three PostgreSQL services on AWS (Europe), DigitalOcean (US), and Google Cloud Platform(Asia):

.. mermaid::

   graph TD
      B[(Aiven for PostgreSQL - AWS EU)]
      C[(Aiven for PostgreSQL - DigitalOcean NA)]
      D[(Aiven for PostgreSQL - GCP Asia)]

Describe the setup
------------------

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name`` and ``api_token``.

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code:: terraform

       terraform {
         required_providers {
           aiven = {
             source  = "aiven/aiven"
             version = ">= 3.7"
           }
         }
       }
   
       provider "aiven" {
         api_token = var.aiven_api_token
       }
   
    You can also set the environment variable ``AIVEN_TOKEN`` for the ``api_token`` property. With this, you don't need to pass the ``-var-file`` flag when executing Terraform commands.
 
    2. To avoid including sensitive information in source control, the variables are defined here in the ``variables.tf`` file. You can then use a ``*.tfvars`` file with the actual values so that Terraform receives the values during runtime, and exclude it.

    The ``variables.tf`` file defines the API token, the project name to use, and the prefix for the service name:

    .. code:: terraform

       variable "aiven_api_token" {
         description = "Aiven console API token"
         type        = string
       }
   
       variable "project_name" {
         description = "Aiven console project name"
         type        = string
       }
   
    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

Here is the sample Terraform file to deploy all three services. Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced PostgreSQL configurations is added at the end of this document.

``services.tf`` file:

.. code:: terraform
   
   # European Postgres Service
   resource "aiven_pg" "aws-eu-pg" {
     project                = var.project_name
     cloud_name             = "aws-eu-west-2" # London
     plan                   = "business-8"    # Primary + read replica
     service_name           = "postgres-eu-aws"
     termination_protection = true
   }
   
   # US Postgres Service
   resource "aiven_pg" "do-us-pg" {
     project                = var.project_name
     cloud_name             = "do-nyc"     # New York
     plan                   = "business-8" # Primary + read replica
     service_name           = "postgres-us-do"
     termination_protection = true
   }
   
   # Asia Postgres Service
   resource "aiven_pg" "gcp-as-pg" {
     project                = var.project_name
     cloud_name             = "google-asia-southeast1" # Singapore
     plan                   = "business-8"             # Primary + read replica
     service_name           = "postgres-as-gcp"
     termination_protection = true
   }
   
.. dropdown:: Expand to check out how to execute the Terraform files.

    The ``init`` command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform provider plugins.
    
    .. code:: shell

       terraform init

    The ``plan`` command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

    .. code:: bash

       terraform plan -var-file=var-values.tfvars

    If you're satisfied with the output of ``terraform plan``, go ahead and run the ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

    .. code:: bash

       terraform apply -var-file=var-values.tfvars

This file creates three Aiven for PostgreSQL services across three cloud providers and in three different regions. The ``termination_protection = true`` property ensures that these databases are protected against accidental or unauthorized deletion.

With termination protection enabled, a ``terraform destroy`` command will result in a 403 response and an error message "Service is protected against termination and shutdown. Remove termination protection first.".

To destroy resources with termination protection, you need to update the script with ``termination_protection = false`` and then execute a ``terraform apply`` followed by a ``terraform destroy``.

More resources
--------------

You might find these related resources useful too:

- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Benefits and challenges of multi-cloud <https://aiven.io/blog/getting-the-most-of-multi-cloud>`_
