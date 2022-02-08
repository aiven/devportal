INSERT INTO CPU_OUT_OS
SELECT
    DATE_FORMAT(time_ltz, 'yyyy/MM/dd hh:mm:ss'),
    hostname,
    cpu,
    usage,
    threshold
FROM CPU_OUT_FILTER_PG
WHERE hostname in ('happy','sleepy')