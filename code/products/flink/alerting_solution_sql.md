## Basic filtering: CPU-IN table
hostname STRING,
cpu STRING,
usage DOUBLE,
occurred_at BIGINT,
proctime AS PROCTIME(),
time_ltz AS TO_TIMESTAMP_LTZ(occurred_at, 3),
WATERMARK FOR time_ltz AS time_ltz - INTERVAL '10' SECOND

## Basic filtering: CPU-OUT-FILTER table
time_ltz TIMESTAMP(3),
hostname STRING,
cpu STRING,
usage DOUBLE

## Basic filtering: job
INSERT INTO CPU_OUT_FILTER 
SELECT 
    time_ltz, 
    hostname, 
    cpu, 
    usage 
FROM CPU_IN 
WHERE usage > 80

## Windowed pipeline: CPU_OUT_AGG table
window_start TIMESTAMP(3),
window_end TIMESTAMP(3),
hostname STRING,
cpu STRING,
usage_avg DOUBLE,
usage_max DOUBLE

## Windowed pipeline: job
INSERT INTO CPU_OUT_AGG
SELECT 
    window_start,
    window_end, 
    hostname, 
    cpu, 
    AVG(usage), 
    MAX(usage)
FROM 
    TABLE( TUMBLE( TABLE CPU_IN, DESCRIPTOR(time_ltz), INTERVAL '30' SECONDS))
GROUP BY 
    window_start,
    window_end, 
    hostname, 
    cpu

## PostgreSQL thresholds: cpu_thresholds table creation
CREATE TABLE CPU_THRESHOLDS (hostname VARCHAR, allowed_top INT);
INSERT INTO CPU_THRESHOLDS VALUES ('doc', 20),('grumpy', 30),('sleepy',40),('bashful',60), ('happy',70),('sneezy',80),('dopey',90);
SELECT * FROM CPU_THRESHOLDS;

## PostgreSQL thresholds: SOURCE_THRESHOLDS table
hostname STRING,
allowed_top INT,
PRIMARY KEY (hostname) NOT ENFORCED

## PostgreSQL thresholds: CPU_OUT_FILTER_PG table
time_ltz TIMESTAMP(3),
hostname STRING,
cpu STRING,
usage DOUBLE,
threshold INT

## PostgreSQL thresholds: job
INSERT INTO CPU_OUT_FILTER_PG 
SELECT time_ltz, 
    CPU.hostname, 
    cpu, 
    usage, 
    allowed_top 
FROM CPU_IN CPU INNER JOIN SOURCE_THRESHOLDS FOR SYSTEM_TIME AS OF proctime AS ST 
    ON CPU.hostname = ST.hostname 
WHERE usage > allowed_top

## Combined pipeline: cpu_load_stats_agg_pg table creation:
CREATE TABLE CPU_LOAD_STATS_AGG_PG (
    time_ltz TIMESTAMP(3) PRIMARY KEY, 
    nr_cpus_over_threshold INT
);

## Combined pipeline: CPU_OUT_AGG_PG table:
time_ltz TIMESTAMP(3),
nr_cpus_over_threshold BIGINT,
PRIMARY KEY (time_ltz) NOT ENFORCED

## Combined pipeline: job
INSERT INTO CPU_OUT_AGG_PG 
WITH JOINING_INFO AS(
    SELECT time_ltz, 
        CPU.hostname, 
        cpu, 
        usage, 
        allowed_top 
    FROM CPU_IN CPU INNER JOIN SOURCE_THRESHOLDS 
        FOR SYSTEM_TIME AS OF proctime AS ST 
        ON CPU.hostname = ST.hostname
),
WINDOWING AS (
    SELECT 
        window_start,
        window_end, 
        hostname, 
        cpu, 
        AVG(usage) USAGE, 
        allowed_top
    FROM TABLE(TUMBLE(TABLE JOINING_INFO, DESCRIPTOR(time_ltz), INTERVAL '30' SECONDS))
    GROUP BY 
        window_start,
        window_end, 
        hostname, 
        cpu, 
        allowed_top
)
SELECT 
    window_start, 
    COUNT(*) 
FROM WINDOWING
WHERE USAGE > ALLOWED_TOP
GROUP BY 
    window_start
