Create organizations and org units
===================================

**Organizations** and **organizational units** (or **org units**) can be used to group projects and apply common settings like authentication and teams (user groups). For details and recommendations on creating hierarchical organizations in Aiven, see :doc:`Organizations, projects, and managing access permissions </docs/platform/concepts/projects_accounts_access>`.


Create a new organization
--------------------------

#. At the top right side of the page, click the organization name and select **Create organization**. 

   If you don't have an organization yet, click **Create organization**. 

#. Enter a name for the organization.

#. Select any projects that you want to assign to this organization. You can search for projects by name.

#. If you want to invite admin users to the organization, set the toggle to **Yes** and enter their email addresses. They will receive an email invitation with a confirmation link.

   .. important:: When admin users accept the invitation, they are added to the default team that has full control over the organization and the projects assigned to it.

#. Click **Create organization**.

The **Admin** page opens, where you can manage your organizational units, teams, projects, and other settings. 


Create a new organizational unit
---------------------------------

#. In the organization where you want to create an organizational unit, click **Admin**.

#. In the **Organizational units** section, click **Create org unit**. 

#. Enter a name for the org unit.

#. Select any projects that you want to assign to this org unit. You can search for projects by name.

#. If you want to invite admin users to the organization, set the toggle to **Yes** and enter their email addresses. They will receive an email invitation with a confirmation link.

   .. important:: Admin have full control over the org unit and the projects assigned to it.

#. Click **Create org unit**.

Your org unit is shown in the **Organizational units** section. Click the org unit name to view and manage the org unit's teams and projects. 

.. note::
   Only one level of nesting is supported. This means that org units cannot be created within other org units.