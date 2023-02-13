``avn card``
===============================

This article has the full list of commands for managing credit card details using ``avn account``. 

``avn card add``
''''''''''''''''

Adds a new credit card.

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

**Example:** Add a credit card:

.. code:: shell

  avn card add --cvc 123         \
    --exp-month 01               \
    --exp-year 2031              \
    --name "Name Surname"        \
    --number 4111111111111111

``avn card list``
'''''''''''''''''

Lists all credit cards.


**Example:** List credit cards:

.. code:: shell

  avn card list


``avn card remove``
'''''''''''''''''''

Removes a credit card.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``card-id``
    - The ID shown for this card in the ``list`` command output


**Example:** Remove a credit card:

.. code:: shell

  avn card remove AAAAAAAA-BBBB-CCCC-DDDD-0123456789AB

``avn card update``
'''''''''''''''''''

Updates a credit card.

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
      - Card expiration year (YYYY)
    * - ``--name``
      - Name on the credit card


**Example:** Update a credit card:

.. code:: shell

    avn card update AAAAAAAA-BBBB-CCCC-DDDD-0123456789AB \
        --exp-month 01                                   \
        --exp-year 2031                                  \
        --name "Name Surname"
