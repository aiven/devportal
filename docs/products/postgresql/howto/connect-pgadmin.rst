Connect with pgAdmin
===========================

`pgAdmin <https://www.pgadmin.org/>`_ is one of the most popular PostgreSQL® clients, useful to manage and query your database.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =======================================================================
Variable                Description
==================      =======================================================================
``HOSTNAME``            Hostname for PostgreSQL connection, from the service overview page
``PORT``                Port for PostgreSQL connection, from the service overview page
``DATABASE``            Database Name for PostgreSQL connection, from the service overview page
``PASSWORD``            ``avnadmin`` password, from the service overview page
==================      =======================================================================

Pre-requisites
''''''''''''''

For this example you'll need pgAdmin already installed on your computer, for installation instructions follow the `pgAdmin website <https://www.pgadmin.org/download/>`_

Connect to PostgreSQL
'''''''''''''''''''''

1. Open pgAdmin and click on **Create New Server**.
2. In the **General** Tab give the connection a Name (e.g. ``MyDatabase``)
3. In the **Connection** tab set
    * **Host name/address** to ``HOSTNAME``
    * **Port**: to ``PORT``
    * **Maintenance database** to ``DATABASE``
    * **Username** to ``avnadmin``
    * **Password** to ``PASSWORD``
4. In the **SSL** tab set **SSL mode** to ``Require``
5. Click on **Save**

.. Tip::

    If you experience a SSL error while connecting, add the service CA certificate as the **Root certificate**.

    * Download the CA Certificate file to your computer.
    * In the pgAdmin connection settings, click on the SSL tab and select the CA certificate file you downloaded. Save the settings.

Your connection to PostgreSQL should now be opened, with a **Dashboard** page showing activity metrics on your PostgreSQL database.

.. image:: /images/products/postgresql/pg-pgadmin-activity.png
   :alt: Screenshot of a pgAdmin Dashboard window
