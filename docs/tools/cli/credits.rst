Command reference: ``avn credits``
==================================

Here you’ll find the full list of commands for ``avn credits``.


Manage Aiven credits
--------------------

Commands for managing Aiven credits.


``avn credits claim``
'''''''''''''''''''''''

Claims a new Aiven credit code.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``code``
    - Credit code to claim
  * - ``--project``
    - The project to claim the credits for

**Example:** Add a credit code to the currently selected project.

::

  avn credits claim "credit-code-123"


**Example:** Add a credit code to a named project.

::

  avn credits claim "credit-code-123"  --project my-project


``avn credits list``
'''''''''''''''''''''''

Lists credit codes associated with the Aiven project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to list the credits for


**Example:** List all credit codes associated with the currently selected Aiven project.

::

  avn credits list

**Example:** List all credit codes associated with a named Aiven project.

::

  avn credits list --project my-project
