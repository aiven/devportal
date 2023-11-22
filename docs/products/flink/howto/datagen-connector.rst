Create a DataGen-based Apache Flink® table
===========================================

The DataGen source table is a built-in connector of the Apache Flink system that generates random data periodically, matching the specified data type of the source table. This section provides you with information on how to connect DataGen as a source table in an Aiven for Apache ®Flink application.

Configure Datagen as source for Flink application
-------------------------------------------------
To configure DataGen as the source using the DataGen built-in connector for Apache Flink, follow these steps: 

1. In the Aiven for Apache Flink service page, select **Application** from the left sidebar.
2. Create a new application or select an existing application for your desired :doc:`data service integration `/docs/products/flink/howto/create-integration`. 

.. note:: 
    If you are editing an existing application, you need to create a new version of the application to make changes to the source or sink table.

3. In the **Create new version** screen, select **Add source tables**.
4. Select **Add new table** or select **Edit** if you want to edit an existing source table. 
5. In the **Table SQL** section of the **Add new source table** or **Edit source table** screen,  set the connector to **datagen** as shown in the example below:

.. code::

    CREATE TABLE `gen_me` 
    ( 
        `id` INT, `price` DECIMAL(32,2)
    ) 
    WITH
    (
        `connector` = 'datagen'
    )

Where:

* ``connector``: The connector parameter is set to ``datagen``, a built-in connector in Flink that generates random data in memory and is used as a source of data in Flink applications. 
   
.. note::
    For more information on the connector types and the requirements for each, see the articles on :doc:`Kafka connector types </docs/products/flink/concepts/kafka-connectors>` and :doc:`the requirements for each connector type </docs/products/flink/concepts/kafka-connector-requirements>`.

6. In the **Add sink tables** screen, select the option to add a new sink table or edit an existing one.
7. In the **Create statement** section, write the statement to test your SQL queries using random data. 
