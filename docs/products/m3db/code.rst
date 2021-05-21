Code Samples
============

In this section we have collected some code samples to get you started with M3DB in your own projects. If there's an example you'd find useful that isn't here, please `open an issue <https://github.com/aiven/devportal>`_ and let us know?

Write Data to M3DB with Python
------------------------------

This example writes some data to an M3DB service from Python, making use of the InfluxDB library.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

=================       =======================================================
Variable                Description
=================       =======================================================
``SERVICE_HOST``        Service hostname, found on the service overview page
``SERVICE_PORT``        Service port number, found on the service overview page
``AVNADMIN_PASS``       Password for the ``avnadmin`` user
=================       =======================================================

Pre-requisites
''''''''''''''

For this example you will need:

1. Python 3.6 or later
 
2. The Python InfluxDB library. You can install this with ``pip``::

    pip install influxdb





