Add or remove customer contacts for your AWS custom cloud in Aiven
==================================================================

.. topic:: Custom clouds

    A :doc:`custom cloud </docs/platform/concepts/byoc>` is a secure environment within your cloud provider account to run Aiven-managed data services. Using a custom cloud in Aiven may be the optimal solution if you have specific business needs or project requirements, such as a strict regulatory compliance. Creating and using custom clouds in your Aiven organization requires enabling :doc:`the bring your own cloud (BYOC) feature </docs/platform/concepts/byoc>`. Check the availability of the feature in :ref:`Who is eligible for BYOC <eligible-for-byoc>`. To activate BYOC in your Aiven organization, follow the steps in :doc:`Enable bring your own cloud (BYOC) with Aiven </docs/platform/howto/byoc/enable-byoc>`.

.. important::

    Custom cloud configuration in Aiven is an :doc:`early availability feature </docs/platform/concepts/beta_services>`. You cover the costs associated with building and maintaining your custom cloud: payments for your integrated AWS infrastructure and Aiven services within the custom cloud.

This article details how to update the list of customer contacts for your custom cloud using `Aiven Console <https://console.aiven.io/>`_.

About updating customer contacts
--------------------------------

With the BYOC feature enabled, you can :doc:`create custom clouds </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organizations. While setting up a custom cloud in Aiven, you add customer contacts for this cloud, which is a part of the initial custom cloud's configuration. Later, you can come back to the the **Customer contact** setting in your cloud's page in `Aiven Console <https://console.aiven.io/>`_ and update the contacts list you initially created for your cloud.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* At least one :doc:`custom cloud created </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization
* Access to `Aiven Console <https://console.aiven.io/>`_

Update the contacts list
------------------------

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select one of the clouds available on the list.
6. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner to select **Customer contact**.
7. In the **Customer contact** window, select a new contact's role from the dropdown menu, enter the email address, and select **+** to add the provided contact's details.

   .. note::
    
    You can add multiple customer contacts for your custom cloud.
    
8. When you're done adding all the contacts, select **Save changes**.

.. topic:: Result

    The list of contacts for your cloud has been updated.

Check it out
------------

You can preview the updated list of contacts by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select one of the clouds available on the list.
6. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner.
7. Select **Customer contact** from the options available on the the ellipsis (**...**) menu.

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
