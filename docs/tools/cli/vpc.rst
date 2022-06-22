``avn vpc``
===========

Here you'll find the full list of commands for ``avn vpc``.


Manage project's VPC
--------------------

Commands for managing project's VPCs (Virtual Private Cloud) and using them with ``avn`` commands.


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
    - The cloud to use by default, to review the list of available cloud regions, check the ``avn cloud list`` :ref:`command <avn-cloud-list>`
  * - ``--network-cidr``
    - The network range in the Aiven project VPC in CIDR format (a.b.c.d/e) (required)

**Example:** Create a new VPC in ``aws-us-west-1`` cloud region with network range ``10.1.2.0/24``

::

  avn vpc create              \
    --cloud aws-us-west-1     \
    --network-cidr 10.1.2.0/24

The command output is:

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
    - The project VPC ID. To get the list of VPC IDs execute ``avn vpc list`` (required)

**Example:** Delete the VPC with id ``1548c3f6-6240-45ab-892f-2dfacc62ed0d``.

::

  avn vpc delete \
  --project-vpc-id 1548c3f6-6240-45ab-892f-2dfacc62ed0d

The command output is:

.. code:: text

    PROJECT_VPC_ID                        STATE     CLOUD_NAME     NETWORK_CIDR
    ====================================  ========  =============  ============
    1548c3f6-6240-45ab-892f-2dfacc62ed0d  DELETING  aws-us-west-1  10.1.2.0/24

``avn vpc list``
''''''''''''''''

Lists all the project's VPCs.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--json``
    - Retrieve the output in JSON format
  * - ``--verbose``
    - Retrieve the verbose output

**Example:** List all project's VPCs.

::

  avn vpc list

The command output is:

.. code:: text

    PROJECT_VPC_ID                        CLOUD_NAME          NETWORK_CIDR   STATE 
    ====================================  ==================  =============  ======
    b132dfbf-b035-4cf5-8b15-b7cd6a68aqqd  aws-us-east-1       10.2.1.0/24    ACTIVE
    c36a0a6a-6cfb-4718-93ce-ec043ae94qq5  aws-us-west-2       10.13.4.0/24   ACTIVE
    d7a984bf-6ebf-4503-bbbd-e7950c49bqqb  azure-eastus        10.213.2.0/24  ACTIVE
    f99601f3-4b00-44d6-b4d9-6f16e9f55qq8  google-us-central1  10.1.13.0/24   ACTIVE
    8af49368-3125-48a8-b94e-3d1a3d601qqf  google-us-east1     10.50.8.0/24   ACTIVE
    6ba650ce-cc08-4e0a-a386-5a354c327qq6  google-us-east4     10.1.17.0/24   ACTIVE
    c4bc3a59-87da-4dce-9243-c197edb43qq2  google-us-west3     10.1.13.0/24   ACTIVE


Manage VPC peering connections
------------------------------


``avn vpc peering-connection create``
'''''''''''''''''''''''''''''''''''''

Creates a peering connection for a project VPC to AWS, GCP or Azure.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command
  * - ``--project-vpc-id``
    - Aiven project VPC ID. To get the list of VPC IDs execute ``avn vpc list`` (required)
  * - ``--peer-cloud-account``
    - AWS account ID, Google project ID, or Azure subscription ID (required)
  * - ``--peer-vpc``
    - AWS VPC ID, Google VPC network name, or Azure VNet name (required)
  * - ``--peer-region``
    - AWS region of peer VPC, if different than the region defined in the Aiven project VPC
  * - ``--peer-resource-group``
    - Azure resource group name (required for Azure)
  * - ``--peer-azure-app-id``
    - Azure app object ID (required for Azure)
  * - ``--peer-azure-tenant-id``
    - Azure AD tenant ID (required for Azure)
  * - ``--user-peer-network-cidr``
    - User-defined peer network IP range for routing/firewall

**Example:** Create a peering connection for AWS.

::

  avn vpc peering-connection create \
    --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aqqd \
    --peer-cloud-account 012345678901 \
    --peer-vpc vpc-abcdef01234567890

The command output is:

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
  * - ``--project-vpc-id``
    - Aiven project VPC ID. To get the list of VPC IDs execute ``avn vpc list`` (required)
  * - ``--peer-cloud-account``
    - AWS account ID, Google project ID, or Azure subscription ID (required)
  * - ``--peer-vpc``
    - AWS VPC ID, Google VPC network name, or Azure VNet name (required)
  * - ``--peer-region``
    - AWS region of peer VPC, if different than the region defined in the Aiven project VPC
  * - ``--peer-resource-group``
    - Azure resource group name (required for Azure)

**Example:** Delete the VPC peering connection between the ``b032dfbf-b035-4cf5-8b15-b7cd6a68aqqd`` Aiven VPC and the ``vpc-abcdef01234567890`` AWS VPC.

::

  avn vpc peering-connection delete \
    --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aqqd \
    --peer-cloud-account 012345678901 \
    --peer-vpc vpc-abcdef01234567890

The command output is:

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
  * - ``--project-vpc-id``
    - Aiven project VPC ID. To get the list of VPC IDs execute ``avn vpc list`` (required)
  * - ``--peer-cloud-account``
    - AWS account ID, Google project ID, or Azure subscription ID (required)
  * - ``--peer-vpc``
    - AWS VPC ID, Google VPC network name, or Azure VNet name (required)
  * - ``--json``
    - Retrieve the output in JSON format
  * - ``--verbose``
    - Retrieve the verbose output

**Example:** Fetch VPC peering connection details.

::

  avn vpc peering-connection get \
    --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aabd \
    --peer-cloud-account 012345678901 \
    --peer-vpc vpc-abcdef01234567890

The command output is:

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
  * - ``--project-vpc-id``
    - Aiven project VPC ID. To get the list of VPC IDs execute ``avn vpc list`` (required)

**Example:** List VPC peering connections for the VPC with id ``b032dfbf-b035-4cf5-8b15-b7cd6a68aabd``.

::

  avn vpc peering-connection list --project-vpc-id b032dfbf-b035-4cf5-8b15-b7cd6a68aabd

The command output is:

.. code:: text

    PEER_CLOUD_ACCOUNT  PEER_RESOURCE_GROUP  PEER_VPC               PEER_REGION  STATE 
    ==================  ===================  =====================  ===========  ======
    012345678901        null                 vpc-abcdef01234567890  us-east-1    ACTIVE
