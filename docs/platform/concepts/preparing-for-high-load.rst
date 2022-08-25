Preparing for high load
=======================

If you are expecting higher than usual traffic on your Aiven services, then we outline several recommendations and best practices that can be applied ahead of time to make sure you have the best tools and your service is ready to sustain high loads. If you still have time to prepare there are many ways to set yourself up for success.

But, if your services are already experiencing the high load, require extra resource or under-performing then you can read our list of short term tactics to survive `here <https://help.aiven.io/en/articles/4660372-reacting-to-high-load>`_.

Service Health
--------------

Subscribe for service notifications
'''''''''''''''''''''''''''''''''''

Please make sure you check the Tech Email Addresses section at the bottom of the Billing Information tab. The emails specified here will receive notifications related to plan sizes, performance, outages and upcoming maintenance. If no emails are specified here we will still send some high priority messages to project admin(s), but one or more people in your team may be missing out on important notifications for your services, especially if they require attention.

.. image:: /images/platform/concepts/tech-email.png
   :alt: Tech Email Addresses

Subscribe to platform status updates
''''''''''''''''''''''''''''''''''''

Now is also a good time to make sure your development team is aware of Aiven's status page in case of platform wide incidents. You can follow the RSS feed, subscribe for email or SMS notifications, or use the Slack integration to get notified where your team is already.

.. image:: /images/platform/concepts/platform-status.png
   :alt: Aiven Status Update

Take a look at our status page here: `https://status.aiven.io/ <https://status.aiven.io/>`_

Monitoring
----------

It's difficult to prepare for something that is not being measured. With Aiven services you have several options for how to get insights into system metrics and logs.

Familiarize yourself with Aiven Console metrics and logs
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Every Aiven service has a tab for Metrics and Logs available for basic monitoring. It is a good idea to check these while your service is performing well to understand what healthy values look like.

In particular, pay attention to increases in CPU load average, memory, and disk usage. If any of these are particularly high it might be time to spend some engineering hours on optimizing your own usage of the service or upgrading the plan to give yourself more breathing room for when high traffic hits.

Integrate an Aiven service
''''''''''''''''''''''''''

If you are not already using an external tool for visualizing metrics and logs you might want to consider using our built-in service integrations to easily connect these to other Aiven services.

For example you could have your service metrics ingested into an InfluxDB service and visualized using a Grafana. The advantage here is that we provide you with pre-built dashboards for any connected Aiven service which give you immediate insights into the performance of your services. The process is outlined `here <https://help.aiven.io/en/articles/1456441-getting-started-with-service-integrations>`_.

.. image:: /images/platform/concepts/grafana-status.png
   :alt: Grafana dashboard

You could also `enable logs integration <https://docs.aiven.io/docs/products/opensearch/howto/opensearch-log-integration.html>`_ for your services to have the logs pumped into an Elasticsearch service (on Aiven or external) and then use the built-in Kibana UI to keep an eye on things.

.. image:: /images/platform/concepts/pg-log-integration.png
   :alt: Logs integration for pg

Integrate an external service
'''''''''''''''''''''''''''''

The Metrics available in the Aiven Console are fine for getting a high-level picture of your service. But, if you are already using an external tool like `Datadog <https://www.datadoghq.com/>`_ or `Prometheus <https://prometheus.io/>`_ for monitoring your application code, then you can set up service integrations to deliver Aiven metrics to these services.

- `Getting Started with Datadog <https://docs.aiven.io/docs/integrations/datadog/datadog-metrics.html>`_
- `Using Aiven with Prometheus <https://docs.aiven.io/docs/platform/howto/integrations/prometheus-metrics.html>`_

For logging you might want to ingest your Aiven service logs into another tool for better filtering, searching, and analyzing alongside your application code logs.

- `Remote Syslog Integration <https://docs.aiven.io/docs/integrations/rsyslog.html>`_

- `Sending logs to AWS CloudWatch <https://docs.aiven.io/docs/integrations/cloudwatch/list-cloudwatch-logs.html>`_

- `Sending logs to Google Cloud Logging <https://help.aiven.io/en/articles/4209837-sending-service-logs-to-google-cloud-logging>`_

Plans
-----

Upgrades
''''''''

If the metrics show that there is not much room for growth on your current plan, then you should consider preemptively upgrading before you encounter problems.

.. image:: /images/platform/concepts/upgrade-plan.png
   :alt: Upgrade plan

After you start the upgrade, Aiven will perform an upgrade in a rolling forward style by provisioning new nodes alongside the existing ones with more CPUs, RAM, and storage alongside the existing nodes, stream across the latest data, and then perform a controlled failover to the new nodes. 

**The earlier you do this, the better.** When load increases to the point where a service is struggling then it makes it harder for the old nodes to stream their changes to the new nodes since they're already under high load. You can avoid this problem by upgrading to a larger plan well in advance when your current plan starts to feel the strain.

Aiven services are billed per hour and can be downgraded to a smaller plan at a later date if the heavy traffic is expected to fall, e.g. after a seasonal spike in demand. Currently the only exception is a Cassandra service: the size of the nodes can be changed freely but the total number of nodes cannot be reduced.

You can read more about how upgrade/updates are applied at Aiven `here <https://help.aiven.io/en/articles/489581-how-do-you-apply-software-updates-and-security-patches>`_.

Custom plans
''''''''''''

If our stock plans are not enough for you, or you would like to tune some aspect of an existing plan to suit your workload, you can get in contact with us to request a custom plan as described `here <https://help.aiven.io/en/articles/4676419-aiven-custom-plans>`_.

Note that we can only offer custom plans for services costing at least $500 per month.

Backups
-------

For PostgreSQL and MySQL databases you can configure a time when the daily backups are taken. You can set the backup_hour and backup_minute variables in the Advanced Configuration section.

.. image:: /images/platform/concepts/advanced-configuration.png
   :alt: Advanced configuration

During the backup process you may experience a temporary higher load, therefore a general recommendation is to choose a time of day (in UTC) outside of your peak traffic hours to lower the impact of when the full base backup is taken. Note that changes between these times are continuously archived to allow point in time recovery.

If you intend to make a plan upgrade, it is a good idea to do it shortly after a full backup is taken. This reduces the amount of incremental changes that need to be applied on top of the base backup and therefore speeds up the upgrade itself.

.. image:: /images/platform/concepts/database-backup.png
   :alt: Database backup

Maintenance
-----------

Similarly to backups, it is important to make sure your maintenance windows are configured correctly.

.. image:: /images/platform/concepts/maintenance.png
   :alt: Maintenance

Choose the quietest time during the week for applying any mandatory maintenance updates. Optional updates will not be automatically installed unless you apply them yourself or a mandatory update is created.

These updates can contain new features, bug fixes, and performance improvements. The earlier you apply the updates the sooner you will benefit from them. It is best to get these out of the way before high traffic hits.

Remember also that in case one of your service nodes terminates unexpectedly at any point in time, then the new node that replaces it will start fresh with all available maintenance updates applied (if any). If you keep up with applying the optional updates then you will have a chance to test the changes out in your staging environment before this happens.

Database Forks
--------------

Did you know that it is possible to run load tests against copies of your production databases using the Fork Database option in the Aiven Console?

This uses the same procedure of restoring a backup to a separate service that can be used for data recovery in case of accidental deletion of data by your code or human error. It is good to practice the steps that would need to be taken in this failure scenario as well as test the maximum load your system can comfortably handle.

.. image:: /images/platform/concepts/database-fork.png
   :alt: Database fork

With a separate service that contains the same data as the production server you can implement a load test without disturbing your real production service and then tear it down when you are done.

Service specific
----------------

Finally it is worth looking at any optimizations you can make to your usage of a service that will allow it to last longer before needing an upgrade. The more efficient your usage, the better you will be able to weather spikes in traffic.

You can read more about this in our individual support articles:

- `Kafka and Kafka Connect best practices <https://help.aiven.io/en/articles/4738784-basic-kafka-best-practices>`_

- `PostgreSQL best practices <https://help.aiven.io/en/articles/4738831-basic-postgresql-best-practices>`_

If you have any questions, please feel free to reach out to our support@aiven.io and let us know.