..
  Platform Variables
.. |failover_primary| replace:: 60 seconds
.. |service_memory_limit| replace:: :math:`{ .80 }`
.. |service_memory| replace:: :math:`{ (RAM - overhead) \times }` |service_memory_limit|

..
  Memory Variables
.. |vm_overhead| replace:: 350 MiB (≈ 0.34 GiB)
.. |vm_fractional_overhead| replace:: :math:`\frac{350}{1024}`
.. |vm_usable_memory| replace:: :math:`{ RAM - overhead }`

..
  MySQL Variables
.. |mysql_max_connections| replace:: :math:`{\times ⌊usable\_memory⌋ } + { extra\_connection }`
.. |mysql_max_concurrency| replace:: :math:`({ service\_memory - global\_buffers })  / { thread\_buffers }`
.. |mysql_connections_per_<4G| replace:: :math:`{75}`
.. |mysql_connections_per_>4G| replace:: :math:`{100}`

.. 
  Postgres Variables
.. |pg_max_connections| replace:: \max({ RAM * 25 }, 1000)