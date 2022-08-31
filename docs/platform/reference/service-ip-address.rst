Service IP address and DNS
==========================

When a new service is created in Aiven, a cloud service provider will dynamically assign a public IP address from their connection pool. This IP address is not a permanent one, because with every service node update (failover, maintenance upgrade or cloud migration) the IP address will change as Aiven will create a new VM, migrate to it and then retire the older node. 

You can however create a VPC and create a peering connection to your own cloud account. This can be used in case you would like to limit connectivity, and keep your service instances isolated from the public-internet.  For more information, please see `Using VPC Peering <https://help.aiven.io/en/articles/778836-using-virtual-private-cloud-vpc-peering>`_ article.

When a new service is being provisioned, the host name for your service is setup as the following:

service-project.aivencloud.com

Additional articles may be found on our `Aiven Support <https://docs.aiven.io/>`_ page.

If you have any questions, please feel free to reach out to our support@Aiven.io and let us know.