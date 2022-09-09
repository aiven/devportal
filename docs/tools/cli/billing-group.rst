``avn billing-group``
==================================

Here you'll find the full list of commands for ``avn billing-group``.


Work with billing groups
-------------------------

Commands for managing billing groups and using them with ``avn`` commands.


``avn billing-group assign-projects``
'''''''''''''''''''''''''''''''''''''

Adds the given projects to the given billing group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group
  * - ``projects``
    - Name(s) of projects to assign (separated by spaces)

**Example:** Add your new project to an existing billing group

::

  avn biling-group assign-projects 55b0e547-58f9-48de-8808-807d385d1f95 new-project


``avn billing-group create`` and ``avn billing-group update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new billing group with ``create`` or amend it with ``update``

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``name`` (required for ``create``)
    - Note: This is a positional argument, not a switch
  * - ``ID`` (required for ``update``)
    - Note: This is a positional argument, not a switch
  * - ``--account-id`` (required for ``update``)
    - The account ID to create the billing group in
  * - ``--card-id``
    - The card ID (see ``avn card``)
  * - ``--vat-id``
    - VAT ID for this billing group
  * - ``--billing-currency``
    - The currency to bill in. The choices are: "AUD" "CAD" "CHF" "DKK" "EUR" "GBP" "NOK" "SEK" "USD"
  * - ``--billing-extra-text``
    - Information to include with an invoice such as a cost center number
  * - ``--billing-email``
    - Email for the billing contact
  * - ``--company``
    - Company name
  * - ``--address-line``
    - First line of address
  * - ``--country-code``
    - `Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ for the billing country
  * - ``--city``
    - City
  * - ``--state``
    - State / Province
  * - ``--zip-code``
    - ZIP / Post Code

**Example:** Create a billing-group named ``qa-dept``.

::

  avn billing-group create qa-dept --account-t c59dde4j9 --billing-currency EUR --billing-email billing@testers.dev --company testers --address-line "1 No Way" --country-code SE --city Stockholm

**Example:** Rename a billing-group 

::

  avn billing-group update \
    55b0e547-58f9-48de-8808-807d385d1f95 \
    --name qa-department 

``avn billing-group credits-claim``
''''''''''''''''''''''''''''''''''''

Claim a credit code within your biling-group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group
  * - ``code``
    - Credit Code

**Example:** Claim a credit code in your billing-group

::

  avn billing-group credits-claim 55b0e547-58f9-48de-8808-807d385d1f95 sneaky-crab

``avn billing-group credits-list``
''''''''''''''''''''''''''''''''''''

Lists all the credits redeemed in your billing-group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** List credits claimed in your billing-group

::

  avn billing-group credits-list 55b0e547-58f9-48de-8808-807d385d1f95

``avn billing-group delete``
''''''''''''''''''''''''''''''''''''

Lists all the credits redeemed in your billing-group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** Delete your billing-group

::

  avn billing-group delete 55b0e547-58f9-48de-8808-807d385d1f95

``avn billing-group events``
'''''''''''''''''''''''''''''

List the events that have occurred for a given billing-group 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** List events in your billing-group

::

  avn billing-group events 55b0e547-58f9-48de-8808-807d385d1f95

``avn billing-group get``
''''''''''''''''''''''''''

Get details for a given billing-group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** Get details for your billing-group

::

  avn billing-group get 55b0e547-58f9-48de-8808-807d385d1f95

``avn billing-group invoice-lines``
''''''''''''''''''''''''''''''''''''

Retrieve the lines for a given invoice

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group
  * -  ``invoice```
    - The number of the invoice

**Example:** Retrieve lines from invoice for your billing group

::

  avn billing-group invoice-lines 55b0e547-58f9-48de-8808-807d385d1f95 94885-2

``avn billing-group invoice-list``
''''''''''''''''''''''''''''''''''''

List all invoices for a given billing group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** List invoices for your billing-group

::

  avn billing-group invoice-list 55b0e547-58f9-48de-8808-807d385d1f95

``avn billing-group list``
'''''''''''''''''''''''''''

List all of your billing-groups

**Example:** List all of your billing-groups

::

  avn billing-group list