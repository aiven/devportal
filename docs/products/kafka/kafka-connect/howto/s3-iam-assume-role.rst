Use AWS IAM assume role credentials provider
============================================


The :doc:`Apache Kafka® S3 sink connector by Aiven <s3-sink-connector-aiven>` allows you to move data from an Aiven for Apache Kafka® cluster to Amazon S3 for long term storage. The connection between the connector and the S3 bucket can be managed either via long-term AWS credentials (``ACCESS_KEY_ID`` and ``SECRET_ACCESS_KEY``), or using `AWS Assume role credentials <https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html>`_ which request a short-term credential every time the connector has a task to store data to an S3 bucket.

To use AWS Assume role credentials in the S3 sink connector, you need to:

* Request a unique IAM user from Aiven support
* Create an AWS cross-account access role
* Create an Kafka Connect S3 Sink connector


Request a unique IAM user from Aiven support
--------------------------------------------

Every customer in Aiven has a dedicated IAM user. Therefore, there are no shared credentials and roles among customers, and a `cross-account role <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html>`_ provides access to one Aiven project only. You can request an IAM user and the `External ID <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html>`_ (the role unique identifier) by contacting the Aiven support at ``support@aiven.io``.

The following is a sample IAM user and External ID:

* IAM user: ``arn:aws:iam::012345678901:user/sample-project-user``
* External ID: ``2f401145-06a0-4938-8e05-2d67196a0695``

Create an AWS cross-account access role
---------------------------------------

To create a cross-account access role:

1. Log in to the AWS Console and navigate to **IAM** -> **Roles** -> **Create role**
2. Select **Another AWS account** as a type of trusted entity 
3. Specify the **Account ID**

   .. Note::

    The **Account ID** is the numerical string contained in the IAM user between ``aws:iam::`` and ``:user/``. 
    
    In the above example, it is ``012345678901``.

4. Select an option **Require external ID** and paste the External ID
5. Select permissions that allow writing to an S3 bucket. The following permissions are needed:

   * ``s3:GetObject``
   * ``s3:PutObject``
   * ``s3:AbortMultipartUpload``
   * ``s3:ListMultipartUploadParts``
   * ``s3:ListBucketMultipartUploads``

6. Optionally, add tags
7. Specify a name for the role. As an example, ``AivenKafkaConnectSink``
8. To further secure the setting and limit access, you associate the newly created role to a unique full **IAM user** name. 

   You can do so, by editing the newly created role (``AivenKafkaConnectSink``) and navigate to **Trust relationships** -> **Edit trust relationship**
9. In a policy document, the **IAM user** should be specified as ``Principal``.
10. Copy the newly created **IAM role ARN**. It will be needed in the Kafka Connector configuration.

Create a Kafka Connect S3 Sink connector
-----------------------------------------

You can view all the necessary steps to create an S3 sink connector in the :doc:`dedicated documentation <s3-sink-connector-aiven>`. To use the IAM assume role credentials provider, you simply need to remove, in the connector configuration, the references to:

* ``aws.access.key.id``
* ``aws.secret.access.key``

And substitute them with

* ``aws.sts.role.arn``: the Amazon Resource Name (ARN) for IAM role created in the previous step
* ``aws.sts.role.external.id``: the role IAM user External Id provided by the Aiven support team

You can also include the following parameters:

* ``aws.sts.role.session.name``: the id of the session used to identify the task. Can be used to separate different tasks from the same project, and it will be visible in AWS Could Trail log
* ``aws.sts.config.endpoint``: the Security Token Service (STS) endpoint. Choosing an endpoint close to the s3 bucket location is likely going to provide better performances. As example, if the S3 bucket is in the AWS region ``eu-north-1``, the STS endpoint shoud be set to ``https://sts.eu-north-1.amazonaws.com``. You can review the list of STS endpoints in the `dedicated AWS documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html>`_.

The connector configurations in a file (we'll refer to it with the name ``s3_sink.json``) should contain at least the following content:

.. code-block:: json

    {
        "name": "<CONNECTOR_NAME>",
        "connector.class": "io.aiven.kafka.connect.s3.AivenKafkaConnectS3SinkConnector",
        "key.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
        "value.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
        "topics": "<TOPIC_NAME>",
        "aws.sts.role.arn": "<AWS_ROLE_ARN>",
        "aws.sts.role.external.id": "<AWS_IAM_USER_EXTERNAL_ID>",
        "aws.sts.role.session.name":"<AWS_STS_SESSION_NAME>",
        "aws.sts.config.endpoint":"<AWS_STS_ENDPOINT>",
        "aws.s3.bucket.name": "<AWS_S3_NAME>",
        "aws.s3.region": "<AWS_S3_REGION>"
    }

To check all the Apache Kafka Connect® S3 sink connector by Aiven parameters and configuration options, browse the :doc:`dedicated document <s3-sink-connector-aiven>`.