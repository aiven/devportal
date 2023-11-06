Create organizations and organizational units
==============================================

Organizations and organizational units can be used to group projects and apply common settings like authentication and access for groups of users. For details and recommendations on creating hierarchical organizations in Aiven, see the article on :doc:`organizations, units, and projects </docs/platform/concepts/projects_accounts_access>`. When you sign up for Aiven, an organization is automatically created for you. 

Create an organizational unit
------------------------------

You can create an organizational unit within an organization to group your projects by, for example, your departments or environments. To create an organizational unit in the `Aiven Console <https://console.aiven.io>`_:

#. In the organization where you want to create an organizational unit, click **Admin**.

#. In the **Organizational units** section, click **Create organizational unit**. 

#. Enter a name for the unit.

#. Optional: Select any projects that you want to assign to this organizational unit. You can search for projects by name.

#. Click **Create organizational unit**.

Your organizational unit is shown in the list. Click the unit name to view and manage its projects. 

.. note::
   Only one level of nesting is supported. This means that organizational units cannot be created within other units.


Create an organization
-----------------------

.. important::
   We recommend using only one organization and using organizational units to group your projects. 
   
   Creating a new organization requires you to manually configure organization-level settings again such as :doc:`billing groups, authentication settings, and groups </docs/platform/concepts/projects_accounts_access>`.

To create an organization in the `Aiven Console <https://console.aiven.io>`_:

#. Click the user information icon in the top right and select **Organizations**. 

#. Click **Create organization**.

#. Select the checkbox to confirm that you understand the effects of creating an organization.

#. Enter a name for the organization.

#. Optional: Select any projects that you want to assign to this organization. You can search for projects by name.

#. Click **Create organization**.
