Migrate a public service to a Virtual Private Cloud (VPC)
==========================================================

If you are running your Aiven service over the public internet, you may want to restrict access or allow connectivity between a your own Virtual Private Cloud (VPC, also known as VNet) and Aiven.

Aiven allows one click migrations between regions and cloud providers; the same is true between the public internet and a VPC. However, the movement of your service can mean that connectivity is interrupted as the service URI will change its resolution from public IP addresses to IP addresses within a VPC. 
In order to ensure consistent access during migration, we will use the ``public access`` advanced configuration to allow our service to be available over the public internet as well as over a VPC.

We want to ensure that we are always able to connect to the service
during the migration phase. We can accomplish this with a few simple
tests during the migration phase.

Overview
--------

We will complete the following steps to safely migrate Aiven services
into a VPC.

#. Create VPC and set up peering

#. Validate network peering connection with test service

#. Enable public access on all services to be migrated

#. Change your application configuration to use public access hostnames

#. Migrate service into VPC

#. Validate peering connections to all private hostnames and ports

#. Change application configuration to use private access hostnames

#. Disable public access on all services

Note that steps 3, 4, 6, 7, 8 are optional but highly recommended.
Following these steps ensures that networking configuration and
firewall rules are set up correctly.

#. Initial setup
---------------------

Ensure that you have the VPC created and peering is active. This is
simple to do and can be automated via terraform if needed. Please check out
:ref:`how to set up VPC peering <platform_howto_setup_vpc_peering>`
on the Aiven platform.

We will be using the ``google-us-east1`` VPC for testing. Ensure that the
VPC and peering are both in an ``Active`` state.

#. Testing the connection
------------------------------

First we want to ensure that we can connect to with a non-critical
service to ensure that the networks are peered. In this case, I am going
to create a small service inside an existing VPC to test the network
connection.

Ensure that your service is deployed into a VPC.

From a host within your own VPC, we want to make sure that we can resolve the DNS
hostname, and connect to the service port. The following commands work
on Ubuntu 20.04 LTS and should work for most Linux distributions.

-  ``nslookup {host}``

-  ``nc -vz {host} {port}``

#. Enable public access
----------------------------

Enable the ``public_access.{service type}`` configuration on all of your services in the
"Advanced Configuration" section. For example, the configuration name is ``public_access.kafka`` for Aiven for Apache Kafka®. This will create a new hostname and
port. It will still be publicly available once the service is moved into the VPC.

You will now see a new hostname and port under "Connection Information"
by selecting the ``Public`` "Access Route"

Ensure that you can connect to each host/port combination.


#. Configure and redeploy application
------------------------------------------

It is highly recommended to configure your applications to use the
public access route during migration. This ensures access to the
services while moving into a private network. In dual access mode, you
can test all connections and ports before finally cutting over to use
the private hostname(s) and underlying private IP addresses.

#. Migrate Aiven service to your VPC
------------------------------------------

Use the "Cloud and VPC" section on the service overview to migrate your
Aiven services into a VPC. Note the ``Public Internet`` tag.

Ensure that you select the region from the ``VPC`` tab. This is a
dedicated VPC for your project.

Ensure that you see the ``Project VPC`` tag after migration. You can
monitor the migration status on the service details page.

#. Testing the service connections
---------------------------------------

After the migration, you will see some private IP addresses if you use
the ``nslookup`` command. Ensure that you can connect to the private
hostnames and ports, i.e. firewall rules and routing works.

#. Configure and redeploy your application(s)
--------------------------------------------------

Now you can convert your application to use the private hostname again.

#. Cleanup by disabling public access
-------------------------------------------

Disable the ``public_access.{service type}`` configuration on all of your services in
the "Advanced Configuration" section. This will remove the ``public-``
prefixed hostname and port.

Conclusion
----------

These steps allow you to perform public => VPC service migrations with
zero downtime in a safe manner by testing connections every step of the
way. As always, ensure that your client applications have failure and
retry logic as the underlying servers and IP addresses change. This is usually
not an issue in clustered services, e.g. Apache Kafka® and OpenSearch®, but
might require additional configuration for services like PostgreSQL® and Redis®*.
