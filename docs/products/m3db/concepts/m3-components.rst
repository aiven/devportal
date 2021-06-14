Aiven for M3 Components
=======================

M3 consists of three components, which at Aiven are provided as two separate services:

* **M3DB** consists of ``X`` number of M3DB + M3Coordinator pairs. Where ``X`` is the number of nodes in the Aiven plan you choose.
* **M3 Aggregator** is an optional additional component that you need if you use aggregated namespaces, the aggregator does the downsampling. Again, the plan you choose dictates how many of these you have.

Example M3 Architecture
-----------------------

An example implementation might look something like this with your application sending data to M3, and then the ability to see that data with Grafana.

.. mermaid::

    graph LR
        App(Your application) ---> M3[(M3DB + M3 Coordinator)]
        M3 ----> Gr((Grafana))
        M3 <-.-> Agg(M3 Aggregator)


Another common setup is to use `Prometheus <https://prometheus.io/>`_ with M3 as the storage element.
