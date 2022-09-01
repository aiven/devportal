Connect with rivery
===================

`Rivery <https://rivery.io/>`_ is a fully-managed solution for data ingestion, transformation, orchestration, reverse ETL and more.
This example shows how to configure PostgreSQL® as a connection in rivery.

Variables
'''''''''

These are the placeholders you will need to replace from your PostgreSQL® connection information:

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

   * **Host** to ``HOSTNAME``
   * **Port**: to ``PORT``
   * **Database** to ``DATABASE``
   * **User name** to ``USERNAME``
   * **Password** to ``PASSWORD``

4. Click on **SSL Options** to expand the settings and set:

   * **SSL** Mode set to ``Require``

5. Click on **Save**.