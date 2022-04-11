Configure GCP for a Google BigQuery sink connector
==================================================

To be able to sink data from Apache Kafka® to Google BigQuery via the dedicated Aiven connector, you need to perform the following steps in the `GCP console <https://console.cloud.google.com/>`_:

* Create a new `Google service account and generate a JSON service key <https://cloud.google.com/docs/authentication/getting-started>`_ 
* Verify that BigQuery API is enabled
* Create a new `BigQuery dataset <https://cloud.google.com/bigquery/docs/datasets>`_ or define an existing one where the data is going to be stored
* Grant `dataset access to the service account <https://cloud.google.com/bigquery/docs/dataset-access-controls>`__



.. _gcp-bigquery-sink-connector-google-account:

Create a new Google service account and generate a JSON service key
-------------------------------------------------------------------

Follow the `instructions <https://cloud.google.com/docs/authentication/getting-started>`_ to: 

* create a new Google service account
* create a JSON service key

The JSON service key will be used in the connector configuration

Verify that BigQuery API is enabled
-----------------------------------

The BigQuery sink connector uses the API to push the data. To enable them:

* Navigate to the `GCP API & Services dashboard <https://console.cloud.google.com/apis>`_ and click on the **BigQuery API**
* Verify the BigQuery API is already enabled or follow the steps given to enable it


.. _gcp-bigquery-sink-connector-bigquery-dataset:

Create the Google BigQuery dataset
----------------------------------

You can either send the Apache Kafka data to an existing Google BigQuery dataset or create a new one using `the GCP console <https://console.cloud.google.com/bigquery>`__ by following the `instructions in the dedicated page <https://cloud.google.com/bigquery/docs/datasets>`_. 

.. Tip::

    When creating the dataset, specify data location in a region close to where your Aiven for Apache Kafka is running, to minimize latency.

.. _gcp-bigquery-sink-connector-bigquery-dataset-grant:

Grant dataset access to the service account
-------------------------------------------

The newly created service account needs to have access to the dataset in order to write data to it. Follow the `dedicated instructions <https://cloud.google.com/bigquery/docs/dataset-access-controls>`_ to check and modify the dataset permissions. The **BigQuery Data Editor** is sufficient for the connector to work.
