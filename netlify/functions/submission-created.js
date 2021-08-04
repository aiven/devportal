const fs = require("fs");
const path = require("path");
const { Client } = require("pg");

const client = new Client({
  // Don't include sslmode=require
  connectionString: process.env.PG_URL,
  ssl: {
    ca: fs.readFileSync(path.join(__dirname, "ca.pem")),
  },
});

exports.handler = async function (event) {
  await client.connect();

  const payload = JSON.parse(event.body).payload;

  await client.query(
    `
    INSERT INTO feedback (referrer, vote, message, created_at)
    VALUES ($1, $2, $3, $4)
    `,
    [
      payload.data.referrer,
      payload.data.vote,
      payload.data.message,
      payload.created_at,
    ]
  );

  await client.end();

  return {
    statusCode: 201,
    body: "",
  };
};
