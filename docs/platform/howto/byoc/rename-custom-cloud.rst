Rename your custom cloud
========================

.. important::

    Creating custom clouds in your Aiven organization requires enabling :doc:`the bring your own cloud (BYOC) feature </docs/platform/concepts/byoc>`, which is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying it out, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

This article details how to change the name of your custom cloud in `Aiven Console <https://console.aiven.io/>`_.

About renaming custom clouds
----------------------------

With the BYOC feature enabled, you can :doc:`create custom clouds </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organizations. While :doc:`setting up a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`, you specify its name, which is a part of the initial custom cloud's configuration. Later, you can come back to the **Rename** setting in your cloud's page in `Aiven Console <https://console.aiven.io/>`_ and update the name you initially specified.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* At least one :doc:`custom cloud created </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization
* Access to `Aiven Console <https://console.aiven.io/>`_

Rename your cloud
-----------------

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the left sidebar, select **Bring your own cloud**.
3. In the **Bring you own cloud** view, select one of the clouds available on the list.
4. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner to select **Rename**.
5. In the **Rename custom cloud** window, enter a new name into the **Custom cloud name** field and select **Rename**.

.. topic:: Result

    The name of your custom cloud has been updated.

Check it out
------------

You can preview the updated name of your cloud by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the left sidebar, select **Bring your own cloud**.
3. In the **Bring you own cloud** view, see the list of the available clouds and identify the cloud with the name you updated.

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
