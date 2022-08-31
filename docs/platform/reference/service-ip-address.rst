Default service IP address and hostname
=======================================

When a new service is created in Aiven, a cloud service provider will dynamically assign a public IP address from their connection pool. This IP address is not a permanent one, because with every service node update (failover, maintenance upgrade or cloud migration) the IP address will change as Aiven will create a new VM, migrate to it and then retire the older node. 

You can however create a VPC and create a peering connection to your own cloud account. This can be used in case you would like to limit connectivity, and keep your service instances isolated from the public-internet.  For more information, please see `Using VPC Peering <https://help.aiven.io/en/articles/778836-using-virtual-private-cloud-vpc-peering>`_ article.

Aiven also offer `static IP <https://docs.aiven.io/docs/platform/concepts/static-ips.html>`_ addresses should you need them for your service. For more information, please use `How to obtain Static IP <https://docs.aiven.io/docs/platform/howto/static-ip-addresses.html>`_ article.

When a new service is being provisioned, the host name for your service is setup as the following:
**<SERVICE_NAME>-<PROJECT_NAME>.aivencloud.com**
where ``<SERVICE_NAME>`` is the name of the service and ``<PROJECT_NAME>`` the one of the project

If the ``<SERVICE_NAME>`` is too short or was recently used (e.g. if you drop and recreate a service with the same name) then the format could be **<SERVICE_NAME><3RANDOMLETTERS>-<PROJECT_NAME>.aivencloud.com**