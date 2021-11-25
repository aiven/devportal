Manage Apache Kafka parameters
===================================

Aiven for Apache Kafka comes by default with a preset of configuration parameters defining for example automatic topic creation, partition count, replication factor, and retention time. These service configurations can be retrieved and managed via the Aiven web console, under the *Advanced configuration* section of the *Overview*
page for your service, or using the ``-c`` options via the :ref:`Aiven CLI service update command <avn-cli-service-update>`.

.. Warning::

    Most of the Apache Kafka settings cause the service to restart when changed. Aiven for Apache Kafka restarts nodes one at a time to ensure minimal disruption to service availability. However, it can take few minutes from the change before the new settings are in use.

Retrieve the current service parameters with Aiven CLI
-----------------------------------------------------------

To retrieve the existing Aiven for Apache Kafka configuration use the following command:

::

    avn service get SERVICE_NAME --json

The output is the JSON representation of the service configuration.

Retrieve the customizable parameters with Aiven CLI
----------------------------------------------------------------

Not all Aiven for Apache Kafka parameters are customizable, to retrieve the list use the following command:

::
    
    avn service types -v

The output is the set of customizable parameters for all the services, browse to the ``kafka`` section to check the ones available for Aiven for Apache Kafka.

Update a service parameter with the Aiven CLI
---------------------------------------------

To modify a service parameter use the :ref:`Aiven CLI service update command <avn-cli-service-update>`. E.g. to modify the ``message.max.bytes`` parameter use the following command:

::

    avn service update SERVICE_NAME -c "kafka.message_max_bytes=newmaximumbytelimit"

.. Note::
    
    For some changes, like the ``message.max.bytes``, client settings need to be amended as well. Otherwise, you may encounter issues with processing Kafka messages.