Azure virtual network peering
=============================

This help article contains step-by-step instructions for setting up
peering in Azure. See the `Using VPC
peering <https://docs.aiven.io/docs/platform/howto/manage-vpc-peering.html>`__
article for how to set up a Project VPC. This creates an isolated
virtual network in the Aiven subscription where you can create services
instead of the Aiven cloud's public network.

.. note:: 
   Microsoft Azure uses the term ``Virtual Network`` (VNet), which is the same as a ``Virtual Private Cloud`` (VPC). We use the terms interchangeably in this article.

.. note::
    You can create VPC peering using :doc:`Aiven Provider for Terraform </docs/tools/terraform/howto/vnet-peering-azure>` as well.


Peer your network with the VPC
------------------------------

For an Azure virtual network peering's state to become **connected**
between networks A and B, a peering must be created both from network A
to B and from B to A. See
`this <https://learn.microsoft.com/en-us/azure/virtual-network/create-peering-different-subscriptions>`__
for an overview. In the case of Project VPCs, one of the networks is
located in the Aiven subscription and the Aiven platform handles
creating the peering from that network to the network you wish to peer.
For this the Aiven platform's `Active Directory application
object <https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals>`__
needs permissions in your subscription. Because the peering is between
subscriptions with different AD tenants, an application object is also
needed to your AD tenant, which can be used to create the peering from
your network to Aiven once it's been given permissions to do so.

Preparation
~~~~~~~~~~~

Please install the `Azure CLI <https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest>`__
as well as the :doc:`Aiven CLI </docs/tools/cli>` to follow this guide.

1. log in with an Azure admin account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the Azure CLI:

::

   az account clear
   az login

| This should open a window in your browser prompting to choose an Azure
  account to log in with. An account with at least the **Application
  administrator** role assignment will be needed for the later steps.

If you manage multiple Azure subscriptions, also configure the Azure CLI
to default to the correct subscription for the subsequent commands. This
is not needed if there's only one subscription:

::

   az account set --subscription <subscription name or id> 


2. create application object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an application object in your AD tenant. Using the Azure CLI,
this can be done with:

::

   az ad app create --display-name "<name of your choosing>" --sign-in-audience AzureADMultipleOrgs --key-type Password

This creates an entity to your AD that can be used to log into multiple
AD tenants ( ``--sign-in-audience AzureADMultipleOrgs`` ), but only the home
tenant (the tenant the app was created in) has the credentials to
authenticate the app. Save the ``appId`` field from the output - this
will be referred to as ``$user_app_id``

3. create a service principal for your app object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a service principal for the app object you created. The service
principal should be created to the Azure subscription the VNet you wish
to peer is located in:

::

   az ad sp create --id $user_app_id

This creates a service principal to your subscription that may given
permissions to peer your VNet. Save the ``id`` field from the JSON
output - this will be referred to as ``$user_sp_id`` . Notice that this
is different from the ``$user_app_id`` value earlier, which is also
shown in the output.

4. set a password for your app object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   az ad app credential reset --id $user_app_id

Save the ``password`` field from the output - this will be referred to
as ``$user_app_secret`` below

5. find the id properties of your virtual network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can be found in the Azure portal in "Virtual networks" -> name of
your network -> "Properties" -> "Resource ID", or using

::

   az network vnet list

Save the ``id`` field which will be referred to as ``$user_vnet_id`` .
Also grab

-  the Azure Subscription ID ("Properties" -> "Subscription ID") or the
   part after ``/subscriptions/`` in the resource ID. This is referred
   to as ``$user_subscription_id``

-  the resource group name ("Properties" -> "Resource group") or the
   ``resourceGroup`` field in the output. This is referred to as
   ``$user_resource_group``

-  the VNet name (title of the network page), or the ``name`` field from
   the output. Save this for later as ``$user_vnet_name``

``$user_vnet_id`` should have the format
``/subscriptions/$user_subscription_id/resourceGroups/$user_resource_group/providers/Microsoft.Network/virtualNetworks/$user_vnet_name``

6. grant your service principal permissions to peer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The service principal created in step 3 needs to be assigned a role that
has permission for the
``Microsoft.Network/virtualNetworks/virtualNetworkPeerings/write``
action on the scope of your VNet. To limit the amount of permissions the
app object and service principal has, you can create a custom role with
just that permission. The built-in *Network Contributor* role includes
that permission, and can be found using the Azure CLI with

::

   az role definition list --name "Network Contributor"

The ``id`` field from the output will be used as
``$network_contributor_role_id`` to assign the service principal that
role:

::

   az role assignment create --role $network_contributor_role_id --assignee-object-id $user_sp_id --scope $user_vnet_id

This allows the application object created earlier to manage the network
in the ``--scope`` above. Since the application object is controlled by
you, it may also be given permission for the scope of an entire resource
group, or the whole subscription to allow create other peerings later
without assigning the role again for each VNet separately.

7. create a service principal for the Aiven application object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Aiven AD tenant contains an application object (similar to the one
you created in step 2 that the Aiven platform uses to create a peering
from the Project VPC VNet in the Aiven subscription to the VNet from step
5 in your subscription. For this the Aiven app object needs a service
principal in your subscription:

::

   az ad sp create --id 55f300d4-fc50-4c5e-9222-e90a6e2187fb

The argument to ``--id`` field above is the ID of the Aiven application
object, this is a fix id and the command must be run like that. Save the ``id`` field from the JSON output - (just above the ``info`` field) - it will be
referred to as ``$aiven_sp_id`` later.

If this fails with the error "When using this permission, the backing
application of the service principal being created must in the local
tenant" then your account does not have the correct permissions. Please
use an account with at least the **Application administrator** role
assigned.

8. create a custom role for the Aiven application object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Aiven application now has a service principal that can be given
permissions. In order to target a network in your subscription with a
peering and nothing else, we'll create a this a custom role definition,
with only a single action allowing to do that and only that:

::

   az role definition create --role-definition '{"Name": "<name of your choosing>", "Description": "Allows creating a peering to vnets in scope (but not from)", "Actions": ["Microsoft.Network/virtualNetworks/peer/action"], "AssignableScopes": ["/subscriptions/'$user_subscription_id'"]}'

Creating a custom role must include your subscription's id in
``AssignableScopes`` . This in itself does not give permissions to your
subscription - it merely restricts which scopes a role assignment can
include. Save the ``id`` field from the output - this will be referred
to as ``$aiven_role_id``


9. assign the custom role to the Aiven service principal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To give the Aiven application object's service principal permissions to
peer with your VNet, assign the role created in the previous step to the
Aiven service principal (step 7) with the scope of your VNet (step 5)
with

::

   az role assignment create --role $aiven_role_id --assignee-object-id $aiven_sp_id --scope $user_vnet_id


10. find your AD tenant id
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ID of your AD tenant will be needed in the next step. Find it from
the Azure portal from "Azure Active Directory" -> "Properties" ->
"Directory ID" or with the Azure CLI using

::

   az account list

saving the ``tenantId`` field from the output. It will be referred to as
``$user_tenant_id`` later


11. create a peering connection from the Aiven Project VPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This leads to the Aiven platform creating a peering from the VNet in the
Aiven Project VPC to the VNet in your subscription. In addition it will
create a service principal for the application object in your tenant (
``--peer-azure-app-id $user_app_id`` ) giving it permission to target
the Aiven subscription VNet with a peering. Your AD tenant ID is also
needed in order for the Aiven application object to authenticate with
your tenant to give it access to the service principal created in step 7
( ``--peer-azure-tenant-id $user_tenant_id`` ).

| ``$aiven_project_vpc_id`` is the ID of the Aiven Project VPC, and can
  be found with ``avn vpc list``
| Using the Aiven CLI:

::

   avn vpc peering-connection create --project-vpc-id $aiven_project_vpc_id --peer-cloud-account $user_subscription_id --peer-resource-group $user_resource_group --peer-vpc $user_vnet_name --peer-azure-app-id $user_app_id --peer-azure-tenant-id $user_tenant_id

Note that the arguments starting with ``$user_`` should be given in
lower case. Azure resource names are case-agnostic, but the Aiven API
currently only accepts names in lower case. If no error is shown, the
peering connection is being set up by the Aiven platform.


12. wait for the Aiven platform to set up the connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command until the state is no longer ``APPROVED`` ,
but ``PENDING_PEER`` :

::

   avn vpc peering-connection get -v --project-vpc-id $aiven_project_vpc_id --peer-cloud-account $user_subscription_id --peer-resource-group $user_resource_group --peer-vpc $user_vnet_name

| A state such as ``INVALID_SPECIFICATION`` or ``REJECTED_BY_PEER`` may
  be shown if the VNet specified in the previous step did not exist, or
  the Aiven app object wasn't given permissions to peer with it. If that
  occurs, check your configuration and then recreate the peering
  connection in step 12
| If everything went as expected, the state changes to ``PENDING_PEER``
  within a couple of minutes showing details to set up the peering
  connection from your VNet to the Project VPC's VNet in the Aiven
  subscription.

Save the ``to-tenant-id`` field from the output. It will be referred to
as the ``aiven_tenant_id`` later. The ``to-network-id`` field from the
output is referred to as the ``$aiven_vnet_id``

13. create peering from your VNet to the VNet of the project VPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Log out the Azure user you logged in with in step 1 using

::

   az account clear

Log in the application object you created with in step 2 to your AD
tenant with

::

   az login --service-principal -u $user_app_id -p $user_app_secret --tenant $user_tenant_id

Log in the same application object to the Aiven AD tenant

::

   az login --service-principal -u $user_app_id -p $user_app_secret --tenant $aiven_tenant_id

Now that your application object has a session with both AD tenants,
create a peering from your VNet to the VNet in the Aiven subscription
with

::

   az network vnet peering create --name <peering name of your choosing> --remote-vnet $aiven_vnet_id --vnet-name $user_vnet_name --resource-group $user_resource_group --subscription $user_subscription_id --allow-vnet-access

Note that without ``--allow-vnet-access`` no traffic is allowed to flow
from the peered VNet and Aiven services cannot be reached through the
peering. After the peering has been created the peering should be in
state ``connected``

In case you get the error below, it's possible the role assignment from
step 6 hasn't taken effect yet. If that is the case, try logging in
again and creating the peering again after waiting a bit by repeating
the commands in this step. If the error message persists, please check
the role assignment in step 6 was correct.

::

   The client '<random uuid>' with object id '<another random uuid>' does not have authorization to perform action 'Microsoft.Network/virtualNetworks/virtualNetworkPeerings/write' over scope '$user_vnet_id' If access was recently granted, please refresh your credentials.


14. wait until the Aiven peering connection is active
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Aiven platform polls peering connections in state ``PENDING_PEER``
regularly to see if the peer (your subscription) has created a peering
connection to the Aiven Project VPC's VNet. Once this is detected, the
state changes from ``PENDING_PEER`` to ``ACTIVE`` . After this services
in the Project VPC can be reached through the peering. To check if the
peering connection is ``ACTIVE`` , run the same Aiven CLI
``avn vpc peering-connection get`` command from step 12. In some cases it has taken up to 15 minutes for the state to update:

::

   avn vpc peering-connection get -v --project-vpc-id $aiven_project_vpc_id --peer-cloud-account $user_subscription_id --peer-resource-group $user_resource_group --peer-vpc $user_vnet_name
