Create a JAR application
========================
Aiven for Apache Flink® enables you to upload and deploy custom code as a JAR file, enhancing your Flink applications with advanced data processing capabilities.

.. important:: 
  
   Custom JARs for Aiven for Apache Flink is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at sales@Aiven.io.

Prerequisite
------------

* To enable custom JARs for a new Aiven for Apache Flink service, toggle the feature during service creation.
* For an existing service, in `Aiven Console <https://console.aiven.io/>`_ , select your project and then choose your Aiven for Apache Flink® service.

  * Click **Service settings** on the left sidebar.
  * Scroll to the **Advanced configuration** section, and click **Configure**.
  * In the **Advanced configuration** screen, click **Add configuration options**, and using the search box find and set ``custom_code`` configuration to **Enabled** position.

Create and deploy application
---------------------------------

1. Access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Flink service where you want to deploy a JAR application.
2. From the left sidebar, click **Applications** and then click **Create new application**.
3. In the **Create new application** dialog, enter a name for your JAR application, and select **JAR** as the application type from the drop-down.
4. Click **Create application** to proceed.
5. Click **Upload first version** to upload the first version of the application. 
6. In the **Upload new version** dialog:

   * Click **Choose file** to select your custom JAR file.
   * Select the *Terms of Service* checkbox to indicate your agreement.
   * Click **Upload version** to upload your JAR file.
   
7. After the upload, you are redirected to the application's overview page.
8. To deploy the application, click **Create deployment**. In the **Create new deployment** dialog:

   * Select the application version to deploy. 
   * Select a :doc:`savepoint </docs/products/flink/concepts/savepoints>` if you wish to deploy from a specific state. No savepoints are available for the first application deployment. 
   * Toggle **Restart on failure** to automatically restart Flink jobs upon failure.
   * Specify the number of `parallel instances <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/execution/parallel/>`_ you require for the task.
  
9.  Click **Deploy without a savepoint** to begin the deployment process.
10. The application status will display as **Initializing** during deployment and change to **Running** once it is ready and deployed. 

