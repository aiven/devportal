Create a PostgreSQL®-based Apache Flink® table
==============================================

.. warning:: 
  As with many beta products, the Aiven for Apache Flink® experience, APIs and CLI calls are currently being redesigned, you might get error messages if using the currently documented ones.

  We will be working to update all the examples in the documentation.


To build data pipelines, Apache Flink® requires source and target data structures to `be mapped as Flink tables <https://ci.apache.org/projects/flink/flink-docs-release-1.15/docs/dev/table/sql/create/#create-table>`_. This functionality can be achieved via the `Aiven console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli/service/flink>`.

A Flink table can be defined over an existing or new Aiven for PostgreSQL® table to be able to source or sink streaming data. To define a table over an PostgreSQL® table, the table name and columns data format need to be defined, together with the Flink table name to use as reference when building data pipelines.

.. Warning::

    To define Flink tables, an :doc:`existing integration <create-integration>`  must be available between the Aiven for Flink service and one or more Aiven for PostgreSQL® services. 

Create a PostgreSQL®-based Apache Flink® table with Aiven Console
------------------------------------------------------------------

To create a Flink table based on Aiven for PostgreSQL® via Aiven console:

1. In the Aiven for Apache Flink service page, open the **Application** tab.

2. Create a new application or select an existing one with Aiven for PostgreSQL® integration.

   .. note:: 
      If editing an existing application, create a new version to make changes to the source or sink tables.

3. In the **Create new version** screen, click **Add source tables**.

4. Click **Add new table** or click **Edit** if you want to edit an existing source table. 

5. In the **Add new source table** or **Edit source table** screen, select the Aiven for PostgreSQL® service as the integrated service. 

6. In the **Table SQL** section, enter the SQL statement to create the PostgreSQL-based Apache Flink table with the following details:

   * Write the PostgreSQL® table name in the **JDBC table** field with the format ``schema_name.table_name``

   .. Warning::

    When using a PostgreSQL® table as target of a Flink data pipeline, the table needs to exist before starting the Flink job otherwise it will fail.

   * Define the **Flink table name**; this name will represents the Flink reference to the topic and will be used during the data pipeline definition

7. To create a sink table, click **Add sink tables** and repeat steps 4-6 for sink tables.

8. In the **Create statement** section, write the SQL schema that defines the fields retrieved from the PostgreSQL® table and any additional transformations, such as format casting or timestamp extraction.

.. Note::

  More details on data types mapping between Apache Flink® and PostgreSQL® are available at the `dedicated JDBC Apache Flink® page <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/jdbc/#data-type-mapping>`_.

Example: Define a Flink table over a PostgreSQL® table   
-------------------------------------------------------

The Aiven for PostgreSQL® service named ``pg-demo`` contains a table named ``students`` in the ``public`` schema with the following structure:

::

  student_id INT,
  student_name VARCHAR

We can define a ``students_tbl`` Flink table with:

* ``pg-demo`` as the selected Aiven for PostgreSQL® service 
* ``public.students`` as **JDBC table**
* ``students_tbl`` as **Name**
* ``student_id INT, student_name VARCHAR`` as **SQL schema** `mapping the existing columns <https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/table/jdbc/#data-type-mapping>`_ in the PostgreSQL® table

