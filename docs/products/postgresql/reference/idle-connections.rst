Idle connections
================

How Aiven for PostgreSQL® handles idle database connection sessions and uses TCP keep-alive.

Currently, the following default keep-alive timeouts are used on the server-side:

-  ``tcp_keepalives_idle=7200``

-  ``tcp_keepalive_count=9``

-  ``tcp_keepalives_interval=75``

You can set the client-side keep-alive timeouts to whatever values you
want. For more information, see
https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-KEEPALIVES
(the ``libpq`` configuration keys are the same as on the server side
except that the ``tcp\_`` prefix is omitted from the configuration keys).

Even though TCP connections usually stay open for extended periods of
time, you should also make sure that your applications can reconnect,
since TCP connections are liable to break at times - usually at very
inconvenient times. Also, when reconnecting you should make sure that
your client always resolves the DNS address on connection, since the
underlying address will change during automatic failover when a primary
node fails.
