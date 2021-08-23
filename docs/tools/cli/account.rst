Command reference: ``avn account``
==================================

Here you’ll find the full list of commands for ``avn account``.


Manage account details
-------------------------

Commands for managing Aiven accounts via ``avn`` commands.


``avn account authentication-method``
'''''''''''''''''''''''''''''''''''''

:doc:`See detailed command information <account/account-authentication-method>`


``avn account create``
'''''''''''''''''''''''

Creates a new account.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--name``
    - The name of the account

**Example:** Create a new account for the  ``billing-analytics`` department.

::

  avn account create --name "Billing Analytics"

``avn account delete``
'''''''''''''''''''''''

Deletes an existing account.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account

**Example:** Delete the account with id ``123456789123``.

::

  avn account delete 123456789123

``avn account list``
'''''''''''''''''''''''

Lists existing accounts information including account id, name, team owner id, created time, tenant id and update time.

**Example:** List existing accounts.

::

  avn account list

An example of account list output:

.. code:: text

    ACCOUNT_ID    ACCOUNT_NAME            ACCOUNT_OWNER_TEAM_ID  CREATE_TIME           IS_ACCOUNT_OWNER  PRIMARY_BILLING_GROUP_ID  TENANT_ID     UPDATE_TIME
    ============  ======================  =====================  ====================  ================  ========================  ============  ====================
    123456789123  Billing Analytics       45678910111213         2020-09-09T20:28:44Z  true              null                      my_tenant_id  2020-09-09T20:28:44Z

``avn account team``
'''''''''''''''''''''''

:doc:`See detailed command information <account/account-team>`

``avn account update``
'''''''''''''''''''''''

Updates an existing account's name.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--name``
    - The account new name

**Example:** Update the name of account with id ``123456789123`` to ``Billing Analytics Account``.

::

  avn account update 123456789123 --name "Billing Analytics Account"
