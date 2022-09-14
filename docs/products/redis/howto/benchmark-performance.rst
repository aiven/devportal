Benchmark performance
=====================

Redis®* **memtier_benchmark** is a command line utility developed by Redis Labs (formerly Garantia Data Ltd.) for load generation and bechmarking NoSQL key-value databases. It is recommended for the performance benchmarking of Aiven Redis®* services.

.. Warning::
    ``redis-benchmark`` is not supported to work with Aiven services, since ``CONFIG`` command is not allowed to run.
    
To set up memtier_benchmark, first download the source code from `github <https://github.com/RedisLabs/memtier_benchmark>`_, and follow the instructions in ``README`` to install all the dependencies, then build and install the tool. Now it's ready to go.

.. Note::
    The ``Testing`` section in ``README`` is not mandatry, can be skipped.

Before using the tool, go through the help or refer to this `Redis article <https://redis.com/blog/memtier_benchmark-a-high-throughput-benchmarking-tool-for-redis-memcached/>`_ to understand what the tool can offer.::

    mentier_benchmark -h

Below is a sample command from the `Redis blog <https://redis.com/blog/benchmark-shared-vs-dedicated-redis-instances/>`_. Each run of the benchmarking tool consists of executing ``10000 (-n 10000)`` SET & GET operations ``(1:1 ratio)`` by launching ``4 threads (-t 4)`` and each thread opening ``25 connections (-c 25)``.  The tool does ``10 iterations (-x 10)`` of each run to collect meaningful aggregate averages. ::

    $ memtier_benchmark -a "<uesrname>:<password>" -s "<hostname>" -p <port>> --tls --tls-skip-verify -t 4 -n 10000 --ratio 1:1 -c 25 -x 10 -d 100 --key-pattern S:S

.. Note::
    Aivens has ``rate limit`` on services. By default it's ``300`` new connections per second per CPU core. Also be aware of the connection limit depending on memory size as explained in `Estimate maximum number of connection <https://docs.aiven.io/docs/products/redis/howto/estimate-max-number-of-connections.html>`_.
