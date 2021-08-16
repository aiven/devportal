Command reference: ``avn user``
==================================

Here you'll find the full list of commands for ``avn user``.


Create and manage users and sessions
------------------------------------

Commands for managing project users and ``avn`` client sessions.

``avn user access-token``
'''''''''''''''''''''''''

:doc:`See detailed command information <user/user-access-token>`

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


**Example:** Retrieves the information for the currently logged user.

::

  avn user info

An example of user information:

.. code:: text

    USER                  REAL_NAME  STATE   TOKEN_VALIDITY_BEGIN              PROJECTS                       AUTH
    ====================  =========  ======  ================================  =============================  ========
    john.doe@example.com  John Doe   active  2021-08-18T09:24:10.298796+00:00  dev-sandbox, prod-environment  password



``avn user login``
''''''''''''''''''''

Logs in the user.


.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``email``
    - The email associated to the user
  * - ``--token``
    - Logs in the user with a pre-created token 

**Example:** Log in the user ``john.doe@example.com`` with prompted password.      
::

  avn user login john.doe@example.com

The user will be prompted to insert the password.


**Example:** Log in the user `john.doe@example.com` with pre-created authentication token.      
::

  avn user login john.doe@example.com --token 

The user will be prompted to insert the pre-created authentication token. 

``avn user logout``
''''''''''''''''''''

Logs out the user.


**Example:** Log out the user.      
::

  avn user logout

``avn user tokens-expire``
''''''''''''''''''''''''''

Expires all the authentication tokens associated with the user.


**Example:** Expire all the authentication tokens.      
::

  avn user tokens-expire

