Command reference: ``avn user access-token``
============================================

Here you'll find the full list of commands for ``avn user access-token``.


Manage access tokens
----------------------------

Commands for managing user's access tokens.

``avn user access-token create``
''''''''''''''''''''''''''''''''

Creates a new access token for the logged-in user.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--description``
    - Description of how the token will be used
  * - ``--max-age-seconds``
    - Maximum age of the token in seconds, if any, after which it will expire(30 days by default)
  * - ``extend-when-used``
    - Extend token's expiry time when used (only applicable if token is set to expire)

**Example:** Create a new access token.

::

  avn user access-token create --description "To be used with Python Notebooks"


**Example:** Create a new token expiring every hour if not used.

::

  avn user access-token create                       \
    --description "To be used with Python Notebooks" \
    --max-age-seconds 3600                           \
    --extend-when-used
    
An example of newly created access token:

.. code:: text

    EXPIRY_TIME           DESCRIPTION                       MAX_AGE_SECONDS  EXTEND_WHEN_USED  FULL_TOKEN
    ====================  ================================  ===============  ================  ===============================
    2021-08-16T16:26:10Z  To be used with python notebooks  3600             true              6JsKDclT3OMQd1V2Fl2...RaraBPg==

``avn user access-token list``
''''''''''''''''''''''''''''''

Retrieves the information for all the access tokens active session in the session:

* Expiration time
* Token prefix
* Description
* Token's max age in seconds
* Extended when used flag 
* Last used time
* Last IP address 
* Last user agent


**Example:** Retrieve the information for the logged-in user.

::

  avn user access-token list

An example of user information:

.. code:: text

    EXPIRY_TIME           TOKEN_PREFIX  DESCRIPTION                       MAX_AGE_SECONDS  EXTEND_WHEN_USED  LAST_USED_TIME        LAST_IP      LAST_USER_AGENT
    ====================  ============  ================================  ===============  ================  ====================  ===========  ===================
    2021-09-15T15:29:14Z  XCJ3+bgWywIh  Test token                        2592000          true              2021-08-16T15:29:14Z  192.168.1.1  aiven-client/2.12.0
    2021-08-16T16:26:10Z  6JsKDclT3OMQ  To be used with Python Notebooks  3600             true              null                  null         null



``avn user access-token revoke``
''''''''''''''''''''''''''''''''

Revokes the specified user access token. 

Tokens can also be expired via the :ref:`avncli user-tokens-expire` command.


.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``token_prefix``
    - The full token or token prefix identifying the token to revoke

**Example:** Revoke the access token starting with ``6JsKDclT3OMQ``.      
::

  avn user access-token revoke "6JsKDclT3OMQ"


``avn user access-token update``
''''''''''''''''''''''''''''''''

Updates the description of an access token.


.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``token_prefix``
    - The full token or token prefix identifying the token to update

**Example:** Update the description of the access token starting with ``6JsKDclT3OMQ``.      
::

  avn user access-token update "6JsKDclT3OMQ" --description "To be used with Jupyter Notebooks"

