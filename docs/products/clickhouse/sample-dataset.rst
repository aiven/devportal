Sample dataset
===============

Official ClickHouse website offers `a list of example datasets <https://clickhouse.com/docs/en/getting-started/example-datasets/>`_ to get you started. Each of the dataset has a description on how to download, inject and transform, when needed, the data samples.

We will look closer at how to use ``Yandex Metrica`` `example dataset <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/>`_. It contains two tables:

- ``hits_v1``, with data for every user action
- ``visits_v1``, with information about every user session

In the steps below we will download the dataset, setup a connection with the server and load the data into the cluster. ClickHouse already offers a detailed instruction `on setting up this dataset <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/>`_, however, we will expand it by adding more details on how to run commands by using ClickHouse client running in Docker.

Download the dataset
--------------------

Original dataset can be downloaded directly from `the dataset documentation page <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/>`_. You can do it by using cURL. Generic command will look like this::

    curl address_to_file_in_format_tsv_xz | unxz --threads=`nproc` > file-name.tsv

.. note::
    Linux command ``nproc``, which prints the number of processing units, is not available on Mac. To still be able to use the above command, add an alias to ``nproc`` equivalent into your  ``~/.zshrc`` file: ``alias nproc="sysctl -n hw.logicalcpu"``.

With this you can download and extract data from the URLs specified in `ClickHouse document <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/#obtaining-tables-from-compressed-tsv-file>`_.

Once done you should have two files available: ``hits_v1.tsv`` and ``visits_v1.tsv``.

Set up the service and get cluster URL
--------------------------------------
If you haven't done this already, create a service by following steps from :doc:`getting started guide <getting-started>`.

To connect to the server we will use connection details that can be found in *Connection information* section in the *Overview* page. You will need **Host**, **Port**, **User** and **Password**.

Install ClickHouse client
--------------------------
We will be using ClickHouse client to connect to the server. Follow :doc:`a separate guide <howto/install-cli>` to familiarize yourself with how to setup and start using ClickHouse client.

Create a database
------------------

During service creation a default database was already added, however, you can create separate databases specific for your use case. We will create a database with the name ``dataset``, keeping it same as in ClickHouse documentation.

You can create a new database through the user interface available in the  `Aiven web console <https://console.aiven.io/>`_ in the tab *Databases & Tables* of your service page.

Create a table
---------------

In a similar fashion we can add a new table to the newly created database. ClickHouse documentation offers `create table` command with `a recommended table structure <https://clickhouse.com/docs/en/getting-started/example-datasets/metrica/#obtaining-tables-from-compressed-tsv-file>`_. Use it in collaboration with Docker command to create tables both for ``hits_v1`` and ``visits_v1``::

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

    If no database is specified, the default one will be used.

Load data
----------

Now that you have a dataset with two empty tables, we will inject data in each of the tables. For this go to the folder where you stored downloaded files for ``hits_v1.tsv`` and ``visits_v1.tsv`` run::

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

``hits_v1.tsv`` contains approximately 7Gb of data. Depending on your internet connection it can take some time to load all the items.

Repeat for ``visits_v1.tsv``::

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


You should be able to see two tables created.

Count items
------------

Once data is loaded you can check number of items available by running::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="SELECT COUNT(*) FROM datasets.hits_v1"


and::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
    --query="SELECT COUNT(*) FROM datasets.visits_v1"

Or, you can experiment with available properties, and, for example, find longest lasting sessions::

    docker run --interactive \
    --rm clickhouse/clickhouse-client \
    --user USER-NAME \
    --password USER-PASSWORD \
    --host YOUR-HOST-NAME.aivencloud.com \
    --port YOUR-PORT \
    --secure \
--query="SELECT StartURL AS URL, MAX(Duration) AS MaxDuration FROM tutorial.visits_v1 GROUP BY URL ORDER BY MaxDuration DESC LIMIT 10"


See tables in the console
---------------------------
You can also use the database and added tables with the data in the  `Aiven web console <https://console.aiven.io/>`_. You can find them in the *Databases & Tables* tab of your service.