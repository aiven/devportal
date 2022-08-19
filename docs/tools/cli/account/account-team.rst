``avn account team``
=======================================

Here you'll find the full list of commands for ``avn account team``.


Manage account teams
-------------------------

Commands for managing Aiven account teams via ``avn`` commands.

``avn account team create``
'''''''''''''''''''''''''''

Creates a new account team.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-name``
    - The name of the team

**Example:** Create a new team named ``clickstream analytics`` for the account id ``123456789123``.

::

  avn account team create 123456789123 --team-name "clickstream analytics"

``avn account team delete``
'''''''''''''''''''''''''''

Deletes an existing account team.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-id``
    - The id of the team to delete

**Example:** Delete the team with id ``at31d79d311b3`` for the account id ``123456789123``.

::

  avn account team delete 123456789123 --team-id at31d79d311b3

``avn account team list``
'''''''''''''''''''''''''''

Lists an existing account teams.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account


**Example:** List all the teams belonging to the account id ``123456789123``.

::

  avn account team list 123456789123 

An example of ``account team list`` output:

.. code:: text

    ACCOUNT_ID    CREATE_TIME           TEAM_ID        TEAM_NAME           UPDATE_TIME
    ============  ====================  =============  ==================  ====================
    123456789123  2020-09-09T20:28:44Z  at3exxxxxxxxx  Account Owners      2020-09-09T20:28:44Z
    123456789123  2021-08-19T20:06:24Z  at3yyyyyyyyyy  admin-team-test     2021-08-19T20:06:24Z
    123456789123  2021-08-17T15:48:29Z  at3zzzzzzzzzz  dev-team-test       2021-08-17T15:48:29Z

``avn account team project-attach``
'''''''''''''''''''''''''''''''''''

Attaches an existing account team to a project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-id``
    - The id of the team
  * - ``--project``
    - The project to attach to
  * - ``--team-type``
    - The permission level (possible values ``admin``, ``developer``, ``operator``, ``read_only``). 
      More info at the :doc:`dedicated page </docs/platform/concepts/projects_accounts_access>`


**Example:** Attach the team with id ``at3exxxxxxxxx`` belonging to the account ``123456789123`` to the project named ``testing-sandbox`` granting ``operator`` access.

::

  avn account team project-attach 123456789123  \
    --team-id at3exxxxxxxxx                     \
    --project testing-sandbox                   \
    --team-type operator

``avn account team project-detach``
'''''''''''''''''''''''''''''''''''

Detaches an existing account team from a project.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-id``
    - The id of the team
  * - ``--project``
    - The project to detach from


**Example:** Detach the team with id ``at3exxxxxxxxx`` belonging to the account ``123456789123`` from the project named ``testing-sandbox``.

::

  avn account team project-detach 123456789123  \
    --team-id at3exxxxxxxxx                     \
    --project testing-sandbox

``avn account team user-invite``
'''''''''''''''''''''''''''''''''''

Invites a new user to an Aiven team.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``email``
    - The new user's email address
  * - ``--team-id``
    - The id of the team

**Example:** Invite the user ``jane.doe@example.com`` to the team id ``at3exxxxxxxxx`` belonging to the account ``123456789123``.

::

  avn account team user-invite 123456789123 jane.doe@example.com  --team-id at3exxxxxxxxx

``avn account team user-delete``
'''''''''''''''''''''''''''''''''''

Deletes an existing user from an Aiven team.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-id``
    - The id of the team
  * - ``--user-id``
    - The existing user's id

**Example:** Remove the user with id ``x5dxxxxxxxxx`` from the team id ``at3exxxxxxxxx`` belonging to the account ``123456789123``.

::

  avn account team user-delete 123456789123 --team-id at3exxxxxxxxx --user-id x5dxxxxxxxxx

``avn account team user-list``
'''''''''''''''''''''''''''''''''''

Lists the existing users in an Aiven team.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-id``
    - The id of the team

**Example:** List all the users in the team id ``at3exxxxxxxxx`` belonging to the account ``123456789123``.

::

  avn account team user-list 123456789123 --team-id at3exxxxxxxxx 

An example of ``account team user-list`` output:

.. code:: text

    CREATE_TIME           REAL_NAME            TEAM_ID        TEAM_NAME        UPDATE_TIME           USER_EMAIL                    USER_ID
    ====================  ===================  =============  ===============  ====================  ============================  ============
    2020-09-22T12:37:21Z  Jane Doe             at3exxxxxxxxx  admin-team-test  2020-09-22T12:37:21Z  jane.doe@example.com          u2xxxxxxxxxx
    2020-09-10T09:05:54Z  Diana Smith          at3exxxxxxxxx  admin-team-test  2020-09-10T09:05:54Z  diana.smith@example.com       u2yyyyyyyyyy
    2020-09-10T04:28:59Z  Filiberta Esposito   at3exxxxxxxxx  admin-team-test  2020-09-10T04:28:59Z  f.esposito@example.com        u2zzzzzzzzzz
    2021-03-18T08:56:47Z  Aki Halvari          at3exxxxxxxxx  admin-team-test  2021-03-18T08:56:47Z  aki.halvari@example.com       u3rrrrrrrrrr
    2021-08-09T13:23:00Z  Michael Klein        at3exxxxxxxxx  admin-team-test  2021-08-09T13:23:00Z  mklein@example.com            u3qqqqqqqqqq

``avn account team user-list-pending``
''''''''''''''''''''''''''''''''''''''

Lists the users with pending invitation from an Aiven team. Unacknowledged invitations are automatically deleted in 72 hours.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--team-id``
    - The id of the team

**Example:** List all the users with pending invitations for the team id ``at3exxxxxxxxx`` belonging to the account ``123456789123``.

::

  avn account team user-list-pending 123456789123 --team-id at3exxxxxxxxx 

An example of ``account team user-list-pending`` output:

.. code:: text

    ACCOUNT_ID    ACCOUNT_NAME    CREATE_TIME           INVITED_BY_USER_EMAIL  TEAM_ID        TEAM_NAME        USER_EMAIL
    ============  ==============  ====================  =====================  =============  ===============  ==========================
    123456789123  Jana Reinhardt  2021-08-23T13:14:20Z  jane.doe@example.com   at3exxxxxxxxx  admin-team-test  jana.reinhardt@example.com