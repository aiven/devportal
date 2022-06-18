
``custom_domain`` => *['string', 'null']*
  **Custom domain** Serve the web frontend using a custom CNAME pointing to the Aiven DNS name



``ip_filter`` => *array*
  **IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips`` => *boolean*
  **Static IP addresses** Use static public IP addresses



``private_access`` => *object*
  **Allow access to selected service ports from private networks** 

  ``influxdb`` => *boolean*
    **Allow clients to connect to influxdb with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access`` => *object*
  **Allow access to selected service components through Privatelink** 

  ``influxdb`` => *boolean*
    **Enable influxdb** 



``public_access`` => *object*
  **Allow access to selected service ports from the public Internet** 

  ``influxdb`` => *boolean*
    **Allow clients to connect to influxdb from the public internet for service nodes that are in a project VPC or another type of private network** 



``recovery_basebackup_name`` => *string*
  **Name of the basebackup to restore in forked service** 



``influxdb`` => *object*
  **influxdb.conf configuration values** 

  ``log_queries_after`` => *integer*
    **The maximum duration in seconds before a query is logged as a slow query. Setting this to 0 (the default) will never log slow queries.** 

  ``max_row_limit`` => *integer*
    **The maximum number of rows returned in a non-chunked query. Setting this to 0 (the default) allows an unlimited number to be returned.** 

  ``max_select_buckets`` => *integer*
    **The maximum number of `GROUP BY time()` buckets that can be processed in a query. Setting this to 0 (the default) allows an unlimited number to be processed.** 

  ``max_select_point`` => *integer*
    **The maximum number of points that can be processed in a SELECT statement. Setting this to 0 (the default) allows an unlimited number to be processed.** 

  ``query_timeout`` => *integer*
    **The maximum duration in seconds before a query is killed. Setting this to 0 (the default) will never kill slow queries.** 

  ``max_connection_limit`` => *integer*
    **Maximum number of connections to InfluxDB. Setting this to 0 (default) means no limit. If using max_connection_limit, it is recommended to set the value to be large enough in order to not block clients unnecessarily.** 



``service_to_fork_from`` => *['string', 'null']*
  **Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from`` => *['string', 'null']*
  **Name of another project to fork a service from. This has effect only when a new service is being created.** 



