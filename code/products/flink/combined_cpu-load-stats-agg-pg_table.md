CREATE TABLE CPU_LOAD_STATS_AGG_PG (
    time_ltz TIMESTAMP(3) PRIMARY KEY, 
    nr_cpus_over_threshold INT
);