Create a custom cloud in Aiven
==============================

A custom cloud is your own cloud infrastructure integrated with your Aiven organization. Using a custom cloud in Aiven may be the optimal solution if you have specific business needs or project requirements, such as a strict regulatory compliance. With a custom cloud, you can manage your own infrastructure based on your expectations and tailor it to your budget.

.. important::

    Creating custom clouds in your Aiven organization requires enabling :doc:`the bring your own cloud (BYOC) feature </docs/platform/concepts/byoc>`, which is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying it out, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Learn how to add a :doc:`custom cloud </docs/platform/concepts/byoc>` to your Aiven organization, and check out how it works.

About creating a custom cloud
-----------------------------

If you enable BYOC and you have the administrator's role in your organization, you can create a custom cloud using `Aiven Console <https://console.aiven.io/>`_. For this purpose, you'll use the **Create custom cloud** wizard to generate a Terraform infrastructure-as-code (IaC) template. Next, you'll deploy this template in your AWS account to acquire Role ARN (Amazon Resource Name). You'll suppy your Role ARN into the **Create custom cloud** wizard, which will give Aiven the permissions to securely access your AWS account and create resources. Finally, you'll assign projects and add customer contacts for your custom cloud.

Limitations
'''''''''''

* Administrator's role is required for creating custom clouds.
* :doc:`BYOC limited availability version </docs/platform/concepts/beta_services>` supports the AWS cloud provider only.
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

.. _generate-infra-template:

Generate an infrastructure template
'''''''''''''''''''''''''''''''''''

In this step, an IaC template is generated. In :ref:`the next step <acquire-role-arn>`, you'll deploy this template in your AWS account to acquire Role ARN (Amazon Resource Name), which you need for configuring your custom cloud.

.. note::

   The Terraform format is supported for the IaC template.

In the **Create custom cloud** wizard, proceed as follows:

1. Specify the following:

   * Custom cloud name
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

    Your infrastructure template gets generated based on your inputs. You can view, copy, or download it. Now, you can use the template to :ref:`acquire Role ARN <acquire-role-arn>`.

.. _acquire-role-arn:

Deploy the template to acquire ``Role ARN``
'''''''''''''''''''''''''''''''''''''''''''

Role ARN is an `identifier of the role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ created when running the infrastructure template in your AWS account. Aiven uses Role ARN to `assume the role <https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>`_ and run operations such as creating VMs for service nodes in your BYOC account.

Use the template generated in step :ref:`Generate an infrastructure template <generate-infra-template>` to create your Role ARN by deploying your Terraform template in your AWS account.

..
   .. topic:: Deploying the IaC template in the AWS account

      To run a Terraform template or an AWS CloudFormation template, use dedicated command line tools. Additionally, you can `deploy the AWS CloudFormation template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html>`_ in the AWS console by taking the following steps:

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

     The custom cloud process has been initiated for you, which is communicated in the the **Create custom cloud** wizard.

Complete the cloud setup
''''''''''''''''''''''''
..
   Now, Aiven needs up to three business days for your setup verification and cloud creation.

You're all set. You'll be notified via email when your custom cloud is ready to use.

Select **Done** to close the **Create custom cloud** wizard.

.. topic:: Result

    As soon as we confirm your custom cloud's availability via email, you'll be able to see it on the list of your custom clouds in the **Bring you own cloud** view.

..
   Check how it works
   ------------------

   After you create a custom cloud, you can use it for multiple purposes on Aiven platform, such as the following:

   * Creating services
   * Forking services
   * Migrating services

   Your custom cloud is available for different operations from `Aiven Console <https://console.aiven.io/>`_. It's visible as the separate **Customer cloud** tab when selecting service regions in a console wizard for specific operation you're performing on your service. 

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
