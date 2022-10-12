const { Client } = require("pg");

const CA_CERT = `-----BEGIN CERTIFICATE-----
MIIEMDCCApigAwIBAgIDE0djMA0GCSqGSIb3DQEBDAUAMDoxODA2BgNVBAMMLzgx
MmRlNWRhLTBiYWItNDk5MC05MGU4LTU3MzAzZWViZmQzMCBQcm9qZWN0IENBMB4X
DTE4MTEyODEyMTg1OFoXDTI4MTEyNTEyMTg1OFowOjE4MDYGA1UEAwwvODEyZGU1
ZGEtMGJhYi00OTkwLTkwZTgtNTczMDNlZWJmZDMwIFByb2plY3QgQ0EwggGiMA0G
CSqGSIb3DQEBAQUAA4IBjwAwggGKAoIBgQCTvreUtxSGFbbWSFr3RBIVLBbUKMgS
yHMjgLzTNixQz6tPDdLWq8DtC1JmhXh1VhjCzVYdyJfTcubQ4bi0K2rPEpD9ln/y
64/blaM4kQafTboiKP+AYV7A+G0h+0uiUy06k2qlev9HIJgjfMW0bNpb0fnxvc09
X0hZCZ8wlKg67zXZRVCsIxrw1L36ECLLc+25QtCQax9+UtnCDAA//sZnEDN7stAS
YxDia6eNsPQIe7jMRypC0UAdpdqUoWlmG9g342SIZVfLNWCuBa9YU15R3FQQCpr3
mdSESEP7raEDDC7a8RbDainBSp8gdtzIkP72Y9T4846qF9ZQQ33qFLcRiRCsEjBp
oHZZl91V3zl5yEuCwpWSFHjlKiu4YLp+sYTI7npq4zmbaVclDAWR6A2G8r17zI1B
4RFgtHXdLINylAf7GI8JtzXMv2t831uUzlmE9caLQrSTcB7TZJ3X/DYbVygov8Qi
JLok7odmkHBd1gy8hM53vUm8MvawxVwX/LkCAwEAAaM/MD0wHQYDVR0OBBYEFLld
r94rp+G/bhc6ZTP4D8mEMuiIMA8GA1UdEwQIMAYBAf8CAQAwCwYDVR0PBAQDAgEG
MA0GCSqGSIb3DQEBDAUAA4IBgQBLcHLn8MW3FpObvAnkCuU1WtOR5U93w/b6Ajw6
XhkWEbqEuMhPx3nmcLIxZPuPM0reyQgcxlFfTseKjvmFWvPhmml+mJChzFp8Hzjp
cF7NUIKKiBcvDzrJadGWuXVN9pVHrua0Nh2roOA8MMY8fIws0+qrnG5VrpjeL8NI
DhYTyiq+8MU6QtPfgmaOLrruDoFtexoFuODJN5NokEoJPX3sJDll0gqBZhU1yyFL
25HuI3DGxbrJviT+vTIerRPxVAT7lYT5V2rxWui9DFXWqt7S95dIMmBRh32/tIsy
gEZ2XVVIwNQ1UhGlpgTF/rDxUuIS2SJXUxfbQqD+HbCcI4P2rnWZaXANZz/MDzCh
Hp1qs02zlit6t1DzgnS0wr3YXSGV160uWtOiIUFuHebg04BaYPLU7LpMIA0+8+kz
JiYMNk2b+h+wmZgz2a6CvU0GI/Li7wWcJUgqD5DM6+h892H855yEqg+DyjKOq3XA
9QS9/GhAhSSJsJq/uA/2Zq/+Fi4=
-----END CERTIFICATE-----

`;

exports.handler = async function (event) {
  const client = new Client({
    // Don't include sslmode=require
    connectionString: process.env.PG_URL,
    ssl: {
      ca: CA_CERT,
    },
  });
  await client.connect();

  try {
    const payload = JSON.parse(event.body);

    await client.query(
      `
    INSERT INTO feedback (referrer, vote, message, created_at)
    VALUES ($1, $2, $3, $4)
    `,
      ["aiven", payload.vote, payload.message, new Date()]
    );

    await client.end();

    return {
      statusCode: 201,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers":
          "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
      },
      body: JSON.stringify(payload),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: JSON.stringify(err),
      }),
    };
  }
};
