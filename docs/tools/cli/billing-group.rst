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

**Example:** Add the project ``new-project`` to the existing billing group with id ``55b0e547-58f9-48de-8808-807d385d1f95``

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
  * - ``--account-id``
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

**Example:** Create a billing-group named ``qa-dept`` under the account with ID ``c59dde4j9`` with the following properties:

* currency: ``EUR``
* e-mail address: ``billing@testers.dev``
* company name: ``testers``
* address: ``1 No Way``
* country code: ``SE``
* city: ``Stockholm``

::

  avn billing-group create qa-dept        \
    --account-id c59dde4j9                \
    --billing-currency EUR                \
    --billing-email billing@testers.dev   \
    --company testers                     \
    --address-line "1 No Way"             \
    --country-code SE                     \
    --city Stockholm

**Example:** Rename your ``qa-dept`` billing group with ID ``55b0e547-58f9-48de-8808-807d385d1f95`` to ``qa-department``.

::

  avn billing-group update               \
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

**Example:** Claim the credit code ``sneaky-crab`` in the billing-group having ID ``55b0e547-58f9-48de-8808-807d385d1f95``

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

**Example:** List credits claimed in the billing-group with ID ``55b0e547-58f9-48de-8808-807d385d1f95``

::

  avn billing-group credits-list 55b0e547-58f9-48de-8808-807d385d1f95

An example of ``avn billing-group credits-list`` output:

.. code:: text

  CODE      REMAINING_VALUE
  ========  ===============
  S18A11Y  0.00


``avn billing-group delete``
''''''''''''''''''''''''''''''''''''

Deletes a billing-group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** Delete your billing-group with id ``55b0e547-58f9-48de-8808-807d385d1f95``

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

**Example:** List events in the billing-group with ID ``55b0e547-58f9-48de-8808-807d385d1f95``

::

  avn billing-group events 55b0e547-58f9-48de-8808-807d385d1f95

An example of ``avn billing-group events`` output:

.. code:: text

  CREATE_TIME           ACTOR             EVENT_DESC
  ====================  ================  ===================================================================================================================
  2021-10-14T21:09:02Z  Aiven Automation  Set VAT ID state to invalid
  2021-10-14T14:31:15Z  me@you.com        "Set billing email address to \"[\"\"me@you.io\"\"]\""
  2021-10-14T14:30:46Z  me@you.com        Set VAT ID state to unconfirmed
  2021-10-14T13:08:45Z  Aiven Automation  Set VAT ID state to invalid
  2021-10-14T08:15:09Z  me@you.com        "Added US$\"400\" credits to the billing group"
  2021-10-14T08:15:00Z  me@you.com        Added project inzone-a-project to billing group
  2021-10-14T08:15:00Z  me@you.com        Added project inzone-b-project to billing group
  2021-10-14T08:15:00Z  me@you.com        Added project inzone-c-project to billing group
  2021-10-14T08:15:00Z  me@you.com        Added project kona-a-project to billing group
  2021-10-14T08:15:00Z  me@you.com        Added project kona-b-project to billing group
  2021-10-14T08:15:00Z  me@you.com        Added project kona-c-project to billing group
  2021-10-14T08:15:00Z  me@you.com        "Added user u2865a92fe3d (\"me@you.com\") to billing group \"u856238c-8213-6592-975e-cfc3662c1084\" with type"
  2021-10-14T08:15:00Z  me@you.com        "Created billing group \"test-group\""


``avn billing-group get``
''''''''''''''''''''''''''

Gets the details for a given billing-group

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``id``
    - The ID of your billing group

**Example:** Get details for the billing-group with ID ``55b0e547-58f9-48de-8808-807d385d1f95``

::

  avn billing-group get 55b0e547-58f9-48de-8808-807d385d1f95

An example of ``avn billing-group get`` output:

.. code:: text

  BILLING_GROUP_ID                      BILLING_GROUP_NAME  ACCOUNT_NAME
  ====================================  ==================  ============
  u856238c-8213-6592-975e-cfc3662c1084  test-group        null


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

**Example:** Retrieve lines from the invoice ``94885-2`` for the billing group with id ``55b0e547-58f9-48de-8808-807d385d1f95``

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

**Example:** List invoices for billing-group with ID ``55b0e547-58f9-48de-8808-807d385d1f95``

::

  avn billing-group invoice-list 55b0e547-58f9-48de-8808-807d385d1f95

An example of ``avn billing-group invoice-list`` output:

.. code:: text

  
  INVOICE_NUMBER  PERIOD_BEGIN          PERIOD_END            STATE     TOTAL_INC_VAT  TOTAL_VAT_ZERO
  ==============  ====================  ====================  ========  =============  ==============
  xxxxx-88        2022-09-01T00:00:00Z  2022-09-30T23:59:59Z  estimate  0.00           0.00

``avn billing-group list``
'''''''''''''''''''''''''''

Lists all of your billing-groups

**Example:** List all of your billing-groups

::

  avn billing-group list

An example of ``avn billing-group list`` output:

.. code:: text

  BILLING_GROUP_ID                      BILLING_GROUP_NAME                               ACCOUNT_NAME
  ====================================  ===============================================  ======================
  2a4981e1-f988-4cb8-b1a8-xxxxxxxxxxxx  Default billing group for abcdddddd              Account 123
  3c575695-4384-4b34-b58c-yyyyyyyyyyyy  Default billing group for project test-demo      Account 223
  51ad078a-4eef-468d-964b-zzzzzzzzzzzz  Default billing group for xxxxxxxxxxx            Account 123
