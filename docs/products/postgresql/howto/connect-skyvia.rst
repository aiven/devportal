Connect with Skyvia
===================

`Skyvia <https://skyvia.com/>`_ is an universal cloud data platform.
This example shows how to configure PostgreSQL® as a connection in skyvia.

Variables
'''''''''

These are the placeholders you will need to replace your PostgreSQL® connection information:

==================      ===========================================================================
Variable                Description
==================      ===========================================================================
``HOSTNAME``            Hostname for the PostgreSQL connection, from the service overview page
``PORT``                Port for the PostgreSQL connection, from the service overview page
``DATABASE``            Database Name for the PostgreSQL connection, from the service overview page
``USERNAME``            Username for the PostgreSQL connection
``PASSWORD``            Password for the above specified username
==================      ===========================================================================

Connect to PostgreSQL®
'''''''''''''''''''''''

1. In skyvia workspace -> **Connections** -> **Connector** -> **PostgreSQL**.
2. In the **General** Tab give the connection a Name (e.g. ``MyDatabase``)
3. In the **Connection** tab set:

   * **Server** to ``HOSTNAME``
   * **Port**: to ``PORT``
   * **User ID** to ``USERNAME``
   * **Password** to ``PASSWORD``
   * **Database** to ``DATABASE``

4. Click on **Advanced Settings** to expand the settings and set:

   * **SSL** Mode set to ``Require``
   * In **SSL CA Cert** copy and paste ``CA Certificate`` from the `Aiven Console <https://console.aiven.io/>`_
   * **SSL Cert** and **SSL Key** empty.
   * **SSL TLS Protocol** to ``1.2``.

5. Click on **Save Connection**.