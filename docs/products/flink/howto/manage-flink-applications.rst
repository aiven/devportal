Manage Aiven for Apache Flink® applications
===========================================

This section provides information on managing your Aiven for Apache Flink® applications.

Creating a new version of an application
----------------------------------------
To create a new version of the application deployed, follow these steps: 

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and select your Aiven for Apache Flink® service. 
2. From the left sidebar, select **Applications**. 
3. On the **Applications** landing page, click on the application name for which you want to create a new version. 

For SQL application 
`````````````````````
1. Click **Create new version**.
2. In the **Create new version** page, modify the create statement, source, or sink tables as needed. 
3. Click **Save and deploy later**. You can see the new version listed in the versions drop-down list. 
4. To deploy the new version of the application, :ref:`stop <stop-flink-application>` any existing version that is running.
5. Click **Create deployment**, and in the **Create new deployment** dialog:

   * Select the version you want to deploy. 
   * Select the savepoint from where you want to deploy. 
   * Toggle **Restart on failure** to automatically restart Flink jobs upon failure.
   * Enter the number of `parallel instances <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/execution/parallel/>`_ you want to have for the task. 
   * Click **Deploy from a savepoint** or **Deploy without savepoint** depending on your previous selection.

For JAR application 
`````````````````````
1. Click **Upload new version**.
2. In the **Upload new version** dialog:

   * Click **Choose file** to select your custom JAR file.
   * Review and accept the terms of service by checking the box.
   * Click **Upload version** to upload your JAR file.
3. In the **Deployment history** you can see the latest version running. 

   
.. _stop-flink-application:

Stop application deployment
---------------------------

To stop a deployment for your Flink application, follow these steps: 

1. In your  Aiven for Apache Flink service, select **Applications** from the left sidebar. 
2. On the **Applications** landing page, click on the application name you want to stop. 
3. In the application's overview page, click **Stop deployment**.
4. In the **Stop deployment** dialog, enable the option to **Create a savepoint before stopping** to save the current state of the application. If you want to stop a deployment without saving the current state of the application, disable the option for **Create a savepoint before stopping** and click **Stop without creating savepoint**.
5. Click **Create savepoint & stop** to initiate the stopping process.

The application status will display ``Saving_and_stop_requested`` and then ``Finished`` once the stopping process is completed.

Additionally, the **Deployment history** provides a record of all the application deployments and statuses. 

Rename application
-------------------
To rename an application, follow these steps: 

1. In your  Aiven for Apache Flink service, select **Applications** from the left sidebar.
2. On the **Applications** landing page, click on the application name you want to rename.
3. In the application's overview page, click the **Application action menu (...)** , and click **Update application** from the menu options. 
4. In the **Update Application** dialog, enter the new name for the application and select **Save changes** to confirm the new name and update the application.


.. _flink-deployment-history:

Accessing deployment history
----------------------------
The **Deployment History** screen provides the following:

* A list of all the deployments for an application 
* The user who created the application (created by)
* Data and time of creation (created at)
* Application version
* If a savepoint was created or not

To view and delete the deployment history of an application, follow these steps: 

1. In your  Aiven for Apache Flink service, select **Applications** from the left sidebar.
2. On the **Applications** landing page, click on the application name for which you want to view the deployment history. 
3. In the application landing page, click **Deployment History** to view the deployment history.
4. To remove a specific deployment from the history, locate it in the deployment history page and click the **Delete** icon next to it.


Delete application
-------------------
Before deleting an application, it is necessary to remove all associated :ref:`deployment history <flink-deployment-history>`.

1. In your  Aiven for Apache Flink service, select **Applications** from the left sidebar.
2. On the **Applications** landing page, click on the application name you want to delete. 
3. In the application's overview page, click the **Application action menu (...)**,  and click **Delete application** from the menu options.
4. In the **Delete Confirmation** dialog, enter the name of the application and click **Confirm** to proceed with the deletion.

