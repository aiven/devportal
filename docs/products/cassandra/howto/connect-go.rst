Connect with Go
---------------

This example connects to an Aiven for Apache Cassandra® service from Go as the ``avnadmin`` user by making use of the ``gocql`` library. 

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

Get the ``gocql`` library::

    go get github.com/gocql/gocql

Code
''''

1. Create a new file named ``main.go`` and add the following content:

.. literalinclude:: /code/products/cassandra/connect.go
   :language: go

This code first creates a keyspace named ``example_keyspace`` and a table named ``example_go`` that contains an ``id`` and a ``message``. Then, it writes a new 
entry into the table with the values ``1`` and ``hello world``. Finally, it reads the entry from the table and prints it.

2. Execute the following from a terminal window to build an executable:: 

    go build main.go

3. Run the program with the required flags to pass the necessary connection details:: 

    ./main --host <HOST> --port <PORT> --user avnadmin --password <PASSWORD> --ssl-certfile <PATH TO CERTFILE>

