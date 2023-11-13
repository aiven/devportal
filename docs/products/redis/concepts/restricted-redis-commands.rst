Restricted Aiven for Redis®* commands 
======================================

In this section, you can find information about Redis commands that are restricted or modified in our Aiven for Redis* service. These restrictions are in place to ensure the stability and security of the Redis environment. Understanding these limitations is essential for effectively managing and usingAiven for Redis* service.

Restricted commands
-------------------

Disabled commands
^^^^^^^^^^^^^^^^^

The following Redis commands are completely disabled in our service:

- ``bgrewriteaof``: Initiates a background append-only file rewrite.
- ``cluster``: Manages Redis cluster commands.
- ``command``: Provides details about all Redis commands.
- ``debug``: Contains sub-commands for debugging Redis.
- ``failover``: Manages manual failover of a master to a replica.
- ``migrate``: Atomically transfers a key from a Redis instance to another one.
- ``role``: Returns the role of the instance in the context of replication.
- ``slaveof``: Makes the server a replica of another instance, or promotes it as master.

Admin commands
^^^^^^^^^^^^^^

The following commands are reserved for administrative use and have been renamed:

- ``acl``: Manages Redis Access Control Lists.
- ``bgsave``: Creates a snapshot of the dataset into a dump file.
- ``config``: Alters the configuration of a running Redis server.
- ``lastsave``: Returns the UNIX timestamp of the last successful save to disk.
- ``monitor``: Streams back every command processed by the Redis server.
- ``replicaof``: Makes the server a replica of another instance.
- ``save``: Synchronously saves the dataset to disk.
- ``shutdown``: Synchronously saves the dataset to disk and then shuts down the server.

Eval commands
^^^^^^^^^^^^^

Script evaluation commands may be restricted based on service configuration:

- ``eval``: Executes a Lua script server-side.
- ``eval_ro``: Read-only variant of the `eval` command.
- ``evalsha``: Executes a script cached on the server side by its SHA1 digest.
- ``evalsha_ro``: Read-only variant of the `evalsha` command.
- ``fcall``: Calls a Redis function.
- ``fcall_ro``: Read-only variant of the `fcall` command.
- ``function``: Manages Redis functions.
- ``script``: Manages the script cache.


.. note:: 
    For enhanced security, certain admin commands are renamed. The renaming involves appending a suffix to the command name. This suffix is determined by the service configuration and is typically known only to our administrative team.
