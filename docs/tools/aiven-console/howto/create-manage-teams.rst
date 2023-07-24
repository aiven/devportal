
Create and manage teams
=======================

.. important::
    **Teams are becoming groups**
    
    Teams will be removed soon and groups will be used to control access to organizations and organizational units. To avoid users losing access, create new groups with the same users and permissions that are currently in your teams.

**Teams** let you create user groups and assign different access levels to specific projects in your organization or org unit. When you :doc:`create an organization or organizational unit </docs/tools/aiven-console/howto/create-accounts>`, a team is automatically created with admin access to the organization or org unit and its projects.

Users must be part of an organization before being added to a team. To create and manage teams, click **Admin** and then select **Teams**.

Create a new team
--------------------------

#. Click **Create new team**.

#. Enter a **Team Name**.

#. Click **Create team**.

Add users to a team
--------------------------

#. Click the name of the team that you want to add users to.

#. On the **Team Members** tab, click **Invite users**.

#. Enter the email address of the user and click **Invite users**. 

The user will get an email with an invitation link. 

Add projects and roles to a team
-------------------------------------------

For each team you can specify which projects they can access and the level of permissions:

* **Admin:** Full access to the project, including inviting other users and modifying billing information.
* **Developer:** Make changes to services that do not affect billing.
* **Operator:** Full access to services, except billing information and project members.
* **Read only:** View services only.

To add projects and roles to a team:

#. Click the name of the team and select the **Projects and Roles** tab.

#. Click **Add projects**.

#. Select a **Project Name** and **Permission Level**.

#. Click **Add project to team**.

You can edit the permissions or delete the project from this team by clicking the more options menu for the project.
