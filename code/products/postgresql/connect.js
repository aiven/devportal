const fs = require('fs');
const pg = require('pg');
const url = require('url');

postgresql_uri = POSTGRESQL_URI;

conn = new URL(postgresql_uri);
conn.search = conn.query = "";

const config = {
    connectionString: conn.href,
    ssl: {
        rejectUnauthorized: true,
        ca: fs.readFileSync('./ca.pem').toString(),
    },
};

const client = new pg.Client(config);
client.connect(function (err) {
    if (err)
        throw err;
    client.query("SELECT VERSION()", [], function (err, result) {
        if (err)
            throw err;

        console.log(result.rows[0]);
        client.end(function (err) {
            if (err)
                throw err;
        });
    });
});
