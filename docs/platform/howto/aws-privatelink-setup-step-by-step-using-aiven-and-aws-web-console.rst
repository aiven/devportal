AWS Privatelink setup step-by-step, using Aiven and AWS web console
===================================================================

This article is suitable for people with experience in VPC but first
time setting up `AWS
Privatelink <https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html>`__
to access an Aiven service.

There are 5 steps

#. Create VPC and EC2 instance in your AWS account

#. Create (Aiven) project VPC and Aiven service

#. Enable Privatelink on an Aiven service

#. Create VPC endpoint in your AWS account

#. Configure Aiven service to accept incoming connections via
   Privatelink

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image1.png

--------------

.. _h_da903a8920:

1. Create VPC and EC2 instance in your AWS account
--------------------------------------------------

This is not directly related to Privatelink but you may use this
checklist while creating VPC in AWS for testing purposes. This will also
create EC2 instance that you can SSH into and to test the Privatelink in
the final step.

.. _h_37c5633407:

1.1 AWS VPC management console:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Create VPC - pick a CIDR

-  Create subnet - also pick a CIDR

   -  Edit the subnet, upper right corner "Actions" → "Edit subnet
      settings" →"Auto-assign IP settings", and tick "Enable auto-assign
      public IPv4 address"

-  Route table - DO NOT create new route table, as it should be created
   automatically

-  Create Internet gateway, and attach it to the VPC

-  At route table, edit route to add Internet gateway (destination
   0.0.0.0/0, target: the internet gateway just created)

-  DO NOT create new security group - the "default" one will be created
   automatically.

-  At the "default" security group for the VPC

   -  Keep the default "allow" source from the security group itself,
      otherwise machines in the same security group cannot talk to each
      other.

   -  Edit inbound rules to allow inbound SSH.

.. _h_cf3bb023be:

1.2 AWS EC2 management console:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  When launching EC2 instance

   -  Select VPC, and "auto-assign public IP" to "enable" if SSH
      directly to the instance is required

   -  Select "default" security group (which we just edit, allow
      incoming SSH)

.. _h_9950f9b97e:

2. Create (Aiven) project VPC and Aiven service
-----------------------------------------------

.. _h_eb163399cb:

2.1 Create VPC in Aiven console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Login Aiven console, select "VPC" in the left and create project VPC

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image2.png

.. _h_dd69fc9964:

2.2 Wait until the VPC become "active"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image3.png

.. _h_586bdede97:

2.3. Create Aiven service in project VPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will use Kafka®, but it's similar for other service
types. While creating Aiven service, select cloud provider "AWS", region
"VPC" and the VPC you just created.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image4.png

.. _h_eb6fca0ecb:

3. Enable Privatelink on an Aiven service
-----------------------------------------

.. _h_37fe703fde:

3.1 Collect information from AWS account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Login AWS console. On the upper right corner, you will see your AWS
account ID and IAM user name. You will need these information later.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image5.png

.. _h_99bfb5711a:

3.2 Create privatelink for the service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Aiven console, click on the service, select "Network" tab, and click
"Create Privatelink"

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image6.png

.. _h_942c4da106:

3.3 Prepare the principles field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A window asking for "principles" will appear.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image7.png

Assuming your AWS account ID is 111122223333 and you'd like to allow
anyone (e.g. you have multiple IAM users) in your AWS account to
establish Privatelink connection to access your Aiven resources, enter
``arn:aws:iam::111122223333:root`` in principle.

If you only allow a specific user (e.g. yourself) to access your Aiven
resource, use ``arn:aws:iam::111122223333:user/IAM_USER`` . Replace
"IAM_USER" with actual user name.

You can also use IAM role. A valid principle looks like

``arn:aws:iam::111122223333:root``

``arn:aws:iam::111122223333:user/IAM_USER``

``arn:aws:iam::111122223333:role/IAM_ROLE``

.. _h_05907748af:

3.4 Wait privatelink status to be active
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After clicking "create", wait for the Privatelink status change from
"creating" to "active". You will also see the AWS service name, looks
like ``com.amazonaws.vpce.ap-southeast-2.vpce-svc-00000000000000000`` .
You will need this in the next step.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image8.png

.. _h_cd615bc6ae:

4. Create VPC endpoint in your AWS account
------------------------------------------

.. _h_d9d62c72b0:

4.1 Create VPC endpoint
~~~~~~~~~~~~~~~~~~~~~~~

In AWS VPC management console, select "endpoints" in the left, and click
"create endpoint" button.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image9.png

.. _h_2e5b8aa8d8:

4.2 Link the vpc endpoint with your service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select "Find service by name".

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image10.png

.. _h_cfca13fa12:

4.3 Provide the AWS service name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fill in the service name with format like:
``com.amazonaws.vpce.ap-southeast-2.vpce-svc-00000000000000000`` then
click "verify". It should respond "service name found."

However, if it prompts "service name not found", please go back and
check the principle configured in the Aiven console (step 3.3).

.. _h_47e75172b8:

4.4 Select VPC
~~~~~~~~~~~~~~

Select your AWS VPC that you want to access your Aiven service, and
click "create endpoint".

.. _h_252e22ec88:

4.5 Wait for the endpoint status change to "available"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note it may take a few minutes to see the status: "available", you may
see "pending acceptance" before that.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image11.png

.. _h_956ceaf913:

5. Configure Aiven service to accept incoming connections via Privatelink
-------------------------------------------------------------------------

.. _h_68754c72b7:

5.1 Enable privatelink access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on the service in Aiven console, select "network" tab, and turn on
"Enable kafka access"

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image12.png

.. _h_e11a485025:

5.2 URL used for privatelink
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While connecting to the service (e.g. from an EC2 instance in your AWS
VPC), make sure you're using the connection information for
"Privatelink" access route.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image13.png
