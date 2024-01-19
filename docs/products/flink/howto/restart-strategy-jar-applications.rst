Restart strategy in JAR applications
======================================

A restart strategy is a set of rules that Apache Flink® adheres to when dealing with Flink job failures. These strategies enable the automatic restart of a failed Flink job under specific conditions and parameters, which is crucial for high availability and fault tolerance in distributed and scalable systems.


Default restart strategy for JAR applications
-----------------------------------------------

Aiven for Apache Flink® includes a default restart strategy for JAR applications. This strategy uses the **exponential-delay** technique, incrementally increasing the delay time between restarts up to a specified maximum. Once this maximum delay is reached, it remains constant for any subsequent restarts. The default strategy is fully integrated into the Aiven for Apache Flink cluster configuration and automatically applies to all JAR applications. 

View the default strategy
````````````````````````````````````````````

You can view the default restart strategy configurations for your Aiven for Apache Flink cluster in the Apache Flink Dashboard. Follow these steps to view the current settings:

1. Access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Flink service.
2. From the **Connection information** section on the overview page, copy the **Service URI** and paste it into your web browser's address bar.
3. When prompted, log in using the **User** and **Password** credentials specified in the **Connection information** section.
4. Once in the **Apache Flink Dashboard**, click the **Job Manager** from the menu.
5. Switch to the **Configuration** tab.
6. Review the configurations and parameters related to the restart strategy. 

Disable default restart strategy
------------------------------------
While Aiven for Apache Flink® typically recommends using the default restart strategy for JAR applications, there are circumstances, particularly during testing or debugging, where disabling automatic restarts might be necessary. You cannot disable the default restart strategy in Aiven for Apache Flink® through configuration files. Instead, directly modify the code of your Jar application to achieve this.


.. code-block:: java

   StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
   env.setRestartStrategy(RestartStrategies.noRestart());

This code sets the restart strategy to 'None', preventing any restart attempts in case of failures.

Key considerations when disabling default restarts
``````````````````````````````````````````````````````````

Before choosing to disable the default restart strategy, consider the following:

- **Persistent failures**: Disabling restarts means that if a Flink Job fails, Flink will not attempt to recover it, leading to permanent job failure.
- **Testing and debugging**: Disabling is beneficial when identifying issues in the application code, as it prevents the masking of errors through automatic restarts.
- **External factors**: Jobs can fail due to external factors, such as infrastructure changes or maintenance activities. If you disable restarts, your Flink jobs will become vulnerable to failures.
- **Operational risks**: In production environments, it is generally advisable to use the default restart strategy to ensure high availability and fault tolerance.


Related pages
--------------
* `Restart strategies in Apache Flink® <https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/ops/state/task_failure_recovery/#restart-strategies>`_