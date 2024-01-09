
``additional_backup_regions``
-----------------------------
*array*

**Additional Cloud Regions for Backup Replication** 



``opensearch_version``
----------------------
*['string', 'null']*

**OpenSearch major version** 



``disable_replication_factor_adjustment``
-----------------------------------------
*['boolean', 'null']*

**Disable replication factor adjustment** DEPRECATED: Disable automatic replication factor adjustment for multi-node services. By default, Aiven ensures all indexes are replicated at least to two nodes. Note: Due to potential data loss in case of losing a service node, this setting can no longer be activated.



``custom_domain``
-----------------
*['string', 'null']*

**Custom domain** Serve the web frontend using a custom CNAME pointing to the Aiven DNS name



``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``service_log``
---------------
*['boolean', 'null']*

**Service logging** Store logs for the service so that they are available in the HTTP API and console.



``static_ips``
--------------
*boolean*

**Static IP addresses** Use static public IP addresses



``saml``
--------
*object*

**OpenSearch SAML configuration** 

``enabled``
~~~~~~~~~~~
*boolean*

**Enable or disable OpenSearch SAML authentication** Enables or disables SAML-based authentication for OpenSearch. When enabled, users can authenticate using SAML with an Identity Provider.

``idp_metadata_url``
~~~~~~~~~~~~~~~~~~~~
*string*

**Identity Provider (IdP) SAML metadata URL** The URL of the SAML metadata for the Identity Provider (IdP). This is used to configure SAML-based authentication with the IdP.

``idp_entity_id``
~~~~~~~~~~~~~~~~~
*string*

**Identity Provider Entity ID** The unique identifier for the Identity Provider (IdP) entity that is used for SAML authentication. This value is typically provided by the IdP.

``sp_entity_id``
~~~~~~~~~~~~~~~~
*string*

**Service Provider Entity ID** The unique identifier for the Service Provider (SP) entity that is used for SAML authentication. This value is typically provided by the SP.

``subject_key``
~~~~~~~~~~~~~~~
*['string', 'null']*

**SAML response subject attribute** Optional. Specifies the attribute in the SAML response where the subject identifier is stored. If not configured, the NameID attribute is used by default.

``roles_key``
~~~~~~~~~~~~~
*['string', 'null']*

**SAML response role attribute** Optional. Specifies the attribute in the SAML response where role information is stored, if available. Role attributes are not required for SAML authentication, but can be included in SAML assertions by most Identity Providers (IdPs) to determine user access levels or permissions.

``idp_pemtrustedcas_content``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['string', 'null']*

**PEM-encoded root CA Content for SAML IdP server verification** This parameter specifies the PEM-encoded root certificate authority (CA) content for the SAML identity provider (IdP) server verification. The root CA content is used to verify the SSL/TLS certificate presented by the server.



``openid``
----------
*object*

**OpenSearch OpenID Connect Configuration** 

``enabled``
~~~~~~~~~~~
*boolean*

**Enable or disable OpenSearch OpenID Connect authentication** Enables or disables OpenID Connect authentication for OpenSearch. When enabled, users can authenticate using OpenID Connect with an Identity Provider.

``connect_url``
~~~~~~~~~~~~~~~
*string*

**OpenID Connect metadata/configuration URL** The URL of your IdP where the Security plugin can find the OpenID Connect metadata/configuration settings.

``roles_key``
~~~~~~~~~~~~~
*['string', 'null']*

**The key in the JSON payload that stores the user’s roles** The key in the JSON payload that stores the user’s roles. The value of this key must be a comma-separated list of roles. Required only if you want to use roles in the JWT

``subject_key``
~~~~~~~~~~~~~~~
*['string', 'null']*

**The key in the JSON payload that stores the user’s name** The key in the JSON payload that stores the user’s name. If not defined, the subject registered claim is used. Most IdP providers use the preferred_username claim. Optional.

``jwt_header``
~~~~~~~~~~~~~~
*['string', 'null']*

**The HTTP header that stores the token** The HTTP header that stores the token. Typically the Authorization header with the Bearer schema: Authorization: Bearer <token>. Optional. Default is Authorization.

``jwt_url_parameter``
~~~~~~~~~~~~~~~~~~~~~
*['string', 'null']*

**URL JWT token.** If the token is not transmitted in the HTTP header, but as an URL parameter, define the name of the parameter here. Optional.

``refresh_rate_limit_count``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**The maximum number of unknown key IDs in the time frame** The maximum number of unknown key IDs in the time frame. Default is 10. Optional.

``refresh_rate_limit_time_window_ms``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**The time frame to use when checking the maximum number of unknown key IDs, in milliseconds** The time frame to use when checking the maximum number of unknown key IDs, in milliseconds. Optional.Default is 10000 (10 seconds).

``client_id``
~~~~~~~~~~~~~
*string*

**The ID of the OpenID Connect client** The ID of the OpenID Connect client configured in your IdP. Required.

``client_secret``
~~~~~~~~~~~~~~~~~
*string*

**The client secret of the OpenID Connect** The client secret of the OpenID Connect client configured in your IdP. Required.

``scope``
~~~~~~~~~
*string*

**The scope of the identity token issued by the IdP** The scope of the identity token issued by the IdP. Optional. Default is openid profile email address phone.

``header``
~~~~~~~~~~
*string*

**HTTP header name of the JWT token** HTTP header name of the JWT token. Optional. Default is Authorization.



``index_patterns``
------------------
*array*

**Index patterns** 



``max_index_count``
-------------------
*integer*

**Maximum index count** DEPRECATED: use index_patterns instead



``keep_index_refresh_interval``
-------------------------------
*boolean*

**Don't reset index.refresh_interval to the default value** Aiven automation resets index.refresh_interval to default value for every index to be sure that indices are always visible to search. If it doesn't fit your case, you can disable this by setting up this flag to true.



``opensearch_dashboards``
-------------------------
*object*

**OpenSearch Dashboards settings** 

``enabled``
~~~~~~~~~~~
*boolean*

**Enable or disable OpenSearch Dashboards** 

``max_old_space_size``
~~~~~~~~~~~~~~~~~~~~~~
*integer*

**max_old_space_size** Limits the maximum amount of memory (in MiB) the OpenSearch Dashboards process can use. This sets the max_old_space_size option of the nodejs running the OpenSearch Dashboards. Note: the memory reserved by OpenSearch Dashboards is not available for OpenSearch.

``opensearch_request_timeout``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Timeout in milliseconds for requests made by OpenSearch Dashboards towards OpenSearch** 



``opensearch``
--------------
*object*

**OpenSearch settings** 

``reindex_remote_whitelist``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['array', 'null']*

**reindex_remote_whitelist** Whitelisted addresses for reindexing. Changing this value will cause all OpenSearch instances to restart.

``http_max_content_length``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**http.max_content_length** Maximum content length for HTTP requests to the OpenSearch HTTP API, in bytes.

``http_max_header_size``
~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**http.max_header_size** The max size of allowed headers, in bytes

``http_max_initial_line_length``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**http.max_initial_line_length** The max length of an HTTP URL, in bytes

``indices_query_bool_max_clause_count``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.query.bool.max_clause_count** Maximum number of clauses Lucene BooleanQuery can have. The default value (1024) is relatively high, and increasing it may cause performance issues. Investigate other approaches first before increasing this value.

``search_max_buckets``
~~~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**search.max_buckets** Maximum number of aggregation buckets allowed in a single response. OpenSearch default value is used when this is not defined.

``indices_fielddata_cache_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**indices.fielddata.cache.size** Relative amount. Maximum amount of heap memory used for field data cache. This is an expert setting; decreasing the value too much will increase overhead of loading field data; too much memory used for field data cache will decrease amount of heap available for other operations.

``indices_memory_index_buffer_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.memory.index_buffer_size** Percentage value. Default is 10%. Total amount of heap used for indexing buffer, before writing segments to disk. This is an expert setting. Too low value will slow down indexing; too high value will increase indexing performance but causes performance issues for query performance.

``indices_memory_min_index_buffer_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.memory.min_index_buffer_size** Absolute value. Default is 48mb. Doesn't work without indices.memory.index_buffer_size. Minimum amount of heap used for query cache, an absolute indices.memory.index_buffer_size minimal hard limit.

``indices_memory_max_index_buffer_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.memory.max_index_buffer_size** Absolute value. Default is unbound. Doesn't work without indices.memory.index_buffer_size. Maximum amount of heap used for query cache, an absolute indices.memory.index_buffer_size maximum hard limit.

``indices_queries_cache_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.queries.cache.size** Percentage value. Default is 10%. Maximum amount of heap used for query cache. This is an expert setting. Too low value will decrease query performance and increase performance for other operations; too high value will cause issues with other OpenSearch functionality.

``indices_recovery_max_bytes_per_sec``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.recovery.max_bytes_per_sec** Limits total inbound and outbound recovery traffic for each node. Applies to both peer recoveries as well as snapshot recoveries (i.e., restores from a snapshot). Defaults to 40mb

``indices_recovery_max_concurrent_file_chunks``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**indices.recovery.max_concurrent_file_chunks** Number of file chunks sent in parallel for each recovery. Defaults to 2.

``action_auto_create_index_enabled``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**action.auto_create_index** Explicitly allow or block automatic creation of indices. Defaults to true

``auth_failure_listeners``
~~~~~~~~~~~~~~~~~~~~~~~~~~
*object*

**Opensearch Security Plugin Settings** 

``enable_security_audit``
~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Enable/Disable security audit** 

``thread_pool_search_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**search thread pool size** Size for the thread pool. See documentation for exact details. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value.

``thread_pool_search_throttled_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**search_throttled thread pool size** Size for the thread pool. See documentation for exact details. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value.

``thread_pool_get_size``
~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**get thread pool size** Size for the thread pool. See documentation for exact details. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value.

``thread_pool_analyze_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**analyze thread pool size** Size for the thread pool. See documentation for exact details. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value.

``thread_pool_write_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**write thread pool size** Size for the thread pool. See documentation for exact details. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value.

``thread_pool_force_merge_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**force_merge thread pool size** Size for the thread pool. See documentation for exact details. Do note this may have maximum value depending on CPU count - value is automatically lowered if set to higher than maximum value.

``thread_pool_search_queue_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**search thread pool queue size** Size for the thread pool queue. See documentation for exact details.

``thread_pool_search_throttled_queue_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**search_throttled thread pool queue size** Size for the thread pool queue. See documentation for exact details.

``thread_pool_get_queue_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**get thread pool queue size** Size for the thread pool queue. See documentation for exact details.

``thread_pool_analyze_queue_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**analyze thread pool queue size** Size for the thread pool queue. See documentation for exact details.

``thread_pool_write_queue_size``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**write thread pool queue size** Size for the thread pool queue. See documentation for exact details.

``action_destructive_requires_name``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['boolean', 'null']*

**Require explicit index names when deleting** 

``cluster_max_shards_per_node``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**cluster.max_shards_per_node** Controls the number of shards allowed in the cluster per data node

``override_main_response_version``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**compatibility.override_main_response_version** Compatibility mode sets OpenSearch to report its version as 7.10 so clients continue to work. Default is false

``script_max_compilations_rate``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**Script max compilation rate - circuit breaker to prevent/minimize OOMs** Script compilation circuit breaker limits the number of inline script compilations within a period of time. Default is use-context

``cluster_routing_allocation_node_concurrent_recoveries``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**Concurrent incoming/outgoing shard recoveries per node** How many concurrent incoming/outgoing shard recoveries (normally replicas) are allowed to happen on a node. Defaults to 2.

``email_sender_name``
~~~~~~~~~~~~~~~~~~~~~
*string*

**Sender name placeholder to be used in Opensearch Dashboards and Opensearch keystore** This should be identical to the Sender name defined in Opensearch dashboards

``email_sender_username``
~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**Sender username for Opensearch alerts** 

``email_sender_password``
~~~~~~~~~~~~~~~~~~~~~~~~~
*string*

**Sender password for Opensearch alerts to authenticate with SMTP server** Sender password for Opensearch alerts to authenticate with SMTP server

``ism_enabled``
~~~~~~~~~~~~~~~
*boolean*

**Specifies whether ISM is enabled or not** 

``ism_history_enabled``
~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Specifies whether audit history is enabled or not. The logs from ISM are automatically indexed to a logs document.** 

``ism_history_max_age``
~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum age before rolling over the audit history index in hours** 

``ism_history_max_docs``
~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The maximum number of documents before rolling over the audit history index.** 

``ism_history_rollover_check_period``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**The time between rollover checks for the audit history index in hours.** 

``ism_history_rollover_retention_period``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*integer*

**How long audit history indices are kept in days.** 



``index_template``
------------------
*object*

**Template settings for all new indexes** 

``mapping_nested_objects_limit``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**index.mapping.nested_objects.limit** The maximum number of nested JSON objects that a single document can contain across all nested types. This limit helps to prevent out of memory errors when a document contains too many nested objects. Default is 10000.

``number_of_shards``
~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**index.number_of_shards** The number of primary shards that an index should have.

``number_of_replicas``
~~~~~~~~~~~~~~~~~~~~~~
*['integer', 'null']*

**index.number_of_replicas** The number of replicas each primary shard has.



``private_access``
------------------
*object*

**Allow access to selected service ports from private networks** 

``opensearch``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to opensearch with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

``opensearch_dashboards``
~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to opensearch_dashboards with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access``
----------------------
*object*

**Allow access to selected service components through Privatelink** 

``opensearch``
~~~~~~~~~~~~~~
*boolean*

**Enable opensearch** 

``opensearch_dashboards``
~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Enable opensearch_dashboards** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Enable prometheus** 



``public_access``
-----------------
*object*

**Allow access to selected service ports from the public Internet** 

``opensearch``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to opensearch from the public internet for service nodes that are in a project VPC or another type of private network** 

``opensearch_dashboards``
~~~~~~~~~~~~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to opensearch_dashboards from the public internet for service nodes that are in a project VPC or another type of private network** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** 



``recovery_basebackup_name``
----------------------------
*string*

**Name of the basebackup to restore in forked service** 



``service_to_fork_from``
------------------------
*['string', 'null']*

**Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from``
------------------------
*['string', 'null']*

**Name of another project to fork a service from. This has effect only when a new service is being created.** 



