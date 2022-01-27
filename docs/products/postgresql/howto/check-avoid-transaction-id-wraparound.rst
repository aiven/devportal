Check and avoid transaction ID wraparound
=========================================

The PostgreSQL® transaction control mechanism assigns a transaction ID to every row that is modified in the database; these IDs control the visibility of that row to other concurrent transactions.

The transaction ID is a 32-bit number, where 2 billion (2 thousand million) IDs are always in the "visible past" and the remainder (about 2.2 billion) are reserved for future transactions and not visible to the running transaction. To avoid a transaction wraparound and having old, existing rows invisible when more transactions are created, PostgreSQL® requires an occasional cleanup and "freezing" of old rows. 

You can do this manually by executing ``VACUUM FREEZE``, but the autovacuum also does this automatically once a configured number of transactions have been created since the last freeze.

Aiven for PostgreSQL® sets that number to scale according to the database size, up to 1.5 billion transactions (which leaves 500 million transaction IDs available before a forced freeze), to avoid unnecessary churn for stable data in existing tables. To check your transaction freeze limits, run the following command in your PostgreSQL® instance::

    show autovacuum_freeze_max_age

This shows you the number of transactions that trigger autovacuum to start freezing old rows.

Some applications may not automatically adjust their configuration based on the actual PostgreSQL® configuration and may show unnecessary warnings. For example, `PgHero <https://github.com/ankane/pghero>`_'s default settings trigger an alert once 500 million transactions have been created, while the correct behavior might be to trigger an alert after 1.5 billion transactions. The ``transaction_id_danger`` setting controls this behavior, and changing the value from 1500000000 (1,500,000,000 or 1.5 billion) to 500000000 (500,000,000 or 500 million) would make it warn you when appropriate.

For more information, see the PostgreSQL® documentation:

* `25.1.5. Preventing Transaction ID Wraparound Failures <https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND>`_
* `Table 9.76. Transaction ID and Snapshot Information Functions <https://www.postgresql.org/docs/14/functions-info.html#FUNCTIONS-PG-SNAPSHOT>`_
