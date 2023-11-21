Set up Google Cloud Platform virtual network peering with Terraform
====================================================================

This help article provides step-by-step instructions for setting up a VPC peering connection between Aiven and Google Cloud Platform (GCP) using Terraform. See the `Using VPC
peering <https://docs.aiven.io/docs/platform/howto/manage-vpc-peering.html>`__
article for how to set up a Project VPC.

Before you start, make sure you have an Aiven authentication token and have set up the Google Cloud SDK.

Prerequisites:
~~~~~~~~~~~~~~~~

* Create an :doc:`Aiven authentication token </docs/platform/howto/create_authentication_token>`.

* `Install the Google Cloud SDK <https://cloud.google.com/sdk/docs/install>`_.

* Authenticate using the following command

.. code-block:: console

    gcloud auth application-default login

Set up the Terraform variables:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named ``variables.tf`` and add the following code:

.. code-block::

    variable "aiven_api_token" {}
    variable "gcp_project_id" {}

This file declares the variables for the Aiven API token and the Google Cloud project ID.

Configure the Terraform providers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named ``provider.tf`` and add the following code:

.. code-block::

    terraform {
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = "~> 3.0"
        }
        aiven = {
          source  = "aiven/aiven"
          version = ">=4.0.0, <5.0.0"
        }
      }
    }
    provider "aiven" {
      api_token = var.aiven_api_token
    }
    provider "google" {
      project = var.gcp_project_id
      region  = "us-central1"
      zone    = "us-central1-a"
    }

This code initializes the Aiven and Google providers, specifying the required provider versions and configurations. It also uses the variables defined in the ``variables.tf`` file

Create a VPC and subnet in GCP:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named project.tf and add the following code:

.. code-block::

    #Get Aiven project details
    data "aiven_project" "my_project" {
      project = "project_name"
    }
    #Create a VPC in GCP
    resource "google_compute_network" "vpc" {
      name                    = "my-vpc"
      auto_create_subnetworks = "false"
    }
    #Create a subnet in the GCP VPC
    resource "google_compute_subnetwork" "subnet" {
      name          = "my-subnet"
      region        = "us-central1"
      ip_cidr_range = "10.0.0.0/24"
      network       = google_compute_network.vpc.self_link
    }

This code retrieves the details of your Aiven project, creates a VPC in GCP, and creates a subnet within that VPC.

Create a VPC in Aiven:
~~~~~~~~~~~~~~~~~~~~~~

Add the following code to your ``project.tf`` file to create a VPC in Aiven:

.. code-block::

    resource "aiven_project_vpc" "my_vpc" {
      project      = data.aiven_project.my_project.project
      cloud_name   = "google-us-central1"
      network_cidr = "192.168.0.0/24"
    }

This code creates a VPC in your Aiven project. The ``network_cidr`` parameter specifies the CIDR range for the Aiven VPC. Ensure that this CIDR range does not overlap with the CIDR range of your GCP VPC. In this example, the Aiven VPC uses the CIDR range "192.168.0.0/24"

Create a peering connection between Aiven and GCP:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following code to your project.tf file to create a peering connection between the Aiven VPC and your GCP VPC:

.. code-block::

    resource "aiven_gcp_vpc_peering_connection" "my_peering" {
      vpc_id             = aiven_project_vpc.my_vpc.id
      gcp_project_id     = var.gcp_project_id
      peer_vpc           = google_compute_network.vpc.name
      }
    resource "google_compute_network_peering" "aiven_peering" {
      depends_on         = [aiven_gcp_vpc_peering_connection.my_peering]
      name               = var.gcp_project_id
      network            = google_compute_network.vpc.self_link
      peer_network       = aiven_gcp_vpc_peering_connection.my_peering.self_link
      }

This code creates a peering connection between the Aiven VPC and the GCP VPC by using the ``aiven_gcp_vpc_peering_connection`` and ``google_compute_network_peering`` resources. The depends_on attribute ensures that the ``aiven_gcp_vpc_peering_connection`` resource is created before the ``google_compute_network_peering`` resource.

Apply the Terraform configuration and verify the VPC peering status:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following commands to initialize and apply the Terraform configuration:

.. code-block:: console

    terraform init
    terraform apply

Review the proposed changes and enter yes when prompted to proceed. Terraform will create the VPC peering connection between Aiven and GCP. After the resources have been created, verify that the VPC peering connection is active by checking the state attribute of the ``google_compute_network_peering`` resource. It should have changed from "PENDING_PEER" to "ACTIVE"

.. code-block:: console

    terraform show

Look for the ``google_compute_network_peering.aiven_peering`` resource in the output, and confirm that the state attribute is set to "ACTIVE". This indicates that the VPC peering connection between Aiven and GCP has been successfully established.