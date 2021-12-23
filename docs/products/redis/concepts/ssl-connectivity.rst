SSL connectivity
================

Client support for SSL-encrypted connections
--------------------------------------------

Aiven for Redis uses SSL encrypted connections by default. This is shown by the use of ``rediss://`` (with double s) prefix in the ``Service URI``. 

.. Tip::
    You can find the ``Service URI`` on `Aiven console <https://console.aiven.io/>`_.

Since **Redis 6**, the redis-cli tool itself supports SSL connections; therefore, you can connect directly to your service using::

    redis-cli -u rediss://username:password@host:port

Alternatively, you can use the third-party `redli tool <https://github.com/IBM-Cloud/redli>`_::

    redli -u rediss://username:password@host:port


Not every Redis client supports SSL-encrypted connections. In those cases, you have some options:


Set up stunnel process
~~~~~~~~~~~~~~~~~~~~~~

Not every Redis client supports SSL-encrypted connections. In such cases, you would have to turn off SSL to use these clients, which is allowed but not recommended. One workaround for this, it is to set up a stunnel process on the client side to handle encryption for the clients that do not support SSL connections. 

You can use the following stunnel configuration, for example ``example-stunnel.conf``, to set up a stunnel process.
::

    client = yes
    foreground = yes
    debug = info
    delay = yes

    [redis]
    accept = 127.0.0.1:6380
    connect = myredis.testproject.aivencloud.com:28173
    TIMEOUTclose = 0
    ; For old services only. New ones use Let's Encrypt and there's no
    ; CA cert available from Aiven console. Most environments trust
    ; Let's Encrypt by default without any explicit CAfile config.
    ; CAfile = /path/to/optional/project/cacert/that/you/can/download/from/aiven/console

Note that when SSL is in use we have a separate service terminating the SSL connections before they are forwarded to Redis. This process has a connection timeout of its own independent of Redis' connection timeout. If you allow very long Redis timeouts this frontend service may end up closing the connection before the Redis timeout has expired. By the time of writing this timeout is set to 12 hours.

Allow plain-text connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To allow plain-text connections, you can change this setting with **Overview** > **Advanced configuration**, or using the :doc:`Aiven Command Line interface<../../../tools/cli>`.

.. Warning::
    Allowing plain-text connections can have some implications regarding the security of your Redis service. If SSL is turned off, anyone who can eavesdrop on the traffic will be able to potentially connect and access your Aiven for Redis service.

Alternatively, once installed, you should run::

    avn login  # if you haven't logged in previously
    avn service update myredis -c "redis_ssl=false"

After this, the ``Service URI`` will change and point at the new location, it will also start with the ``redis://`` prefix denoting that it's a direct Redis connection which does not use SSL.


