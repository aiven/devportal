Connect with skyvia
===================

`skyvia <https://skyvia.com/>`_ is an universal cloud data platform.
This example shows how to configure PostgreSQL® as a connection in skyvia.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =======================================================================
Variable                Description
==================      =======================================================================
``SERVER``              Hostname for PostgreSQL connection, from the service overview page
``PORT``                Port for PostgreSQL connection, from the service overview page
``DATABASE``            Database Name for PostgreSQL connection, from the service overview page
``USERNAME``            ``avnadmin``
``PASSWORD``            ``avnadmin`` password, from the service overview page
==================      =======================================================================

Connect to PostgreSQL
'''''''''''''''''''''

1. In skyvia workspace -> **Connections** -> **Connector** -> **PostgreSQL**.
2. In the **General** Tab give the connection a Name (e.g. ``MyDatabase``)
3. In the **Connection** tab set
    * **Server** to ``SERVER``
    * **Port**: to ``PORT``
    * **User ID** to ``avnadmin``
    * **Password** to ``PASSWORD``
    * **Database** to ``YourDatabase``
  
.. image:: /images/products/postgresql/connect-skyvia-settings.png
    :alt: skyvia settings

4. Click on **Advanced Settings** to expand the settings.

.. image:: /images/products/postgresql/connect-skyvia-ssl.png
    :alt: skyvia advanced settings

5. In the **SSL** Mode set to ``Require``.
6. Copy and paste ``CA Certificate`` from Aiven console into ``SSL CA Cert``.
   
.. image:: /images/products/postgresql/connect-skyvia-cacert.png
    :alt: skyvia CA cert

7. Leave ``empty`` for **SSL Cert** and **SSL Key**.
8. Set ``SSL TLS Protocol`` to ``1.2``.
9. Click on **Save Connection**.