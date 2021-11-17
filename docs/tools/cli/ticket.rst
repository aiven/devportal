Command reference: ``avn ticket``
==================================

Here you'll find the full list of commands for ``avn ticker``.


Create and manage support tickets
------------------------------------

Commands for managing Aiven support tickets.

``avn ticket create``
'''''''''''''''''''''''''

Creates a new ticket.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project for which to create a ticket
  * - ``--service``
    - The service name for which to create a ticket
  * - ``--severity``
    - The ticket severity; possible values are ``low``,``high``,``critical``, more information about severity and support levels are available in `the dedicated page <https://aiven.io/support-services>`_.
  * - ``--title``
    - Short description of the issue
  * - ``--description``
    - Detailed description of the issue


**Example:** Create a new ticket with severity ``low`` for the service ``pg-demo`` in the project ``proj-test``.

::

  avn ticket create --service pg-demo               \
      --project proj-test                           \
      --severity low                                \
      --title "Error during enabling XYZ extension" \
      --description "When enabling XYZ extension I get the error ERROR123: ZZZ"

``avn ticket list``
''''''''''''''''''''''

Retrieves the list of support tickets together with the associated details like ticket ID, status, create and update time.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project for which to create a ticket
  * - ``--state``
    - The ticket state; possible values are ``closed`` or ``open``


**Example:** Retrieve all the tickets in ``open`` state for the ``proj-test`` project

::

  avn ticket list         \
      --project proj-test \
      --state open

An example of ``avn ticket list`` output:

.. code:: text

    TICKET_ID  SEVERITY  STATE  TITLE                                 PROJECT_NAME   SERVICE_NAME           CREATE_TIME           DESCRIPTION                                         UPDATE_TIME           USER_EMAIL         USER_REAL_NAME
    =========  ========  =====  ====================================  =============  ============  ====================  ============================================================ ====================  =================  ==============
    T-4EXXX    high      open   Error during enabling XYZ extension   proj-test      pg-demo       2021-11-01T07:59:52Z  "When enabling XYZ extension I get the error ERROR123: ZZZ"  2021-11-03T22:30:28Z  joe@example.com    Joe Doe
    T-4EXX1    critical  open   Error during service create           proj-test      kafka-tst     2021-11-04T18:14:16Z  "Create service shows ERROR 123"                             2021-11-05T22:10:30Z  maria@example.com  Maria Test
    T-4EXX2    low       open   Billing problem                       proj-test      redis-prod    2021-11-05T10:29:26Z  "Bills are sent twice"                                       2021-11-05T22:10:24Z  carl@example.com   Carl White