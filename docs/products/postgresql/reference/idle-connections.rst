Idle connections
================

This document describes how Aiven for PostgreSQL® sets the keep-alive parameters on the server side, and what keep-alive parameters can be used at the client side.

Currently, the following default keep-alive timeouts are used on the `server-side <https://www.postgresql.org/docs/current/runtime-config-connection.html#RUNTIME-CONFIG-CONNECTION-SETTINGS>`_:

+---------------------------+-------+-----------------------------------------------------------------------+
| Parameter (server)        | Value | Description                                                           | 
+===========================+=======+=======================================================================+ 
|``tcp_keepalives_idle``    |7200   |Specifies the amount of time with no network activity after which the  |
|                           |       |operating system should send a TCP ``keepalive`` message to the client.|
+---------------------------+-------+-----------------------------------------------------------------------+
|``tcp_keepalive_count``    |9      |Specifies the number of TCP ``keepalive`` messages that can be lost    |
|                           |       |before the server's connection to the client is considered dead.       |
+---------------------------+-------+-----------------------------------------------------------------------+
|``tcp_keepalives_interval``|5      |Specifies the amount of time after which a TCP ``keepalive`` message   |
|                           |       |that has not been acknowledged by the client should be retransmitted.  |
+---------------------------+-------+-----------------------------------------------------------------------+

The `client-side <https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-KEEPALIVES>`_ keep-alive parameters can be set to whatever values you want. 

+-----------------------+----------------------------------------------------------------------+
| Parameter (client)    | Description                                                          | 
+=======================+======================================================================+
|``keepalives``         |Controls whether client-side TCP ``keepalives`` are used.             |
|                       |The default value is 1, meaning on.                                   |
+-----------------------+----------------------------------------------------------------------+ 
|``keepalives_idle``    |Controls the number of seconds of inactivity after which TCP should   |
|                       |send a ``keepalive`` message to the server.                           |
+-----------------------+----------------------------------------------------------------------+
|``keepalive_count``    |Controls the number of TCP ``keepalives`` that can be lost before the |
|                       |client's connection to the server is considered dead.                 |
+-----------------------+----------------------------------------------------------------------+
|``keepalives_interval``|Controls the number of seconds after which a TCP ``keepalive`` message|
|                       |that is not acknowledged by the server should be retransmitted.       |
+-----------------------+----------------------------------------------------------------------+


Even though TCP connections usually stay open for extended periods of time, you should also make sure that your applications can reconnect,
since TCP connections are liable to break at times. Also, when reconnecting you should make sure that your client always resolves the DNS address on connection, since the
underlying address will change during automatic failover when a primary node fails.
