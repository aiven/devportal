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
WHERE USAGE > allowed_top
GROUP BY 
    window_start
