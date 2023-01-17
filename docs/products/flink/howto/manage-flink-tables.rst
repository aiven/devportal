Manage tables in Apache Flink® applications
===========================================

Aiven for Apache Flink® allows you to map source and target data structures as `Flink tables <https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql/create/#create-table>`_ and use transformation statements to transform data. Some of the operations you can perform on a table include:

* Import existing tables
* Add new tables
* Clone tables
* Edit tables
* Delete tables

Before performing any operation on a table in a Flink application, you must stop the application. To stop an application, navigate to the **Applications** tab on your Aiven for Apache Flink® service, select the desired application from the list, and click **Stop Deployment**.

Add new table
--------------

Follow these steps add a new table to an application: 

1. Open the application to which you want to add a new table.
2. Navigate to the **Add source tables** or **Add sink tables** screen within your application.
3. Click the **Add new table** button to add a new table to your application.
    .. note:: 
        If you already have a sink table listed, you must delete it before adding a new one.

4. Select the **Integrated service** from the drop-down list in the **Add new source table** or **Add new sink table** screen, respectively.
5. In the **Table SQL** section, enter the statement that will create the table. The interactive query feature if the editor will prompt you for error or invalid queries. 
6. Click **Add table** to complete the process.

Import an existing table
-------------------------
Follow these steps import an existing table from another application: 

1. In the **Add source tables** or **Add sink tables** screen, click **Import existing table** to import a table to your application. 
    .. note::
        If you already have a sink table listed, you must delete it before importing a new one.

2. From the **Import existing source table** or **Import existing sink table** screen:

    - Select the application from which you want to import the table.
    -  Select the version of the application.
    - Select the table you want to import. 

3. Click **Next**.
4. Verify the data on the **Add new source table** or **Add new sink table** screen and click **Add table** to complete the process.

Clone table
-----------

Follow these steps to clone a table in an application: 

1. In the **Add source tables** screen, locate the table you want to clone and click **Clone** next to it. 
    .. note::
        Clone option is not available sink tables. 

2. Select the **Integrated service** from the drop-down list.
3. In the **Table SQL** section, update the table name.
    .. note:: 
        You will not be able to add the table if there are errors within the statement. 
4. Click **Add table** to complete the process.

Edit table
----------
Follow these steps edit an existing table in an application: 
1. In the **Add source tables** or **Add sink tables** screen, locate the table you want to edit and click **Edit** next to it.
2. Make the necessary changes to the table and click **Save changes** to confirm the changes.

Delete table
------------
Follow these steps to delete a table in an application: 
1. In the **Add source tables** or **Add sink tables** screen, locate the table you want to delete and click the **Delete** icon next to it.
2. Confirm the deletion by clicking **Confirm** in the pop-up window.



