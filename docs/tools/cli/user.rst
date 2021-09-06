Command reference: ``avn user``
==================================

Here you'll find the full list of commands for ``avn user``.


Create and manage users and sessions
------------------------------------

Commands for managing project users and ``avn`` client sessions.

``avn user access-token``
'''''''''''''''''''''''''

Set of commands for managing user's access tokens. :doc:`See detailed command information <user/user-access-token>` for more information.

``avn user create``
'''''''''''''''''''''''

Creates a new user.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``email``
    - The email associated to the user
  * - ``--real-name``
    - The user's real name

**Example:** Create a new user.

::

  avn user create john.doe@example.com


**Example:** Create a new user specifying the real name.

::

  avn user create john.doe@example.com --real-name "John Doe"


``avn user info``
''''''''''''''''''''''

Retrieves the current user information such as:

* Username
* Real name
* State (``active`` or ``inactive``)
* Authentication token validity start date 
* Associated projects 
* Authentication method


**Example:** Retrieve the information for the currently logged user.

::

  avn user info

An example of user information:

.. code:: text

    USER                  REAL_NAME  STATE   TOKEN_VALIDITY_BEGIN              PROJECTS                       AUTH
    ====================  =========  ======  ================================  =============================  ========
    john.doe@example.com  John Doe   active  2021-08-18T09:24:10.298796+00:00  dev-sandbox, prod-environment  password



``avn user login``
''''''''''''''''''''

Logs the user in.


.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``email``
    - The email associated to the user
  * - ``--token``
    - Logs in the user with a pre-created token 

**Example:** Log the ``john.doe@example.com`` user in, and prompt for password.      
::

  avn user login john.doe@example.com

The user will be prompted to insert the password.


**Example:** Log the `john.doe@example.com` user `john.doe@example.com` with pre-created authentication token.      
::

  avn user login john.doe@example.com --token 

The user will be prompted to insert the pre-created authentication token. 

``avn user logout``
''''''''''''''''''''

Logs the user out.


**Example:** Log the user out.      
::

  avn user logout

.. _avncli user-tokens-expire:

``avn user tokens-expire``
''''''''''''''''''''''''''

Makes all the authentication tokens associated with the user expired.


**Example:** Make all the authentication tokens expired.      
::

  avn user tokens-expire

See also other :doc:`access-token related commands <user/user-access-token>`