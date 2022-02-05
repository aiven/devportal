Connect to MySQL with Java
============================

This example connects your Java application to a MySQL service.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``MYSQL_HOST``          Host name for the connection, from the service overview page
------------------      -------------------------------------------------------------
``MYSQL_PORT``          Port number to use, from the service overview page
------------------      -------------------------------------------------------------
``MYSQL_PASSWORD``      Password for avnadmin user
------------------      -------------------------------------------------------------
``MYSQL_DATABASE``      Database to connect
==================      =============================================================

Pre-requisites
''''''''''''''

For this example you will need:

* JDK 1.8+

* MySql jdbc Driver which could be downloaded manually from https://dev.mysql.com/downloads/connector/j/
  or it could be downloaded with maven like::

    mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=mysql:mysql-connector-java:8.0.28:jar -Ddest=mysql-driver-8.0.28.jar


Code
''''

Add the following to ``MySqlExample.java``:

.. literalinclude:: /code/products/mysql/connect.java


This code creates a MySQL client and connects to the database. It fetches version of MySql and prints it the output.

Run the code after replacement of the placeholders with values for your project::

    javac MySqlExample.java && java -cp mysql-driver-8.0.28.jar:. MySqlExample -host MYSQL_HOST -port MYSQL_PORT -database MYSQL_DATABASE -username avnadmin -password MYSQL_PASSWORD

If the script runs successfully, the output will be the values that were inserted into the table::

    Version: 8.0.26

Now that your application is connected, you are all set to use Java with Aiven for MySQL.

