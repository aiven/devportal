MySQL ``max_connections``
=========================

``max_connections`` vs RAM
--------------------------

The maximum number of simultaneous connections in Aiven for MySQL® depends on how much RAM your service plan offers and is fixed for each service plan (`Hobbyist`, `Startup`, `Business`, `Premium`, or any other plan available under a specific cloud provider.)

.. note::
    Independent of the plan, an ``extra_connection`` with a value of ``1`` is added for the system process.

Plans under 4 GiB
-----------------

For plans under 4 GiB of RAM, the number of allowed connections is |mysql_connections_per_<4G| per GiB:

    :math:`{max\_connections} =` |mysql_connections_per_<4G| |mysql_max_connections| 

.. topic:: Example

    With 2 GiB of RAM, the maximum number of connections is
            :math:`{max\_connections} =` |mysql_connections_per_<4G| x 2 + 1

Plans with 4 GiB or more
------------------------

For plans higher or equal to 4 GiB, the number of allowed connections is |mysql_connections_per_>4G| per GiB:
    
    :math:`{max\_connections} =` |mysql_connections_per_>4G| |mysql_max_connections|

.. topic:: Example

    With 7 GiB of RAM, the maximum number of connections is
            :math:`{max\_connections} =` |mysql_connections_per_>4G| x 7 + 1

.. include:: /includes/platform-variables.rst