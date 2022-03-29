Static IP addresses
===================

Aiven services are normally addressed by their hostname. There are some
situations however where static IP addresses may be needed for your platform,
and so these are also available for a small additional charge.

Some common use cases for needing a static IP address might include:
* firewall rules for specific IP addresses
* tools, such as some proxies, that use IP addresses rather than hostnames

Static IP addresses on the Aiven platform
-----------------------------------------

Static IP addresses are created in a specific cloud and belong to a specific project. During their lifecycle, the IP addresses can be in a number of states, and move between states by being created/deleted, by being associated with a service, or when the service is reconfigured to use the static IP addresses. This is summarised in the diagram below:

.. mermaid::

    graph LR;

        none[Static IP does not exist]
        created[State: created]
        available[State: available]
        assigned[State: assigned]

        none -- create IP --> created
        created -- associate --> available
        available -- reconfigure service --> assigned
        assigned -- reconfigure service --> available
        available -- dissociate --> created
        created -- delete IP --> none

To create, delete, associate or dissociate IPs, use the :doc:`/docs/tools/cli` tool. To reconfigure a service, set its `static_ips` configuration value to true to use static IPs, or false to stop using them.

.. note:: The ``static_ip`` configuration can only be enabled when enough static IP addresses have been created *and associated* with the service.

For more information, read the step-by-step process :doc:`../howto/static-ip-addresses`
