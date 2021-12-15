Connect to MySQL with MySQL Workbench
=====================================

You can use a graphical client like `MySQL
Workbench <https://www.mysql.com/products/workbench/>`__ to connect to Aiven for MySQL services.
Enter the individual connection parameters as shown on Service Overview
page and also download the SSL CA certificate and specify the file on
SSL page.

.. image:: /images/products/mysql/mysql-workbench.png
   :alt: Screenshot of the MySQL Workbench settings screen

Using SSL is strongly recommended. In order to make a properly secure
connection, download the CA certificate and configure it in client
settings.

To create more databases, go to the service's **Databases** tab, type
in a database name in the **Create a new database** box, and click the "
**Add database** " button.

To add database users, go to the service's **Users** tab. When adding a
new user you can choose the authentication method to use. By default,
the web console uses the ``caching_sha2_password`` authentication
mechanism. To successfully connect, your client libraries need to be new
enough. If for any reason you are forced to use a client that only
supports the older ``mysql_native_password`` authentication mechanism,
select this separately while adding the user. (You can also later change
this on the **Users** tab.) Note that changing the authentication method
for a user resets the password.

