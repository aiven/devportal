hostname STRING,
cpu STRING,
usage DOUBLE,
occurred_at BIGINT,
proctime AS PROCTIME(),
time_ltz AS TO_TIMESTAMP_LTZ(occurred_at, 3),
WATERMARK FOR time_ltz AS time_ltz - INTERVAL '10' SECOND