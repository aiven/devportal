Migrate Elasticsearch data to Aiven for OpenSearch
==================================================

We recommend migrating to Aiven for OpenSearch by reindexing from
your remote cluster. The same process works for migrating from Aiven for
OpenSearch to a self-hosted Elasticsearch service.

.. tip::
    For a larger number of indexes, we recommend that you create a script to run these steps automatically.

As Aiven for OpenSearch does not support joining external
Elasticsearch servers to the same cluster, online migration is not
currently possible.

.. important::
    Migrating from Elasticsearch to OpenSearch may affect the connectivity between client applications and your service. For example, some code included in clients or tools may check the service version, which might not work with OpenSearch. We recommend that you check the following OpenSearch resources for more information:

    * `OpenSearch release notes <https://github.com/opensearch-project/OpenSearch/blob/main/release-notes/opensearch.release-notes-1.0.0.md>`_
    * `OpenSearch Dashboards release notes <https://github.com/opensearch-project/OpenSearch-Dashboards/blob/main/release-notes/opensearch-dashboards.release-notes-1.0.0.md>`_
    * `Frequently asked questions about OpenSearch <https://opensearch.org/faq/>`_


To migrate or copy data:

#. Create a hosted Aiven for OpenSearch service.

#. Use the `Aiven CLI client <https://github.com/aiven/aiven-client>`_ to set the ``reindex.remote.whitelist`` parameter to point to your source Elasticsearch service:

   ::

      avn service update your-service-name -c elasticsearch.reindex_remote_whitelist=your.non-aiven-service.example.com:9200 

   Replace the port number with the one where your source Elasticsearch service is listening.

#. Wait for the cluster to restart.
   This may take several minutes, as the service tries to do a rolling restart to minimize downtime. You do not need to power off the service.

#. Start migrating the indexes.
   For each index:

   #. Stop writes to the index.
      This step is not necessary if you are testing the process.

   #. Export mapping from your source Elasticsearch index.
      For example, using ``curl``:

      ::

         curl https://avnadmin:yourpassword@os-123-demoprj.aivencloud.com:23125/logs-2024-09-21/_mapping > mapping.json
   

      if you have ``jq`` you can run the following or else you need to manually edit ``mapping.json`` to remove the wrapping ``{"logs-2024-09-21":{"mappings": ... }}`` and keep ``{"properties":...}}``
      
      ::

         jq .[].mappings mapping.json > src_mapping.json    


   #. Create the empty index on your destination OpenSearch service.

      ::

         curl -XPUT https://avnadmin:yourpassword@os-123-demoprj.aivencloud.com:23125/logs-2024-09-21

   #. Import mapping on your destination OpenSearch index.

      ::

         curl -XPUT https://avnadmin:yourpassword@os-123-demoprj.aivencloud.com:23125/logs-2024-09-21 \
         -H 'Content-type: application/json' -T src_mapping.json
   #. Submit the reindexing request.

      ::

         curl -XPOST https://avnadmin:yourpassword@os-123-demoprj.aivencloud.com:23125/_reindex \
           -H 'Content-type: application/json' \
           -d '{"source": 
                   {"index": "logs-2024-09-21", 
                    "remote": 
                        {"username": "your-remote-username",
                         "password": "your-remote-password",
                         "host": "https://your.non-aiven-service.example.com:9200"
                        }
                   }, 
                "dest": 
                   {"index": "logs-2024-09-21"}
               }'

   #. Wait for the reindexing process to finish.
      If you see a message like the following in the response, check that the host name and port match the ones that you set earlier:

      ::

         [your.non-aiven-service.example.com:9200] not whitelisted in reindex.remote.whitelist

      Depending on the amount of data that you have, reindexing may take a significant amount of time.

   #. Point clients to use that index from Aiven for OpenSearch for both read and write operations and resume any write activity.

   #. Delete the source index if necessary.

