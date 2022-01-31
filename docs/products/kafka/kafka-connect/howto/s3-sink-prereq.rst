Configure AWS for the S3 sink connector
=======================================

To be able to sink the data from Apache Kafka® to S3 via the dedicated Aiven connector, you need to perform the following steps in the `AWS console <https://s3.console.aws.amazon.com/>`_:

* **Create an AWS S3 bucket** where the data is going to be stored
* **Define an IAM policy** to enable access to the S3 bucket
* **Create a dedicated user** for the connector and associate the policy


Create the AWS S3 bucket
------------------------

You can create S3 bucket using the `dedicated AWS console page <https://s3.console.aws.amazon.com/>`_. When creating the bucket, specify bucket name and region, the other settings can be left as default. 

.. Note::

    You can leave the **block all public access** setting to the default value (on) since permissions can be granted using IAM.

Define an IAM policy
--------------------

The Apache Kafka Connect® S3 sink connector needs the following permission to the target S3 bucket:

* ``s3:GetObject``
* ``s3:PutObject``
* ``s3:AbortMultipartUpload``
* ``s3:ListMultipartUploadParts``
* ``s3:ListBucketMultipartUploads``

The following is an example of AWS inline policy that can be added to the IAM user by replacing the ``<AWS_S3_BUCKET_NAME>`` placeholder:

::

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:AbortMultipartUpload",
                    "s3:ListMultipartUploadParts",
                    "s3:ListBucketMultipartUploads"
                ],
                "Resource": [
                    "arn:aws:s3:::<AWS_S3_BUCKET_NAME>/*",
                    "arn:aws:s3:::<AWS_S3_BUCKET_NAME>"
                ]
            }
        ]
    }


Create the AWS IAM user
-----------------------

Create IAM user using the `IAM AWS console page <https://console.aws.amazon.com/iamv2/home>`_. In the **Select AWS credential type** section check the **Access key - Programmatic access** option generating an **access key ID** and **secret access key**. The two information are parameters in the Apache Kafka Connect® configuration.

In the **Permission** section, associate to the user the IAM policy created in the previous step.

.. Note::

    In case of ``Access Denied`` errors while starting the connector, check the dedicated `AWS access troubleshooting guide <https://aws.amazon.com/premiumsupport/knowledge-center/s3-troubleshoot-403/>`_.
