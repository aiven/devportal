Enable, configure, and visualize OpenSearch® Audit logs
===============================================================

Aiven for OpenSearch® enables audit logging functionality via the OpenSearch Security dashboard, which allows OpenSearch Security administrators to track system events, security-related events, and user activity. These audit logs contain information about user actions, such as login attempts, API calls, index operations, and other security-related events. 

This article details the steps required to enable, configure, and visualize OpenSearch audit logs through the OpenSearch Security dashboard.

Prerequisites
--------------
* Aiven for OpenSearch® service
* :doc:`OpenSearch Security management enabled <../howto/enable-opensearch-security>` for the Aiven for OpenSearch service 


Enable audit logs
---------------------
To enable audit logs in OpenSearch® Security dashboard, follow these steps: 

1. Log in to the OpenSearch® Dashboard using OpenSearch® Security admin credentials.
2. Select **Security** from the left-side menu.
3. Select **Audit logs**.
4. Toggle the switch next to **Enable audit logging** to the on position.

.. note:: 
   The storage location for audit logs on your Aiven for OpenSearch service is configured to be stored on the cluster's storage and cannot be changed.


Audit log event types
-----------------------
OpenSearch® enables audit logging for HTTP requests(REST) and the transport layer, capturing various events related to user authentication, privileges, security, and more.

The following are the types of audit events recorded by OpenSearch:

* ``FAILED_LOGIN``: User authentication failure.
* ``AUTHENTICATED``: User authentication success.
* ``MISSING_PRIVILEGES``: User does not have request privileges.
* ``GRANTED_PRIVILEGES``: User's privileges successfully granted.
* ``SSL_EXCEPTION``: Invalid SSL/TLS certificate in request.
* ``opensearch_SECURITY_INDEX_ATTEMPT``: Unauthorized security plugin modification attempt.
* ``BAD_HEADERS``: Attempted request spoofing with internal security headers.

Configure audit logging 
------------------------

The audit logging settings in OpenSearch® Security can be tailored to meet your organization's requirements by customizing the *General* and *Compliance* settings sections. The following are the available settings for each section:

General settings
```````````````````
* **Layer settings**: This section allows you to enable or disable logging for the REST and Transport layers. You can also exclude specific categories of events from being logged, such as events related to user authentication, to reduce noise in the logs.
* **Attribute settings**: This section allows customization of log data for each event, including options to log the request body, resolved indices, and sensitive headers. Additionally, there is an option to enable or disable logging for bulk requests.
* **Ignore settings**: This section allows you to exclude specific users or requests from being logged. This is useful for excluding internal users or automated processes that generate a lot of noise in the logs.

Compliance settings 
`````````````````````
* **Compliance mode**: This enables logging of all events in a tamper-evident manner, which prevents deletion or modification of logs, ensuring compliance with specific regulations or standards.
* **Config**: This enables logging of changes to OpenSearch Security configuration files, allowing you to monitor security policies and settings changes.
* **Internal config logging**: This enables logging of events on the internal security index, allowing you to monitor changes to the OpenSearch Security configuration made by internal users or processes.
* **External config logging**: This enables logging of external configuration changes, allowing you to monitor changes to external authentication providers or other systems integrated with OpenSearch Security.
* **Read metadata and write metadata options**: This enables metadata logging for read and write operations. You can also exclude specific users or watched fields from being logged.

..note: 
   
   * You cannot modify the name of the audit log index for your Aiven for OpenSearch service as it is set to the default name ``auditlog-YYYY.MM.dd``. 
   * You cannot change the size of the thread pool using ``OpenSearch.yml``. 

Optimize audit log configuration
`````````````````````````````````
Optimizing the configuration of audit logs in OpenSearch Security can ensure that your OpenSearch Security system is logging only the necessary information and protecting sensitive data from unauthorized access.

* **Exclude categories**: To make it easier to identify important events and reduce the amount of data stored, consider excluding categories of events irrelevant to your security policies. For example, you may not need to log every successful login event, but may want to log all failed login attempts.
* **Disable Rest and transport layers**: By disabling logging for Rest and Transport layers, you can prevent sensitive information such as passwords and usernames from being logged. These layers are used to communicate with OpenSearch cluster nodes and may contain sensitive data.
* **Disable request body logging**: To prevent the logging of sensitive information such as credit card numbers and personal information, consider disabling request body logging. This can help prevent unauthorized access to sensitive data.
* **Additional configuration options**: Depending on your specific security requirements and policies, you may want to configure additional options such as disabling logging of all affected index names from an alias or wildcard, configuring bulk request handling, excluding specific requests or users from logs, configuring the audit log index name, and tuning the thread pool.
* **Regular review and maintenance**: It is essential to periodically review and maintain your audit log configuration to ensure that it is up-to-date with your security policies and requirements. This can help you identify potential security threats and take action to prevent them.

Visualize audit log 
--------------------
Visualizing audit logs is an effective way to understand the extensive data generated by these logs. Visualization can help identify patterns or anomalies that may indicate security risks or system issues by presenting the information in user-friendly graphical formats.

To access and visualize audit logs in OpenSearch, follow the steps below:

1. **Create an index pattern**: 
   
   a. Go to the OpenSearch Dashboards left side menu and select **Stack Management**. 
   b. Select on **Index Patterns** and select **Create index pattern**. 
   c. Enter the name of the index that contains the audit logs and follow the prompts to complete the index pattern creation process.

2. **Create a visualization**: 
   
   a. Select **Visualize** in the OpenSearch Dashboards left side menu, and then select **Create new visualization** or **Create visualization** if there are already saved visualizations.
   b. Choose the type of visualization you want to create and select the index pattern you created in the previous step.
   c. Choose the specific fields you want to display in your visualization.

3. **Save visualization**:
   
   a. Select **Save** in the top right corner of the dashboard.
   b. In the **Save visualization** screen, enter a title and description for the visualization.
   c. Click Save.

4. **Modify visualization**: 
   
   To make changes to a visualization, in the **Visualization** screen, select the pencil icon next to the visualization you want to modify, make the desired changes, and save them.


Related reading
----------------
* `OpenSearch audit logs documentation <https://opensearch.org/docs/latest/security/audit-logs/index/>`_