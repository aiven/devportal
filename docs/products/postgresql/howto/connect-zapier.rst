Connect with Zapier
===================

`Zapier <https://zapier.com/>`_ is an automation platform that connects your work apps and does repetitive tasks for you.
This example shows how to configure PostgreSQL® as a connection in zapier.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      ===========================================================================
Variable                Description
==================      ===========================================================================
``HOSTNAME``            Hostname for the PostgreSQL connection, from the service overview page
``PORT``                Port for the PostgreSQL connection, from the service overview page
``DATABASE``            Database Name for the PostgreSQL connection, from the service overview page
``SCHEMA``              Default ``public`` schema or a specific schema
``USERNAME``            Username for the PostgreSQL connection
``PASSWORD``            Password for the above specified username
==================      ===========================================================================

Connect to PostgreSQL
'''''''''''''''''''''

1. In skyvia workspace -> **Connections** -> **Connector** -> **PostgreSQL**.
2. In the **General** Tab give the connection a Name (e.g. ``MyDatabase``)
3. In the **Connection** tab set:

   * **Host** to ``HOSTNAME``
   * **Port**: to ``PORT``
   * **Database** to ``DATABASE``
   * **Schema** to ``SCHEMA``
   * **Username** to ``USERNAME``
   * **Password** to ``PASSWORD``

4. Click on **Yes, Continue**.