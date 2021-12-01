JDBC source connector modes
===========================


JDBC source connector extracts data from a relational database, such as PostgreSQL or MySQL, and pushes it to Apache Kafka where can be transformed and read by multiple consumers. 

This connector type periodically queries the table(s) to extract the data, and can be configured in four main **modes**:

* ``bulk``: the connector will query the full table every time retrieving all rows and publishing them into the Apache Kafka topic
* ``incrementing``: the connector will query the table appending a `WHERE` condition based on a **incrementing column**. This requires the presence of a column containing an always growing number (like a series). The incrementing column is used to check which rows have been added since last query. 
  
  The column name will be passed via the ``incrementing.column.name`` parameter

* ``timestamp``: the connector will query the table appending a ``WHERE`` condition based on a **timestamp column(s)**. This requires the presence of one or more columns containing the row's creation date and modification date. 

  In cases of two columns (e.g. ``creation_date`` and ``modification_date``) the polling query will apply the ``COALESCENCE`` function, parsing the value of the second column only when the first column is null. 
  
  The timestamp column(s) can be passed via the ``timestamp.column.name parameter``.

* ``timestamp+incrementing``: this last mode uses both the incrementing and timestamp functionalities with ``incrementing.column.name`` selecting the incremental column and ``timestamp.column.name`` the timestamp one(s).

Check out the `Aiven JDBC source connector documentation <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/source-connector.md>`_ for more information.