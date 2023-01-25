CREATE TABLE CPU_IN (
    hostname STRING,
    cpu STRING,
    usage DOUBLE,
    occurred_at BIGINT,
    time_ltz AS TO_TIMESTAMP_LTZ(occurred_at, 3),
    WATERMARK FOR time_ltz AS time_ltz - INTERVAL '10' SECOND
    )
WITH (
   'connector' = 'kafka',
   'properties.bootstrap.servers' = '',
   'topic' = 'cpu_load_stats_real',
   'value.format' = 'json',
   'scan.startup.mode' = 'earliest-offset'
)