Manage large shards in OpenSearch®
=====================================

Ensuring an optimal shard size is a critical consideration when operating within OpenSearch. It is recommended that the size of individual shards in OpenSearch® should not exceed 50GB as a best practice.

While OpenSearch does not explicitly enforce this shard size limit. However, exceeding this limit may result in OpenSearch being unable to relocate or recover index shards, potentially leading to data loss.

Aiven proactively monitors shard sizes for all OpenSearch services. If a service's shard exceeds the recommended size, prompt notifications are sent using the user alert ``user_alert_resource_usage_es_shard_too_large``. Below, you'll find recommended solutions on how to address this alert.


Solutions to address large shards
-----------------------------------
When dealing with excessively large shards, you can consider the one of the following solutions:

1. Delete records from the index
`````````````````````````````````
If your application permits, permanently delete records, such as old logs or unnecessary records, from your index. For example, to delete records older than five days, use the following query:

::

   POST /my-index/_delete_by_query
   {
     "query": {
        "range" : {
            "@timestamp" : {
          
                 "lte" : now-5d

               }
           }
       }
   }


2. Re-index into several small indices
```````````````````````````````````````
You can split your index into several smaller indices based on certain criteria. For example, to create an index for each ``event_type``, you can use following script::


   POST _reindex
   {

     "source": {
	   "index": "logs-all-events"
     },
     "dest": {
   	   "index": "logs-2-"
     },
     "script": {
 	   "lang": "painless",
	   "source": "ctx._index = 'logs-2-' + (ctx._source.event_type)"
     }
   }


3. Re-index into a new index with increased shard count
`````````````````````````````````````````````````````````
Another strategy involves re-indexing data into a fresh index while increasing the number of shards. To create a new index with 2 shards, use the following commands:

.. code-block:: python

   PUT /my_new_index/_settings
   {
       "index" : {
           "number_of_shards" : 2
       }
   }


Once the new index is set up, proceed to re-index your data using the following commands:

.. code-block:: python

   POST _reindex
   {
     "source": {
       "index": "my_old_index"
     },
     "dest": {
       "index": "my_new_index"
     }
   }



