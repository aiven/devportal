Create a custom cloud in Aiven |beta|
=====================================

A custom cloud is your own cloud infarstructre integrated with your Aiven organization (as opposed to an Aiven-managed infrastructure). Using a custom cloud in Aiven may be the optimal solution if you have specific business needs or project requirements, such as a strict regulatory compliance. With a custom cloud, you can manage your own infarstructure based on your expectations and tailor it to your budget.

Learn how to add a :doc:`custom cloud </docs/platform/concepts/byoc>` to your Aiven organization, and check out how it works.

.. important::

   * To create a custom cloud in your Aiven organization, you need the bring your own cloud (BYOC) feature enabled for this organization.
   * BYOC is a beta feature, and its availability is limited. To enable BYOC for your Aiven organization, contact `sales@Aiven.io <mailto:sales@Aiven.io>`_.
   * For more information on BYOC, see :doc:`Bring your own cloud </docs/platform/concepts/byoc>`. 

About creating a custom cloud
-----------------------------

If you enabled BYOC and you have the administrator's role in your organization, you can create a custom cloud using `Aiven Console <https://console.aiven.io/>`_.

Limitations
'''''''''''

* Administrator's role is required for creating custom clouds.
* You need to use AWS as a cloud provider.
* You need to use the :ref:`BYOC standard deployment <byoc-standard>` as a deployment model for your custom cloud.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* BYOC feature enabled from `sales@Aiven.io <mailto:sales@Aiven.io>`_
* Access to `Aiven Console <https://console.aiven.io/>`_

Create a custom cloud
---------------------

Navigate to BYOC in Aiven Console
'''''''''''''''''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the left sidebar, select **Bring you own cloud**.
3. In the **Bring you own cloud** view, select **Create custom cloud**.

Generate an infrastructure template
'''''''''''''''''''''''''''''''''''

In this step, an infrastructure-as-code (IaC) template is generated. For that purpose, AWS CloudFormation or Terraform can be used.

In the **Create custom cloud** wizard, proceed as follows:

1. Specify the following:

   * Cloud name
   * Cloud provider
   * Region
   * CIDR

     Aiven needs CIDR for the `CIDR block of the VPC <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html>`_ that will be created in your AWS account.

     Specify inbound rules with the CIDR block notation, for example: 200.1.2.3/32 (allowing 200.1.2.3 as a single address), 0.0.0.0/0 (allowing traffic from anywhere), or 100.1.0.0/16 (allowing traffic from 100.1..).

     Note the following:

     * To create VPC peerings with that VPC, choose a CIDR block that doesn't overlap with CIDR blocks of peer VPCs.
     * CIDR block needs be large enough so that, after splitting it into per-region subnets, each subnet has enough addresses to fit required services.
   * :ref:`Deployment model <byoc-deployment>`

     The deployment model determines how resources within your Aiven organization are arranged. It also imposes the method of connectivity between Aiven's control plane and networks under your cloud provider account.

2. Select **Next**.
   
.. topic:: Result

    Your infrastructure template gets generated based on your inputs. You can view, copy, or download it.

Acquire ``Role ARN``
''''''''''''''''''''

Role ARN (Amazon Resource Name) is an `identifier of the role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ created when running the infrastructure template in your AWS account. Aiven uses Role ARN to `assume the role <https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>`_ and run operations such as creating VMs for service nodes in your BYOC account.

Use the generate template to create your Role ARN by deploying the template in your AWS account. How you do that depends on the type of the template.

.. topic:: Deploying the IaC template in the AWS account

   To run a Terraform template or an AWS CloudFormation template, use dedicated command line tools. Additionally, you can deploy the AWS CloudFormation template in the AWS console by taking the following steps:

   1. Go to the AWS console > the AWS CloudFormation service.
   2. Create a stack, and upload the Aiven-generated template into AWS.
   3. Deploy the template in AWS, and get your Role ARN.

As soon as you acquire Role ARN, enter it into the **Role ARN** field in the **Create custom cloud** wizard, and select **Next** to proceed.

.. note::
   
   You can park your cloud setup here, save your current configuration as a draft, and resume creating your cloud later.

Assign projects and customer contacts
'''''''''''''''''''''''''''''''''''''

Continue working in the **Create custom cloud** wizard by taking the following steps:

1. From the **Assign projects** dropdown menu, select projects for which you want your custom cloud to be available.
2. To add customer contacts, select their roles using the **Role** dropdown menu, and provide email addresses in the **Email** field.

   .. note:: 

      You can add multiple customer contacts for your custom cloud using **+**.

3. Select **Finish**.

.. topic:: Result

     The custom cloud process has been initiated for you.

Complete the cloud setup
''''''''''''''''''''''''

Now, Aiven needs up to three business days for your setup verification and cloud creation. You'll be notified via email when it's done and your custom cloud is ready to use.

Select **Done**, and expect an email confirming your cloud's readiness.

.. topic:: Result

    As soon as we confirm your custom cloud's availability via email, you'll be able to see it on the list of your custom clouds in the **Bring you own cloud** view.

Check how it works
------------------

After you create a custom cloud, you can use it for multiple purposes, such as the following:

* Creating services
* Forking services
* Migrating services

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
