CREATE TABLE CPU_THRESHOLDS(
    hostname STRING,
    allowed_top INT,
    PRIMARY KEY (hostname) NOT ENFORCED
    )
WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://',
    'table-name' = 'public.cpu_thresholds'
)