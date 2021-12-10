Change data retention period
==============================

To avoid running out of disk space, by default Apache Kafka drops the oldest messages from the beginning of each log after their retention period expires. **Aiven for Apache Kafka** allows you to configure the retention period for each topic.

The retention period can be set at a service and at a topic level. The setting at service level will be taken into use when no retention period is defined for a specific topic (the default is 168 hours). The change of service retention period overwrites the retention period of previously created topics.

For a single topic
~~~~~~~~~~~~~~~~~~~~~

#. Log in to the Aiven web console and select your service.

#. Click the **Topics** tab and then click the topic that you want to modify.

#. In the *Advanced configuration* view find **Retention ms**.

#. Change the value of **Retention ms** value to the desired retention length in milliseconds.

You can also change **Retention bytes** setting if you want to limit amount of data retained based on the storage usage.


At a service level
~~~~~~~~~~~~~~~~~~~

#. Log in to the Aiven web console and select your service.

#. In the *Overview* page scroll down to *Advanced configuration* and click on **Add configuration option**.

#. Select either ``kafka.log_retention_hours`` or ``kafka.log_retention_ms`` and assigning desirable length of time.

#. Alternatively specify the value for ``kafka.log_retention_bytes`` if you prefer to limit amount of data retained based on the storage usage.

#. Click on **Save advanced configuration**.

Unlimited retention
~~~~~~~~~~~~~~~~~~~~~

We do not limit the maximum retention period in any way, and in order to disable time-based content expiration altogether set the retention value to ``-1``.

.. warning:: Using high retention periods without monitoring the available storage space can cause your service to run out of disk space. These situations are not covered by our SLA.



