const fs = require('fs');
const pg = require('pg');
const path = require('path');

const postgreSqlUri = 'POSTGRESQL_URI'

const config = {
    // We need to strip the ?sslmode=required from the connection string
    // due to a bug on the `pg` library
    // https://github.com/brianc/node-postgres/issues/2558#issuecomment-855703980

    connectionString: postgreSqlUri.replace('?sslmode=require', ''),
    ssl: {
        ca: fs.readFileSync(path.join(__dirname, '/ca.pem')),
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
