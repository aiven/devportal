Copy data from Aiven for OpenSearch® to AWS S3 using ``elasticsearch-dump``
===========================================================================

It is a good practice to perform backups of your OpenSearch® data to another storage service. This way you can access your data and restore it if something unexpected happens to it. 

In this article, you can find out how to dump your OpenSearch data to AWS S3 bucket.

To copy the index data, we will be using ``elasticsearch-dump`` `tool <https://github.com/elasticsearch-dump/elasticsearch-dump>`__. You can read the `instructions on GitHub <https://github.com/elasticsearch-dump/elasticsearch-dump/blob/master/README.md>`_ on how to install it. From this library, we will use ``elasticdump`` command to copy the input index data to an specific output. 

.. _copy-data-from-os-to-s3:

Prerequisites
~~~~~~~~~~~~~

* ``elasticsearch-dump`` `tool <https://github.com/elasticsearch-dump/elasticsearch-dump>`__ installed
* Aiven for OpenSearch cluster as the ``input``
* AWS S3 bucket as the ``output``

You need to collect the following information about your Aiven for OpenSearch cluster and your AWS service:

Aiven for OpenSearch:

* ``SERVICE_URI``: OpenSearch service URI, which you can find in Aiven's dashboard.
* ``INPUT_INDEX_NAME``: the index that you aim to copy from your input source.

AWS S3:

* AWS credentials (``ACCESS_KEY_ID`` and ``SECRET_ACCESS_KEY``).
* S3 file path. This includes bucket name and file name, for e.g. ``s3://${BUCKET_NAME}/${FILE_NAME}.json``

.. seealso::

    You can find more information about AWS credentials in the `AWS documentation <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html>`_.


Export OpenSearch index data to S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``elasticsearch-dump`` command to copy the data from your **Aiven for OpenSearch cluster** to your **AWS S3 bucket**. Use your Aiven for OpenSearch ``SERVICE_URI`` for the ``input`` . For the ``output``, choose an AWS S3 file path including the file name that you want for your document.


.. code-block:: shell

    elasticdump \
    --s3AccessKeyId "${ACCESS_KEY_ID}" \
    --s3SecretAccessKey "${SECRET_ACCESS_KEY}" \
    --input=SERVICE_URI/INPUT_INDEX_NAME --output "s3://${BUCKET_NAME}/${FILE_NAME}.json"  

Resources
---------

Aiven for OpenSearch databases are automatically backed up, so you can check more information about how the :ref:`Backup process works <opensearch-backup>`.

-------

.. We don't directly reference Elasticsearch itself, but we do use the term
   "elasticsearch" so it is probably polite to include the following
   disclaimer

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
