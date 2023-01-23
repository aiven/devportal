Create a slack-based Apache Flink® table
========================================

With Aiven's Slack Connector for Apache Flink®, you can create sink tables in your Flink application and set up statements to send alerts and notifications to your designated Slack channel. This allows for real-time monitoring and tracking of your Flink job progress and any potential issues that may arise. 

You can access the open-source Slack connect for Apache Flink on Aiven's GitHub repository at `Slack Connector for Apache Flink® <https://github.com/aiven/slack-connector-for-apache-flink>`_.

Prerequisites
-------------

* Slack app created and ready for use. For more information, refer to the `Set-up Slack Application section <https://github.com/aiven/slack-connector-for-apache-flink>`_ on the GitHub repository and the `Slack documentation <https://api.slack.com/start/building>`_.
* Note the **channel ID** and **token value**, as these will be required in the sink connector Table SQL when configuring the connection in your Flink application.



Configure Slack as sink for Flink application
-----------------------------------------------
To configure Slack as the target using the Slack connector for Apache Flink, follow these steps: 

1. On the Aiven for Apache Flink service page, navigate to the **Application** tab.

2. Create a new application or select an existing application for your desired :doc:`data service integration <../howto/create-integration>`. 

.. note::  
   If you are editing an existing application, you need to create a new version of the application to make changes to the source or sink table.

3. In the **Add source tables** screen, click the option to add a new source table, edit an existing one, or import a source table. Select your integrated service and in the **Table SQL** section, enter the statement that will be used to create the table.

4. In the **Add sink tables** screen, click the option to add a new sink table or edit an existing one.

5. In the **Table SQL** section, set the connector to **slack** and enter the necessary token as shown in the example below:

::

    CREATE TABLE channel_name (
    channel_id STRING,
    message STRING
    ) WITH (
        'connector' = 'slack',
        'token' = 'your_token_here'
    )

.. note:: 
    *  ``channel_id`` is the channel ID parameter.
    *  Replace the token value with the token you received from Slack.
    
6. Create the SQL statement to send notifications/alerts to the designated slack channel.

You can check the connection by running a query on the sink table. If the data flows into the slack channel, the connection is successful.
