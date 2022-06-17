Send logs to Amazon CloudWatch
==============================

This article will show you how to use the Aiven integration to send logs from your Aiven services to the `Amazon (AWS) CloudWatch <https://aws.amazon.com/cloudwatch/>`_.

You will need:

* An AWS account, and which region it is in.

* An AWS Access Key and Secret Key. Generate the credentials by visiting **IAM dashboard** then click in **Users**, open the **Security credentials** tab, and choose **Create access key**. Click on **Download** as you will need this shortly.

* An Aiven account with a service running.

Configure the integration
-------------------------

Start by configuring the link between the Aiven service and the AWS CloudWatch. This setup only needs to be done once.

1. Choose **Service integrations** in the left hand menu of the web console, then choose **AWS CloudWatch Logs** and **Add a new endpoint**.

.. image:: /images/integrations/configure-cloudwatch-logs-endpoint.png
   :alt: Screenshot of configuration screen for CloudWatch Logs integration

2. Configure the settings for the new endpoint:

   * ***Endpoint name*** is how you will refer to this logs integration when linking it to other Aiven services.

   * Your AWS credentials: **Access Key** and **Secret Key**.
  
   * Your AWS account **Region**.
  
   * **Log Group Name** where your logs streams can be grouped in a group on AWS CloudWatch. If this field is not provided, it will be generated for you.

3. Click in **Create** to save this endpoint.

Send logs from an Aiven service to AWS CloudWatch
-------------------------------------------------

Follow the steps in this section for each of the services whose logs should be sent to AWS CloudWatch.

4. On the **Service Overview** page, select **Manage integrations** and choose the **AWS CloudWatch Logs** option.

.. image:: /images/integrations/cloudwatch-overview-integrations.png
   :alt: Screenshot of system integrations including AWS CloudWatch Logs

5. Pick the endpoint by the **Endpoint name** you created earlier from the dropdown and choose **Enable**.

6. Visit your AWS account and look under "CloudWatch" and explore the **Logs** section to see the data flowing within a few minutes.

.. seealso:: Learn more about :doc:`/docs/integrations/cloudwatch/index`.
