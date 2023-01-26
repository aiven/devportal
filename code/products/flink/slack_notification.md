INSERT INTO SLACK_SINK
SELECT
    <CHANNEL_ID>, 
    "host:" || hostname || 
    " CPU: " || cpu || 
    " avg CPU value:" ||  cast(usage_avg as string) || 
    " over the threshold " || cast(allowed_top as text)
FROM CPU_IN_AGG CPU INNER JOIN CPU_THRESHOLDS
    ON CPU.hostname = CPU_THRESHOLDS.hostname 
WHERE usage_avg > allowed_top