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
   
This file creates three Aiven for PostgreSQL services across three cloud providers and in three different regions. The ``termination_protection = true`` property ensures that these databases are protected against accidental or unauthorized deletion.

With termination protection enabled, a ``terraform destroy`` command will result in a 403 response and an error message "Service is protected against termination and shutdown. Remove termination protection first.".

To destroy resources with termination protection, you need to update the script with ``termination_protection = false`` and then execute a ``terraform apply`` followed by a ``terraform destroy``.

More resources
--------------

You might find these related resources useful too:

- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Benefits and challenges of multi-cloud <https://aiven.io/blog/getting-the-most-of-multi-cloud>`_
