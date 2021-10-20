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
INSERT INTO CPU_OUT_FILTER Select time_ltz, hostname, cpu, usage FROM CPU_IN WHERE usage > 80

## Windowed pipeline: CPU_OUT_AGG table
window_start TIMESTAMP(3),
window_end TIMESTAMP(3),
hostname STRING,
cpu STRING,
usage_avg DOUBLE,
usage_max DOUBLE,
PRIMARY KEY (window_start, window_end, hostname, cpu) NOT ENFORCED

## Windowed pipeline: job
INSERT INTO CPU_OUT_AGG
select window_start,window_end, hostname, cpu, avg(usage), max(usage)
FROM TABLE( TUMBLE(TABLE CPU_IN, DESCRIPTOR(time_ltz), INTERVAL '30' SECONDS))
GROUP BY window_start,window_end, hostname, cpu

## PostgreSQL thresholds: cpu_thresholds table creation
create table cpu_thresholds (hostname varchar, allowed_top int);
insert into cpu_thresholds values ('doc', 20),('grumpy', 30),('sleepy',40),('bashful',60), ('happy',70),('sneezy',80),('dopey',90)
select * from cpu_thresholds

## PostgreSQL thresholds: SOURCE_THRESHOLDS table
hostname string,
allowed_top int,
PRIMARY KEY (hostname) NOT ENFORCED

## PostgreSQL thresholds: CPU_OUT_FILTER_PG table
time_ltz TIMESTAMP(3),
hostname STRING,
cpu STRING,
usage DOUBLE,
threshold INT

## PostgreSQL thresholds: job
INSERT INTO CPU_OUT_FILTER_PG Select time_ltz, cpu.hostname, cpu, usage, allowed_top FROM CPU_IN cpu inner join SOURCE_THRESHOLDS FOR SYSTEM_TIME AS OF proctime as st on cpu.hostname = st.hostname WHERE usage > allowed_top

## Combined pipeline: cpu_load_stats_agg_pg table creation:
create table cpu_load_stats_agg_pg (time_ltz TIMESTAMP(3) PRIMARY KEY, NR_CPUS_OVER_THRESHOLD int);

## Combined pipeline: CPU_OUT_AGG_PG table:
time_ltz TIMESTAMP(3),
NR_CPUS_OVER_THRESHOLD BIGINT,
PRIMARY KEY (time_ltz) NOT ENFORCED

## Combined pipeline: job
INSERT INTO CPU_OUT_AGG_PG with joining_info as(
Select time_ltz, cpu.hostname, cpu, usage, allowed_top FROM CPU_IN cpu inner join SOURCE_THRESHOLDS FOR SYSTEM_TIME AS OF proctime as st on cpu.hostname = st.hostname
),
windowing as (
select window_start,window_end, hostname, cpu, avg(usage) usage, allowed_top
FROM TABLE(
TUMBLE(TABLE joining_info, DESCRIPTOR(time_ltz), INTERVAL '30' SECONDS))
GROUP BY window_start,window_end, hostname, cpu, allowed_top
)
select window_start, count(*) from windowing
where usage>allowed_top
group by window_start
