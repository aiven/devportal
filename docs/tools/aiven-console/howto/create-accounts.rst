Create organizations and organizational units
==============================================

**Organizations** and **organizational units** (or **unit**) can be used to group projects and apply common settings like authentication and teams (user groups). For details and recommendations on creating hierarchical organizations in Aiven, see :doc:`Organizations, projects, and managing access permissions </docs/platform/concepts/projects_accounts_access>`.


Create an organization
--------------------------

#. At the top right side, click the organization name and select **Create organization**. 

   If you don't have an organization yet, click **Create organization**. 

#. Enter a name for the organization.

#. Select any projects that you want to assign to this organization. You can search for projects by name.

#. If you want to invite admin users to the organization, set the toggle to **Yes** and enter their email addresses. They will receive an email invitation with a confirmation link.

   .. important:: When admin users accept the invitation, they are added to the default team that has full control over the organization and the projects assigned to it.

#. Click **Create organization**.

The **Admin** page opens, where you can add organizational units, and manage teams, projects, and other settings. 


Create an organizational unit
---------------------------------

You can create an organizational unit within an organization to group your projects by things like your departments or environments. To create an organizational unit:

#. In the organization where you want to create an organizational unit, click **Admin**.

#. In the **Organizational units** section, click **Create organizational unit**. 

#. Enter a name for the unit.

#. Select any projects that you want to assign to this organizational unit. You can search for projects by name.

#. If you want to invite admin users to the unit, set the toggle to **Yes** and enter their email addresses. They will receive an email invitation with a confirmation link.

   .. important:: Admin have full control over the organizational unit and the projects assigned to it.

#. Click **Create organizational unit**.

Your organizational unit is shown in the **Organizational units** section. Click the unit name to view and manage it's teams and projects. 

.. note::
   Only one level of nesting is supported. This means that organizational units cannot be created within other units.