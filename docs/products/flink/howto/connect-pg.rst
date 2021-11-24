Create a PostgreSQL-based Apache Flink table
==============================================

To build data pipelines, Apache Flink requires source and target data structures to `be mapped as Flink tables <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#create-table>`_. This functionality can be achieved via the `Aiven console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli/service/flink>`.

A Flink table can be defined over an existing or new Aiven for PostgreSQL table to be able to source or sink streaming data. To define a table over an PostgreSQL table, the table name and columns data format need to be defined, together with the Flink table name to use as reference when building data pipelines.

.. Warning::

    In order to define Flink's tables an :doc:`existing integration <create-integration>` needs to be available between the Aiven for Flink service and one or more Aiven for PostgreSQL services. Moreover, the source or target PostgreSQL table need to pre-exist when stating the Flink job.

Create a PostgreSQL-based Apache Flink table with Aiven Console
---------------------------------------------------------------

To create a Flink table based on Aiven for PostgreSQL via Aiven console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab

2. Select the **Data Tables** sub-tab and select the Aiven for PostgreSQL integration to use

3. Select the Aiven for PostgreSQL service where the table is stored 

4. Write the PostgreSQL table name in the **JDBC table** field with the format ``schema_name.table_name``

.. Warning::

  When using a PostgreSQL table as target of a Flink data pipeline, the table needs to exist before starting the Flink job otherwise it will fail.

5. Define the **Flink table name**; this name will represents the Flink reference to the topic and will be used during the data pipeline definition

7. Define the **SQL schema**: the SQL schema defines the fields retrieved from the PostgreSQL table and additional transformations such as format casting or timestamp extraction.

.. Note::

  More details on data types mapping between Apache Flink and PostgreSQL are available at the `dedicated JDBC Apache Flink page <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/jdbc/#data-type-mapping>`_.

Example: Define a Flink table over a PostgreSQL table   
-----------------------------------------------------

The Aiven for PostgreSQL service named ``pg-demo`` contains a table named ``students`` in the ``public`` schema with the following structure:

::

  student_id INT,
  student_name VARCHAR

We can define a ``students_tbl`` Flink table with:

* ``pg-demo`` as the selected Aiven for PostgreSQL service 
* ``public.students`` as **JDBC table**
* ``students_tbl`` as **Name**
* ``student_id INT, student_name VARCHAR`` as **SQL schema**

