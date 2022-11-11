Default service IP address and hostname
=========================================

Default service IP address
----------------------------

When a new Aiven service is created, the chosen cloud service provider will dynamically assign one or more public IP address from their connection pool. This IP address is not permanent, and with every service maintenance (in case of failover, maintenance upgrade or cloud migration) the IP address changes since Aiven creates a new node, migrates the existing data to it and then retire the old node. 

.. Note::

    Aiven also offer the ability to define :doc:`static IP addresses </docs/platform/concepts/static-ips>` in case you need them a service. For more information about how to obtain a static IP and assign it to a particular service, please check the :doc:`related guide </docs/platform/howto/static-ip-addresses>`.

If you have your own cloud account and want to keep your Aiven services isolated from the public internet, you can however create a VPC and a peering connection to your own cloud account. For more information on how to setup the VPC peering, check `the related article <https://docs.aiven.io/docs/platform/howto/manage-vpc-peering>`_.

Default service hostname
------------------------

When a new service is being provisioned, its hostname is defined as follows::

<SERVICE_NAME>-<PROJECT_NAME>.aivencloud.com


where:

* ``<SERVICE_NAME>`` is the name of the service
* ``<PROJECT_NAME>`` is the name of the project

.. Note::

    If the ``<SERVICE_NAME>`` is too short or was recently used (e.g. if you drop and recreate a service with the same name) then the hostname format could be ``<SERVICE_NAME><3RANDOMLETTERS>-<PROJECT_NAME>.aivencloud.com``
