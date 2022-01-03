Enable Lua scripts
==================

Redis has inbuilt support for running Lua scripts to perform various actions directly on the Redis server. Scripting is typically controlled using the ``EVAL`` , ``EVALSHA`` and ``SCRIPT LOAD`` commands.

For all newly-created Redis instances, ``EVAL``, ``EVALSHA``  and ``SCRIPT LOAD``  commands are enabled by default. 

Scripting commands are disabled by default in Aiven for Redis services created before 03.30.2018. However, you can enable Aiven for Redis scripting by request. Please contact Aiven support to enable scripting on your older Redis service.

.. note:: 
    Any outage caused by customer usage, including custom scripts, is not covered by the service SLA (Service Level Agreement).

For more information about Redis scripting, check `Redis documentation <https://redis.io/commands/eval>`__. 