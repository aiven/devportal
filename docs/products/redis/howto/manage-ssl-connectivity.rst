Manage SSL connectivity
=======================

Client support for SSL-encrypted connections
--------------------------------------------

Default support
~~~~~~~~~~~~~~~
Aiven for Redis uses SSL encrypted connections by default. This is shown by the use of ``rediss://`` (with double s) prefix in the ``Service URI`` on the `Aiven Console <https://console.aiven.io/>`_.

.. Tip::
    You can find the ``Service URI`` on `Aiven console <https://console.aiven.io/>`_.

Since **Redis 6**, the ``redis-cli`` tool itself supports SSL connections; therefore, you can connect directly to your service using::

    redis-cli -u rediss://username:password@host:port

Alternatively, you can use the third-party `Redli tool <https://github.com/IBM-Cloud/redli>`_::

    redli -u rediss://username:password@host:port


Not every Redis client supports SSL-encrypted connections.
In such cases, you would have to turn off or bypass the SSL to use these clients, which is allowed but **not recommended**. You can use one of the following option to achieve this.


Set up ``stunnel`` process
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to keep SSL settings on database side, but hide it from the client side, you can set up a ``stunnel`` process on the client to handle encryption.

You can use the following ``stunnel`` configuration, for example ``stunnel.conf``, to set up a ``stunnel`` process.
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

To understand the global options of the ``stunnel`` configuration, please check `Stunnel Global Options <https://www.stunnel.org/static/stunnel.html#GLOBAL-OPTIONS>`_. Also, you can find out more details about how to setup such a process on the `Stunnel website page <https://www.stunnel.org/index.html>`_.

For ``service-level option``, the following parameters are configured:  

``accept`` => *[host:]port*
  **Accept connections on specified address**



``connect`` => *[host:]port*
  **Connect to a remote address** 



``TIMEOUTclose`` => *seconds*
  **Time to wait for close_notify**

.. note:: It is important to make changes accordingly to your service. On the *Overview* page you can find your **Overview** > **Host** and **Overview** > **Port** to configure the ``connect`` parameter.

It is important to note that when SSL is in use, HAProxy will be responsible for terminating the SSL connections before they get forwarded to Redis. This process has a connection timeout set to 12 hours which is not configurable by the customer. If you allow very long Redis timeouts, this SSL-terminating HAProxy may end up closing the connection before the Redis timeout has expired. This timeout is independent of Redis timeout.

Allow plain-text connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An alternative is disable database SSL allowing allow plain-text connections. To allow plain-text connections, you can change this setting on **Overview** in the **Advanced configuration** section, or using the :doc:`Aiven Command Line interface<../../../tools/cli>`.

.. Warning::
    Allowing plain-text connections can have some implications regarding the security of your Redis service. If SSL is turned off, anyone who can eavesdrop on the traffic can potentially have access to your credentials; therefore, your Aiven for Redis service.

To disable SSL on an existing Redis instance use the following Aiven CLI command substituting the ``<my-redis>`` with your Redis the name service chosen by you when the service was created.

.. code-block:: console

    avn service update <my-redis> -c "redis_ssl=false"

After executing the command, the ``Service URI`` will change and point at the new location, it will also start with the ``redis://`` (removing the extra s) prefix denoting that it's a direct Redis connection which does not use SSL.


