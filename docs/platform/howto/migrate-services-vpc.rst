Migrate a public service to a Virtual Private Cloud (VPC)
==========================================================

If you are running your Aiven service over the public Internet, you may want to restrict access or allow connectivity between a your own Virtual Private Cloud (VPC, also known as VNet) and Aiven.

Aiven allows one click migrations between regions and cloud providers; the same is true between the public Internet and a VPC. However, the movement of your service can mean that connectivity is interrupted as the service URI will change its resolution from public IP addresses to IP addresses within a VPC.

To ensure consistent access during migration, you can use the ``public access`` advanced configuration to allow your service to be available over the public Internet as well as over a VPC.

To ensure that you are always able to connect to the service
during the migration phase, you can use a few simple
tests during the migration phase.

Overview
---------

To safely migrate Aiven services into a VPC, take the following steps:

#. Create a VPC and set up peering.

#. Validate network peering connection with the test service.

#. Enable public access on all the services to be migrated.

#. Change your application configuration to use public access hostnames.

#. Migrate the service into the VPC.

#. Validate peering connections to all private hostnames and ports.

#. Change application configuration to use private access hostnames.

#. Disable public access on all the services.

.. note::

    Steps 3, 4, 6, 7, 8 are optional but highly recommended. Following these steps ensures that networking configuration and firewall rules are set up correctly.

Initial setup
--------------

Ensure that you have the VPC created and peering is active. This is can be automated via Terraform if needed. Check out
:ref:`how to set up VPC peering <platform_howto_setup_vpc_peering>` on the Aiven platform.

In this guide, the ``google-us-east1`` VPC is used for testing. Ensure that the VPC and peering are both in an ``Active`` state.

Testing the connection
-----------------------

Check that you can connect to a non-critical service to ensure that the networks are peered. For that purpose, you can create a small service inside an existing VPC to test the network connection.

Ensure that your service is deployed into a VPC.

From a host within your own VPC, make sure that you can resolve the DNS
hostname, and connect to the service port. The following commands work
on Ubuntu 20.04 LTS and should work for most Linux distributions:

-  ``nslookup {host}``

-  ``nc -vz {host} {port}``

Enable public access
---------------------

Enable the ``public_access.{service type}`` configuration on all of your services in the
**Advanced Configuration** section (in `Aiven Console <https://console.aiven.io/>`_ > your service's **Overview** page). For example, the configuration name is ``public_access.kafka`` for Aiven for Apache Kafka®. This creates a new hostname and
port. It is still publicly available once the service is moved into the VPC.

You will now see a new hostname and port under "Connection Information"
by selecting the ``Public`` "Access Route"

Ensure that you can connect to each host/port combination.


Configure and redeploy application
-----------------------------------

It is highly recommended to configure your applications to use the
public access route during migration. This ensures access to the
services while moving into a private network. In dual access mode, you
can test all connections and ports before finally cutting over to use
the private hostname(s) and underlying private IP addresses.

Migrate Aiven service to your VPC
----------------------------------

In `Aiven Console <https://console.aiven.io/>`_, use the **Cloud and VPC** > **Migrate cloud** section on the service's **Overview** page to migrate your Aiven services into a VPC. Note the ``Public Internet`` tag.

Ensure that you select the region from the ``VPC`` tab. This is a
dedicated VPC for your project.

Ensure that you see the ``Project VPC`` tag after migration. You can
monitor the migration status on the service's page in `Aiven Console <https://console.aiven.io/>`_.

Testing the service connections
--------------------------------

After the migration, you will see some private IP addresses if you use
the ``nslookup`` command. Ensure that you can connect to the private
hostnames and ports, for example, firewall rules and routing works.

Configure and redeploy your applications
-----------------------------------------

Now you can convert your application to use the private hostname again.

Cleanup by disabling public access
-----------------------------------

Disable the ``public_access.{service type}`` configuration on all of your services in
the **Advanced configuration** section (in `Aiven Console <https://console.aiven.io/>`_ > your service's **Overview** page). This removes the ``public-`` prefixed hostname and port.

Conclusion
----------

These steps allow you to perform public => VPC service migrations with
zero downtime in a safe manner by testing connections every step of the
way. As always, ensure that your client applications have failure and
retry logic as the underlying servers and IP addresses change. This is usually
not an issue in clustered services, for example, Apache Kafka® and OpenSearch®, but
might require additional configuration for services like PostgreSQL® and Redis®*.
