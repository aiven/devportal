Command reference: ``avn events``
==================================

Here you’ll find the full list of commands for ``avn events``.


List project events
-------------------

Commands for listing events related to a particular project.


``avn events``
'''''''''''''''''''''''

Lists instance or integration creation, deletion or modification events.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to fetch details for

**Example:** Show the details of the currently selected project.

::

  avn events


**Example:** Show the details of a named project.

::

  avn events --project my-project
