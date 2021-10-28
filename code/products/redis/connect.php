<?php

require 'vendor/autoload.php';
Predis\Autoloader::register();

$redis_uri = 'REDIS_URI';

$client = new Predis\Client($redis_uri);

$client->set('key', 'hello world');
$value = $client->get('key');

echo "The value of key is: {$value}";