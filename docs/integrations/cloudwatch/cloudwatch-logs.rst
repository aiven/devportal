Send logs to Amazon CloudWatch
==============================

This article will show you how to use the Aiven integration to send logs from your Aiven services to the `Amazon (AWS) CloudWatch <https://aws.amazon.com/cloudwatch/>`_. This integration can be done from the Aiven Web Console or by using the Aiven Client.


Send logs to AWS CloudWatch from Aiven web console
--------------------------------------------------

Prerequisites
~~~~~~~~~~~~~

You will need:

* An AWS account, and which region it is in.

* An AWS Access Key and Secret Key. Generate the credentials by visiting **IAM dashboard** then click in **Users**, open the **Security credentials** tab, and choose **Create access key**. Click on **Download** as you will need this shortly.

* An Aiven account with a service running.
  
Configure the integration
~~~~~~~~~~~~~~~~~~~~~~~~~

Start by configuring the link between the Aiven service and the AWS CloudWatch. This setup only needs to be done once.

1. Choose **Service integrations** in the left hand menu of the web console, then choose **AWS CloudWatch Logs** and **Add a new endpoint**.

.. image:: /images/integrations/configure-cloudwatch-logs-endpoint.png
   :alt: Screenshot of configuration screen for CloudWatch Logs integration

2. Configure the settings for the new endpoint:

   * **Endpoint name** is how you will refer to this logs integration when linking it to other Aiven services.

   * Your AWS credentials: **Access Key** and **Secret Key**.
  
   * Your AWS account **Region**.
  
   * **Log Group Name** where your logs streams can be grouped in a group on AWS CloudWatch. If this field is not provided, it will be generated for you.

3. Click in **Create** to save this endpoint.

Send logs from an Aiven service to AWS CloudWatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps in this section for each of the services whose logs should be sent to AWS CloudWatch.

4. On the **Service Overview** page, select **Manage integrations** and choose the **AWS CloudWatch Logs** option.

.. image:: /images/integrations/cloudwatch-overview-integrations.png
   :alt: Screenshot of system integrations including AWS CloudWatch Logs

5. Pick the endpoint by the **Endpoint name** you created earlier from the dropdown and choose **Enable**.

6. Visit your AWS account and look under "CloudWatch" and explore the **Logs** section to see the data flowing within a few minutes.

.. seealso:: Learn more about :doc:`/docs/integrations/cloudwatch/index`.

Send logs to AWS CloudWatch from Aiven client
---------------------------------------------

Prerequisites
~~~~~~~~~~~~~

For sending the logs from your Aiven service to AWS CloudWatch using the Aiven client tool, you will need:

* An Aiven account with a service running.

* Aiven client installed.

* An AWS account, and which region it is in. 

* An AWS Access Key and Secret Key. Generate the credentials by visiting **IAM dashboard** then click in **Users**, open the **Security credentials** tab, and choose **Create access key**. Click on **Download** as you will need this shortly. 

.. important::
   
   Your AWS credentials should have appropriate access rights. According to the offical AWS documentation, the access rights required for the credentials are:

   * "logs:DescribeLogStreams" which lists the log streams for the specified log group endpoint.
   * "logs:CreateLogGroup" which creates a log group with the specified name endpoint.
   * "logs:CreateLogStream" which creates a log stream for the specified log group.
   * "logs:PutLogEvents" which uploads a batch of log events to the specified log stream.

   .. seealso:: Find more information about `CloudWatch API <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Operations.html>`_.
 
Configure the integration
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the Aiven client, and log in::

    avn user login <you@example.com> --token

.. seealso:: Learn more about  :doc:`/docs/tools/cli/user/user-access-token`

2. Collect the following information for the creation of the endpoint between your Aiven account and AWS CloudWatch.

* ``PROJECT``, the Aiven project where your endpoint will be saved to.
* ``LOG_GROUP_NAME``, to group your log streams on AWS CloudWatch. It is an optional field. If the value is not provided, it'll be generated for you.
* ``AWS_REGION``, the AWS region of your account.
* ``AWS_ACCESS_KEY_ID``, your AWS access key ID.
* ``AWS_SECRET_ACCESS_KEY``, your AWS secret access key.
* ``ENDPOINT_NAME``, reference name for this log integration when linking it to other Aiven services.
  
3. Create the endpoint between your Aiven account and AWS CloudWatch.

.. code:: bash

   avn service integration-endpoint-create --project PROJECT \
      -d ENDPOINT_NAME -t external_aws_cloudwatch_logs \
      -c log_group_name=LOG_GROUP_NAME \
      -c access_key=AWS_ACCESS_KEY\
      -c secret_key=AWS_SECRET_ACCESS_KEY \
      -c region=AWS_REGION

4. Collect the ``ENDPOINT_ID`` value. You should be able to see information about your endpoint by running:

.. code:: bash

   avn service integration-endpoint-list --project PROJECT

As an example, an output could be something like:

.. code:: bash

      ENDPOINT_ID                           ENDPOINT_NAME        ENDPOINT_TYPE                  
   ====================================  ===================  ===============================
   50020216-61dc-60ca-b72b-000d3cd726cb  ENDPOINT_NAME        external_aws_cloudwatch_logs

The output will provide you with the ``ENDPOINT_ID`` to identify your endpoint, your customized endpoint name and the endpoint type.

Send logs from an Aiven service to AWS CloudWatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5. Collect the following information for sending the service logs of an Aiven service to your CloudWatch:

* ``PROJECT``, the Aiven project where your endpoint is saved.
* ``ENDPOINT_ID``, reference name for this log integration when linking it to other Aiven services.
* ``AIVEN_SERVICE_NAME``, the Aiven service name that you want to send the logs from.

6. Send logs from the Aiven service to AWS CloudWatch by running:

.. code:: bash

   avn service integration-create --project PROJECT\
      -t external_aws_cloudwatch_logs -s AIVEN_SERVICE_NAME \
      -D ENDPOINT_ID
   
