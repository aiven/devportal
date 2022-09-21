Connect with ``cqlsh``
--------------------------

This example shows how to connect to an Aiven for Apache Cassandra® service using ``cqlsh``.

Pre-requisites
''''''''''''''

For this example you need to have:

1. The ``clqsh`` client installed. You can install this as part of the `Cassandra server installation <https://cassandra.apache.org/doc/latest/cassandra/getting_started/installing.html>`_.
2. Your service's **CA Certificate** downloaded and saved in your file system. 


Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``PASSWORD``            Password of the ``avnadmin`` user
``HOST``                Host name for the connection
``PORT``                Port number to use for the Cassandra service
``SSL_CERTFILE``        Path of the `CA Certificate` for the Cassandra service
==================      =============================================================

.. Tip::

    All the above variables and the CA Certificate file can be found in the `Aiven Console <https://console.aiven.io/>`_, in the service detail page.


Code
''''

Set the `SSL_CERTFILE` environment variable to the location of the *CA Certificate* for the Cassandra service:

::

    export SSL_CERTFILE=<PATH>
    
.. note::

    Alternatively, you can provide the path to the CA Certificate file in the ``[ssl]`` section by setting the the ``certfile`` parameter in ``~/.cassandra/cqlshrc``


Navigate to the directory of your local Cassandra installation and execute the following from a terminal window:

::

    ./cqlsh --ssl -u avnadmin -p <PASSWORD> <HOST> <PORT> 


You are now connected to the Cassandra database.
