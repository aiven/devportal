Troubleshoot Redis®* connection issues
######################################

Discover troubleshooting techniques for your Redis®* service and check out how to resolve common connection issues.

Important notes
---------------
By default :doc:`Aiven for Redis® uses SSL connections</docs/products/redis/howto/manage-ssl-connectivity>` and these connections are closed automatically after 12 hours. This is not a parameter that can be changed. Aiven also sets the ``redis_timeout`` advanced parameter to 300 seconds by default.

Some Redis®* connections are closed intermittently 
--------------------------------------------------
When experiencing connection issues with your Redis®* service, here are some common things to check:
- Some Redis®* clients do not support SSL connections. It is recommended to check the documentation for the Redis®* client being used to ensure SSL connections are supported.
- If you are noticing older connections terminating, you should check to see what the value is configured for the :doc:`redis_timeout advanced parameter</docs/products/redis/reference/advanced-params>`. This parameter controls the timeout value for idle connections. Once the timeout is reached, the connection is terminated.

Methods for troubleshooting connections
---------------------------------------

A great way to troubleshoot connection issues is to arrange for a packet capture to take place. This can be achieved with tools like `Tcpdump <https://www.tcpdump.org/>`_ and `Wireshark <https://www.wireshark.org/>`_. This allows you to see if connections are making it outside your network to the Aiven for Redis®* instance.

Another tool you can use to help diagnose connection issues is the Socket Statistics CLI tool which dumps socket statistics.