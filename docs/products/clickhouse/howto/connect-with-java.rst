Connect to the Aiven for ClickHouse® service with Java
======================================================

Learn how to connect to your Aiven for ClickHouse® service with Java using the ClickHouse JDBC driver and the HTTPS port.

Pre-requisites
--------------

* `Java 8 <https://www.java.com/en/download/>`_ or later
* `ClickHouse JDBC driver <https://github.com/ClickHouse/clickhouse-jdbc/tree/master/clickhouse-jdbc>`_

Identify connection information
-------------------------------

To run the code for connecting to your service, first identify values of the following variables:

===========================     =======================================================================================
Variable                        Description
===========================     =======================================================================================
``CLICKHOUSE_HTTPS_HOST``       ``Host`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``CLICKHOUSE_HTTPS_PORT``       ``Port`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**                 
``CLICKHOUSE_USER``             ``User`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**           
``CLICKHOUSE_PASSWORD``         ``Password`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**           
===========================     =======================================================================================

Connect to the service
----------------------

1. Add the ClickHouse JDBC driver to your Maven dependencies.

.. code-block:: shell

    <dependency>
        <groupId>com.clickhouse</groupId>
        <artifactId>clickhouse-jdbc</artifactId>
        <version>0.3.2-patch11</version>
        <classifier>all</classifier>
        <exclusions>
            <exclusion>
                <groupId>*</groupId>
                <artifactId>*</artifactId>
            </exclusion>
        </exclusions>
    </dependency>

2. Replace ``CLICKHOUSE_HTTPS_HOST`` and ``CLICKHOUSE_HTTPS_PORT`` in the command with your connection values and run the code.

.. code-block:: shell

    jdbc:ch://CLICKHOUSE_HTTPS_HOST:CLICKHOUSE_HTTPS_PORT?ssl=true&sslmode=STRICT

3. Replace ``CLICKHOUSE_USER`` and ``CLICKHOUSE_PASSWORD`` in the code with meaningful data and run the code.

.. code-block:: java

    import com.clickhouse.jdbc.ClickHouseConnection;
    import com.clickhouse.jdbc.ClickHouseDataSource;
    
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Statement;
    
    public class Main {
        public static void main(String[] args) throws SQLException {
            String connString = "jdbc:ch://CLICKHOUSE_HTTPS_HOST:CLICKHOUSE_HTTPS_PORT?ssl=true&sslmode=STRICT";
            ClickHouseDataSource database = new ClickHouseDataSource(connString);
            ClickHouseConnection connection = database.getConnection("CLICKHOUSE_USER", "CLICKHOUSE_PASSWORD");
            Statement statement = connection.createStatement();
            ResultSet result_set = statement.executeQuery("SELECT 1 AS one");
            while (result_set.next()) {
                System.out.println(result_set.getInt("one"));
            }
        }
    }

.. topic:: Expected result

    Now you have your service connection set up and you can proceed to :doc:`uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.

