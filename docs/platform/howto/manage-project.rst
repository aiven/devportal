Manage projects
===============

Create a project
----------------

In the `Aiven Console <https://console.aiven.io/>`_, follow these steps to create a new project:

#. Click **Project** and select **Create project**.

#. Enter a name for the project.

#. Select an organization or orgnizational unit to add the project to.

#. Select a :doc:`billing group </docs/platform/concepts/billing-groups>`.  The costs from all services within this project will be charted to the payment method for that billing group.

.. note::
    You can also :ref:`create a project using the Aiven CLI <avn-create-update-project>`.


Rename a project
----------------

.. important:: 
   
   - Except for Aiven for Apache Kafka®, all services have backups that are restored when you power them back on.
   - The project name in your DNS records will not be updated.

To rename a project in the `Aiven Console <https://console.aiven.io/>`_:

#. Power off all services in the project.
#. In the **Project**, click **Settings**. 
#. Edit the **Project name**.
#. Click **Save changes**. 

.. note::
    You can also :ref:`rename a project using the Aiven CLI <avn-create-update-project>`.

Move a project
---------------

To move a project from one organizational unit to another:

#. Click **Admin** and select the organizational unit with the project you want to move.

#. Click the actions menu for the project you want to move and select **Move project**.

#. Select the organizational unit that you want to move the project to. You can also move the project up a level to the organization.

   .. note:: 
        Projects cannot be moved to other organizations. They cannot be moved to organizational units that are in other organizations.

#. Choose a billing group.

#. Click **Move project**.


Delete a project
----------------

To delete a project:

#. Delete all of the services in the project.

#. Click **Settings**.

#. Click **Delete**. 

#. Click **Confirm**.

.. note::
    You can also :ref:`delete a project using the Aiven CLI <avn-delete-project>`.
