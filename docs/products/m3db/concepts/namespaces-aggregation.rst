About M3DB Namespaces and Aggregation
=====================================

M3DB has a concept of namespaces.

* there is always one unaggregated namespace

* optionally, you may configure additional aggregated namespaces.

Both the retention (how long the data is kept for) and the resolution (how detailed the data is) are measured in **short time format**. This is a number followed by a letter:

.. list-table::

    * - s
      - seconds
    * - m
      - minutes
    * - h
      - hours
    * - d
      - days

So for example to set the retention to 2 weeks, use ``14d``.

Unaggregated Namespace
----------------------

Incoming data points are written to the unaggregated namespace. It's the default table, if you like.

Aggregated Namespace
--------------------

An aggregated namespace has some data, usually downsampled to a lower resolution, and retained for a different period of time.

.. image:: /images/products/m3db/configure-namespace.png
    :alt: Namespace configuration screenshot, showing the namespace name, retention and resolution fields
