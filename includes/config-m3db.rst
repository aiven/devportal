
``custom_domain`` => *['string', 'null']*
  **Custom domain** Serve the web frontend using a custom CNAME pointing to the Aiven DNS name



``ip_filter`` => *array*
  **IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips`` => *boolean*
  **Static IP addresses** Use static public IP addresses



``limits`` => *object*
  **M3 limits** 

  ``query_series`` => *integer*
    **The maximum number of series fetched in single query.** 

  ``query_docs`` => *integer*
    **The maximum number of docs fetched in single query.** 

  ``query_require_exhaustive`` => *boolean*
    **Require exhaustive result** When query limits are exceeded, whether to return error or return partial results.

  ``max_recently_queried_series_disk_bytes_read`` => *integer*
    **The maximum number of disk bytes that can be read in a given lookback period.** 

  ``max_recently_queried_series_blocks`` => *integer*
    **The maximum number of blocks that can be read in a given lookback period.** 

  ``max_recently_queried_series_lookback`` => *string*
    **The lookback period for 'max_recently_queried_series_blocks' and 'max_recently_queried_series_disk_bytes_read'.** 



``m3coordinator_enable_graphite_carbon_ingest`` => *boolean*
  **Enable Graphite ingestion using Carbon plaintext protocol** Enables access to Graphite Carbon plaintext metrics ingestion. It can be enabled only for services inside VPCs. The metrics are written to aggregated namespaces only.



``private_access`` => *object*
  **Allow access to selected service ports from private networks** 

  ``m3coordinator`` => *boolean*
    **Allow clients to connect to m3coordinator with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``public_access`` => *object*
  **Allow access to selected service ports from the public Internet** 

  ``m3coordinator`` => *boolean*
    **Allow clients to connect to m3coordinator from the public internet for service nodes that are in a project VPC or another type of private network** 



``m3_version`` => *['string', 'null']*
  **M3 major version (deprecated, use m3db_version)** 



``m3db_version`` => *['string', 'null']*
  **M3 major version (the minimum compatible version)** 



``namespaces`` => *array*
  **List of M3 namespaces** 



``rules`` => *object*
  **M3 rules** 

  ``mapping`` => *array*
    **List of M3 mapping rules** 



``service_to_fork_from`` => *['string', 'null']*
  **Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from`` => *['string', 'null']*
  **Name of another project to fork a service from. This has effect only when a new service is being created.** 



