
const fs = require('fs');
const pg = require('pg');

const config = {
    connectionString: POSTGRESQL_URI
    ssl: {
        rejectUnauthorized: false,
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
