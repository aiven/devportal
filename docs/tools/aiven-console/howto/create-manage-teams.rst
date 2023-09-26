
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

Replace your existing teams with groups:

#. In the organization, click **Admin** 

#. Click **Organization** and on the **Teams** tab view each team to make a note of: 

* which users are members of the team
* which projects the team is assigned to
* the permission level that is assigned for each project

#. Click **Groups** and then **Create group**. 

#. Enter the name of one of the teams and assign the same users to this group. Do this for each of your organization's teams.

#. :doc:`Add each new group to the same projects </docs/platform/howto/add-groups-projects>` that the teams are assigned to. Set the role to the same permission level that is used for the team.
