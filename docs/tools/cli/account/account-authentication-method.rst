``avn account authentication-method``
========================================================

Here you’ll find the full list of commands for ``avn account authentication-method``.


Manage account authentication methods
-------------------------------------

Commands for managing Aiven accounts authentication methods.

``avn account authentication-method create``
''''''''''''''''''''''''''''''''''''''''''''

Creates a new authentication method. More information about authentication methods creation is available at the `dedicated page <https://docs.aiven.io/docs/platform/howto/saml/saml-authentication>`_

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``--name``
    - New authentication method name
  * - ``--type``
    - The type of the new authentication method. Currently only ``saml`` is available
  * - ``-c``
    - Additional configuration option (in the ``KEY=VALUE`` format)
  * - ``-f``
    - Path to file containing additional configuration options (in the ``KEY=VALUE`` format)

**Example:** Create a new ``saml`` authentication method named ``My Authentication Method`` for the account id ``123456789123``.

::

  avn account authentication-method create 123456789123 \
    --name "My Authentication Method"                   \
    --type saml

``avn account authentication-method delete``
''''''''''''''''''''''''''''''''''''''''''''

Deletes an existing authentication method.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``authentication_id``
    - Id of the authentication method

**Example:** Delete the authentication method with id ``88888888888`` belonging to the account id ``123456789123``.

::

  avn account authentication-method delete 123456789123 88888888888

``avn account authentication-method list``
''''''''''''''''''''''''''''''''''''''''''''

Lists the existing authentication methods.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account

**Example:** List all the authentication methods belonging to the account id ``123456789123``.

::

  avn account authentication-method list 123456789123

An example of account authentication-method list output:

.. code:: text

    ACCOUNT_ID    AUTHENTICATION_METHOD_ENABLED  AUTHENTICATION_METHOD_ID  AUTHENTICATION_METHOD_NAME  AUTHENTICATION_METHOD_TYPE  STATE                  CREATE_TIME           UPDATE_TIME
    ============  =============================  ========================  ==========================  ==========================  =====================  ====================  ====================
    123456789123  true                           am2exxxxxxxxx             Okta                        saml                        active                 2020-10-13T16:48:29Z  2021-08-10T08:33:15Z
    123456789123  true                           am2wwwwwwwwww             Centrify                    saml                        active                 2020-09-28T10:22:50Z  2020-09-28T12:06:06Z
    123456789123  true                           am2qqqqqqqqqq             Azure                       saml                        active                 2020-09-22T12:30:19Z  2020-09-22T12:34:02Z
    123456789123  true                           am2yyyyyyyyyy             Platform authentication     internal                    active                 2020-09-09T20:28:44Z  2020-09-09T20:28:44Z


``avn account authentication-method update``
''''''''''''''''''''''''''''''''''''''''''''

Updates an existing authentication method.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``account_id``
    - The id of the account
  * - ``authentication_id``
    - Id of the authentication method
  * - ``--name``
    - New authentication method name
  * - ``--enable``
    - Enables the authentication method
  * - ``--disable``
    - Disables the authentication method
  * - ``-c``
    - Additional configuration option (in the ``KEY=VALUE`` format)
  * - ``-f``
    - Path to file containing additional configuration options (in the ``KEY=VALUE`` format)

**Example:** Disable the authentication method with id ``am2exxxxxxxxx`` for the account id ``123456789123``.

::

  avn account authentication-method update 123456789123 am2exxxxxxxxx --disable
