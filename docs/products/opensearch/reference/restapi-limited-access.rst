REST API endpoint access
===============================================
For operational reasons, Aiven for OpenSearch® limits access to REST API endpoints. Below you can find which endpoints you can access.

The following endpoints are allowed:

::

   GET /_cluster/health
   GET /_cluster/pending_tasks
   GET /_cluster/settings
   GET /_cluster/stats
   GET /_nodes
   GET /_scripts


The following API endpoint hierarchies are
blocked:

::

   /_cat/repositories
   /_cluster
   /_snapshot

