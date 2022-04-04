Configure GCP for a Google BigQuery sink connector
==================================================

To be able to sink data from Apache Kafka® to Google BigQuery via the dedicated Aiven connector, you need to perform the following steps in the `GCP console <https://console.cloud.google.com/>`_:

* Create a new `Google service account and generate a JSON service key <https://cloud.google.com/docs/authentication/getting-started>`_ 
* Create a `BigQuery dataset <https://cloud.google.com/bigquery/docs/datasets>`_ where the data is going to be stored
* Verify that BigQuery API is enabled

.. _gcp-bigquery-sink-connector-google-account:

Create a new Google service account and generate a JSON service key
-------------------------------------------------------------------

Follow the `instructions <https://cloud.google.com/docs/authentication/getting-started>`_ to: 

* create a new Google service account
* create a JSON service key

The JSON service key will be used in the connector configuration


.. _gcp-bigquery-sink-connector-bigquery-dataset:

Create the Google BigQuery dataset
----------------------------------

You can create the Google BigQuery dataset using `the GCP console <https://console.cloud.google.com/bigquery>`__ by following the `instructions in the dedicated page <https://cloud.google.com/bigquery/docs/datasets>`_. 

.. Tip::

    When creating the dataset, specify data location in a region close to where your Aiven for Apache Kafka is running, to minimize latency.


Verify that BigQuery API is enabled
-----------------------------------

The BigQuery sink connector uses the API to push the data. To enable them:

* Navigate to the `GCP API & Services dashboard <https://console.cloud.google.com/apis>`_ and click on the **BigQuery API**
* Verify the BigQuery API is already enabled or follow the steps given to enable it
