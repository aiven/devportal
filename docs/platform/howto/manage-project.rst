Create a project
================

In the `Aiven web console <https://console.aiven.io/>`_, follow these steps to create a new project:

1. Click on **Project** drop down and click on **Create new project**.
2. Give the new project a name.
3. Select an Account to add the project to.
4. In **Payment method** select a project to copy the billing details from, or select **Use a new credit card**.

When you create a new project, you will need to enable :doc:`billing for creating new services <docs/platform/howto/list-billing>`.

Rename a project
================

Renaming a project is possible **only** when all the services in the project are powered-off. To rename a project in the `Aiven web console <https://console.aiven.io/>`_:

1. Make sure the respective project is selected from the **Project** drop down.
2. Click on **Settings**. 
3. Type in the new project name in the *Project Name* field.
4. Click on **Save changes**. 

.. note:: 
   
   - Except for Aiven for Apache Kafka®, all service types have backups which are restored once you power them back on.
   - Renaming the project will invalidate all of the project's pending invitations.
   - The project name in your existing DNS records will not be updated.

Delete a project
================

In order to delete a project, you need to removes the services in it first. Once all the services are removed:

1. Make sure the respective project is selected from the **Project** drop down.
2. Click on **Settings**.
3. Click on **Remove project**. 

.. note::
    You can :ref:`create, rename and delete a project using the Aiven CLI <avn-manage-project>` as well.
