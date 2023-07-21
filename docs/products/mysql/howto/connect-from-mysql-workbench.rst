Connect to Aiven for MySQL® with MySQL Workbench
================================================

You can use a graphical client like `MySQL
Workbench <https://www.mysql.com/products/workbench/>`__ to connect to Aiven for MySQL® services.

Connect to Aiven for MySQL®
---------------------------

Enter the individual connection parameters as shown in `Aiven Console <https://console.aiven.io/>`__ (the **Overview** page of your service > the **Connection information** section) and also download the SSL CA certificate and specify the file on
SSL page.

.. image:: /images/products/mysql/mysql-workbench.png
   :alt: Screenshot of the MySQL Workbench settings screen

.. important::
   
   Using SSL is strongly recommended. In order to make a properly secure connection, download the CA certificate and configure it in client settings.

Create an additional database
-----------------------------

To create more databases, go to the service's page in `Aiven Console <https://console.aiven.io/>`__ and select **Databases** from the sidebar. In the **Databases** view, select **Create database**, enter a name for your database in the **Create a new database** window, and select **Add database**.

Add a database user
-------------------

To add database users, go to `Aiven Console <https://console.aiven.io/>`__ and select your Aiven for MySQL service from the **Services** page. In your service's page, select **Users** from the sidebar. In the **Users** view, select **Add service user**.

In the **Create a service user** window, you can choose the authentication method to use. By default,
the web console uses the ``caching_sha2_password`` authentication
mechanism. To successfully connect, your client libraries need to be new
enough. If for any reason you are forced to use a client that only
supports the older ``mysql_native_password`` authentication mechanism,
select this separately while adding the user.

.. Tip::
   
   You can change this later in the **Users** view for your service (`Aiven Console <https://console.aiven.io/>`__).
   
.. note::
   
   Changing the authentication method for a user resets the password.

on top of the authentication method, one more input item required from you in the **Create a service user** window is a name for the user. Enter it into the **Username** field and select **Add service user**.
