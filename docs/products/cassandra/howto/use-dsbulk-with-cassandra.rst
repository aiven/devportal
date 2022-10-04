Use DSBULK to load, unload and count data on Aiven service for Cassandra®
=========================================================================

`DSBulk <https://docs.datastax.com/en/dsbulk/docs/reference/dsbulkCmd.html>`_ is a highly configurable tool used to load, unload and count data in Apache Cassandra®.
It has configurable consistency levels for loading and unloading and offers the most accurate way to count records in Cassandra.

Prerequisites
~~~~~~~~~~~~~

To install the latest release of DSBulk, download the `zip` or `tar.gz` file from `dsbulk GitHub repository <https://github.com/datastax/dsbulk>`_.


.. Tip::

   You can read more about the dsbulk different use cases and manual pages in the `dedicated documentation <https://docs.datastax.com/en/dsbulk/docs/getStartedDsbulk.html>`_

Variables
~~~~~~~~~

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

Preparation of the environment 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order for `dsbulk` to read the security certificate to connect to Aiven service for Cassandra, the certificate must be imported in a truststore.

1- download the certificate from `Aiven Console> Services> cassandra-asdfasdf> Overview> CA Certificate`. Save the CA certificate 
in a file called `cassandra-certificate.pem` in a directory on the linux system where `dsbulk` runs.

2- run this command line to create a truststore file and import the certificate in it:

``keytool -import -v -trustcacerts -alias CARoot -file cassandra-certificate.pem -keystore client.truststore``

a truststore file called `client.truststore` is created in the directory where the keytool command has been launched. 
The keytool command assumes the file `cassandra-certificate.pem` is in the same directory where you run `keytool`. If that is not the case, provide a full path 
to `cassandra-certificate.pem`.
During creation of the truststore, you will be need to set a password that is required to access the truststore and retrieve the certificate.

3- next step is to create a configuration file with the connection information.
In this way the `dsbulk`` command line will be more readable and will not show passwords in clear. If you don't create a config file, 
every option must be explicitly provided on the command line.

4- create a file that contains the connection configuration like this::

cat conf.file
datastax-java-driver {
  advanced {
    ssl-engine-factory {
      keystore-password = "cassandra"
      keystore-path = "/home/user1/client.truststore"
      class = DefaultSslEngineFactory
      truststore-password = "cassandra"
      truststore-path = "/home/user1/client.truststore"
    }
    auth-provider {
      username = avnadmin
      password = AVNS_JHMJgrFwIa-uPd7BwEB
    }
  }
}

The config file can contain many different blocks for different configurations. In our case it only contains the datastax-java-driver block.
The careful reader has not missed that the ssl-engine-factory block contains the path of the truststore and the password to read into the 
truststore and access the certificate.
For a full reference and templates of the application configuration file see `here <https://github.com/datastax/dsbulk/blob/1.x/manual/application.template.conf>`_.
For a full reference of the driver configuration file, see `here <https://github.com/datastax/dsbulk/blob/1.x/manual/driver.template.conf>`_.


Run a `dsbulk` command to count records in a Cassandra table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have created the configuration file, we can run the dsbulk command line. 
Go to the `bin` directory of the downloaded `dsbulk` package and run the following command line::

   ./dsbulk count                                  \
   -f /full/path/to/conf.file                      \
   -k baselines                                    \
   -t keyvalue                                     \
   -h cassandra-asdfasdf-project1.aivencloud.com   \
   -port 20341                                     \
   --log.verbosity 2

where:
- `baselines` and `keyvalue` are the names of the sample keyspace and table in the Cassandra database.
- `log.verbosity` controls the amount of logging that is sent at standard output when `dsbulk` runs. `verbosity=2` is used only to troubleshoot problems. To reduce verbosity, reduce the number to 1 or remove the option altogether.
- -f specifies the path to the configuration file
- -h and -p are the hostname and port number to connect to Cassandra db.


Run a `dsbulk` command to load data into a Cassandra table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A command line similar to the one above can be used to load data into a table::

   ./dsbulk unload                               \
   -f ../conf.file                               \
   -k baselines                                  \
   -t keyvalue                                   \
   -h cassandra-asdfasdf-project1.aivencloud.com \
   -port 20341

this command will unload all records from the table in a CSV format. In order to download the data in a file, the output can be redirected to a file.

Load data into a Cassandra table from a CSV file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To load data into a Cassandra table, the command line is very similar to the previous command::

   ./dsbulk load                                 \
   -f ../conf.file                               \
   -k baselines                                  \
   -t keyvalue                                   \
   -h cassandra-asdfasdf-project1.aivencloud.com \ 
   -port 20341                                   \
   -url data.csv

where:
- the file `data.csv` is the file that contains the data to load into Cassandra.

