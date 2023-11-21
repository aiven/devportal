Restricted Aiven for Redis®* commands 
======================================

To maintain the stability and security of the Redis environment, the Aiven for Redis* service restricts certain Redis commands. This section aims to provide you with a list of disabled/restricted commands.


Disabled commands
------------------

The Aiven for Redis* service has disabled the following Redis commands:

- ``bgrewriteaof``: Initiates a background append-only file rewrite.
- ``cluster``: Manages Redis cluster commands.
- ``command``: Provides details about all Redis commands.
- ``debug``: Contains sub-commands for debugging Redis.
- ``failover``: Manages manual failover of a master to a replica.
- ``migrate``: Atomically transfers a key from a Redis instance to another one.
- ``role``: Returns the role of the instance in the context of replication.
- ``slaveof``: Makes the server a replica of another instance, or promotes it as master.
- ``acl``: Manages Redis Access Control Lists.	
- ``bgsave``: Creates a snapshot of the dataset into a dump file.	
- ``config``: Alters the configuration of a running Redis server.	
- ``lastsave``: Returns the UNIX timestamp of the last successful save to disk.	
- ``monitor``: Streams back every command processed by the Redis server.	
- ``replicaof``: Makes the server a replica of another instance.	
- ``save``: Synchronously saves the dataset to disk.	
- ``shutdown``: Synchronously saves the dataset to disk and then shuts down the server.

Disabled Eval commands	
-------------------------
The following script evaluation commands in the Aiven for Redis* service are disabled. If you require these commands to be enabled, contact Aiven support.

- ``eval``: Executes a Lua script server-side.	
- ``eval_ro``: Read-only variant of the `eval` command.	
- ``evalsha``: Executes a script cached on the server side by its SHA1 digest.	
- ``evalsha_ro``: Read-only variant of the `evalsha` command.	
- ``fcall``: Calls a Redis function.	
- ``fcall_ro``: Read-only variant of the `fcall` command.	
- ``function``: Manages Redis functions.	
- ``script``: Manages the script cache.