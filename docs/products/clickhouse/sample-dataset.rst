Sample dataset
===============

The official ClickHouse® website offers `a list of example datasets <https://clickhouse.com/docs/en/getting-started/example-datasets/>`_ to get you started. Each dataset has a description on how to download, inject, and transform the data samples as needed.

This article takes a closer look at how to use the ``Anonymized Web Analytics Data`` `example dataset <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/>`_. This contains two tables:

- ``hits_v1``, with data for every user action
- ``visits_v1``, with information about every user session

The steps below show you how to download the dataset, set up a connection with the server, and load the data into your cluster. ClickHouse already offers detailed instructions `on setting up this dataset <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/>`_, but these steps add some more details on how to run commands by using a ClickHouse client running in Docker.

Download the dataset
--------------------

Download the original dataset directly from `the dataset documentation page <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/>`_. You can do this using cURL, where the generic command looks like this::

    curl address_to_file_in_format_tsv_xz | unxz --threads=`nproc` > file-name.tsv

.. note::
    The ``nproc`` Linux command, which prints the number of processing units, is not available on macOS. To use the above command, add an alias for ``nproc`` into your  ``~/.zshrc`` file: ``alias nproc="sysctl -n hw.logicalcpu"``.

This command allows you to download and extract data from the URLs specified in the `ClickHouse documentation <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/#obtaining-tables-from-compressed-tsv-file>`_.

Once done, you should have two files available: ``hits_v1.tsv`` and ``visits_v1.tsv``.

Set up the service and database
-------------------------------

If you don't yet have an Aiven for ClickHouse service, follow the steps in our :doc:`getting started guide <getting-started>` to create one.

When you create a service, a default database was already added. However, you can create separate databases specific to your use case. We will create a database with the name ``datasets``, keeping it the same as in the ClickHouse documentation.

To create the new database, go to the  `Aiven web console <https://console.aiven.io/>`_ and click the **Databases & Tables** tab of your service page and create the database ``datasets``.

Connect to the ClickHouse database
----------------------------------

We will be using the ClickHouse client to connect to the server. Follow :doc:`the separate guide <howto/use-cli>` to familiarize yourself with how to set up and start using the ClickHouse client.

To connect to the server, use the connection details that you can find in the *Connection information* section of the *Overview* page in the Aiven web console. You will need **Host**, **Port**, **User**, and **Password**.


Create tables
---------------

The next step is to add a new table to your newly created database. The ClickHouse documentation includes a sample ``CREATE TABLE`` command with `the recommended table structure <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/#obtaining-tables-from-compressed-tsv-file>`_.

To use the command through Docker, run the following commands to create the tables for both ``hits_v1`` and ``visits_v1``::

   docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="CREATE TABLE datasets.hits_v1 [...] "

::

   docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="CREATE TABLE datasets.visits_v1 [...] "

.. note::

    If no database is specified, the default one is used.

Load data
----------

Now that you have a dataset with two empty tables, inject data into each of the tables. To do this:

1. Go to the folder where you stored the downloaded files for ``hits_v1.tsv`` and ``visits_v1.tsv``.

#. Run the following command::

        cat hits_v1.tsv | docker run \
        --interactive \
        --rm clickhouse/clickhouse-client \
        --user USER-NAME \
        --password USER-PASSWORD \
        --host YOUR-HOST-NAME.aivencloud.com \
        --port YOUR-PORT \
        --secure \
        --max_insert_block_size=100000
        --query="INSERT INTO datasets.hits_v1 FORMAT TSV"

   ``hits_v1.tsv`` contains approximately 7Gb of data. Depending on your internet connection, it can take some time to load all the items.

#. Run the corresponding command for ``visits_v1.tsv``::

        cat visits_v1.tsv | docker run \
        --interactive \
        --rm clickhouse/clickhouse-client \
        --user USER-NAME \
        --password USER-PASSWORD \
        --host YOUR-HOST-NAME.aivencloud.com \
        --port YOUR-PORT \
        --secure \
        --max_insert_block_size=100000
        --query="INSERT INTO datasets.visits_v1 FORMAT TSV"


You should now see the two tables in your database and you are ready to try out some queries.

Run queries
-----------

Once the data is loaded, you can start running some queries against the sample data you imported. For example, here is a command to query the number of items in the `hits_v1` table::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="SELECT COUNT(*) FROM datasets.hits_v1"


You can use a similar query to count how many items are in the `visits_v1` table::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="SELECT COUNT(*) FROM datasets.visits_v1"

Another example uses some additional query features to find the longest lasting sessions::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="SELECT StartURL AS URL, MAX(Duration) AS MaxDuration FROM tutorial.visits_v1 GROUP BY URL ORDER BY MaxDuration DESC LIMIT 10"


See tables in the console
-------------------------

You can also use the database and added tables with the data in the `Aiven web console <https://console.aiven.io/>`_. You can find them on the *Databases & Tables* tab of your service.
