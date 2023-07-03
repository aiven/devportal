CREATE TABLE CPU_OUT_AGG(
    window_start TIMESTAMP(3),
    window_end TIMESTAMP(3),
    hostname STRING,
    cpu STRING,
    usage_avg DOUBLE,
    usage_max DOUBLE
    )
WITH (
   'connector' = 'kafka',
   'properties.bootstrap.servers' = '',
   'topic' = 'cpu_agg_stats',
   'value.format' = 'json',
   'scan.startup.mode' = 'earliest-offset'
)