
``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``service_log``
---------------
*['boolean', 'null']*

**Service logging** Store logs for the service so that they are available in the HTTP API and console.



``static_ips``
--------------
*boolean*

**Static IP addresses** Use static public IP addresses



``project_to_fork_from``
------------------------
*['string', 'null']*

**Name of another project to fork a service from. This has effect only when a new service is being created.** 



``private_access``
------------------
*object*

**Allow access to selected service ports from private networks** 

``clickhouse``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to clickhouse with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

``clickhouse_https``
~~~~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to clickhouse_https with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

``clickhouse_mysql``
~~~~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to clickhouse_mysql with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access``
----------------------
*object*

**Allow access to selected service components through Privatelink** 

``clickhouse``
~~~~~~~~~~~~~~
*boolean*

**Enable clickhouse** 

``clickhouse_https``
~~~~~~~~~~~~~~~~~~~~
*boolean*

**Enable clickhouse_https** 

``clickhouse_mysql``
~~~~~~~~~~~~~~~~~~~~
*boolean*

**Enable clickhouse_mysql** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Enable prometheus** 



``public_access``
-----------------
*object*

**Allow access to selected service ports from the public Internet** 

``clickhouse``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to clickhouse from the public internet for service nodes that are in a project VPC or another type of private network** 

``clickhouse_https``
~~~~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to clickhouse_https from the public internet for service nodes that are in a project VPC or another type of private network** 

``clickhouse_mysql``
~~~~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to clickhouse_mysql from the public internet for service nodes that are in a project VPC or another type of private network** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** 



``service_to_fork_from``
------------------------
*['string', 'null']*

**Name of another service to fork from. This has effect only when a new service is being created.** 



