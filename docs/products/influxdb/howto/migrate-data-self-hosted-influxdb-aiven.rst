Migrate data from self-hosted InfluxDB to Aiven
===============================================
You can migrate data from a self-hosted InfluxDB® 1.x service to an Aiven for InfluxDB® service by exporting the data in line protocol format using the ``influx_export`` command from the source service. 
The exported file, which is in line protocol format, can then be imported into the target Aiven for InfluxDB® service using the influx client. This process is fast and compatible across different minor versions.

The process of migrating data from a self-hosted InfluxDB to Aiven for InfluxDB® service can be broken down into two main steps:

1. Create the data export file
2. Import the exported data into the destination Aiven for InfluxDB service. 

Create the data export file
---------------------------

To export the data from a self-hosted InfluxDB service, you will first need to run the ``influx_inspect export`` command. This command will create a dump file of your data.

The following is an example command:
::

    $ influx_inspect export -datadir "/var/lib/influxdb/data" -waldir "/var/lib/influxdb/wal" -out "/scratch/weather.influx.gz" -database weather -compress


where, 

* ``-datadir`` and ``-waldir`` options specify the directories where your data and write-ahead log files are stored, respectively. These paths may differ on your system, so double-check your settings before running the command.
* ``-out`` option specifies where the export file will be saved. 
* ``-database`` option specifies which database you want to export. In this example, the database named `weather` is being exported.
* ``-compress`` option implies the command to compress the data.

If you have a large database and only need a specific part of the data, you can optionally define a time span using the ``-start`` and ``-end`` switches to reduce the dump size. This will make the export process faster and take up less space.


Import data into destination Aiven service
-------------------------------------------------
Now that you have successfully created the export file, you can proceed to import it to Aiven for InfluxDB® service by following these steps:

1. **Ensure a stable network connection:**  To ensure a successful data transfer, perform the process from a host with a fast and stable network connection, such as via VPC peering.
2. **Pre-create the destination InfluxDB database:** Before you begin the data transfer process, you must pre-create the InfluxDB database on the destination Aiven for InfluxDB service. 
    - You can do this via the `Aiven Console <https://console.aiven.io/>`_ by navigating to the **Databases** tab on your InfluxDB service or via the :doc:`Aiven CLI </docs/tools/cli>` and `REST API <https://api.aiven.io/doc/>`_. 
    - Optionally, you can also change the retention policies for the destination database. For more information, see :doc:`InfluxDB retention policies <../concepts/influxdb-retention-policy>`. 

.. note:: 
    The ``avnadmin`` admin user does not have full superuser access, so it is necessary to pre-create the database before transferring the data. 

1. **Import the data:** You can now push the exported data to the destination Aiven service using the ``influx -import`` command. You will need to specify the host, port, username, and password of the Aiven for InfluxDB service and the path to the exported data. The following is an example command: 
::

    $ influx -import -host influx-testuser-business-demo.aivencloud.com -port 12691 -username 'avnadmin' -password 'secret' -ssl -precision rfc3339 -compressed -path ./weather.influx.gz

.. note:: 
    During the import process, you might see an error message indicating that the database could not be created. You can disregard this error message as the database has already been pre-created before starting the import process.

After the migration is complete, you can validate your data and start using your new Aiven for InfluxDB service.
