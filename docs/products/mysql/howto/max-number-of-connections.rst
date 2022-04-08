Calculate the maximum number of connections for MySQL
=====================================================


The number of simultaneous connections in Aiven for MySQL depends on the usable memory on the server. The usable memory is the total memory on the node minus the operating system and management overhead. This overhead is currently estimated as 350 MiB (0.341797 GiB). 

It can be estimated as:

.. math::

    {usable\_memory} = {total\_memory\_on\_the\_node - management\_overhead} 

.. note::
    

To calculate the maximum number of connections, we need to check the value of the usable memory. The usable memory is rounded to the nearest GiB. For plans under 4 GiB of usable memory, you can estimate as:

.. math::
    
   {max\_number\_of\_connections} = usable\_memory\_in\_GiB\times 75 + {extra\_connection}


For plans higher or equal to 4 GiB of usable memory, you can calculate as:

.. math::
    
   {max\_number\_of\_connections} = usable\_memory\_in\_GiB\times 100 + {extra\_connection}

Independent of the plan, an ``extra_connection`` with a value of ``1`` will be added for the system process.
