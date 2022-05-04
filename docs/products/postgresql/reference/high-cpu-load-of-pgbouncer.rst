High CPU load when using PgBouncer for Aiven for PostgreSQL®
============================================================

PgBouncer is a Lightweight connection pooler for PostgreSQL. For the setup and configurations of PgBouncer please refer to this `help article. <https://developer.aiven.io/docs/products/postgresql/concepts/pg-connection-pooling.html>`_

During the usage of PgBouncer pooling, you may see high percentage of CPU load by PgBouncer, which indicates a problem of the usage pattern.
Historically, the reason of high CPU usage in PgBouncer is most likely the high incoming SSL connection rate. SSL handshakes cost quite a bit when you have clients that run query and then disconnect/reconnect again for next query.

So best practice would be keeping a connection open and re-use it if possible, spamming PgBouncer with hundreds of new connection requests per second will somehow work but will be reflected in high CPU usage which means all the software running on the node will be affected including PostgreSQL.

If the settings above has been checked, and looks all good, please contact our support team via ``support@aiven.io`` for further investigation.