Upgrade the Aiven Terraform Provider from v2 to v3
==================================================

This article will walk you through upgrading the Aiven Terraform Provider from v2 to v3.

Major changes in v3
'''''''''''''''''''

Aiven Terraform Provider has a `detailed changelog <https://github.com/aiven/terraform-provider-aiven/blob/main/CHANGELOG.md>`_ but the main additions in v3 are:

- Generic ``aiven_vpc_peering_connection`` replaced with provider specific resources
- Generic ``aiven_service_user`` replaced with service specific resources
- Generic ``aiven_database`` replaced with service specific resources

Upgrade Aiven Terraform provider
''''''''''''''''''''''''''''''''

Update the Aiven Terraform Provider by
editing the providers block of your script to include the latest version of
the Aiven Terraform Provider (v3.8.1 at the time of writing):

.. code:: terraform
    
    terraform {
      required_providers {
        aiven = {
          source  = "aiven/aiven"
          version = ">= 3.8.1"
        }
      }
    }
    
    
Update to provider specific VPC peering connection resource syntax
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

V3 of the Aiven Terraform Provider moves away from using ``aiven_vpc_peering_connection`` as a resource,
and instead provides provider specific resources such as ``aiven_azure_vpc_peering_connection``.
Since we probably don't want to destroy existing resources and make new ones,
this guide will help you perform the migration safely.

.. warning::
    Since ``aiven_vpc_peering_connection`` and the new one such as ``aiven_azure_vpc_peering_connection`` are different kinds of resources,
    simply rewriting the code would cause destructive actions.
    These steps will preserve your resources.

Please also note that running ``terraform state mv <a> <b>`` is not recommended
because these are different resource types.

.. tip::
    Backup your Terraform state file ``terraform.tfstate`` (if available),
    just in case of potential rollback.

To safely make this change you will:

-  Change the code
-  Remove old resource from the state
-  Import already existing resource to the Terraform state.

1. To change from the old ``aiven_vpc_peering_connection`` to the new ``aiven_azure_vpc_peering_connection`` resource,
the resource type should be changed.
Any references to ``aiven_vpc_peering_connection.foo.*`` should be updated to instead read ``aiven_azure_vpc_peering_connection.foo.*`` instead.
Here's an example showing the update in action::

    - resource "aiven_vpc_peering_connection" "foo" {
        vpc_id                = data.aiven_project_vpc.vpc.id
    -   peer_cloud_account    = "Azure subscription ID"
    -   peer_vpc              = "Azure virtual network name of the peered VPC"
        peer_azure_app_id     = "Azure app registration id in UUID4 form"
        peer_azure_tenant_id  = "Azure tenant id in UUID4 form"
        peer_resource_group   = "Azure resource group name of the peered VPC"
      }

    + resource "aiven_azure_vpc_peering_connection" "foo" {
        vpc_id                = data.aiven_project_vpc.vpc.id
    +   azure_subscription_id = "Azure subscription ID"
    +   vnet_name             = "Azure virtual network name of the peered VPC"
        peer_azure_app_id     = "Azure app registration id in UUID4 form"
        peer_azure_tenant_id  = "Azure tenant id in UUID4 form"
        peer_resource_group   = "Azure resource group name of the peered VPC"
      }


2. Check the current state of the world::

    terraform state list | grep azure

3. Remove the resource from the control of Terraform::

    terraform state rm aiven_vpc_peering_connection.foo

.. tip::
    Use the ``-dry-run`` flag to see this change before it is actually made

4. Add the resource back to Terraform by importing it as a new resource with the new type::

    terraform import aiven_azure_vpc_peering_connection.foo project_name/vpc_id/azure_subscription_id/vnet_name

5. Check that the import is going to run as you expect::

    terraform plan

6. Finally, go ahead and apply the new configuration::

    terraform apply

.. Note::
    You can follow a similar approach to update ``aiven_database`` and ``aiven_service_user`` resources,
    which have been deprecated in v3 of the provider.
