Change data retention period
==============================

To avoid running out of disk space, by default, Apache Kafka® drops the oldest messages from the beginning of each log after their retention period expires. **Aiven for Apache Kafka®** allows you to configure the retention period for each topic.

The retention period can be configured at both the service and topic levels. If no retention period is specified for a particular topic, the service-level setting will be applied, with a default value of 168 hours. When modifying the service retention period, it will override the retention period of any previously created topics.

For a single topic
~~~~~~~~~~~~~~~~~~~~~

To change the retention period for a single topic, follow these steps:

#. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka® service.

#. Select **Topics** from the left sidebar.

#. Select the topic from the **Topics** screen for which you want to modify the retention period.

#. In the **Topic info** screen, select **Modify**. 

#. In the modify topic screen, update the value of **Retention ms** to the desired retention length in milliseconds. If you cannot find **Retention ms**, use the search bar to locate it

   .. note:: 
      The **Retention ms** option is displayed in the modify topic screen for topics where advanced configuration was enabled during topic creation.

#. Select **Update** to save your changes. 


#. In the *Advanced configuration* view find **Retention ms**.

#. Change the value of **Retention ms** value to the desired retention length in milliseconds.

   .. Tip::

      You can also change **Retention bytes** setting if you want to limit amount of data retained based on the storage usage.


At a service level
~~~~~~~~~~~~~~~~~~~

#.  Log in to `Aiven Console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka® service.
#.  On the **Overview** page, scroll down to **Advanced configuration** and select **Change**. 
#.  In the **Edit advanced configuration** screen, select **Add configuration option**.
#.  You have two options to configure the retention period for Apache Kafka® logs. 

    * You can either select ``kafka.log_retention_hours`` or ``kafka.log_retention_ms`` and set the desired length of time for retention.
    *  Alternatively, if you prefer to limit the amount of data retained based on storage usage, you can specify the value for ``kafka.log_retention_bytes``.

#. Click on **Save advanced configuration**.

Unlimited retention
~~~~~~~~~~~~~~~~~~~~~

We do not limit the maximum retention period in any way, and in order to disable time-based content expiration altogether set the retention value to ``-1``.

.. Warning:: 

    Using high retention periods without monitoring the available storage space can cause your service to run out of disk space. These situations are not covered by our SLA.



