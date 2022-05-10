Report and analyze with Google Data Studio
==========================================

Google Data Studio allows you to create reports and visualisations of the data in your Aiven for PostgreSQL® database, and combine these with data from many other data sources.

Download the Aiven for PostgreSQL CA certificate
------------------------------------------------

On the Aiven web console service page for your PostgreSQL database, download the CA certificate. The default filename is ``ca.pem``.

Generate client side key pairs
------------------------------

Run the following OpenSSL command to generate the client-side public and private key pairs:

.. code:: bash

    openssl req -x509 -newkey rsa:2048 -keyout client-key.pem -out client-cert.pem \
        -days 3650 -nodes -subj '/CN=localhost'

Connect your Aiven for PostgreSQL data source to Google Data Studio
-------------------------------------------------------------------

#. Login to Google and open `Google Data Studio <https://datastudio.google.com/>`__ .

#. Select `Create` and choose `Data source`

#. Fill in the requested information and agree to the Google terms and conditions.

#. Select the **PostgreSQL** Google Connector.

#. On the **Basic** tab, enter the **Host Name** , **Port** ,
   **Database** , **Username** , and **Password** values.
   You can get these values from the **Overview** tab for your
   service in the Aiven web console.

#. Select **Enable SSL** and **Enable client authenticaion**
   and upload your certificate and key files.

   * **Server certificate** is the ``ca.pem``
   * **Client certificate** is the ``client-cert.pem``
   * **Client private key** is the ``client-key.pem``

#. Click **AUTHENTICATE**.

#. Choose the table to be queried, or select **CUSTOM QUERY** to create an SQL query.

#. Click **CONNECT**

You can then proceed to create reports and create visualisations.
