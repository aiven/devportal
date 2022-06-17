``avn vpc``
===========

Here you'll find the full list of commands for ``avn vpc``.


Work with project's VPCs
-------------------------

Commands for managing project's VPCs and using them with ``avn`` commands.


``avn vpc create``
''''''''''''''''''

Creates a new VPC.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to fetch details for
  * - ``--cloud``
    - The cloud to use by default (see ``avn cloud``)
  * - ``--network-cidr``
    - The network range in the Aiven project VPC in CIDR format (required)

**Example:** Create a new VPC in ``aws-us-west-1`` cloud region.

::

  avn vpc create --cloud aws-us-west-1 --network-cidr 10.1.2.0/24

.. code:: text

    PROJECT_VPC_ID                        STATE     CLOUD_NAME     NETWORK_CIDR
    ====================================  ========  =============  ============
    1548c3f6-6240-45ab-892f-2dfacc62ed0d  APPROVED  aws-us-west-1  10.1.2.0/24

``avn vpc delete``
''''''''''''''''''

Deletes an existing VPC.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--project-vpc-id``
    - The project VPC ID. See ``avn vpc list`` (required)

**Example:** Delete the VPC with id ``1548c3f6-6240-45ab-892f-2dfacc62ed0d``.

::

  avn vpc delete --project-vpc-id 1548c3f6-6240-45ab-892f-2dfacc62ed0d

.. code:: text

    PROJECT_VPC_ID                        STATE     CLOUD_NAME     NETWORK_CIDR
    ====================================  ========  =============  ============
    1548c3f6-6240-45ab-892f-2dfacc62ed0d  DELETING  aws-us-west-1  10.1.2.0/24

``avn vpc list``
''''''''''''''''

Lists all the project's VPCs.

**Example:** List all project's VPCs.

::

  avn vpc list

.. code:: text

    PROJECT_VPC_ID                        CLOUD_NAME          NETWORK_CIDR   STATE 
    ====================================  ==================  =============  ======
    b132dfbf-b035-4cf5-8b15-b7cd6a68aabd  aws-us-east-1       10.2.1.0/24    ACTIVE
    c36a0a6a-6cfb-4718-93ce-ec043ae940d5  aws-us-west-2       10.13.4.0/24   ACTIVE
    d7a984bf-6ebf-4503-bbbd-e7950c49bc5b  azure-eastus        10.213.2.0/24  ACTIVE
    f99601f3-4b00-44d6-b4d9-6f16e9f55c18  google-us-central1  10.1.13.0/24   ACTIVE
    8af49368-3125-48a8-b94e-3d1a3d601d7f  google-us-east1     10.50.8.0/24   ACTIVE
    6ba650ce-cc08-4e0a-a386-5a354c327cb6  google-us-east4     10.1.17.0/24   ACTIVE
    c4bc3a59-87da-4dce-9243-c197edb430e2  google-us-west3     10.1.13.0/24   ACTIVE


Manage VPC peering connections
------------------------------


``avn vpc peering-connection create``
'''''''''''''''''''''''''''''''''''''

Creates a peering connection for a project VPC.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--project-vpc-id PROJECT_VPC_ID``
    - Aiven project VPC ID. See ``avn vpc list`` (required)
  * - ``--peer-cloud-account PEER_CLOUD_ACCOUNT``
    - AWS account ID, Google project ID, or Azure subscription ID (required)
  * - ``--peer-vpc PEER_VPC``
    - AWS VPC ID, Google VPC network name, or Azure VNet name (required)
  * - ``--peer-region PEER_REGION``
    - AWS region of peer VPC, if other than the region of the Aiven project VPC
  * - ``--peer-resource-group PEER_RESOURCE_GROUP``
    - Azure resource group name (required for Azure)
  * - ``--peer-azure-app-id PEER_AZURE_APP_ID``
    - Azure app object ID (required for Azure)
  * - ``--peer-azure-tenant-id PEER_AZURE_TENANT_ID``
    - Azure AD tenant ID (required for Azure)
  * - ``--user-peer-network-cidr USER_PEER_NETWORK_CIDRS``
    - User-defined peer network IP range for routing/firewall

**Example:** Create a peering connection for AWS.

::

  avn vpc peering-connection create \
    --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aabd \
    --peer-cloud-account 012345678901 \
    --peer-vpc vpc-abcdef01234567890

.. code:: text

    CREATE_TIME           PEER_AZURE_APP_ID  PEER_AZURE_TENANT_ID  PEER_CLOUD_ACCOUNT  PEER_RESOURCE_GROUP  PEER_VPC               STATE     STATE_INFO  UPDATE_TIME           USER_PEER_NETWORK_CIDRS  VPC_PEERING_CONNECTION_TYPE
    ====================  =================  ====================  ==================  ===================  =====================  ========  ==========  ====================  =======================  ===========================
    2022-06-15T14:50:54Z  null               null                  012345678901        null                 vpc-abcdef01234567890  APPROVED  null        2022-06-15T14:50:54Z      


``avn vpc peering-connection delete``
'''''''''''''''''''''''''''''''''''''

Deletes a VPC peering connection.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--project-vpc-id PROJECT_VPC_ID``
    - Aiven project VPC ID. See ``avn vpc list`` (required)
  * - ``--peer-cloud-account PEER_CLOUD_ACCOUNT``
    - AWS account ID, Google project ID, or Azure subscription ID (required)
  * - ``--peer-vpc PEER_VPC``
    - AWS VPC ID, Google VPC network name, or Azure VNet name (required)
  * - ``--peer-region PEER_REGION``
    - AWS region of peer VPC, if other than the region of the Aiven project VPC
  * - ``--peer-resource-group PEER_RESOURCE_GROUP``
    - Azure resource group name (required for Azure)

**Example:** Delete the VPC peering connection between the ``b032dfbf-b035-4cf5-8b15-b7cd6a68aabd`` Aiven VPC and the ``vpc-abcdef01234567890`` AWS VPC.

::

  avn vpc peering-connection delete \
    --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aabd \
    --peer-cloud-account 012345678901 \
    --peer-vpc vpc-abcdef01234567890

.. code:: text

    CREATE_TIME           PEER_AZURE_APP_ID  PEER_AZURE_TENANT_ID  PEER_CLOUD_ACCOUNT  PEER_REGION  PEER_RESOURCE_GROUP  PEER_VPC               STATE     STATE_INFO  UPDATE_TIME           USER_PEER_NETWORK_CIDRS  VPC_PEERING_CONNECTION_TYPE
    ====================  =================  ====================  ==================  ===========  ===================  =====================  ========  ==========  ====================  =======================  ===========================
    2022-06-15T14:50:54Z  null               null                  012345678901        us-east-1    null                 vpc-abcdef01234567890  DELETING  null        2022-06-15T15:02:12Z  


``avn vpc peering-connection get``
''''''''''''''''''''''''''''''''''

Fetches a VPC peering connection details.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--project-vpc-id PROJECT_VPC_ID``
    - Aiven project VPC ID. See ``avn vpc list`` (required)
  * - ``--peer-cloud-account PEER_CLOUD_ACCOUNT``
    - AWS account ID, Google project ID, or Azure subscription ID (required)
  * - ``--peer-vpc PEER_VPC``
    - AWS VPC ID, Google VPC network name, or Azure VNet name (required)

**Example:** Fetch VPC peering connection details.

::

  avn vpc peering-connection get \
    --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aabd \
    --peer-cloud-account 012345678901 \
    --peer-vpc vpc-abcdef01234567890

.. code:: text

    State: ACTIVE
    Message: Peering connection active

    AWS_VPC_PEERING_CONNECTION_ID  TYPE                             
    =============================  =================================
    pcx-abcdef01234567890          aws-vpc-peering-connection-active 


``avn vpc peering-connection list``
'''''''''''''''''''''''''''''''''''

Lists VPC peering connections.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--project-vpc-id PROJECT_VPC_ID``
    - Aiven project VPC ID. See ``avn vpc list`` (required)

**Example:** List VPC peering connections for the ``b032dfbf-b035-4cf5-8b15-b7cd6a68aabd`` VPC.

::

  avn vpc peering-connection list --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aabd

.. code:: text

    PEER_CLOUD_ACCOUNT  PEER_RESOURCE_GROUP  PEER_VPC               PEER_REGION  STATE 
    ==================  ===================  =====================  ===========  ======
    012345678901        null                 vpc-abcdef01234567890  us-east-1    ACTIVE
