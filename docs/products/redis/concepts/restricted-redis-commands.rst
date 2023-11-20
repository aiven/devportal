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

