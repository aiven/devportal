Connect with Python
-------------------

This example connects to an Aiven for Apache Cassandra® service from Python as the ``avnadmin`` user by making use of the ``cassandra-driver`` library. 

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      ================================================================================
Variable                Description
==================      ================================================================================
``HOST``                Host name of your Cassandra service 
``PORT``                Port number used for connecting to your Cassandra service 
``USER``                Username used for connecting to your Cassandra service. Defaults to ``avnadmin`` 
``PASSWORD``            Password of the ``avnadmin`` user
``SSL-CERTFILE``        Path to the `CA Certificate` file of your Cassandra service
==================      ================================================================================

Pre-requisites
''''''''''''''

Install the ``cassandra-driver`` library::

    pip install cassandra-driver

Code
''''
1. Create a new file named ``main.py`` and add the following content:

.. literalinclude:: /code/products/cassandra/connect.py
   :language: python

This code first creates a keyspace named ``example_keyspace`` and a table named ``example_python`` that contains an ``id`` and a ``message``. Then, it writes a new 
entry into the table with the values ``1`` and ``hello world``. Finally, it reads the entry from the table and prints it.


2. Run the program with the required flags to pass the necessary connection details:: 

    ./main.py --HOST <HOST> --PORT <PORT> --USER avnadmin --PASSWORD <PASSWORD> --SSL-CERTFILE <PATH TO CERTFILE>

