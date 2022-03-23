Configure GCP for a Google Cloud Storage sink connector
=======================================================

To be able to sink data from Apache Kafka® to Google Cloud Storage via the dedicated Aiven connector, you need to perform the following steps in the `GCP console <https://console.cloud.google.com/>`_:

* Create a `Google Cloud Storage (GCS) bucket <https://console.cloud.google.com/storage/>`_ where the data is going to be stored
* Create a new `Google service account and generate a JSON service key <https://cloud.google.com/docs/authentication/getting-started>`_ 
* Grant the service account access to the GCS bucket

.. _gcs-sink-connector-google-bucket:

Create the Google Cloud Storage (GCS) bucket
--------------------------------------------

You can create the GCS bucket using the `dedicated Google cloud console page <https://console.cloud.google.com/storage/>`_. When creating the bucket, specify bucket name and location, the other settings can be left as default.

.. _gcs-sink-connector-google-account:

Create a new Google service account and generate a JSON service key
-------------------------------------------------------------------

Follow the `instructions <https://cloud.google.com/docs/authentication/getting-started>`_ to: 

* create a new Google service account
* create a JSON service key

The JSON service key will be used in the connector configuration


Grant the service account access to the GCS bucket
--------------------------------------------------

Navigate in the GCS bucket detail page, in the **Permissions** tab and grant access to the newly created service account to the bucket. The **Storage Object Creator** role is sufficient for the connector.
