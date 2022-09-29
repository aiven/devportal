Benchmark performance
=====================

Redis®* ``memtier_benchmark*`` is a command line utility developed by Redis Labs for load generation and performing benchmark NoSQL key-value databases. It is recommended for performing benchmark of Aiven for Redis®* services.

.. Warning::
    ``redis-benchmark`` is not supported to work with Aiven services, since ``CONFIG`` command is not allowed to run.
    
Prerequisites
-------------
* An Aiven for Redis service running.
* ``memtier_benchmark`` installed. To install the tool, first download the source code from `GitHub <https://github.com/RedisLabs/memtier_benchmark>`_, and follow the instructions in the `README <https://github.com/RedisLabs/memtier_benchmark/blob/master/README.md>`_ to install all the dependencies, then build and install the tool. Now it's ready to go.

.. Note::
    The ``Testing`` section in `README <https://github.com/RedisLabs/memtier_benchmark/blob/master/README.md>`_ is not mandatory, can be skipped.

Running benchmark
-----------------
Before using ``memtier_benchmark``, read the help from :code:`mentier_benchmark -h` or this `Redis article <https://redis.com/blog/memtier_benchmark-a-high-throughput-benchmarking-tool-for-redis-memcached/>`_ to understand what the tool can offer.

The following variables need to be substituted when running the commands. You can find the information in the **Overview** tab of your Aiven for Redis service.

.. list-table::
  :header-rows: 1
  :widths: 15 60
  :align: left

  * - Variable
    - Description
  * - ``USERNAME``
    - User name of Aiven for Redis connection
  * - ``PASSWORD``
    - Password of Aiven for Redis connection
  * - ``HOST``
    - Hostname for Redis connection
  * - ``PORT``
    - Port for Redis connection
    
Below is a sample command from the `Redis blog <https://redis.com/blog/benchmark-shared-vs-dedicated-redis-instances/>`_. Each run of the benchmarking tool consists of executing ``10000 (-n 10000)`` SET & GET operations with ``1:1 ratio (--ratio 1:1)`` by launching ``4 threads (-t 4)`` and each thread opening ``25 connections (-c 25)``.  The tool does ``10 iterations (-x 10)`` of each run to collect meaningful aggregate averages.

.. Code::

    memtier_benchmark -a 'USERNAME:PASSWORD' -s 'HOST' -p 'PORT' --tls --tls-skip-verify -t 4 -n 10000 --ratio 1:1 -c 25 -x 10 -d 100 --key-pattern S:S

Below is the output of the sample command above. This example demonstrates what performance data ``memtier_benchmark`` can collect. The beginning sections are the data of the ``10`` runs executed. The following sections present, among the 10 runs, the ``BEST RUN``, ``WORST RUN`` and ``AGGREGATED AVERAGE`` results as well as the ``Request Latency Distribution`` of the operations. 

.. Code:: 

    Writing results to stdout
    [RUN #1] Preparing benchmark client...
    [RUN #1] Launching threads now...
    [RUN #1 100%, 216 secs]  0 threads:     1000000 ops,    1996 (avg:    4621) ops/sec, 277.88KB/sec (avg: 642.15KB/sec), 50.54 (avg: 21.63) msec latency

    <<<< many lines for RUN #2 to RUN #9

    [RUN #10] Preparing benchmark client...
    [RUN #10] Launching threads now...
    [RUN #10 100%, 224 secs]  0 threads:     1000000 ops,    4116 (avg:    4444) ops/sec, 572.83KB/sec (avg: 617.53KB/sec), 24.40 (avg: 22.49) msec latency
    
    4         Threads
    25        Connections per thread
    10000     Requests per client
    
    
    BEST RUN RESULTS
    ============================================================================================================================
    Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 
    ----------------------------------------------------------------------------------------------------------------------------
    Sets         2404.11          ---          ---        21.62541        20.60700        48.89500       112.63900       339.90 
    Gets         2404.11      2404.11         0.00        21.62707        20.60700        49.15100       105.98300       328.16 
    Waits           0.00          ---          ---             ---             ---             ---             ---          --- 
    Totals       4808.23      2404.11         0.00        21.62624        20.60700        49.15100       111.10300       668.06 
    
    Request Latency Distribution
    Type     <= msec         Percent
    ------------------------------------------------------------------------
    SET      11.327        0.000
    <<<< many lines 
    GET      66.559      100.000
    ---
    WAIT      0.000      100.000

    WORST RUN RESULTS
    ============================================================================================================================
    Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 
    ----------------------------------------------------------------------------------------------------------------------------
    Sets         2249.10          ---          ---        22.94219        21.63100        47.87100       109.56700       317.98 
    Gets         2249.10      2249.10         0.00        22.94561        21.63100        47.87100       109.05500       307.00 
    Waits           0.00          ---          ---             ---             ---             ---             ---          --- 
    Totals       4498.20      2249.10         0.00        22.94390        21.63100        47.87100       109.56700       624.99 

    Request Latency Distribution
    Type     <= msec         Percent
    ------------------------------------------------------------------------
    SET      10.047        0.000
    <<<< many lines
    GET     191.487      100.000
    ---
    WAIT      0.000      100.000

    AGGREGATED AVERAGE RESULTS (10 runs)
    ============================================================================================================================
    Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 
    ----------------------------------------------------------------------------------------------------------------------------
    Sets         2312.01          ---          ---        22.42681        21.24700        47.35900       101.88700       326.88 
    Gets         2312.01      2312.01         0.00        22.42914        21.24700        47.35900       101.88700       315.59 
    Waits           0.00          ---          ---             ---             ---             ---             ---          --- 
    Totals       4624.02      2312.01         0.00        22.42798        21.24700        47.35900       101.88700       642.47 

    Request Latency Distribution
    Type     <= msec         Percent
    ------------------------------------------------------------------------
    SET       9.791        0.000
    <<<< many lines
    GET     712.703      100.000
    ---
    WAIT      0.000      100.000

Running the same command on different Redis services or on the same service in different conditions can effectively benchmark the performance.

.. Note::
    Aiven has ``rate limit`` on services. By default it's ``300`` new connections per second per CPU core. Also be aware of the connection limit depending on memory size as explained in `Estimate maximum number of connection <https://docs.aiven.io/docs/products/redis/howto/estimate-max-number-of-connections.html>`_.
