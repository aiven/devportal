Google cloud storage sink connector naming and data formats
===========================================================

The Apache Kafka Connect® GCS sink connector by Aiven enables you to move data from an Aiven for Apache Kafka® cluster to a Google Cloud Storage bucket for long term storage. The full connector documentation is available in the dedicated `GitHub repository <https://github.com/aiven/aiven-kafka-connect-gcs>`_.

File name format
----------------

The connector uses the following format for output files (blobs)

::

    <prefix><topic>-<partition>-<start-offset>[.gz]
    
The file name format has the following building blocks:

* ``<prefix>``: the file name prefix, useful, for example, to define subdirectories in the storage bucket
* ``<topic>``:  the source Apache Kafka topic name
* ``<partition>``: the source Apache Kafka topic's partition number
* ``<start-offset>``: the offset of the first record in the file
* ``[.gz]``: the file suffix, added when compression is enabled and depending on compression type

Data format
-----------

The connector output files are text files that contain one record per line (separated by ``\n``).

There are two types of data format available: 

* **Flat structure**: it's the default data format, where the field values are separated by comma (CSV). 
  
  You can use the CSV format by setting the ``format.output.type`` to ``csv``.
* **Complex structure**: the file stores messages in the format of JSON lines. It contains one record per line and each line is a valid JSON object (``jsonl``). 
  
  You can use the JSON format by setting the ``format.output.type`` to ``jsonl``.