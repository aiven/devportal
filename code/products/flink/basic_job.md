INSERT INTO CPU_OUT_FILTER 
SELECT 
    time_ltz, 
    hostname, 
    cpu, 
    usage 
FROM CPU_IN 
WHERE usage > 80