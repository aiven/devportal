Assign a project to your custom cloud |beta|
============================================

.. topic:: Before you start

    Creating custom clouds in your Aiven organization requires enabling the bring your own cloud (BYOC) feature. BYOC is a beta feature, and its availability is limited. To enable BYOC for your Aiven organization, contact `sales@Aiven.io <mailto:sales@Aiven.io>`_. For more information on BYOC, see :doc:`Bring your own cloud </docs/platform/concepts/byoc>`.

This article details how to update the list of projects assigned to your custom cloud using `Aiven Console <https://console.aiven.io/>`_.

About assigning projects to your custom cloud
---------------------------------------------

With the BYOC feature enabled, you can :doc:`create custom clouds </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organizations. While :doc:`setting up a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`, you add projects for this cloud, which is a part of the initial custom cloud's configuration. Later, you can come back to the **Projects availability** tab in your cloud's page in `Aiven Console <https://console.aiven.io/>`_ and update the projects list you initially created for your cloud.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* At least one :doc:`custom cloud created </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization
* Access to `Aiven Console <https://console.aiven.io/>`_

Assign projects
---------------

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the left sidebar, select **Bring your own cloud**.
3. In the **Bring you own cloud** view, select one of the clouds available on the list.
4. In the selected cloud's page, navigate to the **Projects availability** tab and select **Assign projects**.
5. In the **Assign projects** window, use the dropdown menu to select a project you want to assign to your cloud.
6. Confirm your choice by selecting **Assign projects**.

.. topic:: Result

    Another project has been added to your custom cloud.

Check it out
------------

You can preview the updated list of assigned projects by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. From the left sidebar, select **Bring your own cloud**.
3. In the **Bring you own cloud** view, select one of the clouds available on the list.
4. In the selected cloud's page, navigate to the **Projects availability** tab.

Related reading
---------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
