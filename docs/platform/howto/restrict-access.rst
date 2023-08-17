Restrict network access to services
====================================

By default, Aiven services are publicly accessible, but you can restrict access to your service to a single IP, an address block, or any combination of both.

.. important::

     IP filters apply to publicly-accessible endpoints only.

1. Log in to `Aiven Console <https://console.aiven.io>`_.
2. On the **Services** page, select the service you want to restrict.
3. On the **Overview** page of your service, scroll down to **Allowed IP addresses**, and select **Change**. 
4. In the **Allowed inbound IP addresses** window, enter your address or address block using the CIDR notation, and select the **+** icon to add it to the list of the trusted IP addresses.

   .. note::
   
      You can add multiple addresses or address blocks or combination of both at once.

5. Select **Close**.

.. topic:: Result

    Now your service can be accessed from the specified IP addresses only.

.. topic:: Alternative method

   You can also use the :ref:`dedicated service update function <avn-cli-service-update>` to create or update the IP filter for your service via the :doc:`Aiven CLI </docs/tools/cli>`.

.. seealso::

   For more ways of securing your service, check information on Virtual Private Cloud (VPC) in :ref:`Networking with VPC peering <networking-with-vpc-peering>` and :ref:`Configure VPC peering <platform_howto_setup_vpc_peering>`.
