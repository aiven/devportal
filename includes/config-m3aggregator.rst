
``custom_domain``
-----------------
*['string', 'null']*

**Custom domain** Serve the web frontend using a custom CNAME pointing to the Aiven DNS name



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



``m3_version``
--------------
*['string', 'null']*

**M3 major version (deprecated, use m3aggregator_version)** 



``m3aggregator_version``
------------------------
*['string', 'null']*

**M3 major version (the minimum compatible version)** 



