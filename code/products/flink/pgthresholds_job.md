INSERT INTO CPU_OUT_FILTER_PG 
SELECT time_ltz, 
    CPU.hostname, 
    cpu, 
    usage, 
    allowed_top 
FROM CPU_IN CPU INNER JOIN SOURCE_THRESHOLDS FOR SYSTEM_TIME AS OF proctime AS ST 
    ON CPU.hostname = ST.hostname 
WHERE usage > allowed_top