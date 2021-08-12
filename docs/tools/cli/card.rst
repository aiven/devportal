Command reference: ``avn card``
===============================

Here you’ll find the full list of commands for ``avn card``.


Manage credit cards
-------------------

Commands for managing credit card details associated to Aiven projects.


``avn card add``
''''''''''''''''

Adds a new credit card to the Aiven account.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--cvc``
    - Credit card security code
  * - ``--exp-month``
    - Card expiration month (1-12)
  * - ``--exp-year``
    - Card expiration year
  * - ``--name``
    - Name on the credit card
  * - ``--number``
    - Credit card number
  * - ``--update-project``
    - Assign card to a project

**Example:** Add a credit card to a named project.

::

  avn card add --cvc 123         \
    --exp-month 01               \
    --exp-year 2031              \
    --name "Name Surname"        \
    --number 4111111111111111    \
    --update-project my-project


``avn card list``
'''''''''''''''''

Lists credit cards associated with this account.


**Example:** List all credit cards associated with this account.

::

  avn card list


``avn card remove``
'''''''''''''''''''

Removes a credit card associated with the Aiven account.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``card-id``
    - The ID shown for this card in the ``list`` command output


**Example:** Remove a credit card associated with the Aiven account.

::

  avn card remove AAAAAAAA-BBBB-CCCC-DDDD-0123456789AB

``avn card update``
'''''''''''''''''''

Updates a credit card associated with the account.

.. list-table::
    :header-rows: 1
    :align: left

    * - Parameter
      - Information
    * - ``card-id``
      - The ID shown for this card in the ``list`` command output
    * - ``--exp-month``
      - Card expiration month (1-12)
    * - ``--exp-year``
      - Card expiration year
    * - ``--name``
      - Name on the credit card


**Example:** Update a credit card associated with the Aiven account.

::

    avn card update AAAAAAAA-BBBB-CCCC-DDDD-0123456789AB \
        --exp-month 01                                   \
        --exp-year 2031                                  \
        --name "Name Surname"
