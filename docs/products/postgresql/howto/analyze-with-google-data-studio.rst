Report and analyze with Google Data Studio
==========================================

Google Data Studio allows you to create reports and visualisations of the data in your Aiven for PostgreSQL® database, and combine these with data from many other data sources.

Variables
---------

These are the placeholders you will need to replace in the code sample:

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

* You will need a Google account, to access Google Data Studio.

* Install ``openssl`` and run the following to generate the client-side public and private key pairs:

  .. code:: bash

    openssl req -x509 -newkey rsa:2048 -keyout client-key.pem -out client-cert.pem \
        -days 3650 -nodes -subj '/CN=localhost'

* On the Aiven web console service page for your PostgreSQL database, download the CA certificate. The default filename is ``ca.pem``.

Connect your Aiven for PostgreSQL data source to Google Data Studio
-------------------------------------------------------------------

#. Login to Google and open `Google Data Studio <https://datastudio.google.com/>`__ .

#. Select `Create` and choose `Data source`

#. Fill in the requested information and agree to the Google terms and conditions.

#. Select the **PostgreSQL** Google Connector.

#. On the **Basic** tab, set

   * **Host name** to ``HOSTNAME``
   * **Port**: to ``PORT``
   * **Database** to ``DATABASE``
   * **Username** to ``avnadmin``
   * **Password** to ``PASSWORD``

#. Select **Enable SSL** and **Enable client authenticaion**
   and upload your certificate and key files.

   * **Server certificate** is ``ca.pem``
   * **Client certificate** is ``client-cert.pem``
   * **Client private key** is ``client-key.pem``

#. Click **AUTHENTICATE**.

#. Choose the table to be queried, or select **CUSTOM QUERY** to create an SQL query.

#. Click **CONNECT**

You can then proceed to create reports and create visualisations.
