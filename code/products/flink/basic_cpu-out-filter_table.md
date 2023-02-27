CREATE TABLE CPU_OUT_FILTER (
    time_ltz TIMESTAMP(3),
    hostname STRING,
    cpu STRING,
    usage DOUBLE
    )
WITH (
   'connector' = 'kafka',
   'properties.bootstrap.servers' = '',
   'topic' = 'cpu_load_stats_real_filter',
   'value.format' = 'json',
   'scan.startup.mode' = 'earliest-offset'
)