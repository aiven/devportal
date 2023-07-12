Add or remove customer contacts for your custom cloud |beta|
============================================================

.. topic:: Before you start

    Creating custom clouds in your Aiven organization requires enabling the bring your own cloud (BYOC) feature. BYOC is a beta feature, and its availability is limited. To enable BYOC for your Aiven organization, contact `sales@Aiven.io <mailto:sales@Aiven.io>`_. For more information on BYOC, see :doc:`Bring your own cloud </docs/platform/concepts/byoc>`.

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
2. From the left sidebar, select **Bring your own cloud**.
3. In the **Bring you own cloud** view, select one of the clouds available on the list.
4. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner to select **Customer contact**.
5. In the **Customer contact** window, select a new contact's role from the dropdown menu, enter the email address, and select **+** to add the provided contact's details.

   .. note::
    
    You can add multiple customer contacts for your custom cloud.
    
6. When you're done adding all the contacts, select **Save changes**.

.. topic:: Result

    The list of contacts for your cloud has been updated.

Check it out
------------

You can preview the updated list of contacts by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the left sidebar, select **Bring your own cloud**.
3. In the **Bring you own cloud** view, select one of the clouds available on the list.
4. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner.
5. Select **Customer contact** from the options available on the the ellipsis (**...**) menu.

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
