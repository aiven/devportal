Getting started with Aiven for MySQL®
=====================================

Aiven for MySQL® services are managed from `Aiven Console <https://console.aiven.io/>`__ .

Start a service
---------------

1. Start an Aiven for MySQL service by following the steps in :doc:`this article </docs/platform/howto/create_new_service>`.

   Upon creating a service, the view returns to the service list, where the new service is shown with an indicator that it is being created.

2. Select the service name in the list to go to the **Overview** page.

   This view shows the connection parameters for your MySQL service and its current status.
   
3. On the **Overview** page, select **Service settings** from the sidebar to access the **Advanced configuration** section and make changes to the service configuration, even while the service is being built.

   You can find the available configuration options in the :doc:`reference article </docs/products/mysql/reference/advanced-params>`.

The status indicator says **Rebuilding** while the service is being created. Once the service is up and running, the light changes to green and the indicator says **Running**.

.. note::
   Services typically start in a couple of minutes, the performance between clouds varies and it can take longer under some circumstances.

Next steps
----------

* Learn how to connect to MySQL:
    - :doc:`From the command line </docs/products/mysql/howto/connect-from-cli>`
    - :doc:`With MySQL workbench </docs/products/mysql/howto/connect-from-mysql-workbench>`

* Create additional databases:
    - :doc:`Create your database </docs/products/mysql/howto/create-database>`

* Connect from your own :doc:`Python application </docs/products/mysql/howto/connect-with-python>`.

