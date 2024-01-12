Set up AWS virtual network peering with Terraform
==================================================

This help article provides step-by-step instructions for setting up a VPC peering connection between Aiven and Amazon Web Services Platform (AWS) using Terraform. See the `Using VPC
peering <https://docs.aiven.io/docs/platform/howto/manage-vpc-peering.html>`__
article for how to set up a Project VPC.

Before you start, make sure you have an Aiven authentication token and have set up the AWS CLI.

Prerequisites:
~~~~~~~~~~~~~~~~

* Create an :doc:`Aiven authentication token </docs/platform/howto/create_authentication_token>`.

* `Install the AWS CLI <https://docs.aws.amazon.com/cli/latest/userguide/get-started-install.html>`_.

* `Configure the AWS CLI <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html>`_.

Set up the Terraform variables:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named ``variables.tf`` and add the following code:

.. code-block::

    variable "aiven_api_token" {}
    variable "aws_account_id" {}
    variable "aiven_project_name" {}

This file declares the variables for the Aiven API token, Aiven project name and the AWS account ID.

Configure the Terraform providers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named ``provider.tf`` and add the following code:

.. code-block::

    terraform {
      required_providers {
        aiven = {
          source  = "aiven/aiven"
          version = ">= 4.0.0, < 5.0.0"
        }
    
        aws = {
          source  = "hashicorp/aws"
          version = "~> 5.0"
        }
      }
    }
    
    provider "aiven" {
      api_token = var.aiven_api_token
    }
    
    provider "aws" {
        region     = "ap-southeast-2"
    }

This code initializes the Aiven and AWS providers, specifying the required provider versions and configurations. It also uses the variables defined in the ``variables.tf`` file

Create a VPC and subnet in AWS:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named project.tf and add the following code:

.. code-block::

    # Create a VPC in AWS 
    resource "aws_vpc" "awsvpc" {
      cidr_block       = "10.0.0.0/16"
      enable_dns_hostnames = true
      tags = {
        Name = "test-vpc"
      }
    }

    # Create a subnet in the AWS VPC    
    resource "aws_subnet" "awssubnet1" {
      vpc_id     = aws_vpc.awsvpc.id
      cidr_block = "10.0.1.0/24"
    
      tags = {
        Name = "test-subnet1"
      }
    }
     
    #Get Aiven project details
    data "aiven_project" "my_project" {
      project = var.aiven_project_name
    }

This code retrieves the details of your Aiven project, creates a VPC in AWS, and creates a subnet within that VPC.

Create a VPC in Aiven:
~~~~~~~~~~~~~~~~~~~~~~

Add the following code to your ``project.tf`` file to create a VPC in Aiven:

.. code-block::

    # Create Aiven Project VPC
    resource "aiven_project_vpc" "my_vpc" {
      project      = data.aiven_project.my_project.project
      cloud_name   = "aws-ap-southeast-2"
      network_cidr = "192.168.0.0/24"
    }

This code creates a VPC in your Aiven project. The ``network_cidr`` parameter specifies the CIDR range for the Aiven VPC. Ensure that this CIDR range does not overlap with the CIDR range of your AWS VPC. In this example, the Aiven VPC uses the CIDR range "192.168.0.0/24"

Create a peering connection between Aiven and AWS:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following code to your project.tf file to create a peering connection between the Aiven VPC and your AWS VPC:

.. code-block::

    # Create a VPC peering from Aiven.
    resource "aiven_aws_vpc_peering_connection" "peertoaws" {
      vpc_id         = aiven_project_vpc.my_vpc.id
      aws_account_id = var.aws_account_id
      aws_vpc_id     = aws_vpc.awsvpc.id
      aws_vpc_region = "ap-southeast-2"
      depends_on = [
        aiven_project_vpc.my_vpc, aws_vpc.awsvpc
      ]
    
    }
    # Accept the VPC peering initiated from Aiven.
    resource "aws_vpc_peering_connection_accepter" "peer" {
      vpc_peering_connection_id = aiven_aws_vpc_peering_connection.peertoaws.aws_vpc_peering_connection_id
      auto_accept               = true
    
      tags = {
        Side = "Accepter"
      }
    
      depends_on = [
        aiven_aws_vpc_peering_connection.peertoaws
      ]
    }

    # Route tables should be updated, this is an example routing the Aiven VPC CIDR through the peering connection.
    resource "aws_route_table" "route_aiven" {
      vpc_id = aws_vpc.awsvpc.id
    
      route {
        cidr_block = "192.168.0.0/24"
        vpc_peering_connection_id = aiven_aws_vpc_peering_connection.peertoaws.aws_vpc_peering_connection_id
      }
    }
    # Route table should be associated to the subnets.
    resource "aws_route_table_association" "subnet1_aiven" {
      subnet_id      = aws_subnet.awssubnet1.id
      route_table_id = aws_route_table.route_aiven.id
    }

This code creates a peering connection between the Aiven VPC and the AWS VPC by using the ``aiven_aws_vpc_peering_connection`` and ``aws_vpc_peering_connection_accepter`` resources. The depends_on attribute ensures that the required resources exist before the new resource is created. Route tables should be updated/created to enable routes to the Aiven VPC from AWS VPC.

Apply the Terraform configuration and verify the VPC peering status:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following commands to initialize and apply the Terraform configuration:

.. code-block:: console

    terraform init
    terraform apply

Review the proposed changes and enter yes when prompted to proceed. Terraform will create the VPC peering connection between Aiven and AWS. After the resources have been created, verify that the VPC peering connection is active by checking the state attribute of the ``aiven_aws_vpc_peering_connection`` resource. It should have changed from "PENDING_PEER" to "ACTIVE", this may take some minutes (10-15). In order to refresh the status and show current status run the following code:  

.. code-block:: console

    terraform apply
    terraform show

Look for the ``aiven_aws_vpc_peering_connection`` resource in the output, and confirm that the state attribute is set to "ACTIVE". This indicates that the VPC peering connection between Aiven and AWS has been successfully established.