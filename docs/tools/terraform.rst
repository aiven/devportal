Aiven Terraform Provider
=========================

    Terraform is an open-source infrastructure as code software tool that provides a consistent CLI workflow to manage hundreds of cloud services. Terraform codifies cloud APIs into declarative configuration files. `Terraform website <https://www.terraform.io/>`_.

With Aiven's Terraform Provider you can manage all our services with code.

See the `official documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ to learn about all the possible services and resources and the `GitHub repository <https://github.com/aiven/terraform-provider-aiven>`_ for reporting issues and contributing.

.. caution::
  Recreating stateful services with Terraform will possibly delete the service and all its data before creating it again. Whenever the Terraform plan indicates that a service will be deleted or replaced, a catastrophic action is possibly about to happen.

  Some properties, like project and the resource name, cannot be changed and it will trigger a resource replacement.

  To avoid any issues, please set the termination_protection property to true on all production services, it will prevent Terraform to remove the service until the flag is set back to false again. While it prevents a service to be deleted, any logical databases, topics or other configurations may be removed even when this section is enabled. Be very careful!

Getting Started
---------------

Requirements 
''''''''''''
- `Download and install Terraform <https://www.terraform.io/downloads.html>`_
- `Signup <https://console.aiven.io/signup?utm_source=github&utm_medium=organic&utm_campaign=devportal&utm_content=repo>`_ for Aiven if you haven't already
- `Generate an authentication token <https://help.aiven.io/en/articles/2059201-authentication-tokens>`_ on Aiven's console or CLI

Setting up the provider
'''''''''''''''''''''''
Create a file named `main.tf` and add the content below:

.. code :: terraform

    terraform {
      required_providers {
        aiven = {
          source  = "aiven/aiven"
          version = "2.1.12" # check out the latest version in the github release section
        }
      }
    }

    provider "aiven" {
      api_token = "your-api-token"
    }

Run the following command to initialize the Terraform environment::

  $ terraform init

Deploying a PostgreSQL database
'''''''''''''''''''''''''''''''
Add the following block of code to the file. It will deploy a PostgreSQL database on the GCP Frankfurt region:

.. code :: terraform

    resource "aiven_pg" "postgresql" {
      project                = "your-project-name"
      service_name           = "postgresql"
      cloud_name             = "google-europe-west3"
      plan                   = "startup-4"
    }
    
    output "postgresql_service_uri" {
      value     = aiven_pg.postgresql.service_uri
      sensitive = true
    }

Plan and apply the Terraform code::

  $ terraform plan
  $ terraform apply

Access the database::

  $ psql "$(terraform output -raw postgresql_service_uri)"

Cleaning Up
'''''''''''
To destroy the created PostgreSQL database, use the following command::

  $ terraform destroy

Learn More
----------
Check out these resources to learn more about Terraform and our Provider:

* `Learn Terraform <https://learn.hashicorp.com/collections/terraform/aws-get-started>`_
* `Aiven Terraform Provider documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_

Contributing
------------
If you have any issues or would like to contribute to the tool, please join us on the `GitHub repository <https://github.com/aiven/terraform-provider-aiven>`_.