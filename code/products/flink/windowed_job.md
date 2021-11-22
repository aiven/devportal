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