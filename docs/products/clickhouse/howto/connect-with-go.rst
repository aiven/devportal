
Connect to the Aiven for ClickHouse® service with Go
====================================================

To connect to your Aiven for ClickHouse® service with Go, you can use the native protocol or the HTTPS protocol in specific cases. This article provides you with instructions for both scenarios.

Prerequisites
-------------

`Go 1.17 or later <https://go.dev/dl/>`_

Install the ClickHouse Go module
--------------------------------

To install the ClickHouse Go module, run the following command:

.. code-block:: go

    go get github.com/ClickHouse/clickhouse-go/v2

.. note::

    If the version of Go is lower than 1.18.4 (visible via ``go version``), you need to install an older version of ``clickhouse-go``. For this purpose, use command ``go get github.com/ClickHouse/clickhouse-go/v2@v2.2``.

Connect with the native protocol
--------------------------------

Identify connection information
'''''''''''''''''''''''''''''''

To run the code for connecting to your service, first identify values of the following variables:

==================      =====================================================================
Variable                Description
==================      =====================================================================
``Host``                **Host** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``Port``                **Port** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``Database``            **Database Name** in your the ClickHouse service available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``Username``            **User** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``Password``            **Password** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
==================      =====================================================================

Connect to the service
''''''''''''''''''''''

Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code:: go

    package main
    import "fmt"
    import "log"
    import "crypto/tls"
    import "github.com/ClickHouse/clickhouse-go/v2"
    func main() {
        host := "HOST"
        native_port := NATIVE_PORT
        database := "DATABASE_NAME"
        username := "USERNAME"
        password := "PASSWORD"
        tls_config := &tls.Config{}
        conn, err := clickhouse.Open(&clickhouse.Options{
            Addr: []string{fmt.Sprintf("%s:%d", host, native_port)},
            Auth: clickhouse.Auth{
                Database: database,
                Username: username,
                Password: password,
            },
            TLS: tls_config,
        })
        if err != nil {
            log.Fatal(err)
        }
        v, err := conn.ServerVersion()
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(v)
    }

Connect with HTTPS
------------------

.. important::

    The HTTPS connection is supported for the database/sql API only. By default, connections are established over the native protocol. The HTTPS connection needs to be enabled either by modifying the DSN to include the HTTPS protocol or by specifying the protocol in the connection options.

Identify connection information
'''''''''''''''''''''''''''''''

To run the code for connecting to your service, first identify values of the following variables:

==================      =====================================================================
Variable                Description
==================      =====================================================================
``Host``                **Host** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``HttpPort``                **Port** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``Database``            **Database Name** in your the ClickHouse service available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``Username``            **User** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``Password``            **Password** for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
==================      =====================================================================

Connect to the service
''''''''''''''''''''''

Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code:: go

    package main
    import "database/sql"
    import "fmt"
    import "log"
    import _ "github.com/ClickHouse/clickhouse-go/v2"
    func main() {
            host := "HOST"
            https_port := HTTPS_PORT
            username := "USERNAME"
            password := "PASSWORD"
            conn, err := sql.Open(
                    "clickhouse",
                    fmt.Sprintf(
                            "https://%s:%d?username=%s&password=%s&secure", host, https_port, username, password))
            if err != nil {
                    log.Fatal(err)
            }
            rows, err := conn.Query("SELECT version()")
            if err != nil {
                    log.Fatal(err)
            }
            defer rows.Close()
            for rows.Next() {
                    var version string
                    if err := rows.Scan(&version); err != nil {
                            log.Fatal(err)
                    }
                    fmt.Println(version)
            }
    }

.. topic:: Expected result

    Now you have your service connection established and (possibly) configured. You can proceed to :doc:`uploading data into your database <load-dataset>`.

.. seealso::

    * For instructions on how to configure connection settings, see `Connection settings <https://clickhouse.com/docs/en/integrations/go/clickhouse-go/clickhouse-api/#connection-settings>`_.
    * For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.
