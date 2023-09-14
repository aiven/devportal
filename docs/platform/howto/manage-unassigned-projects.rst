Manage unassigned projects
===========================
An unassigned project is a project that isn't assigned to an organization or organizational unit. Projects that are part of an organization or unit are easier to maintain as common settings like authentication are centrally managed at the organization level.

.. important::
    Aiven is planning to discontinue support for unassigned projects. Organize your projects in the way that works best for you by assigning them now to an organization or organizational unit. If you have unassigned projects after that date, they will be assigned to your organization. If you don't have an organization, one will be created and the unassigned projects will be moved there.

Learn more about :doc:`organizations, organizational units, and projects </docs/platform/concepts/projects_accounts_access>`.

Manage unassigned projects in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assign standalone projects to an organization or unit
------------------------------------------------------

If you don't have an organization, you need to :ref:`create an organization <create-org>` first and then assign your projects to it.

To assign standalone projects to an organization or unit in the `Aiven web console <https://console.aiven.io/>`_: 

1. Click **Projects**.
2. Click **View unassigned projects** to see a list of all projects not assigned to an organization or organizational unit. If you don't see **View unassigned projects** in the dropdown menu, then you don't have any unassigned projects.
3. On the **Unassigned projects** page, click **Assign project**.
4. Add any other projects that you want to assign to the same organization or unit.
5. Select the organization or organizational unit.
6. Click **Associate Projects**.

.. _create-org:

Create an organization
-----------------------

Projects must be assigned to organizations or units within organizations. We recommend using **only one organization** and creating organizational units to group your projects. 

If you don't have any organization yet, you can create one:

#. At the top right side, click **Create organization**. 

#. Enter a name for the organization.

#. Select the projects that you want to assign to this organization. You can search for projects by name.

#. If you want to invite admin users to the organization, set the toggle to **Yes** and enter their email addresses. They will receive an email invitation with a confirmation link.

   .. important:: When admin users accept the invitation, they have full control over the organization and the projects assigned to it.

#. Click **Create organization**.

The **Admin** page opens, where you can add organizational units, and manage users, groups, and other settings. 


Manage unassigned projects with the API 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check for unassigned projects
------------------------------

To see a list of names of all unassigned projects use the following:

.. code::

    curl -sXGET \
     https://api.aiven.io/v1/project \
     -H "Authorization: Bearer TOKEN" | jq -r '.projects[] | select(.account_id==null) | .project_name'



Assign standalone projects to an organization or unit
------------------------------------------------------

If you don't have an organization, you need to :ref:`create an organization <create-org-api>` first and then assign your projects to it.

To assign a standalone project to an organization or unit use the following call. Replace ``ACCOUNT_ID`` with the ID of the organization or unit and ``PROJECT_NAME`` with the name of the project to assign.

.. code::

    curl -sXPUT \
     https://api.aiven.io/v1/project/PROJECT_NAME \
     -H "Authorization: Bearer TOKEN" \
     -H 'content-type: application/json' \
     --data-raw '{"account_id":"ACCOUNT_ID","add_account_owners_admin_access":true}' | jq

.. _create-org-api:

Create an organization
-----------------------

To create an organization use the following call. Replace ``ORG_NAME`` with a name for your new organization.

.. code::

    curl -sXPOST \
     https://api.aiven.io/v1/account \
     -H "Authorization: Bearer TOKEN" \
     -H 'content-type: application/json' \
     --data '{"account_name":"ORG_NAME"}' | jq

