``avn project``
==================================

Here you'll find the full list of commands for ``avn project``.


Work with project details
-------------------------

Commands for managing projects and using them with ``avn`` commands.


``avn project details``
'''''''''''''''''''''''

Fetches project details.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to fetch details for

**Example:** Show the details of the currently selected project.

::

  avn project details


**Example:** Show the details of a named project.

::

  avn project details --project my-project


``avn project switch``
''''''''''''''''''''''

Sets the default project to use with ``avn``.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to use when a project isn't specified for an ``avn`` command

**Example:** Change to use the project called ``my-project`` as default for all commands where the ``--project`` parameter isn't supplied.

::

  avn project switch --project my-project


``avn project list``
''''''''''''''''''''

Lists all the projects that you have access to.

**Example:** List all the projects available to use with a ``--project`` command switch.

::

  avn project list


``avn project create`` and ``avn project update``
'''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new project with ``create`` or changes the settings with ``update``.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project_name`` (required for ``create``)
    - Note: This is a positional argument, not a switch
  * - ``--project`` (required for ``update``)
    - The project to amend, use with ``update`` only
  * - ``--name`` (``update`` only)
    - Supply a new name for the project
  * - ``--account-id``
    - The account to create the project in
  * - ``--billing-group-id``
    - Billing group ID to use
  * - ``--card-id``
    - The card ID (see ``avn card``)
  * - ``--cloud``
    - The cloud to use by default (see ``avn cloud``)
  * - ``--no-fail-if-exists``
    - Makes the command safe to run repeatedly, it will succeed if a project of this name already exists.
  * - ``--copy-from-project`` (``create`` only)
    - Project name to use as a template
  * - ``--country-code``
    - `Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ for the billing country
  * - ``--billing-address``
    - Address to bill to
  * - ``--billing-extra-text``
    - Information to include with an invoice such as a cost center number
  * - ``--billing-currency``
    - The currency to bill in. The choices are: "AUD" "CAD" "CHF" "DKK" "EUR" "GBP" "NOK" "SEK" "USD"
  * - ``--vat-id``
    - VAT ID for this project
  * - ``--billing-email``
    - Email for the billing contact
  * - ``--tech-email``
    - Email for the technical contact

**Example:** Create a project named ``my-project``.

::

  avn project create my-project

**Example:** Create a project in a specific account using ``my-project`` as a template and set the email address for the technical contact.

::

  avn project create \
    --create-project-from my-project \
    --account-id abcdef0123456789 \
    --tech-email geek@example.com \
    my-other-project

**Example:** Rename a project.

::

  avn project update
    --project my-project
    --name my-better-named-project



``avn project delete``
''''''''''''''''''''''

Deletes an empty project. If the project isn't empty, it removes the services in it first.

.. Note::
    Aiven doesn't allow the deletion of non-empty projects as safeguard against accidental code execution.

**Example:** Delete ``my-project``.

::

  avn project delete my-project


Manage project certificates
------------------------------

CA certificates are managed at the project level.

``avn project ca-get``
''''''''''''''''''''''

Downloads the CA certificate for this project, the certificate is saved in the file name you supply.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to fetch details for
  * - ``--target-filepath``
    - File name, including path, to use

**Example:** Download the CA certificate for the current project, and save it in a file in the current directory called ``ca.pem``.

::

  avn project ca-get --target-filepath ca.pem


Manage users and invitations
----------------------------

Manage user access to the project.

``avn project invite-list``
'''''''''''''''''''''''''''

Lists the open invitations to the project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to show invitations for

**Example:** List the invitations for the current project.

::

  avn project invite-list


``avn project user-list``
'''''''''''''''''''''''''

Lists the users with access to the project

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to show users for


**Example:** List the users with access to project ``my-project``.

::

  avn project user-list --project my-project

``avn project user-invite``
'''''''''''''''''''''''''''

Sends an invitation to a user (by email) to join a project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``email`` (required)
    - Note: this is a positional argument
  * - ``--project``
    - The project to invite the user to
  * - ``--role``
    - Can be "operator", "developer" or "admin"

**Example:** Invite an important person to be an admin on the currently-selected project.

::

  avn project user-invite --role admin boss@example.com


``avn project user-remove``
'''''''''''''''''''''''''''

Removes a user with the supplied email address from the project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``email`` (required)
    - Note: This is a positional argument
  * - ``--project``
    - The project to remove the user from

**Example:** Remove the user with email ``alice@example.com`` from project ``my-project``.

::

  avn project user-remove --project my-project alice@example.com
