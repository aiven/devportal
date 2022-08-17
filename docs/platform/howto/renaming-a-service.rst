Renaming a service
==================

Currently Aiven does not support renaming existing service. Service name can only be set when creating the service.

If you need to have your service running under a different name, the best option is to create a database fork and pointing clients to the new database. Do note that after creating a fork, writes to the original database are not synced, so database writes should be stopped before forking.

Learn more :doc:`about service forking <../concepts/service-forking>`.

Get in touch with Aiven support either over Intercom chat or with support@aiven.io email in case you have questions about the process.
