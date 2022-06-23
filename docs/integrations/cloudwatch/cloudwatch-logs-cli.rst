Send logs to AWS CloudWatch from Aiven client
=============================================

This article will show you how you can send logs from your Aiven service to the AWS CloudWatch using the :doc:`Aiven client </docs/tools/cli>`.

Prerequisites
-------------

This is what you'll need to send your logs from the AWS CloudWatch using the :doc:`Aiven client </docs/tools/cli>`.


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
-------------------------

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
-------------------------------------------------

5. Collect the following information for sending the service logs of an Aiven service to your CloudWatch:

* ``PROJECT``, the Aiven project where your endpoint is saved.
* ``ENDPOINT_ID``, reference name for this log integration when linking it to other Aiven services.
* ``AIVEN_SERVICE_NAME``, the Aiven service name that you want to send the logs from.

6. Send logs from the Aiven service to AWS CloudWatch by running:

.. code:: bash
   avn service integration-create --project PROJECT\
      -t external_aws_cloudwatch_logs -s AIVEN_SERVICE_NAME \
      -D ENDPOINT_ID