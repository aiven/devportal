Resolve shards too large
==========================

It is a best practice that OpenSearch® shard size should not go above 50GB for a single shard.  

The limit for shard size is not directly enforced by OpenSearch. However, if you go above this limit you can find that OpenSearch is unable to relocate or recover index shards (with the consequence of possible loss of data).

At Aiven, we monitor the size of the shard for all OpenSearch services. We will send out a user alert ``user_alert_resource_usage_es_shard_too_large`` to the customer if we find the service's shard is too large. You can find information on what to do if you receive this user alert below.

How to resolve this issue
-------------------------
If your shards are too large, then you have 3 options:

**1. Delete records from the index**

If appropriate for your application, you may consider permanently deleting records from your index (for example old logs or other unnecessary records).::

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

**2. Re-index into several small indices**

The following would reindex into one index for each event_type.::

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

**3. Re-index into another single index but increase the number of shards**

.. code-block:: python

   PUT /my_new_index/_settings
   {
       "index" : {
           "number_of_shards" : 2
       }
   }

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



