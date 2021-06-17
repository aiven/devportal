<?php

require "vendor/autoload.php";

// create a client
$client = new InfluxDB\Client(
    SERVICE_HOST,
    SERVICE_PORT,
    "avnadmin",
    AVNADMIN_PASS,
    true,
    true,
);

// construct a data point
$point = new InfluxDB\Point(
		'php_example_metric', // name of the measurement
		0.64, // the measurement value
		['host' => 'server1', 'location' => 'EU-DE-22'], // optional tags
		['cpucount' => 8], // optional additional fields
);

// write to the database using the path
$result = $client->write(["url" => "api/v1/influxdb/write?db=default"], $point);
var_dump($result);
