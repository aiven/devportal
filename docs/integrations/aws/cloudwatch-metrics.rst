Send metrics to Amazon CloudWatch
=================================

Aiven enables you to send your service metrics to your `Amazon (AWS) CloudWatch <https://aws.amazon.com/cloudwatch/>`_. This article covers all the steps to enable this integration for your Aiven service.

Prepare your AWS account
------------------------

* An AWS account, and which region it is in.

* An AWS Access Key and Secret Key. Generate the credentials by visiting your AWS console under the **IAM dashboard** then click in **Users**, open the **Security credentials** tab, and choose **Create access key**. Click on **Download** as you will need this shortly.

* An Aiven account with a service running.

Configure the integration
-------------------------

Your first step is to create the endpoint to be used between the Aiven service and the AWS CloudWatch. This setup only needs to be done once.

1. Choose **Service integrations** in the left-hand menu of the web console, then choose **AWS CloudWatch Metrics** and **Add a new endpoint**.

.. image:: /images/integrations/configure-cloudwatch-metrics-endpoint.png
   :alt: Screenshot of configuration screen for CloudWatch Metrics integration

2. Configure the settings for the new endpoint:

   * ***Endpoint name*** is how you will refer to the AWS CloudWatch metrics integration when linking it to an Aiven service.

   * Your AWS credentials: **Access Key** and **Secret Key**.
  
   * Your AWS account **Region**.
  
   * **Cloudwatch Namespace** where your metrics can be organized in different spaces. This field is **Optional** and if not provided, it will be generated.

3. Click in **Create** to save this endpoint.

Send metrics from an Aiven service to AWS CloudWatch
----------------------------------------------------

Follow the steps in this section for each of the services whose metrics should be sent to AWS CloudWatch.

4. From the **Service Overview** page, select **Manage integrations** and choose the **AWS CloudWatch Metrics** option.

.. image:: /images/integrations/cloudwatch-overview-integrations.png
   :alt: Screenshot of system integrations including AWS CloudWatch Metrics

5. Choose the endpoint by the **Endpoint name** you created earlier from the dropdown and choose **Enable**.

6. Go to your AWS account and check the "CloudWatch" service. You can go to the **Metrics** section to see your Aiven service metrics data. It may take a few minutes until the data arrives.

.. seealso:: Learn more about :doc:`/docs/integrations/aws/index`.
