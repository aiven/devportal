Monitoring services
===================

When spinning Aiven services, you get access by default to both metrics and logs to monitor the health of your service. 

Review a service using the console
----------------------------------

1. Log in to the Aiven console. 
2. Go to your **Services**, and open the service you want to review.
3. Metrics can be reviewed under the **Metrics** tab, with the choice of spanning the last hour, day, week, month or year.
4. Logs can be reviewed under the **Logs** tab. Older logs are loaded progressively. To come back to the most recent log entry, click on **Got to most recent message**


Review a service using the Aiven client (CLI)
----------------------------------------------

1. Prepare the command to review the service.

2. Add the ``service_to_review`` parameter to specify the service you want to review.

3. To review your service logs, you can use this command:

    avn service logs ``service_to_review``

3. To review your service metrics, you can use this command:

    avn service metrics ``service_to_review``



