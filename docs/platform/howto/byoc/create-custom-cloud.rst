Create a custom cloud in Aiven
==============================

A :doc:`custom cloud </docs/platform/concepts/byoc>` is your own cloud infrastructure integrated with your Aiven organization. Using a custom cloud in Aiven may be the optimal solution if you have specific business needs or project requirements, such as a strict regulatory compliance.

.. important::

    Creating custom clouds in your Aiven organization requires enabling :doc:`the bring your own cloud (BYOC) feature </docs/platform/concepts/byoc>`, which is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying it out, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

This article provides you with instructions on how to :ref:`add a custom cloud <create-cloud>` to your Aiven organization.

About creating a custom cloud
-----------------------------

If you have the administrator's role in your Aiven organization, and you enable BYOC, you can create a custom cloud on the Aiven platform. For this purpose, you'll need to configure your custom cloud setup in `Aiven Console <https://console.aiven.io/>`_ and prepare your own Amazon Web Services (AWS) account so that Aiven can access it.

In `Aiven Console <https://console.aiven.io/>`_, you'll use the **Create custom cloud** workflow to generate a Terraform infrastructure-as-code (IaC) template. Next, you'll deploy this template in your AWS account to acquire Role ARN (Amazon Resource Name). You'll supply your Role ARN into the **Create custom cloud** workflow, which will give Aiven the permissions to securely access your AWS account, create resources, and manage them onward. Finally, you'll assign projects and add customer contacts for your custom cloud.

Limitations
'''''''''''

* Administrator's role is required for creating custom clouds.
* :doc:`BYOC limited availability version </docs/platform/concepts/beta_services>` supports the AWS cloud provider only.
* BYOC is supported with the :ref:`standard deployment <byoc-deployment>` model only.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* AWS account
* BYOC feature enabled for your Aiven organization by the sales team (`sales@Aiven.io <mailto:sales@Aiven.io>`_)
* Access to `Aiven Console <https://console.aiven.io/>`_
* Terraform installed

.. _create-cloud:

Create a custom cloud
---------------------

Navigate to BYOC in Aiven Console
'''''''''''''''''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the top navigation bar, select **Admin**.
3. From the left sidebar, select **Bring you own cloud**.
4. In the **Bring you own cloud** view, select **Create custom cloud**.

.. _generate-infra-template:

Generate an infrastructure template
'''''''''''''''''''''''''''''''''''

In this step, an IaC template is generated in the Terraform format. In :ref:`the next step <acquire-role-arn>`, you'll deploy this template in your AWS account to acquire Role ARN (Amazon Resource Name), which Aiven needs for accessing your AWS account.

In the **Create custom cloud** workflow, proceed as follows:

1. Specify the following:

   * Custom cloud name
   * Cloud provider

     .. important::

        **Amazon Web Services (AWS)** is the only option supported currently.

   * Region
   * CIDR

     Aiven needs CIDR for the `CIDR block of the VPC <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html>`_ that will be created in your AWS account.

     * Specify inbound rules with the CIDR block notation, for example: 200.1.2.3/32 (allowing 200.1.2.3 as a single address), 0.0.0.0/0 (allowing traffic from anywhere), or 100.1.0.0/16 (allowing traffic from 100.1..).
     * To create VPC peerings with that VPC, choose a CIDR block that doesn't overlap with CIDR blocks of peer VPCs.
     * Keep in mind that CIDR block needs be large enough so that, after splitting it into per-region subnets, each subnet has enough addresses to fit required services.

2. Select **Next**.
   
.. topic:: Result

    Your IaC Terraform template gets generated based on your inputs. You can view, copy, or download it. Now, you can use the template to :ref:`acquire Role ARN <acquire-role-arn>`.

.. _acquire-role-arn:

Deploy the template to acquire ``Role ARN``
'''''''''''''''''''''''''''''''''''''''''''

Role ARN is an `identifier of the role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ created when running the infrastructure template in your AWS account. Aiven uses Role ARN to `assume the role <https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>`_ and run operations such as creating VMs for service nodes in your BYOC account.

Use the Terraform template generated in step :ref:`Generate an infrastructure template <generate-infra-template>` to create your Role ARN by deploying the template in your AWS account.

.. important::

   When running ``terraform plan`` and ``terraform apply``, make sure you add ``-var-file=FILE_NAME.vars`` as an option.

As soon as you acquire Role ARN, enter it into the **Role ARN** field in the **Create custom cloud** workflow, and select **Next** to proceed.

.. note::
   
   You can park your cloud setup here, save your current configuration as a draft, and resume creating your cloud later.

Assign projects and customer contacts
'''''''''''''''''''''''''''''''''''''

Continue working in the **Create custom cloud** workflow by taking the following steps:

1. From the **Assign projects** dropdown menu, select projects for which you want your custom cloud to be available.
2. To add customer contacts, select their roles using the **Role** dropdown menu, and provide email addresses in the **Email** field. Using **+**, add as many customer contacts as needed for your custom cloud.

   .. note::

      The customer contact information is used by the Aiven support team to contact you in case any technical issue with the custom cloud needs fixing.

3. Select **Finish**.

.. topic:: Result

     The custom cloud process has been initiated for you, which is communicated in the the **Create custom cloud** workflow.

Complete the cloud setup
''''''''''''''''''''''''

You're all set. Select **Done** to close the **Create custom cloud** workflow.

.. topic:: Result

   The deployment of your new custom cloud might take a few minutes. As soon as it's over, and your custom cloud is ready to use, you'll be able to see it on the list of your custom clouds in the **Bring you own cloud** view.

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
