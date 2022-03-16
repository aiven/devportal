
Dump OpenSearch index using ``elasticsearch-dump``
==================================================

It is a good practice to perform backups of your OpenSearch data to another storage service. This way you can access your data and restore it if something unexpected happens to it. 

In this article, you can find out how to dump your OpenSearch data to an:

* :ref:`Aiven OpenSearch <copy-data-from-os-to-os>`
* :ref:`AWS S3 bucket <copy-data-from-os-to-s3>`

To copy the index data, we will be using ``elasticsearch-dump`` `tool <elashttps://github.com/elasticsearch-dump/elasticsearch-dump>`__. You can read the `instructions on GitHub <https://github.com/elasticsearch-dump/elasticsearch-dump/blob/master/README.md>`_ in how to install it. From this library, we will use ``elasticdump`` command to copy the ``input`` index data to an specific ``output``. 

.. note::

    Make sure to have ``elasticsearch-dump`` `tool <elashttps://github.com/elasticsearch-dump/elasticsearch-dump>`__ installed for the next steps.

.. _copy-data-from-os-to-os:

Copying data from OpenSearch to Aiven OpenSearch
------------------------------------------------

Prerequisites
~~~~~~~~~~~~~

* OpenSearch cluster as the ``input`` (can be in Aiven or elsewhere)
* Aiven for OpenSearch cluster as the ``output``

.. note::
    
    The ``input`` and ``ouput`` can be either an OpenSearch URL or a file path (local or remote file storage). In this particular case, we are using both URLs, one from an **OpenSearch cluster** and the other one from **Aiven for OpenSearch cluster**. 


Here are some information you need to collect to copy your data:

OpenSearch cluster:

* OpenSearch cluster URL , for e.g. ``http://opensearch-url:9243/``

Aiven for OpenSearch:

* ``INDEX_NAME``: the name of the index that you aim to backup.
* ``SERVICE_URI``: OpenSearch service URI. You can find it in Aiven's dashboard.




Import mapping
~~~~~~~~~~~~~~

The process of defining how a document and the fields are stored and indexed is called mapping. When no data structure is specified, we rely on OpenSearch to automatically detect the fields using dynamic mapping. However, we can set our data mapping before the data is sent:

.. code-block:: shell

    elasticdump \
    --input=http://opensearch-url:9243/INDEX_NAME \
    --output=SERVICE_URI/INDEX_NAME \
    --type=mapping


Import data 
~~~~~~~~~~~

This is how you can copy your index data from an OpenSearch cluster (can be in Aiven or elsewhere) to an Aiven for OpenSearch one.

.. code-block:: shell

    elasticdump \
    --input=http://opensearch-url:9243/INDEX_NAME \
    --output=SERVICE_URI/INDEX_NAME \
    --type=data

When the dump is completed, you can check that the index is available in the OpenSearch service you send it to. You will be able to find it under the **Indexes** tab in your Aiven console.

.. _copy-data-from-os-to-s3:

Copying data from Aiven OpenSearch to AWS S3
--------------------------------------------

Prerequisites
~~~~~~~~~~~~~

* Aiven for OpenSearch cluster as the ``input``
* AWS S3 bucket as the ``output``

You need to collect this information about your Aiven for OpenSearch cluster and your AWS service:

Aiven for OpenSearch:

* ``SERVICE_URI``: OpenSearch service URI, which you can find in Aiven's dashboard.
* ``INDEX_NAME``: the name of the index that you aim to backup.

AWS S3:

* AWS credentials (``ACCESS_KEY_ID`` and ``SECRET_ACCESS_KEY``).
* S3 file path, with the bucket name and file name, for e.g. ``s3://${BUCKET_NAME}/${FILE_NAME}.json``

.. seealso::

    You can find more information about AWS credentials in the `AWS documentation <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html>`_.


Export OpenSearch index data to S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``elasticsearch-dump`` command to copy the data from your **Aiven OpenSearch cluster** to your **AWS S3 bucket**. Use your Aiven OpenSearch ``SERVICE_URI`` for the ``input`` . For the ``output``, choose an AWS S3 file path including the file name that you want for your document. 


.. code-block:: shell

    elasticdump \
    --s3AccessKeyId "${ACCESS_KEY_ID}" \
    --s3SecretAccessKey "${SECRET_ACCESS_KEY}" \
    --input=SERVICE_URI/index_name --output "s3://${BUCKET_NAME}/${FILE_NAME}.json"  

Resources
---------

Aiven for OpenSearch databases are automatically backed up, so you can check more information about how the :ref:`Backup process works <opensearch-backup>`.
