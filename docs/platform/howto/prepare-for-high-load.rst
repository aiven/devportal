Prepare services for high load
==============================

If you are expecting higher than usual traffic on your Aiven services, you can follow the recommendations and best practices detailed below ahead of time to make sure you have the best tools and your service is ready to sustain high loads. 

.. Tip::

    If your services are already experiencing high load, under-performing or requiring extra resource, read `short term suggestion to handle the load <https://help.aiven.io/en/articles/4660372-reacting-to-high-load>`_.

Monitor service health
----------------------

Subscribe for service notifications
'''''''''''''''''''''''''''''''''''

To receive notifications about the service health, you can set the appropriate emails in `Aiven Console <https://console.aiven.io/>`_:

1. Go to your project, and select **Settings** from the sidebar.
2. In the **Settings** page, include relevant email addresses in the **Technical Emails** section.

The specified email addressees will receive notifications related to plan size change, performance, outages and upcoming maintenance. 

.. Warning::

    If no technical emails are specified, Aiven sends some high priority messages to the project admin(s). 
    
    Therefore, if some technical support members are not admins, they might be missing important notifications for your services.

Subscribe to platform status updates
''''''''''''''''''''''''''''''''''''

The Aiven services are managed by the Aiven platform, therefore is a good idea to check its status and receive notifications in case of platform wide incidents. You can follow the RSS feed, subscribe for email or SMS notifications, or use the Slack integration to get notified where your team is already.

You can check the status of the the Aiven platform and subscribe to updates on incidents directly from `status.Aiven.io <https://status.aiven.io/>`_.

Monitor the services
--------------------

It's difficult to prepare for high load if the usual load is not monitored. Check out how to setup adequate monitoring for your needs in :doc:`Monitoring services <monitoring-services>`.

Modify the service plan
-----------------------

If you forecast a load that can't be handled by the current service plan, you can decide either to :doc:`scale up your service plan<scale-services>`, or :doc:`request a custom plan <custom-plans>` if none of the available plans satisfies your requirements.

Define the backups schedule
---------------------------

To minimize the impact of the higher load during the backup process, it is recommended to schedule backups outside of peak traffic hours.

To configure the daily backup time in  **Aiven for PostgreSQL®** and **Aiven for MySQL®** services:

#. Access the `Aiven Console <https://console.aiven.io/>`, select your project and then choose your service. 
#. In the service page, select **Service settings** from the sidebar, and scroll down to the **Advanced configuration** section. 
#. Click **Configure**.
#. In the **Advanced configuration** dialog, configure the values for these variables: 

   * ``backup_hour``: The hour of the day when the backup starts.
   * ``backup_minute``: The minute of the hour to begin the backup. 

.. Tip::

    If you intend to make a plan upgrade, it is a good idea to do it shortly after a full backup is taken. This reduces the amount of incremental changes that need to be applied on top of the base backup and therefore speeds up the upgrade itself.

Define the maintenance schedule
-------------------------------

Similar to backups, it is important to make sure your :doc:`maintenance windows </docs/platform/concepts/maintenance-window>` are configured correctly.

.. Tip::

    Plan maintenance updates outside of your peak traffic hours and days. Optional updates will not be automatically installed unless you apply them yourself or a mandatory update is created.

Run load test on service forks
-------------------------------

To test the impact on high traffic on a service, you can run load tests against copies of your production service using the :doc:`fork service option <console-fork-service>` option in `Aiven Console <https://console.aiven.io/>`_ > your service's **Overview** page > **Fork Database** > **New database fork**.

Perform service specific optimizations
--------------------------------------

Optimizing a service allows it to perform better under stress therefore avoiding the need of an upgrade. The more optimized a service is for your usage, the better you can weather spikes in traffic.

.. seealso::

   - :doc:`Apache Kafka® and Apache Kafka® Connect best practices </docs/products/kafka/howto/best-practices>`
   - :doc:`PostgreSQL® best practices </docs/products/postgresql/howto/optimize-pg-slow-queries>`
