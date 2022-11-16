
Connect to the Aiven for ClickHouse® service with Go
====================================================

To connect to your Aiven for ClickHouse® service with Go, you can use the native protocol or the HTTP protocol in specific cases. This article provides you with instructions for both scenarios.

Prerequisites
-------------

* `Go installed <https://go.dev/dl/>`_
* ``TLS`` option enabled

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

    conn, err := clickhouse.Open(&clickhouse.Options{
        Addr: []string{fmt.Sprintf("%s:%d", env.Host, env.Port)},
        Auth: clickhouse.Auth{
            Database: env.Database,
            Username: env.Username,
            Password: env.Password,
        },
    })
    if err != nil {
        return err
    }
    v, err := conn.ServerVersion()
    fmt.Println(v)

Connect with HTTP
-----------------

.. important::

    The HTTP connection is supported for the database/sql API only. By default, connections are established over the native protocol. The HTTP connection needs to be enabled either by modifying the DSN to include the HTTP protocol or by specifying the protocol in the connection options.

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

    func ConnectHTTP() error {
        env, err := GetStdTestEnvironment()
        if err != nil {
            return err
        }
        conn := clickhouse.OpenDB(&clickhouse.Options{
            Addr: []string{fmt.Sprintf("%s:%d", env.Host, env.HttpPort)},
            Auth: clickhouse.Auth{
                Database: env.Database,
                Username: env.Username,
                Password: env.Password,
            },
            Protocol: clickhouse.HTTP,
        })
        return conn.Ping()
    }

    func ConnectDSNHTTP() error {
        env, err := GetStdTestEnvironment()
        if err != nil {
            return err
        }
        conn, err := sql.Open("clickhouse", fmt.Sprintf("http://%s:%d?username=%s&password=%s", env.Host, env.HttpPort, env.Username, env.Password))
        if err != nil {
            return err
        }
        return conn.Ping()
    }

Established a configured connection
-----------------------------------

When opening a connection, you can specify a number of settings in the ``Options`` struct to configure the connection.

Identify connection information
'''''''''''''''''''''''''''''''

To run the code that not only opens a connection but also controls the client behavior, first identify the following connection details:

========================    ========================================================================================================================================================================================================================
Setting                     Description                                                                                                               
========================    ========================================================================================================================================================================================================================
``Protocol``                Either native or HTTP (HTTP supported for the database/sql API only)                                                                              
``TLS``                     `TLS options <https://clickhouse.com/docs/en/integrations/go/clickhouse-go/clickhouse-api#using-tls>`_. A non-nil value enables TLS.                                                                                       
``Addr``                    Slice of addresses including port                                                                            
``Auth``                    `Authentication detail <https://clickhouse.com/docs/en/integrations/go/clickhouse-go/clickhouse-api#authentication>`_                                                             
``DialContext``             Custom dial function to determine how connections are established         
``Debug``                   ``true``/``false`` to enable debugging                                                                
``Debugf``                  Provides a function to consume debug output. Requires ``debug`` to be set to ``true``.                                                                                                 
``Settings``                Map of ClickHouse settings to be applied to all ClickHouse queries. `Using Context <https://clickhouse.com/docs/en/integrations/go/clickhouse-go/clickhouse-api#using-context>`_ allows settings to be set per query.                                                   
``Compression``             `Enables compression <https://clickhouse.com/docs/en/integrations/go/clickhouse-go/clickhouse-api#compression>`_ for blocks                                                                                                                   
``DialTimeout``             Maximum time to establish a connection (defaults to 1 s)                                                                                 
``MaxOpenConns``            Maximum number of connections for use at any time. More or fewer connections may be in the idle pool, but only this number can be used at any time (defaults to MaxIdleConns+5).                
``MaxIdleConns``            Number of connections to maintain in the pool. Connections will be reused if possible (defaults to 5) 
``ConnMaxLifetime``         Maximum lifetime of a connection (defaults to 1 h)                                                         
``ConnOpenStrategy``        Determines how the list of node addresses should be consumed and used to open connections (`<https://clickhouse.com/docs/en/integrations/go/clickhouse-go/clickhouse-api#connecting-to-multiple-nodes>`_)                                                       
========================    ========================================================================================================================================================================================================================

Connect to the service
''''''''''''''''''''''

To open a configured connection with with your service, replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code:: go

    conn, err := clickhouse.Open(&clickhouse.Options{
        Addr: []string{fmt.Sprintf("%s:%d", env.Host, env.Port)},
        Auth: clickhouse.Auth{
            Database: env.Database,
            Username: env.Username,
            Password: env.Password,
        },
        DialContext: func(ctx context.Context, addr string) (net.Conn, error) {
            dialCount++
            var d net.Dialer
            return d.DialContext(ctx, "tcp", addr)
        },
        Debug: true,
        Debugf: func(format string, v ...interface{}) {
            fmt.Printf(format, v)
        },
        Settings: clickhouse.Settings{
            "max_execution_time": 60,
        },
        Compression: &clickhouse.Compression{
            Method: clickhouse.CompressionLZ4,
        },
        DialTimeout:      time.Duration(10) * time.Second,
        MaxOpenConns:     5,
        MaxIdleConns:     5,
        ConnMaxLifetime:  time.Duration(10) * time.Minute,
        ConnOpenStrategy: clickhouse.ConnOpenInOrder,
    })
    if err != nil {
        return err
    }

.. topic:: Expected result

    Now you have your service connection established and (possibly) configured. You can proceed to :doc:`uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.
