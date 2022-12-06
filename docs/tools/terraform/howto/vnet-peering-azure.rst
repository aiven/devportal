Azure virtual network peering
=============================

This how-to is based on original :doc:`article </docs/platform/howto/vnet-peering-azure>`
made for Aiven and Azure cli.
It follows original chapter-by-chapter,
I will find every step signed with the very same title below in the example.

And while most of terraform manifestos can be applied in one go,
we'll have to break it up into two:

1. First, we will create most of the necessary resources
2. Then we will configure Azure provider using data from step one
   to create the last resource and connect networks together

Before you start
~~~~~~~~~~~~~~~~

Create an  `Aiven authentication token </docs/platform/howto/create_authentication_token>`.
Then set up `authentication for Azure <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs>`_
and `Azure Active Directory <https://registry.terraform.io/providers/hashicorp/azuread/latest/docs>`_.
For example:

.. code-block::

    terraform {
      required_providers {
        aiven = {
          source = "aiven/aiven"
          verstion = ">= 3.8.0, < 4.0.0"
        }
        azuread = {
          source  = "hashicorp/azuread"
          version = "=2.30.0"
        }
        azurerm = {
          source  = "hashicorp/azurerm"
          version = "=3.30.0"
        }
      }
    }

    provider "aiven" {
      api_token = var.aiven_api_token
    }

    provider "azuread" {
      client_id     = "00000000-0000-0000-0000-000000000000"
      client_secret = var.azure_client_secret
      tenant_id     = "00000000-0000-0000-0000-000000000000"
    }

    provider "azurerm" {
      features {}
      subscription_id = "00000000-0000-0000-0000-000000000000"
      client_id       = "00000000-0000-0000-0000-000000000000"
      client_secret   = var.azure_client_secret
      tenant_id       = "00000000-0000-0000-0000-000000000000"
    }


Step 1: Create or bind the resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create or bind the existing resources using ``terraform import`` using the steps in this example:

.. code-block::

    data "aiven_project" "avn_project" {
      project = "aiven-ci-kubernetes-operator"
    }

    data "azurerm_subscription" "subscription" {
      subscription_id = "00000000-0000-0000-0000-000000000000"
    }

    resource "aiven_project_vpc" "avn_vpc" {
      project      = data.aiven_project.avn_project.project
      cloud_name   = "azure-germany-westcentral"
      network_cidr = "192.168.1.0/24"

      timeouts {
        create = "15m"
      }
    }

    resource "azurerm_resource_group" "resource_group" {
      location = "germanywestcentral"
      name     = "my-azure-resource-group"
    }

    resource "azurerm_virtual_network" "virtual_network" {
      name                = "my-azure-virtual-network"
      address_space       = ["10.0.0.0/16"]
      location            = azurerm_resource_group.resource_group.location
      resource_group_name = azurerm_resource_group.resource_group.name
    }

    # 1. Log in with an Azure admin account
    # Already done.

    # 2. Create application object
    resource "azuread_application" "app" {
      display_name = "my-azure-application"
      sign_in_audience = "AzureADandPersonalMicrosoftAccount"

      api {
        requested_access_token_version = 2
      }
    }

    # 3. Create a service principal for your app object
    resource "azuread_service_principal" "app_principal" {
      application_id = azuread_application.app.application_id
    }

    # 4. Set a password for your app object
    resource "azuread_application_password" "app_password" {
      application_object_id = azuread_application.app.object_id
    }

    # 5. Find the id properties of your virtual network
    # Skip, we have values in the state

    # 6. Grant your service principal permissions to peer
    resource "azurerm_role_assignment" "app_role" {
      role_definition_name = "Network Contributor"
      principal_id         = azuread_service_principal.app_principal.object_id
      scope                = azurerm_virtual_network.virtual_network.id
    }

    # 7. Create a service principal for the Aiven application object
    # Yes, application_id is hardcoded.
    resource "azuread_service_principal" "aiven_app_principal" {
      application_id = "55f300d4-fc50-4c5e-9222-e90a6e2187fb"
    }

    # 8. Create a custom role for the Aiven application object
    resource "azurerm_role_definition" "role_definition" {
      name        = "my-azure-role-definition"
      description = "Allows creating a peering to vnets in scope (but not from)"
      scope       = "/subscriptions/${data.azurerm_subscription.subscription.subscription_id}"

      permissions {
        actions = ["Microsoft.Network/virtualNetworks/peer/action"]
      }

      assignable_scopes = [
        "/subscriptions/${data.azurerm_subscription.subscription.subscription_id}"
      ]
    }

    # 9. Assign the custom role to the Aiven service principal
    resource "azurerm_role_assignment" "aiven_role_assignment" {
      role_definition_id = azurerm_role_definition.role_definition.role_definition_resource_id
      principal_id       = azuread_service_principal.aiven_app_principal.object_id
      scope              = azurerm_virtual_network.virtual_network.id

      depends_on = [
        azuread_service_principal.aiven_app_principal,
        azurerm_role_assignment.app_role
      ]
    }

    # 10. Find your AD tenant id
    # Skip, it's in the env

    # 11. Create a peering connection from the Aiven Project VPC
    # 12. Wait for the Aiven platform to set up the connection
    resource "aiven_azure_vpc_peering_connection" "peering_connection" {
      vpc_id                = aiven_project_vpc.avn_vpc.id
      peer_resource_group   = azurerm_resource_group.resource_group.name
      azure_subscription_id = data.azurerm_subscription.subscription.subscription_id
      vnet_name             = azurerm_virtual_network.virtual_network.name
      peer_azure_app_id     = azuread_application.app.application_id
      peer_azure_tenant_id  = "00000000-0000-0000-0000-000000000000"

      depends_on = [
        azurerm_role_assignment.aiven_role_assignment
      ]
    }


Step 2: Create peering in Azure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now create the connection using the credentials from the previous step.
.. note::

Terraform doesn't support dynamic provider configuration.
In the same file, follow these steps to create the connection:


.. code-block::

    # 13. Create peering from your VNet to the Project VPC's VNet
    provider "azurerm" {
      features {}
      alias                = "app"
      client_id            = azuread_application.app.application_id
      client_secret        = azuread_application_password.app_password.value
      subscription_id      = data.azurerm_subscription.subscription.subscription_id
      tenant_id            = "00000000-0000-0000-0000-000000000000"
      auxiliary_tenant_ids = [azuread_service_principal.aiven_app_principal.application_tenant_id]
    }

    resource "azurerm_virtual_network_peering" "network_peering" {
      provider                     = azurerm.app
      name                         = "my-azure-virtual-network-peering"
      remote_virtual_network_id    = aiven_azure_vpc_peering_connection.peering_connection.state_info["to-network-id"]
      resource_group_name          = azurerm_resource_group.resource_group.name
      virtual_network_name         = azurerm_virtual_network.virtual_network.name
      allow_virtual_network_access = true
    }

    # 14. Wait until the Aiven peering connection is active

