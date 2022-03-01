Write data to M3DB with Python
------------------------------

This example writes some data to an M3DB service from Python, making use of the InfluxDB® library.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

=================       =======================================================
Variable                Description
=================       =======================================================
``SERVICE_HOST``        Service hostname, found on the service overview page
``SERVICE_PORT``        Service port number, found on the service overview page
``AVNADMIN_PASS``       Password for the default ``avnadmin`` user
=================       =======================================================

Pre-requisites
''''''''''''''

For this example you will need:

1. Python 3.6 or later

2. The Python InfluxDB library. You can install this with ``pip``::

    pip install influxdb

.. note::

    M3DB supports InfluxDB (v1) protocol so we can use the existing library for this database too.

Code
''''

Add the following to ``main.py`` and replace the placeholders with values for your project:

.. literalinclude:: /code/products/m3db/write.py


This code creates an InfluxDBClient and connects to the InfluxDB-literate endpoint on the M3DB. Then the code constructs the expected data format, and writes it to the client.

To run the code::

    python main.py

If the script outputs ``True`` then there is data in your M3DB. If you'd like to you can take a look at :doc:`grafana` to see how to inspect your data with Grafana®.
