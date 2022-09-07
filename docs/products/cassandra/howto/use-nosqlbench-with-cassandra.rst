Stress test Aiven for Apache Cassandra® using nosqlbench
========================================================

Downloading and installing nosqlbench
-------------------------------------

`Nosqlbench <https://docs.nosqlbench.io/>`_ was originally developed by
Datastax and then open sourced into an independent project. It is a
great tool to stress-test and benchmark several SQL and NOSQL databases
including Cassandra, MongoDB and PostgreSQL®.

To download the latest release, search for "latest" in `nosqlbench GitHub repository <https://github.com/nosqlbench/nosqlbench/releases/latest>`_.
Nosqlbench can be downloaded as a Linux binary executable called ``nb``. The ``nb`` executable is built with all java libraries and includes a number of sample scenarios ready to be run.

Prerequisites
-------------

ADD STUFF HERE

Running a nosqlbench scenario against your Aiven for Apache Cassandra® service
------------------------------------------------------------------------------

Without getting into the details of the `nosqlbench core concepts <https://docs.nosqlbench.io/docs/nosqlbench/core-concepts/>`_, 
we want to provide you with a number of command lines to start using nosqlbench effectively with Aiven.

Preparing to use authentication and SSL
---------------------------------------

In Aiven console, select your Cassandra service and download the SSL certificate to a 
file on your linux computer where you have installed the ``nb`` executable. We will assume the certificate has been  saved 
in a file called ``ca_cassandra.pem``, in the same directory of the ``nb`` executable.

The second thing to do is to create an environment variable called ``AVNADMPWD`` with the ``avnadmin`` password that can be found in the details 
of the Cassandra service in the Aiven console. 
This can be done by adding this line in the ``.bashrc`` file::

   export AVNADMPWD=avnadmin-password

Once you have saved and sourced the ``.bashrc`` file, you can run this ``nb`` command line to create a sample schema and load data::

   ./nb run driver=cql workload=cql-keyvalue username=avnadmin password=$AVNADMPWD ssl=openssl certFilePath=~/ca_cassandra.pem tags=phase:schema cycles=100k --progress console:1s host=cassandra-f5c27ca-demo.aivencloud.com port=20341

where ``driver`` specifies the type of client you are going to use, in our case it's ``cql``
the ``workload``option calls a specific workload file that is compiled
inside the ``nb`` executable and instructs ``nb`` to generate key/value
pairs for a table called ``baselines.keyvalue``. 
The ``phase`` option refers to a specific point in the **workload** definition file and specifies 
the particular **activity** to run. In our case, the phase is ``schema`` which means that the nosqlbench will create the schema of the Cassandra keyspace.

In order to run client connections and generate actual data in the keyspace and tables created, these command lines need to be run::

    ./nb run driver=cql workload=cql-keyvalue username=avnadmin password=$AVNADMPWD ssl=openssl certFilePath=~/ca_cassandra.pem tags=phase:rampup cycles=100k --progress console:1s host=cassandra-f5c27ca-demo.aivencloud.com port=20341
    
or::

    ./nb run driver=cql workload=cql-keyvalue username=avnadmin password=$AVNADMPWD ssl=openssl certFilePath=~/ca_cassandra.pem tags=phase:main cycles=100k --progress console:1s host=cassandra-f5c27ca-demo.aivencloud.com port=20341

where the phases ``rampup`` or ``main`` identify other activities that are defined in the ``cql-keyvalue`` workload file.


To understand how the ``cql-keyvalue`` workload functions, it will help to have a look at the workload definition file for the key-value example.
First of all you can list all the precompiled workloads::

   ./nb --list-workloads

The above command will generate a list like the following::

    # An IOT workload with more optimal settings for DSE
    /activities/baselines/cql-iot-dse.yaml
    
    # Time-series data model and access patterns
    /activities/baselines/cql-iot.yaml
    
    # A workload with only text keys and text values
    /activities/baselines/cql-keyvalue.yaml

    ...

To dump and edit the particular workload file locally on disk, you can use this command line:

::

   ./nb --copy cql-keyvalue

this command will generate the file called ``cql-keyvalue.yaml`` which
contatins the specifications for the keyvalue workload.

Other useful ``nb`` commands
----------------------------

For a list of all the pre-compiled scenarios:

::

   ./nb --list-scenarios

This command line is similar to the one used to load the data but is
using ``threads`` option to parallelise at the client side:

::

   ./nb run driver=cql workload=cql-keyvalue username=avnadmin password=$AVNADMPWD ssl=openssl certFilePath=~/ca_cassandra.pem tags=phase:main cycles=100k threads=50 --progress console:1s host=cassandra-f5c27ca-demo.aivencloud.com port=20341


Check that data has been loaded
-------------------------------

Use this command line to check if the sample data has been loaded into the tables:

::

   SSL_CERTFILE=ca_cassandra-123.pem cqlsh --ssl -u avnadmin -p $AVNADMPWD cassandra-f5c27ca-demo.aivencloud.com 20341

which will open a cqlsh prompt to run queries on the Cassandra db.

Another way to check that data has been loaded correctly is to count
records in the table. Now, in a distributed db like Cassandra, counting
is not the most straightforward things because depending on the
consistency level of the request, different results may be obtained.
DSBULK an open source loading, unloading and counting tool for Cassandra,
allows for configurable consistency level and provides reliable and fast
counting capabilities.