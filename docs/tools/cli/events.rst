``avn events``
==================================

The ``avn events`` command is an audit log of things that have happened in a particular project, including:

- timestamp of when the event occurred
- which user performed the action (email address of the user, or "Aiven Automation" where it was an automatic change)
- the type of event, such as ``service_create``, ``project_vpc_create`` or ``service_master_promotion`` (this is not an exhaustive list and new event types are added from time to time
- the name of the service affected
- a more detailed description of the event

An example of events output (note that the newest event is shown first):

.. code:: text

    TIME                  ACTOR                    EVENT_TYPE                SERVICE_NAME    EVENT_DESC                                                                                    
    ====================  =======================  ========================  ==============  ==============================================================================================

    2021-08-10T13:38:23Z  my_user@aiven.io         service_update            demo-pg         Reset service user password
    2021-08-10T13:38:22Z  my_user@aiven.io         service_update            demo-kafka      Reset service user password
    2021-08-10T13:37:21Z  Aiven Automation         service_master_promotion  demo-pg         Promoted demo-pg-1 to be the new master in service demo-pg.
    2021-08-10T13:35:39Z  my_user@aiven.io         service_create            demo-pg         Created 'pg' service 'demo-pg' with plan 'business-4' in cloud 'google-europe-west3'
    2021-08-10T13:35:22Z  my_user@aiven.io         service_create            demo-kafka      Created 'kafka' service 'demo-kafka' with plan 'business-4' in cloud 'google-europe-west3'



Project events
--------------

Information about the events that have occurred in a project.


``avn events``
''''''''''''''

Lists instance or integration creation, deletion or modification events.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--project``
    - The project to fetch details for

**Example:** Show the recent events of the currently selected project.

::

  avn events


**Example:** Show the most recent 10 events of a named project.

::

  avn events -n 10 --project my-project
