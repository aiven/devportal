Add or remove customer contacts for your AWS custom cloud in Aiven
==================================================================

Update the list of customer contacts for your :doc:`custom cloud </docs/platform/concepts/byoc>`.

About updating customer contacts
--------------------------------

With the BYOC feature enabled, you can :doc:`create custom clouds </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organizations. While creating a custom cloud in Aiven, you need to add at least **Admin** customer contact, which is a mandatory role required as a primary support contact. Later, you can come back to the the **Customer contact** setting in your cloud's page in `Aiven Console <https://console.aiven.io/>`_ and update the contacts list you initially created for your cloud.

.. important::

    While you can add multiple different customer contacts for your custom cloud, **Admin** is a mandatory role that is always required as a primary support contact.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* At least one :doc:`custom cloud created </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization
* Access to `Aiven Console <https://console.aiven.io/>`_

Update the contacts list
------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select one of the clouds available on the list.
6. In the selected cloud's page, use the ellipsis (**...**) menu in the top right corner to select **Customer contact**.
7. In the **Customer contact** window, select a new contact's role from the dropdown menu, enter the email address, and select **+** to add the provided contact's details.
8. When you're done adding all the contacts, select **Save changes**.

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

Related pages
-------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
