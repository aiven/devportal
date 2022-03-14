
Dump OpenSearch index using ``elasticsearch-dump``
==================================================

It is a good practice to perform backups of your OpenSearch data to another storage service. This way you can access your data and restore it if something unexpected happens to it. 

In this article, you can find out how to dump your OpenSearch data to an:

* :ref:`OpenSearch cluster <copy-data-from-os-to-os>`
* :ref:`AWS S3 bucket <copy-data-from-os-to-s3>`

We will be using ``elasticsearch-dump`` `tool <elashttps://github.com/elasticsearch-dump/elasticsearch-dump>`__ for these processes. To install the ``elasticsearch-dump``, read the `instructions <https://github.com/elasticsearch-dump/elasticsearch-dump/blob/master/README.md>`_ on GitHub.

.. _copy-data-from-os-to-os:

Copying data from OpenSearch to Aiven OpenSearch
------------------------------------------------

Prerequisites
~~~~~~~~~~~~~

* Aiven for OpenSearch cluster 
* OpenSearch cluster 
* ``elasticsearch-dump`` `tool <elashttps://github.com/elasticsearch-dump/elasticsearch-dump>`__ installed

To import the data we will use ``elasticdump`` command. This command works by copying the ``input`` index data to an specific ``output``. The ``input`` and ``ouput`` can be either an OpenSearch URL or a file path (local or remote file storage). In this particular case, we are using both URLs, one from an **OpenSearch cluster** and the other one from **Aiven for OpenSearch cluster**.

Import mapping
~~~~~~~~~~~~~~

.. code-block:: shell

    elasticdump \
    --input=http://opensearch-url:9243/index_name \
    --output=SERVICE_URI/index_name \
    --type=mapping

Import data 
~~~~~~~~~~~

.. code-block:: shell

    elasticdump \
    --input=http://opensearch-url:9243/index_name \
    --output=SERVICE_URI/index_name \
    --type=data

When the dump is completed, you can check that the index is available in the OpenSearch service you send it to. You will able to find it under the **Indexes** tab in your Aiven console.

.. _copy-data-from-os-to-s3:

Copying data from Aiven OpenSearch to S3
----------------------------------------

Prerequisites
~~~~~~~~~~~~~

* Aiven for OpenSearch cluster 
* S3 bucket
* ``elasticsearch-dump`` `tool <elashttps://github.com/elasticsearch-dump/elasticsearch-dump>`__ installed

Export OpenSearch index data to S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``elasticsearch-dump`` command to copy the data from your **Aiven OpenSearch cluster** to your **S3 bucket**. For the ``input`` use your Aiven OpenSearch ``SERVICE_URI``. For the ``output``, choose an AWS S3 file path including the file name that you want for your document. 

.. Tip::

    You can find the ``SERVICE_URI`` on Aiven's dashboard.


.. code-block:: shell

    elasticdump \
    --s3AccessKeyId "${access_key_id}" \
    --s3SecretAccessKey "${access_key_secret}" \
    --input=SERVICE_URI/index_name --output "s3://${bucket_name}/${file_name}.json"  


The AWS credentials are required for the operation to succeed. You can find more information about those credentials in the `AWS documentation <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html>`_.
