Enable Karapace schema registry authorization
=============================================

Schema registry authorization feature enabled in :doc:`Karapace schema registry <../howto/enable-karapace>`  allows you to both authenticate the user, and additionally grant or deny access to individual `Karapace schema registry REST API endpoints <https://github.com/aiven/karapace>`_ and filters the content the endpoints return.

Enable Karapace schema registry authorization via Aiven CLI
-----------------------------------------------------------

Karapace schema registry authorization has been available in Aiven since 2022-06-30 in all Aiven for Apache Kafka® services created after that date have it enabled by default and it's not possible to disable it.  Aiven-client version 2.16 or later is required for enabling Karapace schema registry authorization via Aiven CLI.

For the services created before 2022-06-30 the feature needs to be enabled using the following :doc:`Aiven CLI </docs/tools/cli>` command by substituting the ``SERVICE_NAME`` placeholder with the name of the Aiven for Apache Kafka service where to enable Karapace schema registry authorization::

    avn service update --enable-schema-registry-authorization SERVICE_NAME

Karapace schema registry authorization can be similarly be disabled using::

    avn service update --disable-schema-registry-authorization SERVICE_NAME

.. Note::

    Enabling Karapace schema registry authorization can lead to access rights issues if the ACL hasn't been configured properly.


.. Warning::

    Currently there's no `Aiven Console <https://console.aiven.io/>`_ support for Karapace schema registry authentication management. Enabling it, and managing the ACL entries can only be done using Aiven Client. Console support will be added later.