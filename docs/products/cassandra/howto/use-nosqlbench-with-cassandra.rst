Perform a stress test using nosqlbench
========================================================

`Nosqlbench <https://docs.nosqlbench.io/>`_ is an open source project that can be used to stress-test and benchmark several SQL and NOSQL databases including Cassandra® and PostgreSQL®.

Prerequisites
-------------

To download the latest nosqlbench release, search for "latest" in `nosqlbench GitHub repository <https://github.com/nosqlbench/nosqlbench/releases/latest>`_.
Nosqlbench can be downloaded as a Linux binary executable called ``nb``. The ``nb`` executable is built with all java libraries and includes a number of sample scenarios ready to be run.

.. Tip::

   You can read more about the nosqlbench core concepts and parameters in the `dedicated documentation <https://docs.nosqlbench.io/docs/nosqlbench/core-concepts/>`_

Variables
-------------

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

Run nosqlbench against your Aiven for Apache Cassandra® service
---------------------------------------------------------------

The following sections shows how to run several nosqlbench worKloads against an Aiven for Cassandra service.

Create a schema and load data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nosqlbench can be used to create a sample schema and load data.

The schema can be created with the following command, after substituting the placeholders for ``HOST``, ``PORT``, ``PASSWORD`` and ``SSL_CERTFILE``::

   ./nb run                            \
      host=HOST                        \
      port=PORT                        \
      username=avnadmin                \
      password=PASSWORD                \
      driver=cql                       \
      workload=cql-keyvalue            \
      ssl=openssl                      \
      certFilePath=SSL_CERTFILE        \
      tags=phase:schema                \
      cycles=100k                      \
      --progress console:1s
      

The following parameters are used: 

*  ``driver``: specifies the type of client you are going to use, in the example ``cql``
* ``workload``: option calls a specific workload file that is compiled inside the ``nb`` executable and instructs ``nb`` to generate key/value pairs for a table called ``baselines.keyvalue``. You can read more on how to define custom workloads in the :ref:`dedicated documentation <nosqlbench_cassandra>`
* ``phase``: refers to a specific point in the ``workload`` definition file and specifies the particular ``activity`` to run. In the example, the phase is ``schema`` which means that the nosqlbench will create the schema of the Cassandra keyspace.

To create client connections and produce data in the keyspace and tables created, you need to run the following command line, after substituting the placeholders for ``HOST``, ``PORT``, ``PASSWORD`` and ``SSL_CERTFILE``::

    ./nb run \
      host=HOST                        \
      port=PORT                        \
      username=avnadmin                \
      password=PASSWORD                \
      driver=cql                       \
      workload=cql-keyvalue            \
      ssl=openssl                      \
      certFilePath=SSL_CERTFILE        \
      tags=phase:rampup                \
      cycles=100k                      \
      threads=50                       \
      --progress console:1s

.. Note::

   You can also run a command replacing the phase ``rampup`` with ``main`` to execute other activities defined in the ``cql-keyvalue`` workload file.

The ``threads`` parameter, specifies the number of concurrent threads used to load the data.

Customise nosqlbench workflows
------------------------------

Nosqlbench uses workflows to define the load activity. You can define your own workflow to satisfy specific loading/benchmarking needs.

Check the workflow details
~~~~~~~~~~~~~~~~~~~~~~~~~~

To check the details of the several predefined workloads and activities, you can dump the definition to a file. To have the list of all the pre-compiled workloads execute::

   ./nb --list-workloads

The above command will generate the list of pre-compiled workloads like::

    # An IOT workload with more optimal settings for DSE
    /activities/baselines/cql-iot-dse.yaml
    
    # Time-series data model and access patterns
    /activities/baselines/cql-iot.yaml
    
    # A workload with only text keys and text values
    /activities/baselines/cql-keyvalue.yaml


To edit a particular workload file locally, you execute the following, replacing the placeholder ``WORKLOAD_NAME`` with the name of the workload::

   ./nb --copy WORKLOAD_NAME

The command generates a file called ``cql-keyvalue.yaml`` containing the specifications for the keyvalue workload.

.. _nosqlbench_cassandra:

Create your own workload
------------------------

Workload files can be modified and then executed with ``nb`` using the command option ``workload=WORKLOAD_NAME``.

The tool expects the file ``WORKLOAD_NAME.yaml`` to be in the same directory of the ``nb`` command.
If you create the file called ``my-workload.yaml`` in the same directory of ``nb`` command, the new workload can be run with this command line::

   ./nb run                   \
      driver=cql              \
      workload=my-workload

.. Tip::

   You can check the data load using ``cqlsh`` as mentioned in the :doc:`dedicated document <connect-cqlsh-cli>`.