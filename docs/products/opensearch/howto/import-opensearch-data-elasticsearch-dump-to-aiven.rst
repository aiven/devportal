Copy data from OpenSearch to Aiven for OpenSearch® using ``elasticsearch-dump``
===============================================================================

It is a good practice to perform backups of your OpenSearch® data to another storage service. This way you can access your data and restore it if something unexpected happens to it. 

In this article, you can find out how to dump your OpenSearch data to Aiven for OpenSearch®.

To copy the index data, we will be using ``elasticsearch-dump`` `tool <https://github.com/elasticsearch-dump/elasticsearch-dump>`__. You can read the `instructions on GitHub <https://github.com/elasticsearch-dump/elasticsearch-dump/blob/master/README.md>`_ on how to install it. From this library, we will use ``elasticdump`` command to copy the input index data to an specific output. 

.. _copy-data-from-os-to-os:

Prerequisites
~~~~~~~~~~~~~

* ``elasticsearch-dump`` `tool <https://github.com/elasticsearch-dump/elasticsearch-dump>`__ installed
* OpenSearch cluster as the ``input`` (can be in Aiven or elsewhere)
* Aiven for OpenSearch cluster as the ``output``

.. note::
    
    The ``input`` and ``ouput`` can be either an OpenSearch URL or a file path (local or remote file storage). In this particular case, we are using both URLs, one from an **OpenSearch cluster** and the other one from **Aiven for OpenSearch cluster**. 


Here are some information you need to collect to copy your data:

OpenSearch cluster:

* ``INPUT_SERVICE_URI``: OpenSearch cluster URL, for e.g. ``http://opensearch-url:9243/``
* ``INPUT_INDEX_NAME``: the index that you aim to copy from your input source.

Aiven for OpenSearch:

* ``OUTPUT_INDEX_NAME``: the index that you want to have in your output with the copied data.
* ``SERVICE_URI``: OpenSearch service URI. You can find it in Aiven's dashboard.

Import mapping
~~~~~~~~~~~~~~

The process of defining how a document and the fields are stored and indexed is called mapping. When no data structure is specified, we rely on OpenSearch to automatically detect the fields using dynamic mapping. However, we can set our data mapping before the data is sent:

.. code-block:: shell

    elasticdump \
    --input=INPUT_SERVICE_URI/INPUT_INDEX_NAME \
    --output=SERVICE_URI/OUTPUT_INDEX_NAME \
    --type=mapping


Import data 
~~~~~~~~~~~

This is how you can copy your index data from an OpenSearch cluster (can be in Aiven or elsewhere) to an Aiven for OpenSearch one.

.. code-block:: shell

    elasticdump \
    --input=INPUT_SERVICE_URI/INPUT_INDEX_NAME \
    --output=SERVICE_URI/OUTPUT_INDEX_NAME \
    --type=data

When the dump is completed, you can check that the index is available in the OpenSearch service you send it to. You will be able to find it under the **Indexes** tab in your Aiven console.

Resources
---------

Aiven for OpenSearch databases are automatically backed up, so you can check more information about how the :ref:`Backup process works <opensearch-backup>`.

-------

.. We don't directly reference Elasticsearch itself, but we do use the term
   "elasticsearch" so it is probably polite to include the following
   disclaimer

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
