Stress test Aiven for Apache Cassandra® using nosqlbench
========================================================

`Nosqlbench <https://docs.nosqlbench.io/>`_ was originally developed by
Datastax and then open sourced into an independent project. It is a
great tool to stress-test and benchmark several SQL and NOSQL databases
including Cassandra and PostgreSQL®.

Download and install nosqlbench
-------------------------------------

To download the latest release, search for "latest" in `nosqlbench GitHub repository <https://github.com/nosqlbench/nosqlbench/releases/latest>`_.
Nosqlbench can be downloaded as a Linux binary executable called ``nb``. The ``nb`` executable is built with all java libraries and includes a number of sample scenarios ready to be run.

Prerequisites
-------------

In Aiven console, select your Cassandra service and download the SSL certificate to a 
file on the same linux computer where you have installed the ``nb`` executable. We will assume the certificate has been  saved 
in a file called ``ca_cassandra.pem``, in the same directory of the ``nb`` executable.

The second thing to do is to create an environment variable called ``AVNADMPWD`` with the password of Aiven user ``avnadmin``. 
This password can be copied from the Cassandra service details in the Aiven console  

In order to store this password securely, add this line in the ``.bashrc`` file in the home of the user running the ``nb`` command line::

   export AVNADMPWD=avnadmin-password

Save and source the ``.bashrc`` file.

Run a nosqlbench scenario against your Aiven for Apache Cassandra® service
------------------------------------------------------------------------------

Getting into the details of the `nosqlbench core concepts <https://docs.nosqlbench.io/docs/nosqlbench/core-concepts/>`_ is beyond the scope of this article.
However the successful student will find the core concepts extemely useful to understand how ``nb`` works internally.
The scope of this article is to provide you with a number of command lines to start using nosqlbench effectively with Aiven.


This ``nb`` command line creates a sample schema and loads data in the new table (called ``baselines.keyvalue``)::

   ./nb run \
   driver=cql \
   workload=cql-keyvalue \
   username=avnadmin \
   password=$AVNADMPWD \
   ssl=openssl \
   certFilePath=~/ca_cassandra.pem \
   tags=phase:schema \
   cycles=100k \
   --progress console:1s \
   host=cassandra-f5c27ca-demo.aivencloud.com port=20341

- where ``driver`` specifies the type of client you are going to use, in our case it's ``cql``
- the ``workload``option calls a specific workload file that is compiled inside the ``nb`` executable and instructs ``nb`` to generate key/value pairs for a table called ``baselines.keyvalue``. 
- The ``phase`` option refers to a specific point in the **workload** definition file and specifies the particular **activity** to run. In our case, the phase is ``schema`` which means that the nosqlbench will create the schema of the Cassandra keyspace.

In order to run client connections and generate actual data in the keyspace and tables created, these command lines need to be run::

    ./nb run \
    driver=cql \
    workload=cql-keyvalue \
    username=avnadmin \
    password=$AVNADMPWD \
    ssl=openssl \
    certFilePath=~/ca_cassandra.pem \
    tags=phase:rampup \
    cycles=100k \
    --progress console:1s \
    host=cassandra-f5c27ca-demo.aivencloud.com port=20341
    
or::

    ./nb run \
    driver=cql \
    workload=cql-keyvalue \
    username=avnadmin \
    password=$AVNADMPWD \
    ssl=openssl \
    certFilePath=~/ca_cassandra.pem \
    tags=phase:main \
    cycles=100k \
    --progress console:1s \
    host=cassandra-f5c27ca-demo.aivencloud.com port=20341

where the phases ``rampup`` or ``main`` identify other activities that are defined in the ``cql-keyvalue`` workload file.


In order to see the details of the several predefined workloads and activities, it will help to dump the workload definition to a file.
With this command line you can list all the precompiled workloads::

   ./nb --list-workloads

The above command will generate a list like this below::

    # An IOT workload with more optimal settings for DSE
    /activities/baselines/cql-iot-dse.yaml
    
    # Time-series data model and access patterns
    /activities/baselines/cql-iot.yaml
    
    # A workload with only text keys and text values
    /activities/baselines/cql-keyvalue.yaml

    ...

To dump and edit the particular workload file locally on disk, you can use this command line::

   ./nb --copy cql-keyvalue

this command will generate the file called ``cql-keyvalue.yaml`` which
contatins the specifications for the keyvalue workload.

Create your own workload
------------------------

Workload files can be modified and customised and then run with ``nb``.
The command option ``workload=cql-keyvalue`` expects the file ``cql-keyvalue.yaml`` to be in the same directory of the ``nb`` command.
If you create a new yaml file called ``my-workload.yaml`` in the same directory of ``nb`` command, the new workload can be run with this command line::

      ./nb run \
    driver=cql \
    workload=my-workload

Parallelise ``nb`` execution
----------------------------

This command line is similar to the one used to load the data but is
using ``threads`` option to parallelise at the client side::

   ./nb run \
   driver=cql \
   workload=cql-keyvalue \
   username=avnadmin \
   password=$AVNADMPWD \
   ssl=openssl \
   certFilePath=~/ca_cassandra.pem \
   tags=phase:main \
   cycles=100k \
   threads=50 \
   --progress console:1s \
   host=cassandra-f5c27ca-demo.aivencloud.com port=20341


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