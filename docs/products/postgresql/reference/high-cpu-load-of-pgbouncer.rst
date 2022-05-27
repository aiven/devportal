High CPU load when using PgBouncer
==================================

PgBouncer is a lightweight connection pooler for PostgreSQL®. For the setup and configurations of PgBouncer please refer to this `help article. <https://developer.aiven.io/docs/products/postgresql/concepts/pg-connection-pooling.html>`_

During the usage of PgBouncer pooling, you may see a high percentage of CPU load by PgBouncer, which indicates a problem with the usage pattern.
Historically, the reason for the high CPU usage in PgBouncer is most likely the high incoming SSL connection rate. SSL handshakes cost quite a bit when the user run the query and then disconnect/reconnect again for the next query.

So the best practice would be to keep a connection open and re-use it if possible. Spamming PgBouncer with hundreds of new connection requests per second will work but will result in high CPU usage, which means all the software running on the node will be affected, including PostgreSQL®.

If you have followed the recommendations in this article and still facing problems, you can contact the ``support@aiven.io`` for further investigation.