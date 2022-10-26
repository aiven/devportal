Prepare services for high load
==============================

If you are expecting higher than usual traffic on your Aiven services, you can follow the recommendations and best practices detailed below  ahead of time to make sure you have the best tools and your service is ready to sustain high loads. 

.. Tip::

    If your services are already experiencing high load, under-performing or requiring extra resource, read `short term suggestion to handle the load <https://help.aiven.io/en/articles/4660372-reacting-to-high-load>`_.

Monitor service health
----------------------

Subscribe for service notifications
'''''''''''''''''''''''''''''''''''

To receive notifications about the service health you can set the appropriate emails in the `Aiven Console <https://console.aiven.io/>`_:

* Navigate to the **Settings** tab under the specific project
* Include the relevant emails under the **Technical Emails** section

The specified emails will receive notifications related to plan size change, performance, outages and upcoming maintenance. 

.. Warning::

    If no Technical Emails are specified, Aiven sends some high priority messages to the project admin(s). 
    
    Therefore, if not all the tech support members are also admins, one or more people might be missing important notifications for your services.

Subscribe to platform status updates
''''''''''''''''''''''''''''''''''''

The Aiven services are managed by the Aiven platform, therefore is a good idea to check its status and receive notifications in case of platform wide incidents. You can follow the RSS feed, subscribe for email or SMS notifications, or use the Slack integration to get notified where your team is already.

You can check the status and subscribe to Aiven's platform updates directly from the status page: `https://status.aiven.io/ <https://status.aiven.io/>`_

Monitor the services
--------------------

It's difficult to prepare for high load if the usual load is not monitored. Check out how to setup adequate monitoring for your needs in the :doc:`dedicated documentation <monitoring-services>`.


Modify the service plan
-----------------------

If you forecast a load that can't be handled by the current service plan, you can decide either to :doc:`scale up your service plan<scale-services>`, or :doc:`request a custom plan<custom-plans>` if none of the available plans satisfies your requirements.

Define the backups schedule
---------------------------

During the backup process, you may experience a temporary higher load. It is therefore recommended to perform them outside of your peak traffic hours to lower the impact.

For Aiven for PostgreSQL® and Aiven for MySQL® services you can configure the time in the day when the daily backups are taken by setting the ``backup_hour`` and ``backup_minute`` variables in the `Aiven Console <https://console.aiven.io/>`_, under the **Advanced Configuration** section.

.. Tip::

    If you intend to make a plan upgrade, it is a good idea to do it shortly after a full backup is taken. This reduces the amount of incremental changes that need to be applied on top of the base backup and therefore speeds up the upgrade itself.

Define the maintenance schedule
-------------------------------

Similar to backups, it is important to make sure your :doc:`maintenance windows </docs/platform/concepts/maintenance-window>` are configured correctly.

.. Tip::

    Plan maintenance updates outside of your peak traffic hours and days. Optional updates will not be automatically installed unless you apply them yourself or a mandatory update is created.

Run load test on service forks
-------------------------------

To test the impact on high traffic on a service, you can run load tests against copies of your production service using the :doc:`fork service option <console-fork-service>` option in the `Aiven Console <https://console.aiven.io/>`_.

Perform service specific optimizations
--------------------------------------

Optimizing a service allows it to perform better under stress therefore avoiding the need of an upgrade. The more optimised a service is for your usage, the better you will be able to weather spikes in traffic.

You can read more on this under the service specific articles:

- :doc:`Apache Kafka® and Apache Kafka® Connect best practices </docs/products/kafka/howto/best-practices>`

- :doc:`PostgreSQL® best practices </docs/products/postgresql/howto/optimize-pg-slow-queries>`
