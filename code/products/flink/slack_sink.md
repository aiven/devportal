create table SLACK_SINK (
    channel_id STRING,
    message STRING
) WITH (
    'connector' = 'slack',
    'token' = '$SLACK_TOKEN'
)