INSERT INTO SLACK_SINK
SELECT
    '$CHANNEL_ID', 
    'host:' || CPU.hostname || 
    ' CPU: ' || cpu || 
    ' avg CPU value:' ||  TRY_CAST(usage_avg as string) || 
    ' over the threshold ' || TRY_CAST(allowed_top as string)
FROM CPU_IN_AGG CPU INNER JOIN CPU_THRESHOLDS
    ON CPU.hostname = CPU_THRESHOLDS.hostname 
WHERE usage_avg > allowed_top