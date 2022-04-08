Calculate the maximum number of connections for MySQL
=====================================================

The number of simultaneous connections in Aiven for MySQL depends on the usable memory on the server. The usable memory is the total memory on the node minus the operating system and management overhead. This overhead is currently estimated as 350 MiB (≈ 0.34 GiB). 

It can be estimated as:

.. math::

    {usable\_memory} = {total\_memory\_on\_the\_node - management\_overhead} 

To calculate the maximum number of connections, we need to check the value of the usable memory. For this estimation, the usable memory value is **rounded down** to the nearest integer value of GiB. 

**For plans under 4 GiB of usable memory**, you can estimate as

.. note::
    Independent of the plan, an ``extra_connection`` with a value of ``1`` will be added for the system process.

.. math::
    
   {max\_number\_of\_connections} = {75\times usable\_memory\_in\_GiB} + {extra\_connection}

So for example on a server with 3.6 GiB total memory, the rounded value of usable memory is:

.. math::

    {usable\_memory} = 3.6 - \frac{350}{1024} = 3 GiB

As result, you can calculate the maximum number of connections as:

.. math::    
    {max\_number\_of\_connections} = {75\times 3} + {1} = {226\ connections}


For plans higher or equal to 4 GiB of usable memory, the number of allowed connections increases to 100 connections per Gib. This increase is because those plans are less memory constrained compared to plans under 4 GiB of usable memory. 

**For plans higher or equal to 4 GiB**, you can estimate the maximum number of connections as:

.. math::
    
   {max\_number\_of\_connections} = 100\times usable\_mem\_in\_GiB + {extra\_connection}

As an example, if your server has 4.5 GiB total memory, the rounded value of usable memory is:

.. math::

    {usable\_memory} = 4.5 - \frac{350}{1024} = 4\ GiB

So the maximum number of connections will be:

.. math::    
    {max\_number\_of\_connections} = {100\times 4} + {1} = {401\ connections}