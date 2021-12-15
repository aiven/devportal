JDBC source connector modes
===========================


JDBC source connector extracts data from a relational database, such as PostgreSQL or MySQL, and pushes it to Apache Kafka where can be transformed and read by multiple consumers. The details of the connector are covered in the `Aiven JDBC source connector GitHub documentation <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/source-connector.md>`_. 

This connector type periodically queries the table(s) to extract the data, and can be configured in four **modes**.

Bulk mode
---------

In ``bulk`` mode the connector will periodically query the full table retrieving all the rows and publishing them into the Apache Kafka topic.
Thus, if the source table contains ``100.000`` rows, the connector will insert ``100.000`` new messages in the Apache Kafka topic for every poll, no matter how many rows in the database are new or stale.

.. Tip::

  Since the bulk mode replicates the whole table content into the Apache Kafka topic at every poll, it's a suitable option only for tables with limited amount of data which don't have any incremental or timestamp column.

Incrementing mode
-----------------

Using the ``incrementing`` mode, the connector will query the table and append a `WHERE` condition based on an **incrementing column** in order to fetch new rows. The incrementing mode requires that a column containing an always growing number (like a series) is present in the source table. The incrementing column is used to check which rows have been added since last query. 

.. Note::

  The column name is passed via the ``incrementing.column.name`` parameter

If for example the database ``students`` table contains the following entries:

.. list-table::
  :header-rows: 1
  :align: left

  * - ``student_id``
    - ``student_name``
  * - 1
    - ``Jon Doe``
  * - 2
    - ``Mary English``
  * - 3
    - ``Carol Tunder``

The column ``student_id`` can be used as an incremental column. On the first poll, the Apache Kafka connector will select all rows from the table and record the maximum ``student_id`` value in the table (``3`` in the above example). 

The following polls will append a ``WHERE`` condition to the query selecting only rows with ``student_id`` greater than the previously recorded maximum value. In the example below, the condition will be ``WHERE student_id > 3``. If the new records are available in the table, then the highest value for the incremental column is stored, and used as filter for the following polls. 

.. list-table::
  :header-rows: 1
  :align: left

  * - ``student_id``
    - ``student_name``
  * - 1
    - ``Jon Doe``
  * - 2
    - ``Mary English``
  * - 3
    - ``Carol Tunder``
  * - **6**
    - ``Sam Cricket``

In the case above, where a new row for ``Sam Cricket`` is added, a new record will be sent to the Apache Kafka topic, and the maximum ``student_id`` value will be updated to ``6`` and used in ``WHERE`` condition in the next polls.

.. Warning::

  With the incremental mode, any change which doesn't generate rows with an id higher than the maximum recorded in the previous poll will **not** be detected. E.g. updating the ``student_name`` without changing the ``student_id`` will not generate any new records in Apache Kafka. 

Timestamp mode
--------------

Using the ``timestamp`` mode, the connector will query the table appending a ``WHERE`` condition based on one or more **timestamp columns**. This requires that creation date and modification date are present for every row. 

In cases of two columns (e.g. ``creation_date`` and ``modification_date``) the polling query will apply the ``COALESCENCE`` function, parsing the value of the second column only when the first column is null. 

.. Tip::
  
  The timestamp column(s) is passed via the ``timestamp.column.name parameter``.

If, for example, the database ``students`` table contains the following entries:

.. list-table::
  :header-rows: 1
  :align: left

  * - ``student_id``
    - ``student_name``
    - ``created_date``
    - ``modified_date``
  * - 1
    - ``Jon Doe``
    - 2021-01-01
    -
  * - 2
    - ``Mary English``
    - 2021-03-01
    - 2021-04-05
  * - 3
    - ``Carol Tunder``
    - 2021-03-02
    - 2021-04-06

The columns ``created_date`` and ``modified_date`` can be used as timestamp columns. On the first poll, the Kafka connector will select all rows from the table and record the value in the ``modified_date`` and ``created_date`` columns (``2021-04-06`` in the above example). 

The following polls will append a ``WHERE`` condition to the query selecting only rows with ``modified_date`` or ``created_date`` greater than the previously recorded maximum value using the ``COALESCENCE`` function. In the example below, the condition will be:

::
 
  WHERE COALESCENCE(modified_date, created_date) > '2021-04-06'
  
If new records with more recent ``modified_date`` or ``created_date`` are available in the table, then the highest value for the timestamp columns is stored, and used as filter for the following polls. 

.. Warning::

  With the timestamp mode, any change which doesn't generate a more recent timestamp than the maximum recorded in the previous poll will **not** be detected. E.g. updating the ``Jon Doe``'s ``modified_date`` to ``2021-04-03`` will not be captured since a more recent date (``2021-04-06``) was already recorded in the previous poll. 

Timestamp and incrementing mode
-------------------------------

Using the ``timestamp+incrementing`` mode, Kafka connect implements both the incrementing and timestamp functionalities described above. 

.. Tip:: 
  
  The incremental column name is passed via the ``incrementing.column.name`` and the timestamp column(s) is passed via the ``timestamp.column.name parameter``. 

Check out the `Aiven JDBC source connector GitHub documentation <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/source-connector.md>`_ for more information.