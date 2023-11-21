``avn account``
================

This article has the full list of commands for managing organization or organizational unit details using ``avn account``. An account is the same as an :doc:`organization or organizational unit </docs/platform/concepts/projects_accounts_access>`.

Check out the full description of :doc:`Aiven's security model </docs/platform/concepts/cloud-security>` for more information.

``avn account authentication-method``
'''''''''''''''''''''''''''''''''''''

A full list of commands is available in a :doc:`separate article for managing authentication methods in the CLI <account/account-authentication-method>`.

``avn account create``
'''''''''''''''''''''''

Creates a new organization or organizational unit.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--name``
    - The name of the organization or unit
  * - ``--parent-account-id``
    - The ID of the organization

To create a new organizational unit, specify the parent organization using ``--parent-account-id``.

**Example:** Create an organizational unit for production in an organization with the ID ``123456789123``. 

.. code::

  avn account create --name "Production" --parent-account-id 123456789123

**Example:** Create a new organization for the billing analytics department.

.. code::

  avn account create --name "Billing Analytics"


``avn account delete``
'''''''''''''''''''''''

Deletes an organization or organizational unit.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the organization or unit

**Example:** Delete the organization with id ``123456789123``.

.. code::

  avn account delete 123456789123


``avn account list``
'''''''''''''''''''''

Lists the details of organizations and organizational units including ID (account ID), name, team owner ID, created time, tenant ID, and time last updated.

An example of the output:

.. code:: text

    ACCOUNT_ID    ACCOUNT_NAME            ACCOUNT_OWNER_TEAM_ID  CREATE_TIME           IS_ACCOUNT_OWNER  PRIMARY_BILLING_GROUP_ID  TENANT_ID     UPDATE_TIME
    ============  ======================  =====================  ====================  ================  ========================  ============  ====================
    123456789123  Billing Analytics       45678910111213         2020-09-09T20:28:44Z  true              null                      my_tenant_id  2020-09-09T20:28:44Z


``avn account team``
'''''''''''''''''''''''

A full list of commands is available in a :doc:`separate article for managing teams in the CLI <account/account-team>`.


``avn account update``
'''''''''''''''''''''''

Changes the name of an organization or organizational unit.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The ID of the organization or unit
  * - ``--name``
    - The new name

**Example:** Change the name of organizational unit with the ID ``123456789123`` to ``Billing Analytics Account``.

.. code::

  avn account update 123456789123 --name "Billing Analytics Account"