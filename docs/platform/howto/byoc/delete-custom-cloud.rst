Delete your AWS custom cloud in Aiven
=====================================

A :doc:`custom cloud </docs/platform/concepts/byoc>` is a secure environment within your cloud provider account to run Aiven-managed data services. Using a custom cloud in Aiven may be the optimal solution if you have specific business needs or project requirements, such as a strict regulatory compliance. Creating and using custom clouds in your Aiven organization requires enabling :doc:`the bring your own cloud (BYOC) feature </docs/platform/concepts/byoc>`. Check the availability of the feature in :ref:`Who is eligible for BYOC <eligible-for-byoc>`. To activate BYOC in your Aiven organization, follow the steps in :doc:`Enable bring your own cloud (BYOC) with Aiven </docs/platform/howto/byoc/enable-byoc>`.

.. important::

    Custom cloud configuration in Aiven is an :doc:`early availability feature </docs/platform/concepts/beta_services>`. You cover the costs associated with building and maintaining your custom cloud: payments for your integrated AWS infrastructure and Aiven services within the custom cloud.

This article details how to delete your custom cloud in `Aiven Console <https://console.aiven.io/>`_.

About deleting custom clouds
----------------------------

After deleting a custom cloud, the data co-hosted in this cloud will no longer be available from the Aiven platform. Before deleting your custom cloud, make sure there are no active services using this cloud.

Impact on your Aiven resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The deletion impacts mostly resources on the Aiven site, such as cloud configuration files.

Impact on your AWS account resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A bastion service and the corresponding EC2 instance are deleted as a consequence of your custom cloud's removal. As for resources created when applying the Terraform template to create the custom cloud, they are not removed after deleting your custom cloud.Unless you've removed them earlier, you're advised to do that if deleting your cloud.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* At least one :doc:`custom cloud created </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization
* No running services that uses a custom cloud to be deleted
* Access to `Aiven Console <https://console.aiven.io/>`_

Delete your cloud
-----------------

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select one of the clouds available on the list.
6. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner to select **Delete**.
7. Make sure you understand the impact and, if so, confirm that you want to delete the cloud by selecting **Delete** in the **Warning** window.

.. topic:: Result

    Your custom cloud has been deleted.

.. important::

    Remember to remove the resources created in your AWS account when applying the Terraform template to create the custom cloud. They are not removed automatically after deleting the cloud. Unless you've removed them earlier, use the ``terraform destroy`` command to delete them. See the guidelines on how to use the ``destroy`` command in `Command: destroy <https://developer.hashicorp.com/terraform/cli/commands/destroy>`_.

Check it out
------------

You can verify if you deleted your cloud successfully by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, see the list of the available clouds to make sure the cloud you intended to delete is actually gone.

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Enable bring your own cloud (BYOC) </docs/platform/howto/byoc/enable-byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
