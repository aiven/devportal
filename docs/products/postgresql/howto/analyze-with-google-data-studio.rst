Report and analyze with Google Data Studio
==========================================

Google Data Studio allows you to create reports and visualisations of the data in your Aiven for PostgreSQL® database, and combine these with data from many other data sources.

Variables
---------

These are the values you will need to connect to Google Data Studio:

==================      ===========================================================================
Variable                Description
==================      ===========================================================================
``HOSTNAME``            Hostname for the PostgreSQL connection, from the service overview page
``PORT``                Port for the PostgreSQL connection, from the service overview page
``DATABASE``            Database Name for the PostgreSQL connection, from the service overview page
``PASSWORD``            ``avnadmin`` password, from the service overview page
==================      ===========================================================================

Pre-requisites
--------------

1. You will need a Google account, to access Google Data Studio.

2. On the Aiven Console service page for your PostgreSQL database, download the CA certificate. The default filename is ``ca.pem``.

Connect your Aiven for PostgreSQL data source to Google Data Studio
-------------------------------------------------------------------

#. Login to Google and open `Google Data Studio <https://datastudio.google.com/>`__ .

#. Select **Create** and choose **Data source**.

#. Fill in the requested information and agree to the Google terms and conditions.

#. Select the **PostgreSQL** Google Connector.

#. On the **Basic** tab, set

   * **Host name** to the ``HOSTNAME``
   * **Port**: to the ``PORT``
   * **Database** to the ``DATABASE``
   * **Username** to ``avnadmin``
   * **Password** to the ``PASSWORD``

#. Select **Enable SSL** and upload your server certificate file, ``ca.pem``.

#. Click **AUTHENTICATE**.

#. Choose the table to be queried, or select **CUSTOM QUERY** to create an SQL query.

#. Click **CONNECT**

You can then proceed to create reports and create visualisations.
