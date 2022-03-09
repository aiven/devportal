Static IP addresses
===================

.. Note:: Each static IP addresses has an hourly price ranging from $0.025 to $0.075 depending on region. The feature is recent and Aiven's**\ `pricing page <https://aiven.io/pricing>`__\ **doesn't include static IPs yet.**

By default an Aiven service will use public IP addresses allocated from
the cloud provider's shared pool of addresses for the cloud region. As a
result, Aiven service nodes effectively get a random IP address. Since
the addresses are shared with all other users of the cloud region, it's
not feasible to create firewall rules to limit access to/from nodes
using public IP addresses as the firewall would need granting access to
other users in the cloud region's for the entire IP range.

You can however create IP addresses to your project. These addresses
have a static IP for the lifetime of the address resource, and makes the
addresses predictable for firewall rules. After creating the address it
can be associated with an Aiven service. Once enough IP addresses have
been associated with a service, you can turn on static IP use on the
service.

.. _platform_howto_setup_static_ip:

Reserve static IP addresses
---------------------------
**Calculate the number of static IP addresses needed**

| Start by creating IP addresses into the cloud region you intend to use
  them for a service. The amount of IP addresses depends on the service
  plan. You'll need 2x the number of IP addresses compared to the amount
  of nodes in the plan. We request a number of static IPs two times the 
  amount of the cluster nodes, since it guarantees upgrades and failovers 
  to be handled using only static IP addresses and not relying on random ones
  can be handled without using non-static IP addresses. However no more
  than 6 additional addresses will be used, so for example a 3 node plan
  will need 2 \* 3 = 6 static IPs, but a 9 node plan will need 9 + 6 =
  15 static IPs.
| Static IPs are created to your project with

::

   avn static-ip create --cloud azure-westeurope

.. code:: text

   CLOUD_NAME        IP_ADDRESS  SERVICE_NAME  STATE     STATIC_IP_ADDRESS_ID
   ================  ==========  ============  ========  ====================
   azure-westeurope  null        null          creating  ip359373e5e56

When the IP address has been provisioned, the state turns to ``created``
and there the allocated IP address is visible:

::

   avn static-ip list

.. code:: text


   CLOUD_NAME        IP_ADDRESS     SERVICE_NAME  STATE    STATIC_IP_ADDRESS_ID
   ================  =============  ============  =======  ====================
   azure-westeurope  13.81.29.69    null          created  ip359373e5e56
   azure-westeurope  13.93.221.175  null          created  ip358375b2765

``created`` IP address can be associated with a service. These makes the
addresses eligible for use for the service, but only after the static IP
feature has been enabled on the service.

::

   avn static-ip associate --service my-static-pg ip359373e5e56
   avn static-ip associate --service my-static-pg ip358375b2765

Enable static IPs for the service by setting the ``static_ips`` user
configuration option:

::

   avn service update -c static_ips=true my-static-pg

Note that this leads to a rolling forward replacement of service nodes,
similar to applying a maintenance upgrade. The new nodes will use the
static IPs associated with the service

::

   avn static-ip list

.. code:: text

   CLOUD_NAME        IP_ADDRESS     SERVICE_NAME  STATE      STATIC_IP_ADDRESS_ID
   ================  =============  ============  =========  ====================
   azure-westeurope  13.81.29.69    my-static-pg  assigned   ip359373e5e56
   azure-westeurope  13.93.221.175  my-static-pg  available  ip358375b2765

.. _platform_howto_setup_static_ip:

Removing static IPs
-------------------

Static IP addresses are removed by first dissociating them from a
service. This returns them back to the ``created`` state to either be
associated with another service, or deleted.

::

   avn static-ip dissociate ip358375b2765
   avn static-ip list

.. code:: text

   CLOUD_NAME        IP_ADDRESS     SERVICE_NAME  STATE     STATIC_IP_ADDRESS_ID
   ================  =============  ============  ========  ====================
   azure-westeurope  13.81.29.69    my-static-pg  assigned  ip359373e5e56
   azure-westeurope  13.93.221.175  null          created   ip358375b2765

To delete a static IP:

::

   avn static-ip delete ip358375b2765
