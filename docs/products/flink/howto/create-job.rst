Create an Apache Flink job
=================================

Prerequisites
'''''''''''''

To build data pipelines, Apache Flink requires source or target data structures to :doc:`be mapped as Flink tables <connect>`.

Create a Flink job via Aiven Console
'''''''''''''''''''''''''''''''''''''

To create a new data pipeline defined by a Flink job via the Aiven Console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab

2. Select the **Create SQL job** sub-tab

3. Define the Flink **Job Name**, the list of Flink source and target **tables** and data pipeline SQL **Statement** 

**Example**: Define a Flink job named ``JobExample`` transforming data from the ``KCpuIn`` table and inserting data in the ``KAlert`` table.

Settings:

* ``JobExample`` as **Job Name**
* ``KCpuIn, KAlert`` as **Tables**
* ``INSERT INTO KAlert SELECT * FROM KCpuIn WHERE `cpu` > 70`` as **Statement**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-job.png
  :scale: 80 %
  :alt: Image of the Aiven for Apache Flink Jobs and Data tab when creating a Flink job