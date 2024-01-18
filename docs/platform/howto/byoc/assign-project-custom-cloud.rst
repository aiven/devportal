Enable your AWS custom cloud in Aiven organizations, units, or projects
=======================================================================

To be able to use a :doc:`custom cloud </docs/platform/concepts/byoc>` in your Aiven organizations, units, or projects, you need to configure its availability.

.. important::

    Custom cloud configuration in Aiven is an :doc:`early availability feature </docs/platform/concepts/beta_services>`. You cover the costs associated with building and maintaining your custom cloud: payments for your integrated AWS infrastructure and Aiven services within the custom cloud.

About making custom clouds available from your projects
-------------------------------------------------------

With the BYOC feature enabled, you can :doc:`create custom clouds </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization. As a part of the :doc:`initial custom cloud's setup in Aiven Console </docs/platform/howto/byoc/create-custom-cloud>`, you select in what projects you'll be able to use your new custom cloud to create services. You decide if you want to make your cloud available for all the projects in your organization, selected organizational units, or specific projects only.

Later, you can come back to the **Available projects** tab in your cloud's page in `Aiven Console <https://console.aiven.io/>`_ and update the settings you configured during the :doc:`initial custom cloud's setup </docs/platform/howto/byoc/create-custom-cloud>`.


1. In the **Custom cloud's availability in your organization** section, select either:

   * **By default for all projects** to make your custom cloud available in all existing and future projects in the organization, or;

   * **By selection** to pick specific projects or organizational units where you want your custom cloud to be available.

2. If you go for the **By selection** option, the **Assign organizational units** field and the **Assign projects** field show up. Enter the names of organizational units and/ or projects in which you want to be able to use your custom cloud.

Prerequisites
-------------

* Administrator's role for your Aiven organization
* At least one :doc:`custom cloud created </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization
* Access to `Aiven Console <https://console.aiven.io/>`_

Enable projects to use your custom cloud
----------------------------------------

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select one of the clouds available on the list.
6. In the selected cloud's page, navigate to the **Available projects** tab and modify the settings provided as needed:
   
   * Select **Set availability** to decide if your custom cloud is available in all the projects in your organization or in selected projects only. In the **Custom cloud's availability in your organization** window, select either **By default for all projects** or **By selection**. If you go for the **By selection** option, dropdown menus **Assign organizational units** and **Assign projects** show up. Use them to select desired organizational units and/ or projects and confirm your choice by selecting **Save**.

   .. note::

      By selecting an organizational unit, you make your custom cloud available from all the projects in this unit.

   * Select **Assign projects** to enable your custom cloud in specific organizational units and/ or projects. In the **Assign projects** window, use the available dropdown menus to select desired units and/ or projects as needed. Confirm your choice by selecting **Assign projects**.

.. topic:: Result

    In the projects and/ or organizational units you assigned, you can create services using your custom cloud.

Check it out
------------

You can verify if the cloud availability changes you made are live by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select one of the clouds available on the list.
6. In the selected cloud's page, navigate to the **Available projects** tab and check the available projects and organizational units list for the updates you made.

Related pages
-------------

* :doc:`Bring your own cloud </docs/platform/concepts/byoc>`
* :doc:`Enable the bring your own cloud (BYOC) feature </docs/platform/howto/byoc/enable-byoc>`
* :doc:`Create a custom cloud in Aiven </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
