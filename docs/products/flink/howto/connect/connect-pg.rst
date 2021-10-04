Create a PostgreSQL based Flink table
==============================================

To create a Flink table based on Aiven for PostgreSQL via Aiven console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab

2. Select the **Data Tables** sub-tab and select the Aiven for PostgreSQL integration to use

3. Define the Flink table **Name**, the source **JDBC table** name and **Schema SQL** 

**Example**: Define a Flink table named ``node_info`` pointing to a PostgreSQL table named ``public.node_definition`` available in the Aiven for PostgreSQL service named ``pg-devportal-example``

Settings:

* ``pg-devportal-example`` as the selected service 
* ``node_info`` as **Name**
* ``public.node_definition`` as **JDBC table**
* ``node INT, node_description VARCHAR`` as **SQL schema**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-table-pg.png
  :scale: 70 %
  :alt: Image of the Aiven for Apache Flink Jobs and Data tab when creating a Flink table on top of an Aiven for PostgreSQL table