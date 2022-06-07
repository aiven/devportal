const { Client } = require('pg');

const CA_CERT = `-----BEGIN CERTIFICATE-----
MIIEQTCCAqmgAwIBAgIUWzk7WT+z/d0XDB4aVliDlO+p3LQwDQYJKoZIhvcNAQEM
BQAwOjE4MDYGA1UEAwwvYjJiZDJjOTAtZWMwOS00MzE3LWIzZmMtNWI3ODNmNWU2
MWM2IFByb2plY3QgQ0EwHhcNMjEwNjAyMTA0OTA1WhcNMzEwNTMxMTA0OTA1WjA6
MTgwNgYDVQQDDC9iMmJkMmM5MC1lYzA5LTQzMTctYjNmYy01Yjc4M2Y1ZTYxYzYg
UHJvamVjdCBDQTCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBAN+BOq7T
+fI3NV5l0/fisXQMX9GvuqSFAkq8TlGiB6SkGjwxMyMxi5fX876N4M05V5B6YON8
KEvHm3A1pzRJGGjfllPKW/WTweBW1WWzgsQeP+Qm82/1ty8MLYnt+IcmEPH3hav/
d3amGRf4UbR9XgKHp2AkQ5N3mctxEmZjlNgQnQ540VXEFGpTZMWSK7q8bZluKGbL
tLRsk7yH1oWlPHcXNxRJqMrVQQe3zLH9/cN9VRO7n+edQ1R4WN5OT9He+Xzf2sSQ
xxVfvXQ8Wy/sAa13ow3cv/EmP4Ilxd9jObi0bsxHRD/naeJXGZzcklAQ4qmeVVI8
grTuW3kHuWSCT1WWLWfGJJdwzTUZyaH125tehgUggEMuh/kkEWLrZwLlJTZzD32Q
8ONwL0X9QjvFgejAJCQhpENREf1dlkMa8gbprv3c9Dxd7kmZgpajdv09WwDqQQYS
N7Q2VABf8eAu4t4/AWHcaM0STNm9vCaUVQW3/gf/20H70L8PlOGeRb8MjQIDAQAB
oz8wPTAdBgNVHQ4EFgQUXxUYWQx7MwNj8brNLUMaPRxJhNgwDwYDVR0TBAgwBgEB
/wIBADALBgNVHQ8EBAMCAQYwDQYJKoZIhvcNAQEMBQADggGBAMwLodo+0s6M/ueg
q73t8rP2L7o9J0odWOaOrUFODZwQytjo5H84FN3s2Ufufz/Mrs9RrCCH2SmDE5NC
kWsPkwXU68vfA6Mow9JB1bvcsHpLhPLN4Py7UxSw47alkyDfldB9/2ZnNHhlG32I
8kPHFAt6ZDziPhzVn9I+m0P3aThQ0iouqY8/t9Zx1SfoA5yYwYdKH9j29UFmUrxV
hem4kMZSZFSQw4Zu50vjBtN2uop4nMZm1wAgpKLcnwwNccfzXZ5xx7MG4PjJ17PP
Csxufy4QKUu/JrfBmFtzkG37YQXYDLORFs4S/kTU0CKPx7Y987b6X4wJeZPGf+SF
J05/977y9FUwH0/rNcd7CwTmGXxe5Tzl/rcCh5bVonOJAx0K1dOvOYUCMP/EHgrU
Mv0erJkJ6S0T3TMOLPNPiphzCN4DW12bH4tqUPwQSCKqGeEdBCwDleX8ZmcE967d
FiFH9jljdl+UOOzBx4BsYAWfBb3Z/ED/is54ceAAxzyz1Kv2Hg==
-----END CERTIFICATE-----
`;

const client = new Client({
  // Don't include sslmode=require
  connectionString: process.env.PG_URL,
  ssl: {
    ca: CA_CERT,
  },
});

exports.handler = async function (event) {
  // TODO: USE CODE BELOW A CLOUDFLARE REFERENCE
  // export async function onRequest(context) {
  //   const {
  //     request, // same as existing Worker API
  //     env, // same as existing Worker API
  //     params, // if filename includes [id] or [[path]]
  //     waitUntil, // same as ctx.waitUntil in existing Worker API
  //     next, // used for middleware or to fetch assets
  //     data, // arbitrary space for passing data between middlewares
  //   } = context;

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
    body: '',
  };
};
