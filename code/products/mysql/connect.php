<?php

$uri = "MYSQL_URI";

$fields = parse_url($uri);

// build the DSN including SSL settings
$conn = "mysql:";
$conn .= "host=" . $fields["host"];
$conn .= ";port=" . $fields["port"];;
$conn .= ";dbname=defaultdb";
$conn .= ";sslmode=verify-ca;sslrootcert=ca.pem";

$db = new PDO($conn, $fields["user"], $fields["pass"]);

foreach ($db->query("SELECT VERSION()") as $row) {
    print($row[0]);
}
