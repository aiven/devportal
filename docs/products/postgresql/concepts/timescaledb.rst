About TimescaleDB
=================

`TimescaleDB <https://github.com/timescale/timescaledb>`_ is an open-source database designed to make your existing relational database scalable for time series data. TimescaleDB is available as a PostgreSQL® extension on Aiven.

A time series indexes a series of data points in chronological order, usually as a sequence over regular intervals. Examples of a time series include:

* the temperature of a home during a day
* the position of a satellite during a day

The data in these examples consists of a measured value (temperature or position) corresponding to the time at which the reading of the value took place. 

Enable TimescaleDB on Aiven for PostgreSQL
------------------------------------------

TimescaleDB is available as an extension; you can enable it by running::

     CREATE EXTENSION timescaledb CASCADE;

After enabling the extension, you can create TimescaleDB hypertables and make use of its features for working with time-series data.
For further information, have a look at the `Getting Started <https://docs.timescale.com/timescaledb/latest/getting-started/create-hypertable/>`_ guide from Timescale.

More information about :doc:`how to install and manage extensions <../howto/manage-extensions>` is also available.

TSL-licensed features
---------------------

The majority of TimescaleDB functionality is open source, however since TimescaleDB 1.2.0 some features have been restricted to the Timescale License, which explicitly prohibits them from being made available in any database-as-a-service offering. Therefore some features, such as ``time_bucket_gapfill``, are not available on the Aiven hosted TimescaleDB service.

When you try using these features, you will see an error similar to the following:

``ERROR 0A000 (feature_not_supported) function "<function>" is not supported under the current license "ApacheOnly"``

Since Aiven only offers open source licensed platforms, these features cannot be made available.
