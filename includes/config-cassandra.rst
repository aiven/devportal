
``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips``
--------------
*boolean*

**Static IP addresses** Use static public IP addresses



``cassandra``
-------------
*object*

**cassandra configuration values** 

``batch_size_warn_threshold_in_kb``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**batch_size_warn_threshold_in_kb** Log a warning message on any multiple-partition batch size exceeding this value.5kb per batch by default.Caution should be taken on increasing the size of this thresholdas it can lead to node instability.

``batch_size_fail_threshold_in_kb``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**batch_size_fail_threshold_in_kb** Fail any multiple-partition batch exceeding this value. 50kb (10x warn threshold) by default.

``datacenter``
~~~~~~~~~~~~~~
*string*

**Cassandra datacenter name** Name of the datacenter to which nodes of this service belong. Can be set only when creating the service.



``migrate_sstableloader``
-------------------------
*boolean*

**Migration mode for the sstableloader utility** Sets the service into migration mode enabling the sstableloader utility to be used to upload Cassandra data files. Available only on service create.



``service_to_join_with``
------------------------
*string*

**Name of the service to form a bigger cluster with** When bootstrapping, instead of creating a new Cassandra cluster try to join an existing one from another service. Can only be set on service creation.



``cassandra_version``
---------------------
*['string', 'null']*

**Cassandra major version** 



``private_access``
------------------
*object*

**Allow access to selected service ports from private networks** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``public_access``
-----------------
*object*

**Allow access to selected service ports from the public Internet** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** 



``service_to_fork_from``
------------------------
*['string', 'null']*

**Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from``
------------------------
*['string', 'null']*

**Name of another project to fork a service from. This has effect only when a new service is being created.** 



