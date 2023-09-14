
Create and manage teams
=======================

.. important::
    **Teams are becoming groups**
    
    :doc:`Groups </docs/platform/howto/manage-groups>` are an easier way to control access to your organization's projects and services for a group of users. 
    
    :ref:`migrate_teams_to_groups`


**Teams** let you create user groups and assign different access levels to specific projects. Users must be part of an organization before being added to a team. To create and manage teams, click **Admin** and then select **Teams**.

Create a new team
--------------------------

#. Click **Create new team**.

#. Enter a **Team Name**.

#. Click **Create team**.

Add users to a team
--------------------

#. Click the name of the team that you want to add users to.

#. On the **Team Members** tab, click **Invite users**.

#. Enter the email address of the user and click **Invite users**. 

The user will get an email with an invitation link. 

Add projects and roles to a team
----------------------------------

.. important::
    Teams cannot be assigned to units. 

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

.. _migrate_teams_to_groups:

Migrate teams to groups
------------------------

To help you get started using groups, the migration feature creates new groups from the existing teams in your organization all at once.

You can do this in two places:

* In the organization, go to **Admin**, select **Organization**, and then the **Teams** tab.
* In a project, select **Members** and then the **Teams** tab.

As part of the migration, the members of the account owners team for an organization are made super admin. Super admin have full access to an organization's admin, billing, units, projects, and services.
