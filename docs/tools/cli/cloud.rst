``avn cloud``
==================================

Here you’ll find the full list of commands for ``avn cloud``.


List cloud region details
-------------------------

Commands for listing cloud regions to be used when creating or moving instances with ``avn`` commands.

.. _avn-cloud-list:

``avn cloud list``
'''''''''''''''''''''''

Lists cloud regions with related geographical region, latitude and longitude.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to fetch details for

**Example:** Show the clouds available to the currently selected project.

::

  avn cloud list


**Example:** Show the clouds available to a named project.

::

  avn cloud list --project my-project


Reference list of clouds
------------------------

A quick reference list of the default available clouds, but bear in mind that this may differ between projects.


.. include:: /includes/clouds-list.rst

