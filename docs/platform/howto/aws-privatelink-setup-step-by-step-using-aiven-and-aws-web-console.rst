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
   :alt: Image 1

--------------

.. _h_da903a8920:

Create VPC and EC2 instance in your AWS account
-----------------------------------------------

This is not directly related to Privatelink but you may use this
checklist while creating VPC in AWS for testing purposes. This will also
create EC2 instance that you can SSH into and to test the Privatelink in
the final step.

.. _h_37c5633407:

AWS VPC management console:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Create VPC - pick a CIDR:
   -  In the search box in AWS console, search for VPC and open the VPC Service. A VPC Dashboard will open.
   -  Press on the `Create VPC` button and choose `VPC and more`
   -  In the `IPv4 CIDR block` choose a CIDR, i.e. 10.11.0.0/20 and press `Create VPC`.
   -  After creation of the VPC, press the `X` to close the VPC workflow window and go back to `VPC dashboard`.

-  Create subnet - also pick a CIDR:
   
   - In `VPC dashboard` press on `Your VPCs` and identify the VPC and the region you want to work with and remember its `VPC ID`.
   - In the left panel, select `Subnets`, sort the subnets by `VPC`
   - select the subnet that refer to the VPC that you just created and edit that by clicking upper right corner "Actions" → "Edit subnet settings" →"Auto-assign IP settings", and tick "Enable auto-assign public IPv4 address". At the bottom of the page, press `Save`.
   - Do this for all the subnets referring to the VPC.
   - Go back to the `VPC dashboard` by navigating back to `VPC`.

-  Route table - DO NOT create new route table, as it should be created automatically

-  Internet gateway, a new internet gateway is automatically created and attached to the VPC when you created the VPC

-  A `default` security group is also created automatically upon creation of the VPC

-  To allow SSH connectivity, select `Security groups` on the left panel
  
   -  select the `Security group ID` that refers to the VPC you are working on.
   -  Press the button `Edit inbound rules` and select `SSH` in the `Type` field drop down list.
   -  press on `Save rules` and exit

.. _h_cf3bb023be:

AWS EC2 management console:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Go to `EC2  dashboard` - search EC2 in the search box if you don't know how to open the EC2 dashboard.
   
   -  At the top right corner, press on `Launch instances`, and provide a name for the instance and choose from one of the available images or start from your template.
   -  In the instance configuration, scroll down to `Network settings`
   -  Press `Edit` to edit the configuration.
   -  Select the VPC that was created in the previous steps
   -  Select the subnet that refers to that VPC and make sure that "auto-assign public IP" is enabled to allow to SSH directly to the instance
   -  In the `Firewall (security groups)` block, choose `Select existing security group` and choose the `default` security group (which we just edit to allow incoming SSH)
   -  Press on `Launch instance` to start your instance

.. _h_9950f9b97e:

Create (Aiven) project VPC and Aiven service
--------------------------------------------

.. _h_eb163399cb:

Create VPC in Aiven console
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Login to Aiven console, select "VPC" in the left panel and create project VPC in any region in AWS cloud. To create a privatelink in other public clouds you must use the `avn` command line.
For now, we will describe AWS privatelink setup.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image2.png
   :alt: Image 2

.. _h_dd69fc9964:

Wait until the VPC becomes "active"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image3.png
   :alt: Image 3

.. _h_586bdede97:

Create Aiven service in project VPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will use Kafka®, but it's similar for other service
types. While creating Aiven service, select cloud provider "AWS", region
"VPC" and the VPC you just created.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image4.png
   :alt: Image 4

.. _h_eb6fca0ecb:

Enable ``Privatelink`` on an Aiven service
------------------------------------------

.. _h_37fe703fde:

Collect information from AWS account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Login AWS console. On the upper right corner, you will see your AWS
account ID and IAM user name. You will need this information later.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image5.png
   :alt: Image 5

.. _h_99bfb5711a:

Create privatelink for the service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Aiven console, click on the service created in point 2.3, select "Network" tab, and click "Create Privatelink"

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image6.png
   :alt: Image 6

.. _h_942c4da106:

Prepare the principals field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A window asking for "principals" will appear.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image7.png
   :alt: Image 7

Assuming your AWS account ID is 111122223333 and you'd like to allow
anyone (e.g. you have multiple IAM users) in your AWS account to
establish Privatelink connection to access your Aiven resources, enter
``arn:aws:iam::111122223333:root`` in `Principals`.

If you only allow a specific user (e.g. yourself) to access your Aiven
resource, use ``arn:aws:iam::111122223333:user/IAM_USER`` . Replace
"IAM_USER" with actual user name.

You can also use IAM role. A valid principal looks like

``arn:aws:iam::111122223333:root``

``arn:aws:iam::111122223333:user/IAM_USER``

``arn:aws:iam::111122223333:role/IAM_ROLE``

.. _h_05907748af:

Wait for ``Privatelink`` status to be active
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After clicking "create", wait for the Privatelink status to change from
"creating" to "active". You will also see the AWS service name, looks
like ``com.amazonaws.vpce.ap-southeast-2.vpce-svc-00000000000000000`` .
You will need this in the next step.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image8.png
   :alt: Image 8

.. _h_cd615bc6ae:

Create VPC endpoint in your AWS account
---------------------------------------

.. _h_d9d62c72b0:

Create VPC endpoint
~~~~~~~~~~~~~~~~~~~

In AWS VPC dashboard, select `Endpoints` from the panel on the left, and click on `Create endpoint` button.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image9.png
   :alt: Image 9

.. _h_2e5b8aa8d8:

Link the VPC endpoint with your service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the create endpoint page:

- Provide a new name for the endpoint
- In `Service category` choose `PrivateLink Ready partner services`

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image10.png
   :alt: Image 10

- In `Service settings` put the name of the service as you find it in the Aiven console. The privatelink service name will be of the form ``com.amazonaws.vpce.ap-southeast-2.vpce-svc-00000000000000000``
- Press `Verify service` and AWS should respond with `Service name verified`
- Next, select your AWS VPC that you want to access from your Aiven service, and press `Create endpoint`.

.. _h_252e22ec88:

Wait for the endpoint status change to become "available"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note it may take a few minutes to see the status: "available", you may see "pending acceptance" before that.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image11.png
   :alt: Image 11

.. _h_956ceaf913:

Configure Aiven service to accept incoming connections via ``Privatelink``
--------------------------------------------------------------------------

.. _h_68754c72b7:

Enable ``Privatelink`` access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on the service in Aiven console, select "network" tab, and turn on "Enable Kafka access"

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image12.png
   :alt: Image 12

.. _h_e11a485025:

URL used for ``Privatelink``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While connecting to the service (e.g. from an EC2 instance in your AWS
VPC), make sure you're using the connection information for
"Privatelink" access route.

.. image:: /images/platform/howto/5858370-aws-privatelink-setup-step-by-step-using-aiven-and-aws-web-console_image13.png
   :alt: Image 13
