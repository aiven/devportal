Migrate from Redis to Aiven for Redis
=====================================

Move your data from a source, standalone Redis data store to an Aiven-managed Redis service. The migration first attempts to use the ``replication`` method, and if it fails, it uses ``scan``. 

In the following steps, we show you how to create a new Aiven for Redis service, and migrate data from AWS ElastiCache Redis. The Aiven project name is ``test``, and the service name for the target Aiven for Redis is ``redis``.

.. Important::
        Migrating from Google Cloud Memorystore for Redis is not currently supported.


What you'll need
----------------

* A target Aiven for Redis service. See :doc:`get-started` to create one, or follow the instructions below. 

* The hostname, port and password of the source Redis service. 

* The source Redis service secured with SSL which is the default for migration.

* Publicly accessible source Redis service or a service with a VPC peering between the private networks. The migration process requires VPC ID and the cloud name. 

.. Note::
        AWS ElastiCache for Redis instances cannot have public IP addresses, and thus require project VPC and peering connection.




-> To create a service and perform the migration
-------------------------------------------------

1. Check the Aiven configuration options and Redis connection details:

    * for Aiven configuration options, type::


        $ avn service types -v
        ...
        Service type 'redis' options:
        ...
        Remove migration
            => --remove-option migration
        Hostname or IP address of the server where to migrate data from 
            => -c migration.host=<string>
        Password for authentication with the server where to migrate data from
            => -c migration.password=<string>
        Port number of the server where to migrate data from
            => -c migration.port=<integer>
        The server where to migrate data from is secured with SSL
            => -c migration.ssl=<boolean>  (default=True)
        User name for authentication with the server where to migrate data from
            => -c migration.username=<string>
    
    * for the VPC information, type::

        $ avn vpc list --project test
        PROJECT_VPC_ID                        CLOUD_NAME     ...
        ====================================  =============
        40ddf681-0e89-4bce-bd89-25e246047731  aws-eu-west-1

    .. Note::
            Here are your required values for the hostname, port and password of the source Redis service, as well as the VPD ID and cloud name. 

2. Create the Aiven for Redis service (if you don't have one yet), and migrate::

    $ avn service create --project test -t redis -p hobbyist --cloud aws-eu-west-1 --project-vpc-id 40ddf681-0e89-4bce-bd89-25e246047731 -c migration.host="master.jappja-redis.kdrxxz.euw1.cache.amazonaws.com" -c migration.port=6379 -c migration.password=<password> redis

.. Tip::
        If the source Redis server is publicly accessible, the project-vpc-id and cloud parameters are not needed.

3. Check the migration status::

    $ avn service migration-status --project test redis
    STATUS  METHOD  ERROR
    ======  ======  =====
    done    scan    null


.. Note::
        Status can be one of done, failed or running. In case of failure, the error contains the error message::

            $ avn service migration-status --project test redis
            STATUS  METHOD  ERROR           
            ======  ======  ================
            failed  scan    invalid password


-> To migrate to an existing Aiven for Redis service
----------------------------------------------------

Migrate to an existing Aiven for Redis service by updating the service configuration::

    $ avn service update --project test -c migration.host="master.jappja-redis.kdrxxz.euw1.cache.amazonaws.com" -c migration.port=6379 -c migration.password=<password> redis

-> To remove migration from configuration
---------------------------------------------
Migration is one-time operation - once the status is ``done``, the migration cannot be restarted. If you need to run migration again, you should first remove it from the configuration, and then configure it again::

    $ avn service update --project test --remove-option migration redis
