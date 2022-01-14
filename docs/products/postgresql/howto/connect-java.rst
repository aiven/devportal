Connect with Java
-----------------

This example connects to PostgreSQL service from Java, making use of JDBC Driver.

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

For this example you will need:

Download PostgreSQL Driver.
There are several options to do that

1. In case you have maven version >= 2+ run the code::

    mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=org.postgresql:postgresql:42.2.24:jar -Ddest=postgresql-42.2.24.jar

2. Manually the jar could be downloaded from https://jdbc.postgresql.org/download.html

Code
''''

Add the following to ``PostgresqlExample.java`` and replace the placeholder with the PostgreSQL URI:

.. literalinclude:: /code/products/postgresql/connect.java

This code creates a PostgreSQL client and opens a connection to the database. Then runs a query checking the database version and prints the response

Before running the code replace
    * **HOST** to ``HOSTNAME``
    * **PORT**: to ``PORT``
    * **DATABASE** to ``DATABASE``
    * **PASSWORD** to ``PASSWORD``

To run the code::

    javac PostgresqlExample.java && java -cp postgresql-42.2.24.jar:. PostgresqlExample -host HOST -port PORT -database DATABASE -username avnadmin -password PASSWORD

If the script runs successfully, the outputs should be the PostgreSQL version running in your service like::

    Version: PostgreSQL 13.4 on x86_64-pc-linux-gnu, compiled by gcc, a cdda7373b4 p 9751fce1e6, 64-bit
